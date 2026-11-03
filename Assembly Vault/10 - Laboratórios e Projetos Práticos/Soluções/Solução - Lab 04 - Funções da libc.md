---
titulo: "Solução - Lab 04 - Funções da libc"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - libc
  - calling-convention
nivel: intermediario
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 04 - Funções da libc

> [!warning] Tente primeiro!
> Primeiro o [[Lab 04 - Funções da libc]]. Depois compare.

Voltar: [[Lab 04 - Funções da libc]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada com `nasm -f elf64`, ligada com `gcc` (PIE) e também com `gcc -no-pie`; as duas versões imprimem a mesma saída. `valgrind --leak-check=full` não reportou nenhum erro nem vazamento.

## 1. Código completo comentado

```nasm
; Lab 04 - Funções da libc: malloc + rand + qsort (com comparador em Assembly) + printf + free
; Montar:  nasm -f elf64 lab04.asm && gcc -no-pie lab04.o -o lab04     (ou sem -no-pie, graças ao 'wrt ..plt')
default rel
extern printf, malloc, free, qsort, srand, rand, puts
global main

N equ 10

section .rodata
fmt_hdr  db "Antes : ", 0
fmt_hdr2 db "Depois: ", 0
fmt_num  db "%d ", 0
fmt_nl   db 10, 0
fmt_sum  db "soma = %ld", 10, 0

section .text
; int cmp_int(const void *a, const void *b)  -- chamado pelo qsort
cmp_int:
    mov  eax, [rdi]
    mov  ecx, [rsi]
    xor  edx, edx
    cmp  eax, ecx
    setg dl                ; 1 se a > b
    setl al
    movzx eax, al          ; 1 se a < b
    sub  edx, eax          ; (a>b) - (a<b)  -> evita overflow de "a - b"
    mov  eax, edx
    ret

; void print_arr(const char *titulo, int *a, int n)  -- usa registradores preservados (callee-saved)
print_arr:
    push rbx
    push r12
    push r13               ; 3 pushes + ret addr = 32 bytes -> pilha ALINHADA em 16 para os calls
    mov  r12, rsi
    mov  r13d, edx
    xor  eax, eax          ; o título (RDI) já é o formato do printf
    call printf wrt ..plt
    xor  ebx, ebx
.l: cmp  ebx, r13d
    jge  .e
    lea  rdi, [fmt_num]
    mov  esi, [r12 + rbx*4]
    xor  eax, eax          ; AL = nº de registradores vetoriais (variádica!)
    call printf wrt ..plt
    inc  ebx
    jmp  .l
.e: lea  rdi, [fmt_nl]
    xor  eax, eax
    call printf wrt ..plt
    pop  r13
    pop  r12
    pop  rbx
    ret

main:
    push rbx
    push r12               ; 2 pushes + ret addr = 24 -> sub 8 para alinhar
    sub  rsp, 8
    mov  edi, 42
    call srand wrt ..plt
    mov  edi, N*4
    call malloc wrt ..plt
    test rax, rax
    jz   .fail
    mov  r12, rax          ; r12 = array
    xor  ebx, ebx
.fill:
    call rand wrt ..plt
    xor  edx, edx
    mov  ecx, 100
    div  ecx               ; edx = rand % 100
    sub  edx, 50           ; -50..49
    mov  [r12 + rbx*4], edx
    inc  ebx
    cmp  ebx, N
    jb   .fill

    lea  rdi, [fmt_hdr]
    mov  rsi, r12
    mov  edx, N
    call print_arr

    mov  rdi, r12          ; base
    mov  esi, N            ; nmemb
    mov  edx, 4            ; size
    lea  rcx, [cmp_int]    ; comparador
    call qsort wrt ..plt

    lea  rdi, [fmt_hdr2]
    mov  rsi, r12
    mov  edx, N
    call print_arr

    xor  eax, eax          ; soma com extensão de sinal
    xor  ebx, ebx
    xor  esi, esi
.s: movsxd rcx, dword [r12 + rbx*4]
    add  rsi, rcx
    inc  ebx
    cmp  ebx, N
    jb   .s
    lea  rdi, [fmt_sum]
    xor  eax, eax
    call printf wrt ..plt

    mov  rdi, r12
    call free wrt ..plt
    xor  eax, eax
    jmp  .out
.fail:
    mov  eax, 1
.out:
    add  rsp, 8
    pop  r12
    pop  rbx
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

### `cmp_int` (callback)
Recebe **ponteiros** em `RDI` e `RSI`, lê os dois `int` e devolve `(a>b) - (a<b)`. `cmp` é feito **uma vez**; `setg dl` e `setl al` leem as mesmas *flags* (instruções `setcc` não alteram flags). Como `EDX` foi zerado antes e `AL` é sobrescrito, o `movzx eax, al` limpa o resto de `EAX`. Não há `push`: é uma função folha.

### `print_arr`
Três registradores preservados (`RBX` = índice, `R12` = ponteiro do vetor, `R13D` = tamanho) mantêm os valores **durante as chamadas ao `printf`**. Três `push` + endereço de retorno = 32 bytes: a pilha já fica múltiplo de 16 em todos os `call`. O título (`RDI`) é usado diretamente como formato do primeiro `printf` (não contém `%`).

### `main`
- `push rbx`, `push r12`, `sub rsp, 8`: alinhamento (a conta está no comentário).
- `malloc(N*4)` → `R12`; `test rax, rax` / `jz .fail`.
- Laço de preenchimento: `rand() % 100 - 50` com `div ecx` (`EDX` = resto).
- `qsort(R12, N, 4, cmp_int)` com `lea rcx, [cmp_int]`.
- Soma de 64 bits com `movsxd`, `printf("soma = %ld")` (`RSI` = valor, `AL = 0`).
- `free`, `eax = 0` e **desfaz exatamente** o que foi feito no prólogo (`add rsp, 8`, `pop r12`, `pop rbx`).

### `call ... wrt ..plt`
Em um executável **PIE** (padrão), o endereço da libc só é conhecido em tempo de execução. `wrt ..plt` pede ao NASM um desvio por uma **entrada da PLT**, que salta pela **GOT** para a função real (resolvida pelo carregador dinâmico). Em `-no-pie` o `call printf` sem `wrt ..plt` também liga (testado); em PIE não. O `wrt ..plt` funciona nos dois casos, por isso é o hábito recomendado.

## 3. Variações

| Variação | Mudança |
|----------|---------|
| **`argc/argv`** | `main(int argc, char **argv)`: `EDI` = argc, `RSI` = argv. `mov rdi, [rsi+8]` / `call atoi wrt ..plt` |
| **`snprintf`** | reservar 128 bytes com `sub rsp, 128` (múltiplo de 16, o alinhamento não muda); `RDI` = `rsp`, `RSI` = 128 (tamanho) |
| **MASM x64** | `extern printf:proc`, `sub rsp, 28h` (32 do *shadow space* + 8 de alinhamento), argumentos em `RCX/RDX/R8/R9`, **`call printf`** sem `wrt` |
| **`-no-pie` e inspeção da PLT** | `objdump -d lab04np` mostra `call 401030 <printf@plt>`; `readelf -r` lista as relocações da GOT |

## 4. Análise de desempenho

Resumo na seção 6 do lab: comparador em Assembly (105 ms) e em C (108 ms) para `qsort` de 1 milhão de elementos: **praticamente iguais**. O custo está na **chamada indireta repetida** e nos acessos à memória, não na comparação.

## 5. Erros comuns

> [!warning]
> 1. **Pilha desalinhada**: `SIGSEGV` em `movaps` dentro da libc, às vezes só com `printf("%f")` (veja o experimento do lab).
> 2. **Esquecer `xor eax, eax` antes de `printf`**: `AL` com lixo pode fazer a libc salvar registradores vetoriais que você não passou.
> 3. **Guardar valores em `RAX`, `RCX`, `RDX`, `RSI`, `RDI`, `R8-R11` entre `call`s**: são destruídos. Use `RBX`, `RBP`, `R12-R15`.
> 4. **Não restaurar os registradores preservados** na saída (`main` volta com `RBX` alterado: quebra o código de inicialização).
> 5. **Comparador que devolve `a - b`**: estouro de inteiro.
> 6. **`call malloc` sem `wrt ..plt` em PIE**: erro de ligação `relocation R_X86_64_PC32 against symbol 'printf@@GLIBC_2.2.5' can not be used when making a PIE object; recompile with -fPIE`.
> 7. **Chamar `free` com ponteiro que você já sobrescreveu** (`R12` reutilizado): corrupção do *heap*.
