---
titulo: "Cheat Sheet de Calling Conventions"
aliases: []
tipo: cheatsheet
tags:
  - assembly
  - cheatsheet
  - calling-convention
  - abi
  - x64
  - arm
nivel: todos
arquitetura:
  - x64
  - x86
  - arm
criado: 2026-10-21
---

# Cheat Sheet de Calling Conventions

> [!abstract] Resumo
> As convenções de chamada lado a lado: **System V AMD64** (Linux/macOS), **Microsoft x64** (Windows), as de 32 bits (`cdecl`, `stdcall`, `fastcall`) e **AAPCS64/AAPCS32** (ARM). Teoria completa no [[04 - Procedimentos, Stack e Calling Conventions]]; ARM no [[08 - ARM e AArch64]]. Voltar: [[11 - Recursos e Referências]] · [[00 - Índice]]

Tags: #assembly #cheatsheet #calling-convention #abi

---

## 1. x86-64: System V × Microsoft

| Item | **System V AMD64** (Linux, macOS, BSD) | **Microsoft x64** (Windows) |
|------|----------------------------------------|-----------------------------|
| Argumentos inteiros/ponteiros | `rdi, rsi, rdx, rcx, r8, r9` | `rcx, rdx, r8, r9` |
| Argumentos `float`/`double` | `xmm0`-`xmm7` | `xmm0`-`xmm3` |
| Posições | cada tipo tem sua **própria** sequência | **por posição**: o 3º argumento é sempre `r8` ou `xmm2` |
| Argumentos extras | pilha, da direita para a esquerda | pilha, da direita para a esquerda |
| Retorno inteiro | `rax` (e `rdx` para 128 bits) | `rax` |
| Retorno de `float`/`double` | `xmm0` (e `xmm1`) | `xmm0` |
| ***Shadow space*** | não existe | **32 bytes** reservados pelo **chamador** logo acima do endereço de retorno |
| ***Red zone*** | **128 bytes** abaixo de `rsp` (folhas podem usar sem mexer em `rsp`) | **não existe** |
| Alinhamento de `rsp` | múltiplo de **16 antes do `call`** | múltiplo de **16 antes do `call`** |
| Limpeza da pilha | **chamador** | **chamador** |
| ***Callee-saved*** (a função preserva) | `rbx, rbp, r12, r13, r14, r15` | `rbx, rbp, rdi, rsi, r12`-`r15`, **`xmm6`-`xmm15`** |
| ***Caller-saved*** (podem ser destruídos) | `rax, rcx, rdx, rsi, rdi, r8`-`r11`, todos os `xmm`/`ymm` | `rax, rcx, rdx, r8`-`r11`, `xmm0`-`xmm5` |
| Função variádica | `al` = número de registradores `xmm` usados | argumentos de ponto flutuante também copiados nos registradores inteiros |
| Estrutura grande | por cópia na pilha (ou classes de registradores) | por **referência** (ponteiro) se > 8 bytes (ou tamanho não é 1, 2, 4, 8) |
| Instrução de chamada de sistema | `syscall` (kernel) | via DLLs (`ntdll`), **não** use `syscall` direto |

> [!tip] Memorize assim
> **Linux:** *Di, Si, Dx, Cx, 8, 9* (`rdi rsi rdx rcx r8 r9`). **Windows:** *Cx, Dx, 8, 9*. E no Windows, **sempre reserve 32 bytes** de *shadow space* antes de chamar.

### 1.1 Esqueleto de função (System V)

```nasm
funcao:
    push rbp                 ; (opcional) frame pointer
    mov  rbp, rsp
    push rbx                 ; preserva o que for usar de callee-saved
    sub  rsp, 8              ; mantém rsp alinhado em 16 antes de qualquer call
    ; ... corpo ...
    add  rsp, 8
    pop  rbx
    pop  rbp
    ret
```

Na **entrada** de uma função, `rsp ≡ 8 (mod 16)` (o `call` empilhou 8 bytes). Cada `push` troca o alinhamento.

### 1.2 Esqueleto de chamada (Microsoft x64)

```nasm
    sub  rsp, 40             ; 32 de shadow space + 8 para alinhar (entrada: rsp ≡ 8 mod 16)
    mov  rcx, arg1
    mov  rdx, arg2
    call funcao
    add  rsp, 40
```

---

## 2. x86 de 32 bits

| Convenção | Argumentos | Retorno | Quem limpa a pilha | Preservados | Uso |
|-----------|------------|---------|:------------------:|-------------|-----|
| **cdecl** | pilha, da direita p/ esquerda | `eax` (`st0` para `float`) | **chamador** | `ebx, esi, edi, ebp` | padrão do C; suporta variádicas |
| **stdcall** | pilha, da direita p/ esquerda | `eax` | **função** (`ret n`) | idem | API do Windows de 32 bits |
| **fastcall** (MS) | `ecx, edx`, depois pilha | `eax` | **função** | idem | desempenho |
| **thiscall** (MS) | `this` em `ecx`, resto na pilha | `eax` | função | idem | C++ no MSVC |
| **System V i386** | pilha | `eax` | chamador | `ebx, esi, edi, ebp` | Linux 32 bits |

---

## 3. ARM

| Item | **AAPCS64** (AArch64) | **AAPCS32** (ARM 32 bits) |
|------|-----------------------|---------------------------|
| Argumentos inteiros | `x0`-`x7` (ou `w0`-`w7`) | `r0`-`r3` |
| Argumentos de ponto flutuante | `v0`-`v7` (`s0`-`s7` / `d0`-`d7`) | `s0`-`s15` / `d0`-`d7` (VFP) ou pilha (soft-float) |
| Retorno | `x0` (e `x1`); FP em `v0` | `r0` (e `r1`); FP em `s0`/`d0` |
| Resultado grande (*indirect result*) | endereço em **`x8`** | ponteiro em `r0` |
| ***Callee-saved*** | `x19`-`x28`, `x29` (FP), `v8`-`v15` (só os 64 bits baixos: `d8`-`d15`) | `r4`-`r11`, `sp`, `d8`-`d15` |
| ***Caller-saved*** | `x0`-`x15` (`x16`/`x17` = IP0/IP1, *scratch*), resto dos `v` | `r0`-`r3`, `r12` (IP), `d0`-`d7`, `d16`-`d31` |
| Endereço de retorno | **`x30` (LR)** | **`r14` (LR)** |
| *Frame pointer* | `x29` | `r11` |
| `x18` | registrador da plataforma (reservado no Windows/Apple) | — |
| Alinhamento da pilha | **16 bytes sempre** (em todo acesso via `sp`) | 8 bytes em interfaces públicas (4 bytes no mínimo, sempre) |
| Instrução de chamada | `bl alvo` / `blr xN` | `bl alvo` / `blx rN` |
| Retorno | `ret` (salta para `x30`) | `bx lr` / `pop {pc}` |

> [!warning] ARM não empilha o endereço de retorno
> `bl` **grava o retorno em LR**. Uma função que chame outra precisa **salvar LR** (`stp x29, x30, [sp, #-16]!` em AArch64) antes e restaurá-lo antes de `ret`; senão, o retorno é perdido.

### 3.1 Esqueleto AArch64

```asm
funcao:
    stp  x29, x30, [sp, #-16]!   // salva FP e LR (pré-decremento, sp continua múltiplo de 16)
    mov  x29, sp
    // ... corpo ...
    ldp  x29, x30, [sp], #16     // restaura (pós-incremento)
    ret
```

---

## 4. Tabela de chamada rápida (função de 4 argumentos inteiros)

| Arquitetura | `f(a, b, c, d)` | Retorno |
|-------------|-----------------|---------|
| x86-64 System V | `rdi, rsi, rdx, rcx` | `rax` |
| x86-64 Windows | `rcx, rdx, r8, r9` | `rax` |
| x86 cdecl | `push d; push c; push b; push a` (nessa ordem) | `eax` |
| AArch64 | `x0, x1, x2, x3` | `x0` |
| AArch32 | `r0, r1, r2, r3` | `r0` |

---

## 5. Erros comuns

> [!warning] Lista de armadilhas
> 1. **Pilha desalinhada** antes de `call` (quebra `printf`/SSE com `movaps` na libc).
> 2. **Esquecer o *shadow space*** no Windows (a função chamada sobrescreve a pilha do chamador).
> 3. **Destruir um registrador *callee-saved*** (`rbx`, `r12`-`r15`; `rdi`/`rsi` no Windows; `xmm6`-`xmm15` no Windows).
> 4. **Usar `rcx` no 4º argumento de `syscall`**: use `r10` (e `syscall` destrói `rcx` e `r11`).
> 5. **Variádica sem `al`** (`printf` com `double`, no System V).
> 6. **Usar a *red zone* em código de tratamento de interrupção/sinal** ou no Windows.
> 7. **Misturar cdecl e stdcall** (pilha vaza ou corrompe).
> 8. **Em ARM, esquecer de salvar `LR`** antes de um `bl` interno.

**Voltar:** [[11 - Recursos e Referências]] · **Ver também:** [[Cheat Sheet de Instruções]] · [[04 - Procedimentos, Stack e Calling Conventions]] · [[Glossário#Assembly (x86-64 e ARM)]]
