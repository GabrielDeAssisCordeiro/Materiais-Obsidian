---
titulo: "Solução - Lab 06 - Ordenação"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - ordenacao
  - recursao
nivel: intermediario
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 06 - Ordenação

> [!warning] Tente primeiro!
> Primeiro o [[Lab 06 - Ordenação]]. Depois compare.

Voltar: [[Lab 06 - Ordenação]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada com NASM 2.16 e ligada ao `test6.c`: `testes OK` (3 algoritmos × 4 tipos de dados × `n` de 0 a 300, mais 1 milhão de elementos no quicksort), todos conferidos contra o `qsort`.

## 1. Código completo comentado

```nasm
; Lab 06 - Ordenação de int32 (System V). Todas: void f(int32_t *a, size_t n)
default rel
global sort_bubble, sort_insertion, sort_quick

section .text
; ---------- bubble sort com parada antecipada ----------
sort_bubble:
    cmp  rsi, 2
    jb   .d
.pass:
    xor  r8d, r8d              ; trocou?
    mov  rcx, 1                ; i = 1
.in: cmp  rcx, rsi
    jae  .chk
    mov  eax, [rdi + rcx*4 - 4]
    mov  edx, [rdi + rcx*4]
    cmp  eax, edx
    jle  .nx
    mov  [rdi + rcx*4 - 4], edx
    mov  [rdi + rcx*4], eax
    mov  r8d, 1
.nx: inc rcx
    jmp  .in
.chk:
    dec  rsi                   ; o maior já está no fim
    test r8d, r8d
    jnz  .pass
.d: ret

; ---------- insertion sort ----------
sort_insertion:
    mov  rcx, 1                ; i
.o: cmp  rcx, rsi
    jae  .d
    mov  eax, [rdi + rcx*4]    ; chave
    mov  rdx, rcx              ; j = i
.s: test rdx, rdx
    jz   .p
    mov  r8d, [rdi + rdx*4 - 4]
    cmp  r8d, eax
    jle  .p
    mov  [rdi + rdx*4], r8d    ; desloca
    dec  rdx
    jmp  .s
.p: mov  [rdi + rdx*4], eax
    inc  rcx
    jmp  .o
.d: ret

; ---------- quicksort (Hoare, pivô = mediana de 3; recursão só na menor metade -> pilha O(log n); insertion em n<=16) ----------
; void sort_quick(int32_t *a, size_t n)
; Por que Hoare e não Lomuto? Com MUITOS valores repetidos o Lomuto degenera em O(n^2)
; (medimos 33 s para 1e6 elementos com 4 valores distintos). Hoare para os dois ponteiros em
; valores iguais ao pivô e divide ao meio.
sort_quick:
    push rbx
    push r12
    push r13
.top:
    cmp  rsi, 16
    ja   .part
    pop  r13
    pop  r12
    pop  rbx
    jmp  sort_insertion        ; tail call: n pequeno
.part:
    ; ordena a[0], a[mid], a[n-1] (rede de 3 comparações): min, mediana, max
    mov  rax, rsi
    shr  rax, 1                ; mid
    mov  r8d, [rdi]
    mov  r9d, [rdi + rax*4]
    mov  r10d, [rdi + rsi*4 - 4]
    cmp  r8d, r9d
    jle  .a1
    xchg r8d, r9d
.a1: cmp r9d, r10d
    jle  .a2
    xchg r9d, r10d
    cmp  r8d, r9d
    jle  .a2
    xchg r8d, r9d
.a2:
    mov  [rdi], r8d            ; a[0] <= pivô  (sentinela à esquerda)
    mov  [rdi + rax*4], r9d
    mov  [rdi + rsi*4 - 4], r10d ; a[n-1] >= pivô (sentinela à direita)
    mov  ebx, r9d              ; pivô (valor)
    mov  r11, -1               ; i
    mov  rcx, rsi              ; j = n
.l1: inc r11
    cmp  [rdi + r11*4], ebx
    jl   .l1                   ; avança i enquanto a[i] < pivô
.l2: dec rcx
    cmp  [rdi + rcx*4], ebx
    jg   .l2                   ; recua j enquanto a[j] > pivô
    cmp  r11, rcx
    jge  .end
    mov  eax, [rdi + r11*4]
    mov  edx, [rdi + rcx*4]
    mov  [rdi + r11*4], edx
    mov  [rdi + rcx*4], eax
    jmp  .l1
.end:                          ; partes: [0..j] e [j+1..n)
    lea  r13, [rcx + 1]        ; tamanho da esquerda
    mov  rax, r13              ; início da direita
    mov  rdx, rsi
    sub  rdx, rax              ; tamanho da direita
    cmp  r13, rdx
    ja   .rec_right
    ; direita maior: recorre na esquerda, itera na direita
    push rdi
    push rsi
    push rdx
    push rax
    mov  rsi, r13
    call sort_quick            ; (rdi já é a base)
    pop  rax
    pop  rdx
    pop  rsi
    pop  rdi
    lea  rdi, [rdi + rax*4]
    mov  rsi, rdx
    jmp  .top
.rec_right:
    push rdi
    push r13
    lea  rdi, [rdi + rax*4]
    mov  rsi, rdx
    call sort_quick
    pop  rsi
    pop  rdi
    jmp  .top

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

### `sort_bubble`
`RCX` percorre `1..n-1` comparando `a[i-1]` e `a[i]` (por isso `[rdi + rcx*4 - 4]`). `R8D` registra se houve troca. No fim de cada passada, `dec rsi` (o maior já está na posição final) e, se não houve troca, o vetor está ordenado: **parada antecipada** → `O(n)` em dados ordenados.

### `sort_insertion`
`EAX` guarda a chave; `RDX` é a posição `j`. O laço interno desloca `a[j-1]` para `a[j]` enquanto for maior que a chave, e só depois grava a chave. Duas condições de parada: `j = 0` (`test rdx, rdx`) ou `a[j-1] <= chave` (`jle`). É **estável**: elementos iguais mantêm a ordem.

### `sort_quick`: visão geral
1. Se `n <= 16`, **desfaz** os `push` e salta (`jmp`, *tail call*) para `sort_insertion`: a função de insertion retorna **direto** ao chamador de `sort_quick`.
2. **Mediana de 3**: `R8D = a[0]`, `R9D = a[n/2]`, `R10D = a[n-1]`; uma pequena rede de trocas deixa `min` em `R8D`, mediana em `R9D` e máximo em `R10D`, e os três são **gravados de volta**. Dois efeitos: o pivô é a mediana e `a[0] <= pivô <= a[n-1]` funcionam como **sentinelas** (os laços `.l1` e `.l2` nunca saem do vetor).
3. **Hoare**: `R11` = `i` (começa em -1), `RCX` = `j` (começa em `n`). `.l1` avança `i` enquanto `a[i] < pivô`; `.l2` recua `j` enquanto `a[j] > pivô`; se `i >= j`, termina; senão **troca** e continua. As partes são `[0..j]` e `[j+1..n)`.
4. **Recursão na menor**: calcula os dois tamanhos; recorre na menor e **volta ao topo** com a maior (`jmp .top`, que substitui `RDI`/`RSI`).

### Pilha e alinhamento
Entrada: `RSP ≡ 8 (mod 16)`. Três `push` (`rbx, r12, r13`) → `RSP ≡ 0`. Antes de `call sort_quick`, mais **quatro** `push` (no ramo "esquerda menor") ou **dois** (no outro): número **par**, o alinhamento é mantido. Esses `push` guardam `RDI`, `RSI`, tamanho e início da outra metade, que o `call` pode destruir. `RBX` é o pivô e `R13` o tamanho da esquerda, ambos **preservados** pela convenção.

> [!tip] Por que `cmp [rdi + r11*4], ebx` / `jl`?
> Comparação direta de memória com registrador: uma instrução (e uma µop fundida com o `jl`). Com os sentinelas, não é preciso testar limites dentro do laço: **menos instruções por elemento**.

## 3. Variações

| Variação | O que muda |
|----------|------------|
| **Lomuto** (pivô = último) | mais simples, mas `O(n²)` com valores repetidos ou dados ordenados (1,3 s para 200 000 elementos, 4 valores distintos) |
| **Insertion com busca binária** | menos comparações, mas o mesmo número de **deslocamentos** |
| **Rede de ordenação** | para `n ≤ 8`, só `cmp` + `cmov`, sem desvio imprevisível |
| **Introsort** | quicksort que troca para *heapsort* quando a recursão fica profunda (garante `O(n log n)`) |
| **MASM x64** | `sort_quick proc frame` ... argumentos em `RCX` (vetor) e `RDX` (n); `push` + `.allocstack` |

## 4. Análise de desempenho

Resumo na seção 6 do lab: quick 0,84 ms contra bubble 399 ms em 20 000 elementos; o quick ganha da libc por ~1,8× (comparação inline).

## 5. Erros comuns

> [!warning]
> 1. **Comparação com sinal nos índices** (`jl` em vez de `jb`): quebra quando `n` é grande ou o índice "vira negativo".
> 2. **Comparação sem sinal nos valores** (`jb` em vez de `jl`): números negativos aparecem **no fim**.
> 3. **Esquecer a parada em `j = 0`** no insertion sort: lê `a[-1]`.
> 4. **Lomuto com muitos valores iguais**: `O(n²)` e, sem a regra da menor metade, **estouro de pilha**.
> 5. **Recursão com `RDI`/`RSI` não salvos**: depois do `call`, eles contêm lixo.
> 6. **Pilha desalinhada** nos `call` recursivos.
> 7. **Particionar com `<=`/`>=` nos dois laços** de Hoare: loop infinito ou limites ultrapassados (os laços devem **parar em valores iguais** ao pivô).
> 8. **Testar só vetores aleatórios**: os bugs aparecem em dados ordenados, inversos, repetidos e com `n` pequeno (0, 1, 2, 3).
