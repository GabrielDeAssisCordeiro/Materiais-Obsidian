---
titulo: "Lab 04 - Funções da libc"
aliases:
  - Lab 04
  - Funções da libc
tipo: lab
tags:
  - assembly
  - lab
  - nasm
  - libc
  - calling-convention
  - stack
  - x64
nivel: intermediario
arquitetura:
  - x64
criado: 2026-10-21
---

# Lab 04 - Funções da libc

> [!abstract] Resumo
> Agora é o **Assembly que chama a libc**: `srand`, `rand`, `malloc`, `printf`, `qsort`, `free`. Você escreverá um `main` em NASM que sorteia 10 inteiros, ordena com `qsort` usando um **comparador escrito em Assembly** (uma *callback*) e imprime antes e depois. O foco: **alinhamento da pilha em 16 bytes**, registradores **preservados** (*callee-saved*), funções **variádicas** (`AL`) e como a **PLT/GOT** entra no jogo.

Voltar ao índice: [[00 - Índice]] · Módulo: [[10 - Laboratórios e Projetos Práticos]] · Anterior: [[Lab 03 - Manipulação de Strings e Arrays]] · Próximo: [[Lab 05 - Sistema de Arquivos Simples]] · Solução: [[Solução - Lab 04 - Funções da libc]]

**Pré-requisitos:** [[04 - Procedimentos, Stack e Calling Conventions]] (leitura obrigatória), [[05 - Entrada-Saída e System Calls]], [[07 - Assembly Avançado (x86-x64)]] (PIC, PLT e GOT).

Tags: #assembly #lab #nasm #libc #calling-convention #stack

---

## 1. Objetivos

- Chamar funções da libc com a ABI System V (`RDI, RSI, RDX, RCX, R8, R9`), sem escrever `_start`: o ponto de entrada passa a ser **`main`**.
- Manter a **pilha alinhada em 16 bytes** no momento de cada `call`.
- Escolher onde guardar valores que devem **sobreviver a chamadas**: `RBX, RBP, R12-R15` (*callee-saved*), e salvá-los/restaurá-los.
- Chamar **funções variádicas** (`printf`): `AL` = nº de registradores vetoriais usados.
- Escrever uma **função de *callback*** (comparador do `qsort`).
- Entender `call printf wrt ..plt` e a diferença entre executável **PIE** e `-no-pie`.

> [!note] NASM (Linux) × MASM (Windows)
> No **Windows x64**: argumentos em `RCX, RDX, R8, R9`, **32 bytes de *shadow space*** reservados pelo chamador, sem `AL` para variádicas, e a libc é a UCRT (`printf` etc.) ou a Windows API. A regra do **alinhamento em 16** é a mesma. Veja [[Cheat Sheet de Calling Conventions]].

## 2. Material de partida (*starter code*)

```nasm
; starter04.asm - ESQUELETO do Lab 04: chamando a libc a partir do Assembly
;   nasm -f elf64 lab04.asm -o lab04.o && gcc lab04.o -o lab04
default rel
extern printf, malloc, free, qsort, srand, rand
global main

N equ 10

section .rodata
fmt_num db "%d ", 0
fmt_nl  db 10, 0

section .text
; int cmp_int(const void *a, const void *b)     comparador do qsort: <0, 0 ou >0
cmp_int:
    ; TODO (Passo 3): devolver (a > b) - (a < b), SEM fazer "a - b" (pode estourar)
    xor  eax, eax
    ret

main:
    push rbx
    push r12                 ; 2 pushes + endereço de retorno = 24 bytes  ->  sub 8 alinha em 16
    sub  rsp, 8

    ; TODO (Passo 1): srand(42); r12 = malloc(N * 4)            (confira se malloc devolveu NULL)
    ; TODO (Passo 2): preencher com rand() % 100 - 50
    ; TODO (Passo 3): imprimir o vetor com printf("%d ", ...)    (AL = 0 antes de chamar função variádica)
    ; TODO (Passo 4): qsort(r12, N, 4, cmp_int)  e imprimir de novo
    ; TODO (Passo 5): free(r12)

    xor  eax, eax            ; return 0
    add  rsp, 8
    pop  r12
    pop  rbx
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
```

```bash
nasm -f elf64 lab04.asm -o lab04.o
gcc lab04.o -o lab04          # gcc faz a ligação com a libc e cria o executável (PIE por padrão)
./lab04
```

> [!question] Por que `gcc` e não `ld`?
> O `gcc` já sabe onde estão a libc, o carregador dinâmico (`ld-linux`) e o código de inicialização (`crt1.o`), que chama o **seu `main`** depois de preparar a libc. Ligar à mão com `ld` é possível, mas trabalhoso (módulo [[05 - Entrada-Saída e System Calls]]).

## 3. Passo a passo

### Passo 1: alinhamento e *prólogo* do `main`
Na entrada de uma função, `RSP ≡ 8 (mod 16)` (o endereço de retorno acabou de ser empilhado). Antes de **cada** `call`, `RSP` precisa ser múltiplo de 16. Regra prática: conte os `push` (8 bytes cada); com **número ímpar de `push`**, o `RSP` já está alinhado; com **par**, faça `sub rsp, 8`. O esqueleto usa 2 `push` + `sub rsp, 8`.

```mermaid
flowchart LR
    A["entrada de main<br/>RSP ≡ 8"] --> B["push rbx<br/>RSP ≡ 0"]
    B --> C["push r12<br/>RSP ≡ 8"]
    C --> D["sub rsp, 8<br/>RSP ≡ 0 ✔"]
    D --> E["call ... (alinhado)"]
```

### Passo 2: `srand`, `malloc` e preenchimento
`srand(42)`; `malloc(N*4)` devolve o ponteiro em `RAX`, que você guarda em **`R12`** (preservado: sobrevive às chamadas seguintes). Confira se é `NULL`. Para cada `i`, chame `rand()` e calcule `rand() % 100 - 50` com `div` (lembre-se: `xor edx, edx` antes, e o **resto fica em `EDX`**).

### Passo 3: imprimir com `printf` (função variádica)
`printf("%d ", x)`: `RDI` = formato, `ESI` = `x` e **`xor eax, eax`** (zero registradores vetoriais). **Sem isso, o comportamento é indefinido.** Faça `print_arr` como função auxiliar; ela usa `push rbx / r12 / r13` (3 `push` = pilha alinhada para os `call`).

### Passo 4: o comparador e o `qsort`
`qsort(base, nmemb, size, cmp)` → `RDI, RSI, RDX, RCX`. O comparador recebe **ponteiros** para dois elementos (`RDI`, `RSI`) e devolve `<0`, `0` ou `>0`. Escreva `(a > b) - (a < b)` com `setg`/`setl`. **Nunca** devolva `a - b`: para `INT_MIN` e `1`, a subtração estoura e inverte a ordem.

> [!tip] Endereço de uma função em código PIE
> `lea rcx, [cmp_int]` (relativo a `RIP`) dá o endereço da função, sem relocação de texto.

### Passo 5: somar com extensão de sinal e liberar
Some os elementos em 64 bits (`movsxd`), imprima com `printf("soma = %ld\n", ...)` e chame `free(r12)`. Devolva 0 em `EAX` (código de saída).

## 4. Desafios progressivos

| Nível | Desafio | Dica |
|:-----:|---------|------|
| ★ | Ler `N` de `argv[1]` com `atoi` (`main(int argc, char **argv)`: `EDI`, `RSI`) | `mov rdi, [rsi + 8]` e `call atoi` |
| ★ | Imprimir **mínimo e máximo** com `printf("%d %d\n", ...)` | 3º argumento em `EDX` |
| ★★ | Ordem **decrescente** (troque o comparador) | inverta os operandos do `sub` |
| ★★ | `snprintf` + `puts`: montar a linha em um *buffer* de 128 bytes na pilha | `sub rsp, 128` (múltiplo de 16: não altera o alinhamento) |
| ★★ | Sorteie `double`s e imprima com `%f` (AL = 1; valor em `XMM0`) | cuidado com o alinhamento: este é o caso que **quebra** (veja a seção 6) |
| ★★★ | Escrever o **próprio `qsort`** reaproveitando o [[Lab 06 - Ordenação]] e comparar com a libc | seção 6 |
| ★★★ | Compilar com `-no-pie` e inspecionar a PLT com `objdump -d` | `call printf@plt`, `jmp *GOT` |

## 5. Verificação

```bash
./lab04
# Antes : 16 -10 31 -9 -38 8 -29 -10 -15 -7
# Depois: -38 -29 -15 -10 -10 -9 -7 8 16 31
# soma = -63

valgrind -q --leak-check=full ./lab04     # nenhuma mensagem = sem vazamento e sem acesso inválido
```

Os números são **os mesmos em qualquer execução** porque `srand(42)` fixa a semente (com a mesma glibc). Confira também que `Depois` está em ordem crescente.

## 6. Análise de desempenho (e o experimento do alinhamento)

**Alinhamento de pilha: o erro que só aparece às vezes.** Este programa de 10 linhas chama `printf("%f")` **sem** o `sub rsp, 8`:

```nasm
default rel
extern printf
global main
section .rodata
fmt db "x = %f", 10, 0
d   dq 1.5
section .text
main:                          ; na entrada RSP ≡ 8 (mod 16): SEM 'sub rsp, 8', o call abaixo fica DESALINHADO
%ifdef ALINHAR
    sub  rsp, 8
%endif
    lea  rdi, [fmt]
    movsd xmm0, [d]
    mov  eax, 1                ; 1 registrador vetorial usado
    call printf wrt ..plt
%ifdef ALINHAR
    add  rsp, 8
%endif
    xor  eax, eax
    ret
section .note.GNU-stack noalloc noexec nowrite progbits
```

```bash
nasm -f elf64 mis.asm -o mis_bad.o && gcc mis_bad.o -o mis_bad && ./mis_bad
# Segmentation fault   (código de saída 139)
nasm -f elf64 -dALINHAR mis.asm -o mis_ok.o && gcc mis_ok.o -o mis_ok && ./mis_ok
# x = 1.500000
```

No GDB: `=> __printf+54: movaps %xmm0,-0x80(%rbp)`. A glibc salva os registradores vetoriais com **`movaps`**, que exige endereço alinhado em 16: `SIGSEGV`. Detalhe importante: o **mesmo erro** no `main` do `lab04` (sem `sub rsp, 8`) **não** quebrou nesta máquina, porque `printf("%d")` não usa `movaps`. **Código desalinhado "funciona" até o dia em que quebra** (outra versão da libc, outro formato).

**Custo da callback.** `qsort` de 1 000 000 de `int`:

| Comparador | Tempo |
|------------|:-----:|
| em Assembly (`cmp_int`) | 105,4 ms |
| em C (`-O2`) | 108,3 ms |

> [!tip] Lição
> O comparador **não é o gargalo**: o custo do `qsort` está nas ~20 milhões de **chamadas indiretas** e nos acessos à memória. Escrever o comparador em Assembly rende ~3% (ruído). Para ganhar de verdade, ordene sem callback (seu quicksort do [[Lab 06 - Ordenação]] ordena 1 milhão de `int32` em ~60 ms contra ~110 ms do `qsort`, porque compara **inline**).

## 7. Próximo passo

Veja a [[Solução - Lab 04 - Funções da libc|solução]] e siga para o [[Lab 05 - Sistema de Arquivos Simples]], de volta ao mundo **sem libc**, só com syscalls: `open`, `read`, `write`, `close`.

> [!abstract] O que você praticou
> `main` em Assembly, alinhamento em 16, registradores *callee-saved*, funções variádicas (`AL`), *callbacks*, PLT/`wrt ..plt`, `valgrind` e o *debug* de `SIGSEGV` em `movaps`.
