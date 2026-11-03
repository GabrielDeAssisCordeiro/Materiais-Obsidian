---
titulo: "Solução - Lab 08 - Projeto Final"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - projeto
  - nasm
  - syscall
nivel: avancado
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 08 - Projeto Final

> [!warning] Tente primeiro!
> Primeiro o [[Lab 08 - Projeto Final]]. Depois compare.

Voltar: [[Lab 08 - Projeto Final]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada com NASM 2.16 e ligada com `ld`. O `teste8.sh` passou em todos os 21 tamanhos de borda (0 a 300 000 bytes), em modo arquivo e modo *pipe*, mais o código de saída em erro. A comparação foi feita com a referência em Python do mesmo formato (o `hexdump` não existia no ambiente de teste): **rode o `teste8.sh` na sua máquina, onde ele usará o `hexdump -vC` de verdade.** A variação com tabela de 256 entradas (seção 3) passou nos mesmos testes.

## 1. Código completo comentado

```nasm
; Lab 08 - Projeto final: "hd", um hexdump -vC em Assembly puro (sem libc)
;   ./hd arquivo        ou        comando | ./hd
; Formato idêntico a `hexdump -vC`:
;   00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64 21 0a           |Hello World!.|
default rel
global _start

INSZ  equ 65536                  ; múltiplo de 16
OUTSZ equ (INSZ / 16) * 80 + 16  ; cada linha gera no máx. 79 bytes

section .rodata
hexd db "0123456789abcdef"
usage db "uso: hd [arquivo]", 10
usage_n equ $ - usage
eopen db "hd: nao foi possivel abrir o arquivo", 10
eopen_n equ $ - eopen

section .bss
inbuf  resb INSZ
outbuf resb OUTSZ

section .text
; flush(RSI=ptr, RDX=len) -> escreve tudo em stdout (trata escrita parcial); CF=1 em erro
flush:
.l: test rdx, rdx
    jz   .ok
    mov  eax, 1
    mov  edi, 1
    push rsi
    push rdx
    syscall
    pop  rdx
    pop  rsi
    test rax, rax
    jle  .err
    add  rsi, rax
    sub  rdx, rax
    jmp  .l
.ok: clc
    ret
.err: stc
    ret

; read_full(RDI=fd) -> RAX = bytes lidos em inbuf (até INSZ ou EOF); preenche o buffer
; (read em pipe pode devolver menos que o pedido -> repetir até encher ou EOF)
read_full:
    xor  r8d, r8d
.l: cmp  r8d, INSZ
    jae  .d
    mov  eax, 0
    lea  rsi, [inbuf + r8]
    mov  edx, INSZ
    sub  edx, r8d
    push rdi
    syscall
    pop  rdi
    test rax, rax
    jle  .d                    ; EOF (0) ou erro (<0)
    add  r8, rax
    jmp  .l
.d: mov  rax, r8
    ret

_start:
    mov  rax, [rsp]            ; argc
    xor  r12d, r12d            ; fd = 0 (stdin)
    cmp  rax, 1
    je   .go
    cmp  rax, 2
    jne  .usage
    mov  rdi, [rsp + 16]       ; argv[1]
    xor  esi, esi              ; O_RDONLY
    mov  eax, 2
    syscall
    test rax, rax
    js   .eopen
    mov  r12, rax
.go:
    xor  r13d, r13d            ; offset global (nº de bytes já impressos)
    lea  r14, [hexd]
.chunk:
    mov  rdi, r12
    call read_full
    test rax, rax
    jz   .final
    mov  r15, rax              ; bytes neste bloco
    lea  rsi, [inbuf]          ; rsi = origem
    lea  rdi, [outbuf]         ; rdi = destino
    lea  rbx, [inbuf + r15]    ; fim dos dados
.line:
    cmp  rsi, rbx
    jae  .emit
    ; --- offset: 8 dígitos hex ---
    mov  eax, r13d
    mov  ecx, 8
.off:
    rol  eax, 4
    mov  edx, eax
    and  edx, 15
    mov  dl, [r14 + rdx]
    mov  [rdi], dl
    inc  rdi
    dec  ecx
    jnz  .off
    mov  word [rdi], 0x2020    ; dois espaços
    add  rdi, 2
    ; --- 16 colunas de hex ---
    mov  rbp, rbx
    sub  rbp, rsi              ; bytes restantes
    cmp  rbp, 16
    jbe  .lim
    mov  ebp, 16
.lim:                          ; ebp = bytes desta linha (1..16)
    xor  ecx, ecx
.hx:
    cmp  ecx, 16
    jae  .asc0
    cmp  ecx, ebp
    jae  .pad
    movzx eax, byte [rsi + rcx]
    mov  edx, eax
    shr  edx, 4
    mov  dl, [r14 + rdx]
    mov  [rdi], dl
    and  eax, 15
    mov  al, [r14 + rax]
    mov  [rdi + 1], al
    mov  byte [rdi + 2], ' '
    jmp  .nx
.pad:
    mov  word [rdi], 0x2020
    mov  byte [rdi + 2], ' '
.nx:
    add  rdi, 3
    cmp  ecx, 7
    jne  .nn
    mov  byte [rdi], ' '       ; espaço extra no meio
    inc  rdi
.nn:
    inc  ecx
    jmp  .hx
.asc0:
    mov  byte [rdi], ' '       ; (o hexdump põe um espaço antes do '|')
    mov  byte [rdi + 1], '|'
    add  rdi, 2
    xor  ecx, ecx
.as:
    cmp  ecx, ebp
    jae  .endl
    movzx eax, byte [rsi + rcx]
    lea  edx, [rax - 32]
    cmp  dl, 94                ; 32..126 imprimível
    jbe  .pr
    mov  al, '.'
.pr:
    mov  [rdi], al
    inc  rdi
    inc  ecx
    jmp  .as
.endl:
    mov  byte [rdi], '|'
    mov  byte [rdi + 1], 10
    add  rdi, 2
    add  rsi, rbp
    add  r13, rbp
    jmp  .line
.emit:
    lea  rsi, [outbuf]
    mov  rdx, rdi
    sub  rdx, rsi
    call flush
    jc   .exit1
    cmp  r15, INSZ
    je   .chunk                ; bloco cheio: pode haver mais
.final:
    test r13, r13
    jz   .ok0                  ; arquivo vazio: hexdump não imprime nada
    ; linha final: só o offset total (como o hexdump)
    lea  rdi, [outbuf]
    mov  eax, r13d
    mov  ecx, 8
.fo:
    rol  eax, 4
    mov  edx, eax
    and  edx, 15
    mov  dl, [r14 + rdx]
    mov  [rdi], dl
    inc  rdi
    dec  ecx
    jnz  .fo
    mov  byte [rdi], 10
    inc  rdi
    lea  rsi, [outbuf]
    mov  rdx, rdi
    sub  rdx, rsi
    call flush
    jc   .exit1
.ok0:
    xor  edi, edi
    jmp  .exit
.usage:
    lea  rsi, [usage]
    mov  edx, usage_n
    jmp  .err
.eopen:
    lea  rsi, [eopen]
    mov  edx, eopen_n
.err:
    mov  edi, 2
    mov  eax, 1
    syscall
.exit1:
    mov  edi, 1
.exit:
    mov  eax, 60
    syscall

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

### Constantes e buffers
`INSZ = 65536` (múltiplo de 16: cada bloco cheio contém linhas completas). `OUTSZ = (INSZ/16)*80 + 16`: cada linha ocupa **no máximo 79 bytes**, 80 por margem, e o `+16` cobre a linha final do total. Os dois buffers estão em `.bss`.

### `flush(RSI, RDX)`
Escreve **tudo** em `stdout` repetindo o `write` até acabar (escrita parcial). Devolve `CF = 1` em erro (`jle .err` trata `0` e negativos: um `write` que devolve 0 em laço seria infinito). Empilha `RSI` e `RDX` antes da `syscall` (redundante, como no [[Solução - Lab 05 - Sistema de Arquivos Simples|Lab 05]]: o kernel só destrói `RAX`, `RCX` e `R11`).

### `read_full(RDI = fd)`
Repete `read` até **encher** `inbuf` ou chegar ao fim do arquivo. Por que não um único `read`? Em um *pipe*, ele devolve só o que há disponível, em geral 4 KiB ou menos: sem este laço, as **linhas de 16 bytes seriam cortadas no meio** e o *offset* sairia errado. Devolve em `RAX` o total lido.

### `_start`
Se `argc = 1`, `fd = 0`. Se `argc = 2`, `open(argv[1], O_RDONLY)`; falha → mensagem em stderr e código 1. Mais de um argumento → uso.

### Laço de linhas (`.line`)
1. **Offset:** `mov eax, r13d` e 8 vezes `rol eax, 4` / `and edx, 15` / `mov dl, [r14 + rdx]`: converte nibble a nibble do mais significativo ao menos, **sem divisão**. Depois dois espaços.
2. **Quantos bytes tem esta linha:** `RBP = min(16, fim - RSI)`.
3. **16 colunas:** para `ecx < ebp`, converte o byte em dois dígitos (`shr edx, 4`, `and eax, 15`) e um espaço; senão, escreve 3 espaços (*padding*). Depois da 8ª coluna (`cmp ecx, 7`), um espaço extra.
4. **` |`**, a **coluna ASCII** (imprimível → o próprio byte; senão `.`) e **`|\n`**.
5. Avança `RSI` e `R13` de `RBP`.

### `.emit` e o fim
Escreve o bloco inteiro de uma vez (`flush`). Se o bloco foi **cheio** (`r15 == INSZ`), pode haver mais dados: volta a `.chunk`. Senão, ou quando `read_full` devolve 0, vai para `.final`, que imprime o *offset* total, **exceto** se `r13 = 0` (arquivo vazio: o `hexdump` não imprime nada).

> [!tip] Um `write` por bloco, não por linha
> 64 KiB de entrada geram ~320 KB de saída em **uma** chamada (ou algumas, se parcial). Um `write` por linha seriam 4096 syscalls por bloco: com ~0,2 µs cada, é 0,8 ms a mais por bloco, mais que o formatador.

## 3. Variação testada: tabela de 256 entradas

Em vez de duas consultas de 8 bits por byte (`shr`, `and`, duas cargas, dois armazenamentos), **uma** consulta de 16 bits em uma tabela de 512 bytes (`tbl[b]` = os dois caracteres de `b`). Mudanças:

```nasm
section .bss
tbl    resw 256                ; tbl[b] = os 2 caracteres hex do byte b

; no início de _start: monta a tabela
    lea  r14, [hexd]
    lea  rdi, [tbl]
    xor  ecx, ecx
.mk:
    mov  eax, ecx
    shr  eax, 4
    mov  al, [r14 + rax]       ; dígito alto
    mov  edx, ecx
    and  edx, 15
    movzx edx, byte [r14 + rdx]
    shl  edx, 8
    movzx eax, al
    or   eax, edx              ; ax = (dígito baixo << 8) | dígito alto
    mov  [rdi + rcx*2], ax
    inc  ecx
    cmp  ecx, 256
    jb   .mk

; a cada bloco, depois de read_full:   lea r8, [tbl]    (read_full destrói R8)

; no laço de colunas, no lugar das duas consultas:
    movzx eax, byte [rsi + rcx]
    mov  ax, [r8 + rax*2]      ; 1 carga de 16 bits
    mov  [rdi], ax
    mov  byte [rdi + 2], ' '
```

Resultado: **0,105 s → 0,089 s** para 50 MB (16% mais rápido), com a mesma saída (o `little-endian` faz o dígito alto ficar no primeiro byte).

> [!warning] Armadilha do `ah`
> A primeira tentativa usou `mov ah, [r14 + rdx]`. O NASM recusa: **`ah`, `bh`, `ch`, `dh` não podem ser usados em instruções com prefixo REX** (que é necessário para `r8-r15`). A correção é montar o valor com `movzx` + `shl` + `or`.

## 4. Variações e extensões

| Extensão | Esboço |
|----------|--------|
| **`*` para linhas repetidas** | guarde a linha anterior (16 bytes); compare com `movdqu`/`pcmpeqb`/`pmovmskb` (`0xFFFF` = igual); imprima um `*` na primeira repetição e pule as demais; ao final, imprima o *offset* total |
| **`-n N` e `-s N`** | contador no laço de leitura; `lseek(fd, N, SEEK_SET)` para pular (só serve em arquivos, não em *pipes*) |
| **CRC-32** | tabela de 256 `dword`: `c = i; repita 8 vezes: c = (c & 1) ? (c >> 1) ^ 0xEDB88320 : c >> 1`; depois, para cada byte, `crc = tabela[(crc ^ b) & 0xFF] ^ (crc >> 8)`, com `crc` iniciando em `0xFFFFFFFF` e `not` no final |
| **SIMD** | 16 bytes → 32 caracteres: `pand` (nibbles baixos) e `psrlw` + `pand` (altos); `pshufb` na tabela `"0123456789abcdef"`; `punpcklbw`/`punpckhbw` intercalam |
| **MASM x64** | `CreateFileA`/`ReadFile`/`WriteFile` em vez das syscalls; `GetCommandLineA` ou `__argc/__argv` em vez da pilha inicial |
| **AArch64** | `x8` = número da syscall (`read` = 63, `write` = 64, `openat` = 56, `exit` = 93), `svc #0`; `ubfx` extrai nibbles |

## 5. Erros comuns

> [!warning]
> 1. **Um único `read`**: com *pipe*, devolve blocos parciais e corta as linhas.
> 2. **Esquecer a linha final do total** (ou imprimi-la no arquivo vazio).
> 3. **Padding da linha incompleta** sem o **espaço extra do meio** (a coluna ASCII se desalinha).
> 4. **Buffer de saída pequeno demais**: *overflow* silencioso em `.bss`, que sobrescreve `inbuf`.
> 5. **Escrever em `stdout` sem tratar escrita parcial.**
> 6. **Usar `ah`/`bh`/`ch`/`dh` junto com `r8-r15`**: erro do montador.
> 7. **Esquecer que `read_full` e `syscall` destroem registradores** (`R8`, `RCX`, `R11`, `RAX`).
> 8. **Offset de 32 bits**: arquivos acima de 4 GiB repetem o *offset* (o `hexdump` usa 8 dígitos até o limite e depois mais; trate com 64 bits se importar).
