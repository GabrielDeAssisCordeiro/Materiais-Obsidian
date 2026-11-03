---
titulo: "Solução - Lab 01 - Hello World e Operações Básicas"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - syscall
nivel: iniciante
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 01 - Hello World e Operações Básicas

> [!warning] Tente primeiro!
> Só abra esta nota depois de ter tentado o [[Lab 01 - Hello World e Operações Básicas]]. Comparar com a **sua** solução ensina mais do que ler a minha.

Voltar: [[Lab 01 - Hello World e Operações Básicas]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Esta solução foi **montada e executada** (NASM 2.16, `ld`, Linux x64) e produz exatamente:
> ```text
> Ola, Assembly!
> Soma 1..100 = 5050
> 10! = 3628800
> ```

## 1. Código completo comentado

```nasm
; Lab 01 - Hello World e operações básicas (NASM, Linux x64, sem libc)
default rel
global _start

section .data
msg      db "Ola, Assembly!", 10
msg_len  equ $ - msg
lbl_soma db "Soma 1..100 = "
lbl_soma_len equ $ - lbl_soma
lbl_fat  db "10! = "
lbl_fat_len equ $ - lbl_fat

section .bss
buf resb 32

section .text
; print(rsi=ptr, rdx=len)
print:
    mov  eax, 1
    mov  edi, 1
    syscall
    ret

; print_u64: RAX = número -> imprime em decimal + '\n'
print_u64:
    lea  rsi, [buf + 31]
    mov  byte [rsi], 10
    mov  rcx, 10
.dig:
    xor  edx, edx
    div  rcx               ; rax = q, rdx = resto
    add  dl, '0'
    dec  rsi
    mov  [rsi], dl
    test rax, rax
    jnz  .dig
    lea  rdx, [buf + 32]
    sub  rdx, rsi          ; tamanho
    jmp  print             ; tail call

_start:
    lea  rsi, [msg]
    mov  edx, msg_len
    call print

    ; soma 1..100
    lea  rsi, [lbl_soma]
    mov  edx, lbl_soma_len
    call print
    xor  eax, eax
    mov  ecx, 100
.s: add  rax, rcx
    loop .s
    call print_u64

    ; fatorial 10
    lea  rsi, [lbl_fat]
    mov  edx, lbl_fat_len
    call print
    mov  eax, 1
    mov  ecx, 10
.f: imul rax, rcx
    dec  ecx
    jnz  .f
    call print_u64

    mov  eax, 60
    xor  edi, edi
    syscall

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

| Trecho | O que faz | O que acontece no processador |
|--------|-----------|-------------------------------|
| `default rel` | endereçamento relativo ao `RIP` | `lea rsi,[msg]` vira `lea` com deslocamento a partir de `RIP`: código independente de posição ([[07 - Assembly Avançado (x86-x64)]]) |
| `msg_len equ $ - msg` | o montador calcula o tamanho em **tempo de montagem** | nenhuma instrução é gerada: `msg_len` vira uma constante |
| `print:` | `RAX=1` (write), `EDI=1` (stdout), `syscall` | `syscall` troca para o modo kernel; o kernel lê `RSI`/`RDX` e devolve o nº de bytes em `RAX`; **destrói `RCX` e `R11`** |
| `print_u64`: `lea rsi,[buf+31]` | aponta para o **último** byte do buffer | o número é montado de trás para frente |
| `mov byte [rsi], 10` | grava `'\n'` | |
| `.dig: xor edx,edx / div rcx` | `RDX:RAX ÷ 10` → `RAX` = quociente, `RDX` = resto | uma divisão de 128 por 64 bits (microcodificada, cara) |
| `add dl,'0'` ... `mov [rsi],dl` | resto (0–9) → ASCII (`'0'` = 48) e grava | |
| `jnz .dig` | repete enquanto o quociente ≠ 0 | o `test rax,rax` anterior define `ZF` |
| `lea rdx,[buf+32]` / `sub rdx,rsi` | tamanho = fim − início | |
| `jmp print` | **tail call**: reaproveita o `ret` de `print` | um `ret` a menos e nenhuma pilha extra |
| laço `loop .s` | `RCX--`; salta se ≠ 0 | `loop` é **mais lento** que `dec`+`jnz` em CPUs modernas; aqui é didático |
| `imul rax, rcx` | `RAX *= RCX` | latência de 3 ciclos |

### Por que `print_u64` pode usar `jmp print`?
Porque a **última coisa** que ela faz é chamar `print`. O `ret` de `print` devolve o controle direto ao chamador de `print_u64`. É a mesma otimização que compiladores fazem (*tail call*, [[04 - Procedimentos, Stack e Calling Conventions]]).

## 3. Variações dos desafios

**Imprimir 1 a 10** (guarde o contador em registrador que a syscall **não** destrói):

```nasm
    mov  ebx, 1
.p: mov  eax, ebx
    call print_u64        ; print_u64 usa RAX, RCX, RDX, RSI, RDI e R11 (via syscall); RBX está a salvo
    inc  ebx
    cmp  ebx, 10
    jbe  .p
```

**Hexadecimal:** troque `mov rcx, 10` por `mov rcx, 16` e converta o resto com `cmp dl, 9 / jbe / add dl, 'a'-10` (ou use uma tabela `"0123456789abcdef"` e `mov dl, [tab + rdx]`).

## 4. Análise de desempenho

| Item | Comentário |
|------|------------|
| **Chamadas ao kernel** | `strace -c`: **5 `write`**. Cada uma custa bem mais que todo o resto do programa. Reduza com **um buffer único** |
| **`div` por 10** | Para converter, a multiplicação por `0xCCCCCCCD` e `shr 35` (32 bits) foi **5,9× mais rápida** que `div r32` nos experimentos do [[09 - Otimização, SIMD e Performance]] |
| **`loop`** | simples e correto aqui, mas em laços críticos use `dec` + `jnz` (macro-fusão) |
| **Fatorial/soma** | 10 e 100 voltas: custo desprezível. Para somar 1..N, a fórmula `N*(N+1)/2` troca N somas por 1 multiplicação |

## 5. Erros comuns neste lab

> [!warning]
> 1. **Esquecer `xor edx, edx` antes do `div`** → resultado errado ou `SIGFPE`.
> 2. **Esquecer a syscall `exit`** → o processador executa lixo e dá `SIGSEGV`.
> 3. **Usar `RCX` como contador de laço que chama `print`** → `syscall` destrói `RCX`.
> 4. **Contar o tamanho errado** da mensagem (esquecer o `10` do `'\n'`): use `equ $ - msg`.
> 5. **Imprimir o buffer inteiro** (32 bytes) em vez de só a parte usada.

Próximo: [[Lab 02 - Calculadora em Assembly]] · Ver também: [[Glossário#Assembly (x86-64 e ARM)]]
