---
titulo: "Solução - Lab 03 - Manipulação de Strings e Arrays"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - strings
  - arrays
nivel: iniciante
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 03 - Manipulação de Strings e Arrays

> [!warning] Tente primeiro!
> Primeiro o [[Lab 03 - Manipulação de Strings e Arrays]]. Depois compare.

Voltar: [[Lab 03 - Manipulação de Strings e Arrays]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada com NASM 2.16 e ligada ao `test3.c` (`gcc -O2 -Wall`): imprime `lab03 OK`. Também passou no `valgrind` sem erros. Todo o código abaixo é o arquivo testado.

## 1. Código completo comentado

```nasm
; Lab 03 - Strings e arrays (System V; funções chamáveis de C)
default rel
global str_len, str_rev, str_upper, str_is_pal, arr_sum, arr_minmax, str_find

section .text
; size_t str_len(const char *s)
str_len:
    xor  eax, eax
.l: cmp  byte [rdi + rax], 0
    je   .d
    inc  rax
    jmp  .l
.d: ret

; void str_rev(char *s)  -- inverte no lugar
str_rev:
    mov  rsi, rdi
.f: cmp  byte [rsi], 0
    je   .e
    inc  rsi
    jmp  .f
.e: dec  rsi               ; rsi = último caractere
.s: cmp  rdi, rsi
    jae  .d
    mov  al, [rdi]
    mov  cl, [rsi]
    mov  [rdi], cl
    mov  [rsi], al
    inc  rdi
    dec  rsi
    jmp  .s
.d: ret

; void str_upper(char *s)  -- 'a'..'z' -> 'A'..'Z'
str_upper:
.l: movzx eax, byte [rdi]
    test al, al
    jz   .d
    lea  ecx, [rax - 'a']
    cmp  cl, 25
    ja   .n
    sub  byte [rdi], 32
.n: inc  rdi
    jmp  .l
.d: ret

; int str_is_pal(const char *s) -> 1/0 (compara exatamente, sem ignorar espaços)
str_is_pal:
    mov  rsi, rdi
.f: cmp  byte [rsi], 0
    je   .e
    inc  rsi
    jmp  .f
.e: dec  rsi
.c: cmp  rdi, rsi
    jae  .yes
    mov  al, [rdi]
    cmp  al, [rsi]
    jne  .no
    inc  rdi
    dec  rsi
    jmp  .c
.yes: mov eax, 1
    ret
.no: xor eax, eax
    ret

; int64_t arr_sum(const int32_t *a, size_t n)  -- soma com extensão de sinal
arr_sum:
    xor  eax, eax
    test rsi, rsi
    jz   .d
    xor  ecx, ecx
.l: movsxd rdx, dword [rdi + rcx*4]
    add  rax, rdx
    inc  rcx
    cmp  rcx, rsi
    jb   .l
.d: ret

; void arr_minmax(const int32_t *a, size_t n, int32_t *min, int32_t *max)  (n >= 1)
arr_minmax:
    mov  eax, [rdi]        ; min
    mov  r8d, eax          ; max
    mov  r9d, 1
.l: cmp  r9, rsi
    jae  .d
    mov  r10d, [rdi + r9*4]
    cmp  r10d, eax
    cmovl eax, r10d
    cmp  r10d, r8d
    cmovg r8d, r10d
    inc  r9
    jmp  .l
.d: mov  [rdx], eax
    mov  [rcx], r8d
    ret

; const char *str_find(const char *hay, const char *needle) -> ponteiro ou NULL (busca ingênua)
str_find:
    cmp  byte [rsi], 0
    je   .ret_hay          ; agulha vazia -> hay
.o: cmp  byte [rdi], 0
    je   .nf
    mov  r8, rdi
    mov  r9, rsi
.i: mov  al, [r9]
    test al, al
    jz   .ret_hay          ; casou tudo: o início do casamento é RDI (r8 só andou)
    cmp  al, [r8]
    jne  .nx
    inc  r8
    inc  r9
    jmp  .i
.nx: inc rdi
    jmp  .o
.nf: xor eax, eax
    ret
.ret_hay:
    mov  rax, rdi
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

### `str_len`
`RAX` faz duas funções: índice do laço e resultado. `cmp byte [rdi + rax], 0` lê **um byte** (sem `movzx`, porque só comparamos). A função devolve quando encontra o terminador; o índice dele **é** o tamanho.

### `str_rev` e `str_is_pal`
Ambas começam achando o fim e usam **dois ponteiros** que se aproximam (`jae` termina quando `rdi >= rsi`, o que cobre a string vazia, em que `rsi` fica uma posição antes de `rdi`, e o caso dos ponteiros iguais, o caractere central). Em `str_rev` a troca usa `AL` e `CL` como registradores temporários (nenhuma memória extra, nenhum `xchg [mem]`, que é **lento** porque tem `lock` implícito).

> [!tip] Por que não `xchg al, [rdi]`?
> `xchg` com operando de memória trava o barramento (`lock` implícito) e custa dezenas de ciclos. Duas cargas e dois armazenamentos são muito mais baratos.

### `str_upper`
`lea ecx, [rax - 'a']` calcula `c - 'a'` **sem alterar flags** e sem destruir `RAX`; `cmp cl, 25` + `ja` testa `0 <= c-'a' <= 25` com uma só comparação sem sinal. `sub byte [rdi], 32` altera direto na memória (`read-modify-write`).

### `arr_sum`
`movsxd rdx, dword [rdi + rcx*4]` lê `int32_t` e **estende o sinal** para 64 bits antes de somar em `RAX`. O teste `test rsi, rsi` / `jz` cobre `n = 0`.

### `arr_minmax`
Mínimo em `EAX`, máximo em `R8D`, ambos iniciados com `a[0]`. Dois `cmov` por elemento (um por `cmp`) fazem o laço **sem desvio dependente dos dados**: o único `jcc` é o do contador. No fim, os resultados vão para os ponteiros em `RDX` e `RCX`, que ficaram **intocados** durante o laço (por isso o laço usa `R9` e `R10`, e não eles).

### `str_find`
Dois laços aninhados. `R8`/`R9` percorrem a tentativa atual; `RDI` marca onde ela começou, então, quando `*R9` chega ao zero (agulha toda casada), o resultado é `RDI`. Agulha vazia devolve `hay`, como `strstr`.

## 3. Variações

| Variação | O que muda |
|----------|------------|
| **`count_vowels` por máscara** | `mov r8d, 0x104111` ... `or ecx, 0x20` (minúscula) ... `sub ecx,'a'` / `cmp ecx,25` / `ja` ... `bt r8d, ecx` / `adc eax, 0` |
| **`arr_sum` com SSE2** | `movdqu` + `paddd` (4 somas por instrução), mas **cuidado**: `paddd` soma em 32 bits e estoura; para somar em 64 bits, estenda antes (`pmovsxdq`, SSE4.1) |
| **MASM x64** | `str_len proc` ... `cmp byte ptr [rcx + rax], 0` ... `str_len endp`; o ponteiro chega em `RCX` |
| **Versão com `repne scasb`** | `xor eax,eax` / `mov rcx,-1` / `repne scasb` / `not rcx` / `lea rax,[rcx-1]`: curta, mas **mais lenta** que o laço (módulo 09, experimento 5.6) |

## 4. Análise de desempenho

Veja a seção 6 do lab: `str_len` à mão é 51× mais lenta que a libc, e `arr_sum` escalar é 2× mais lenta que o `gcc -O3`. O ganho de SIMD **não é mágico**: vem de processar vários elementos por instrução e de quebrar dependências ([[09 - Otimização, SIMD e Performance]]).

## 5. Erros comuns

> [!warning]
> 1. **`mov eax, [rdi + rcx*4]` em vez de `movsxd`**: soma de negativos sai errada (zero-extensão).
> 2. **Usar `ecx` como índice e depois endereçar com `rcx`** sem zerar a parte alta (em 64 bits, escrever em `ecx` **zera** a parte alta; escrever em `cl` **não**).
> 3. **String vazia em `str_rev`**: sem `jae`/comparação sem sinal, `rsi = rdi - 1` iria "inverter" bytes fora da string.
> 4. **Destruir `RDX`/`RCX` antes de gravar o mínimo/máximo** em `arr_minmax`.
> 5. **Esquecer que `cmp cl, 25` é sem sinal** quando se testa o intervalo com `ja`/`jbe` (com `jg`/`jle`, o truque falha).
> 6. **Esquecer `section .note.GNU-stack`**: o `ld` avisa que a pilha ficaria executável.
