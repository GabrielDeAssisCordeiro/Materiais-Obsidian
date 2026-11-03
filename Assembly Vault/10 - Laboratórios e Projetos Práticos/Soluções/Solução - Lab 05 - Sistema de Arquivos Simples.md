---
titulo: "Solução - Lab 05 - Sistema de Arquivos Simples"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - syscall
  - arquivos
nivel: intermediario
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 05 - Sistema de Arquivos Simples

> [!warning] Tente primeiro!
> Primeiro o [[Lab 05 - Sistema de Arquivos Simples]]. Depois compare.

Voltar: [[Lab 05 - Sistema de Arquivos Simples]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada com NASM e ligada com `ld` (sem libc). `cat` e `cp` conferidos com `cmp` em arquivos de texto, vazios e de 300 KB e 50 MB aleatórios; `wc` conferido com o `wc` do GNU em arquivos de texto; erros (arquivo inexistente, destino inválido, comando desconhecido) devolvem código 1.

## 1. Código completo comentado

```nasm
; Lab 05 - Mini sistema de arquivos: cat | cp | wc  (sem libc)
;   ./lab05 cat arq        ./lab05 cp origem destino        ./lab05 wc arq
default rel
global _start

SYS_read equ 0
SYS_write equ 1
SYS_open equ 2
SYS_close equ 3
SYS_exit equ 60
O_RDONLY equ 0
O_WRONLY_CREAT_TRUNC equ 0x241     ; O_WRONLY|O_CREAT|O_TRUNC
BUFSZ equ 65536

section .data
usage   db "uso: lab05 cat ARQ | cp ORIG DEST | wc ARQ", 10
usage_n equ $ - usage
err_open db "erro: nao foi possivel abrir/criar arquivo", 10
err_open_n equ $ - err_open
err_io  db "erro de E/S", 10
err_io_n equ $ - err_io
l_lines db " linhas "
l_words db " palavras "
l_bytes db " bytes", 10

section .bss
buf    resb BUFSZ
numbuf resb 24

section .text
; --- utilitários ---
die:                        ; RSI/RDX = mensagem; sai com código 1
    mov  edi, 2
    mov  eax, SYS_write
    syscall
    mov  edi, 1
    mov  eax, SYS_exit
    syscall

; streq(RDI, RSI) -> ZF=1 se iguais
streq:
.l: mov  al, [rdi]
    cmp  al, [rsi]
    jne  .d
    test al, al
    jz   .d
    inc  rdi
    inc  rsi
    jmp  .l
.d: ret

; write_all(RDI=fd, RSI=ptr, RDX=len): trata escritas parciais; RAX<0 em erro
write_all:
.l: test rdx, rdx
    jz   .ok
    push rdi
    push rsi
    push rdx
    mov  eax, SYS_write
    syscall
    pop  rdx
    pop  rsi
    pop  rdi
    test rax, rax
    js   .ret
    add  rsi, rax
    sub  rdx, rax
    jmp  .l
.ok: xor eax, eax
.ret: ret

; print_dec(RAX): imprime número e mantém tudo que importa em r12-r15
print_dec:
    lea  rsi, [numbuf + 23]
    mov  rcx, 10
.d: xor  edx, edx
    div  rcx
    add  dl, '0'
    dec  rsi
    mov  [rsi], dl
    test rax, rax
    jnz  .d
    lea  rdx, [numbuf + 23]
    sub  rdx, rsi
    mov  edi, 1
    jmp  write_all

; open_or_die(RDI=path, RSI=flags) -> RAX = fd
open_or_die:
    mov  edx, 0644o
    mov  eax, SYS_open
    syscall
    test rax, rax
    jns  .ok
    lea  rsi, [err_open]
    mov  edx, err_open_n
    jmp  die
.ok: ret

_start:
    mov  rbx, [rsp]            ; argc
    lea  r15, [rsp + 8]        ; argv
    cmp  rbx, 3
    jb   .usage
    mov  r14, [r15 + 8]        ; argv[1] = comando
    ; cat?
    mov  rdi, r14
    lea  rsi, [c_cat]
    call streq
    je   .cat
    mov  rdi, r14
    lea  rsi, [c_cp]
    call streq
    je   .cp
    mov  rdi, r14
    lea  rsi, [c_wc]
    call streq
    je   .wc
.usage:
    lea  rsi, [usage]
    mov  edx, usage_n
    jmp  die

; ---- cat ----
.cat:
    mov  rdi, [r15 + 16]
    xor  esi, esi
    call open_or_die
    mov  r12, rax
    mov  r13d, 1               ; destino = stdout
    jmp  .copy
; ---- cp ----
.cp:
    cmp  rbx, 4
    jb   .usage
    mov  rdi, [r15 + 16]
    xor  esi, esi
    call open_or_die
    mov  r12, rax
    mov  rdi, [r15 + 24]
    mov  esi, O_WRONLY_CREAT_TRUNC
    call open_or_die
    mov  r13, rax
.copy:
    mov  rdi, r12
    lea  rsi, [buf]
    mov  edx, BUFSZ
    xor  eax, eax              ; SYS_read
    syscall
    test rax, rax
    js   .io
    jz   .done
    mov  rdx, rax
    mov  rdi, r13
    lea  rsi, [buf]
    call write_all
    test rax, rax
    js   .io
    jmp  .copy
.done:
    mov  eax, SYS_close
    mov  rdi, r12
    syscall
    cmp  r13, 1
    je   .exit0
    mov  eax, SYS_close
    mov  rdi, r13
    syscall
.exit0:
    xor  edi, edi
    mov  eax, SYS_exit
    syscall
.io:
    lea  rsi, [err_io]
    mov  edx, err_io_n
    jmp  die

; ---- wc: linhas, palavras, bytes (palavra = sequência de não-brancos) ----
.wc:
    mov  rdi, [r15 + 16]
    xor  esi, esi
    call open_or_die
    mov  r12, rax
    xor  r13d, r13d            ; linhas
    xor  r14d, r14d            ; palavras
    xor  r15d, r15d            ; bytes
    xor  ebx, ebx              ; estado: 1 = dentro de palavra
.wr:
    mov  rdi, r12
    lea  rsi, [buf]
    mov  edx, BUFSZ
    xor  eax, eax
    syscall
    test rax, rax
    js   .io
    jz   .wprint
    add  r15, rax
    lea  rsi, [buf]
    lea  rdi, [rsi + rax]      ; fim
.wl:
    cmp  rsi, rdi
    jae  .wr
    movzx eax, byte [rsi]
    inc  rsi
    cmp  al, 10
    jne  .nl
    inc  r13
.nl:
    cmp  al, ' '
    je   .sp
    lea  ecx, [rax - 9]
    cmp  cl, 4                 ; \t \n \v \f \r  (9..13)
    jbe  .sp
    test ebx, ebx              ; não-branco
    jnz  .wl
    mov  ebx, 1
    inc  r14
    jmp  .wl
.sp: xor ebx, ebx
    jmp  .wl
.wprint:
    mov  rax, r13
    call print_dec
    lea  rsi, [l_lines]
    mov  edx, 8
    mov  edi, 1
    call write_all
    mov  rax, r14
    call print_dec
    lea  rsi, [l_words]
    mov  edx, 10
    mov  edi, 1
    call write_all
    mov  rax, r15
    call print_dec
    lea  rsi, [l_bytes]
    mov  edx, 7
    mov  edi, 1
    call write_all
    jmp  .exit0

section .rodata
c_cat db "cat", 0
c_cp  db "cp", 0
c_wc  db "wc", 0

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

### Dados e constantes
`equ` define constantes de assembly (não ocupam memória). `O_WRONLY_CREAT_TRUNC = 0x241` é `O_WRONLY (1) | O_CREAT (0x40) | O_TRUNC (0x200)`. O *buffer* de 64 KiB está em `.bss` (não ocupa espaço no arquivo, só na memória).

### `die`
Escreve a mensagem em **stderr** (`fd 2`) e termina com código 1. Termina com `jmp`, não `call`: **não volta**.

### `streq`
Compara byte a byte. A saída é a **flag ZF**: depois do último `cmp al, [rsi]`, se os bytes eram iguais e `al` era zero, `ZF = 1` (`test al, al` deixa `ZF = 1`). Quem chama usa `je`/`jne` direto, sem `cmp` extra. Atenção: se os bytes diferem, `jne .d` sai com `ZF = 0`.

### `write_all`
O kernel só destrói `RAX`, `RCX` e `R11` numa `syscall`; `RDI`, `RSI` e `RDX` voltam intactos. O código **empilha** os três antes da chamada e os restaura depois: é redundante (e dá para remover, como exercício), mas deixa explícito o que o laço precisa. Se `RAX < 0` devolve o erro; senão **avança** `RSI`, **diminui** `RDX` e repete até `RDX = 0`.

### `print_dec`
Converte `RAX` em decimal escrevendo **de trás para frente** em `numbuf + 23` (divisões sucessivas por 10) e termina com `jmp write_all`, uma chamada em cauda: o `ret` de `write_all` volta ao chamador de `print_dec`.

### `open_or_die`
`open(RDI = caminho, RSI = flags, RDX = 0644o)`. Um **valor negativo** é `-errno`. A mensagem única não distingue o erro; veja a variação.

### `_start`: despacho
`argc` em `RBX`, `argv` em `R15`; `streq` contra `"cat"`, `"cp"` e `"wc"`. Três registradores **preservados em fato** (`R12-R15`, `RBX`) guardam estado entre syscalls (o kernel só destrói `RAX`, `RCX`, `R11`).

### `cat` e `cp`
Compartilham o laço `.copy`: `r12` = fd de entrada, `r13` = fd de saída (1 para `cat`). No fim, `close` dos descritores (o de saída só se não for o stdout) e `exit(0)`.

### `wc`
`R13` = linhas, `R14` = palavras, `R15` = bytes, `RBX` = estado. Para cada byte do bloco: `\n` incrementa linhas; branco (`' '` ou `9..13`) zera o estado; outro caractere, se o estado era 0, incrementa palavras. Os números saem com `print_dec`.

## 3. Variações

| Variação | O que muda |
|----------|------------|
| **Mensagem de erro com `errno`** | `neg rax` dá o `errno` (2 = `ENOENT`, 13 = `EACCES`); imprima com `print_dec` |
| **Entrada padrão** | se `argc == 2`, `fd = 0` e leia do stdin |
| **`copy_file_range`** | `mov eax, 326` (`RDI` = fd origem, `RSI` = 0, `RDX` = fd destino, `R10` = 0, `R8` = tamanho, `R9` = 0): o kernel copia sem passar pelo espaço do usuário |
| **`mmap`** | mapear o arquivo (`mmap`, syscall 9) e contar sem `read` |
| **MASM x64** | `CreateFileA`, `ReadFile(h, buf, n, &lido, 0)`, `WriteFile`, `CloseHandle`, com *shadow space* |

## 4. Análise de desempenho

Veja a seção 6 do lab: o buffer de 1 byte leva **1,98 s** para copiar 5 MB, e o de 64 KiB, **3 ms**. O custo está no **número de syscalls**, não nas instruções do laço.

## 5. Erros comuns

> [!warning]
> 1. **Ignorar `RAX < 0`** depois de `open`: usar `-2` (`ENOENT`) como *file descriptor*.
> 2. **Supor que `write` escreve tudo**: em *pipes* e terminais pode ser parcial.
> 3. **Esquecer que `syscall` destrói `RCX` e `R11`**: perda de contador de laço guardado em `RCX`.
> 4. **`argv` no lugar errado**: `argv[1]` está em `[rsp + 16]` no `_start` (não em `[rsp + 8]`).
> 5. **Flags de `open` erradas**: sem `O_TRUNC`, o arquivo de destino **mais longo** mantém a cauda antiga; sem `O_CREAT` e o modo, a abertura falha.
> 6. **Ler o arquivo todo em um único `read` de buffer pequeno**: ele devolve **menos** que o pedido; só `0` indica o fim.
> 7. **Esquecer o código de saída**: o `wc` tem que terminar com `exit(0)` (saia sem `exit` e o processo **executa lixo**).
