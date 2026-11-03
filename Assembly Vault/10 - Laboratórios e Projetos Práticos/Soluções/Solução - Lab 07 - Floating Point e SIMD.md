---
titulo: "Solução - Lab 07 - Floating Point e SIMD"
aliases:
tipo: solucao
tags:
  - assembly
  - lab
  - solucao
  - nasm
  - simd
  - avx
  - fma
nivel: avancado
arquitetura:
  - x64
criado: 2026-10-21
---

# Solução - Lab 07 - Floating Point e SIMD

> [!warning] Tente primeiro!
> Primeiro o [[Lab 07 - Floating Point e SIMD]]. Depois compare.

Voltar: [[Lab 07 - Floating Point e SIMD]] · Módulo: [[10 - Laboratórios e Projetos Práticos]]

> [!success] Testada
> Montada com NASM 2.16 e ligada ao `test7.c` em uma CPU com AVX2 e FMA: `lab07 testes OK` (n = 0..200, 20 000 pontos de Mandelbrot idênticos ao C).

## 1. Código completo comentado

```nasm
; Lab 07 - Ponto flutuante e SIMD (System V). Requer AVX2+FMA nas versões *_avx
default rel
global dot_scalar, dot_avx, saxpy_scalar, saxpy_avx, norm_f32, mandel_iter

section .text
; float dot_scalar(const float *a, const float *b, size_t n)  -- 1 acumulador (limitado pela latência)
dot_scalar:
    xorps xmm0, xmm0
    xor   eax, eax
.l: cmp   rax, rdx
    jae   .d
    movss xmm1, [rdi + rax*4]
    mulss xmm1, [rsi + rax*4]
    addss xmm0, xmm1
    inc   rax
    jmp   .l
.d: ret

; float dot_avx(const float *a, const float *b, size_t n)  -- 4 acumuladores ymm + FMA + epílogo escalar
dot_avx:
    vxorps ymm0, ymm0, ymm0
    vxorps ymm1, ymm1, ymm1
    vxorps ymm2, ymm2, ymm2
    vxorps ymm3, ymm3, ymm3
    xor    eax, eax
    mov    rcx, rdx
    and    rcx, -32            ; elementos cobertos pelo laço principal (múltiplo de 32)
.big:
    cmp    rax, rcx
    jae    .rest
    vmovups ymm4, [rdi + rax*4]
    vmovups ymm5, [rdi + rax*4 + 32]
    vmovups ymm6, [rdi + rax*4 + 64]
    vmovups ymm7, [rdi + rax*4 + 96]
    vfmadd231ps ymm0, ymm4, [rsi + rax*4]
    vfmadd231ps ymm1, ymm5, [rsi + rax*4 + 32]
    vfmadd231ps ymm2, ymm6, [rsi + rax*4 + 64]
    vfmadd231ps ymm3, ymm7, [rsi + rax*4 + 96]
    add    rax, 32
    jmp    .big
.rest:
    vaddps ymm0, ymm0, ymm1
    vaddps ymm2, ymm2, ymm3
    vaddps ymm0, ymm0, ymm2
    ; redução horizontal: 8 -> 1
    vextractf128 xmm1, ymm0, 1
    vaddps xmm0, xmm0, xmm1
    vmovhlps xmm1, xmm1, xmm0
    vaddps xmm0, xmm0, xmm1
    vmovshdup xmm1, xmm0
    vaddss xmm0, xmm0, xmm1
.tail:                         ; resto (< 32 elementos): escalar
    cmp    rax, rdx
    jae    .d
    vmovss xmm1, [rdi + rax*4]
    vfmadd231ss xmm0, xmm1, [rsi + rax*4]
    inc    rax
    jmp    .tail
.d: vzeroupper
    ret

; void saxpy_scalar(float a, const float *x, float *y, size_t n)   y += a*x    (a em XMM0; x=RDI, y=RSI, n=RDX)
saxpy_scalar:
    xor   eax, eax
.l: cmp   rax, rdx
    jae   .d
    movss xmm1, [rdi + rax*4]
    mulss xmm1, xmm0
    addss xmm1, [rsi + rax*4]
    movss [rsi + rax*4], xmm1
    inc   rax
    jmp   .l
.d: ret

saxpy_avx:
    vbroadcastss ymm1, xmm0    ; a em todas as 8 posições
    xor    eax, eax
    mov    rcx, rdx
    and    rcx, -8
.v: cmp    rax, rcx
    jae    .t
    vmovups ymm2, [rsi + rax*4]
    vfmadd231ps ymm2, ymm1, [rdi + rax*4]   ; y += a*x
    vmovups [rsi + rax*4], ymm2
    add    rax, 8
    jmp    .v
.t: cmp    rax, rdx
    jae    .d
    vmovss xmm2, [rsi + rax*4]
    vfmadd231ss xmm2, xmm1, [rdi + rax*4]
    vmovss [rsi + rax*4], xmm2
    inc    rax
    jmp    .t
.d: vzeroupper
    ret

; float norm_f32(const float *a, size_t n) = sqrt(sum a[i]^2)
norm_f32:
    mov    rdx, rsi
    mov    rsi, rdi            ; b = a
    sub    rsp, 8              ; na entrada RSP ≡ 8 (mod 16); com sub 8 fica ≡ 0 antes do call (regra da ABI)
    call   dot_avx
    add    rsp, 8
    sqrtss xmm0, xmm0
    ret

; int mandel_iter(double cr, double ci, int max)   -> nº de iterações até |z|^2 > 4 (ou max)
;   cr = XMM0, ci = XMM1, max = EDI
mandel_iter:
    xorpd xmm2, xmm2           ; x = 0
    xorpd xmm3, xmm3           ; y = 0
    movsd xmm7, [quatro]
    xor   eax, eax
.l: cmp   eax, edi
    jge   .d
    movapd xmm4, xmm2
    mulsd  xmm4, xmm4          ; x²
    movapd xmm5, xmm3
    mulsd  xmm5, xmm5          ; y²
    movapd xmm6, xmm4
    addsd  xmm6, xmm5          ; x²+y²
    ucomisd xmm6, xmm7
    ja    .d                   ; escapou
    mulsd  xmm3, xmm2          ; y*x
    addsd  xmm3, xmm3          ; 2xy
    addsd  xmm3, xmm1          ; y' = 2xy + ci
    subsd  xmm4, xmm5          ; x²-y²
    addsd  xmm4, xmm0          ; x' = x²-y²+cr
    movapd xmm2, xmm4
    inc    eax
    jmp    .l
.d: ret

section .rodata
align 8
quatro dq 4.0

section .note.GNU-stack noalloc noexec nowrite progbits
```

## 2. Explicação por blocos

### `dot_avx`
- **Zerar acumuladores:** `vxorps ymm0, ymm0, ymm0` (idioma de zeragem: não espera valor antigo).
- **Laço de 32:** `rcx = n & ~31`. As quatro cargas vão para `ymm4..ymm7` e as quatro FMAs usam a memória da segunda matriz como terceiro operando (carga fundida). Quatro acumuladores = quatro cadeias de dependência independentes: com latência de FMA de 4 ciclos e 2 FMAs por ciclo seriam necessários **8** para saturar; já com **4** o ganho de 16× sobre o escalar vem do vetor de 8 e da quebra da cadeia.
- **Redução:** `ymm0..ymm3` somam-se em `ymm0`; depois `vextractf128` traz os 4 `float` de cima, `vaddps` (8 → 4), `vmovhlps` + `vaddps` (4 → 2), `vmovshdup` + `vaddss` (2 → 1).
- **Epílogo:** os últimos `n mod 32` elementos, um a um (`vfmadd231ss`). É simples e correto; a variação abaixo reduz o custo.
- **`vzeroupper`** antes do `ret`.

> [!tip] Por que a redução horizontal só no fim?
> `haddps`/shuffles custam várias µops. Dentro do laço, destruiriam o ganho. Acumule **verticalmente** (lane a lane) e reduza **uma vez**.

### `saxpy_avx`
`vbroadcastss ymm1, xmm0` replica `a`. Para `y += a*x`: carrega `y` em `ymm2`; `vfmadd231ps ymm2, ymm1, [x]` faz `ymm2 += ymm1 * x`; grava. Resto em escalar com `vfmadd231ss`. Sem `vzeroupper` no meio do laço (só no final).

### `norm_f32`
`dot_avx(a, a, n)` seguido de `sqrtss`. O `sub rsp, 8` / `add rsp, 8` mantém a pilha alinhada em 16 no `call` (a função dot não usa pilha, mas a **regra da ABI** vale sempre).

### `mandel_iter`
Variáveis em registradores (`x` em `xmm2`, `y` em `xmm3`). Cálculo: `x²` (`xmm4`), `y²` (`xmm5`), `x²+y²` (`xmm6`); `ucomisd xmm6, [quatro]` e `ja .d` (escapou). **`y'` é calculado antes de `x'`**, com o `x` antigo: `y*x` (`mulsd`), dobra (`addsd xmm3, xmm3`), soma `ci`. Depois `x' = x² − y² + cr`.

> [!note] `ucomisd` e `NaN`
> `ucomisd` com operando `NaN` ("não ordenado") liga `ZF`, `PF` e `CF`. `ja` (salta se `CF = 0` e `ZF = 0`) **não salta**: um `NaN` nunca "escapa" e o laço roda até `max`. Se quiser tratar `NaN`, teste `jp` (paridade) antes.

## 3. Variações

| Variação | O que muda |
|----------|------------|
| **Epílogo em blocos de 8** | depois do laço de 32, um laço de 8 (`vmovups` + `vfmadd231ps` em `ymm0`) e só então o escalar: até 7 elementos ficam no escalar, em vez de 31 |
| **8 acumuladores** | ganha pouco em L1 se o gargalo passa a ser as **cargas** (2 por ciclo); meça |
| **Arredondamento diferente** | FMA arredonda **uma vez**; `mulps` + `addps`, duas. Resultados diferem nos últimos bits: por isso o teste tem tolerância |
| **MASM x64** | `vmovups ymm4, ymmword ptr [rcx + rax*4]`; `float` em `XMM0-XMM3` (Windows usa a **posição** do argumento: o 1º argumento é `XMM0`, o 2º `XMM1`, mesmo se o 1º for ponteiro); `XMM6-XMM15` são **preservados** (callee-saved), com salvamento explícito |
| **AVX-512** | `zmm` com 16 `float` e máscaras `k1-k7`: o epílogo vira uma única iteração com máscara |

## 4. Análise de desempenho

Veja a seção 6 do lab: dot 16,3× mais rápido que o escalar em L1, 4,4× fora do cache; `saxpy` empata com o compilador.

## 5. Erros comuns

> [!warning]
> 1. **Passar `float` em `RDI`**: em System V, `float`/`double` vão para `XMM0..XMM7`.
> 2. **Esquecer `vzeroupper`** (ou misturar VEX e SSE legado): penalidades de transição.
> 3. **`movaps`/`vmovaps` em endereço não alinhado**: `SIGSEGV`. Use `movups`/`vmovups`, a menos que você garanta alinhamento.
> 4. **Comparar o resultado com `==`**: use tolerância; a ordem das somas muda o resultado.
> 5. **Calcular `x'` antes de `y'` no Mandelbrot** (usa `x` novo): imagem errada.
> 6. **Ler além do fim do vetor** no laço de 32: sempre `and rcx, -32` (só blocos completos).
> 7. **Esquecer que `EAX`/`RAX` guarda o índice** e usar `RAX` como retorno depois: o retorno de `float` é em `XMM0`.
> 8. **Redução horizontal dentro do laço**: destrói o ganho de SIMD.
