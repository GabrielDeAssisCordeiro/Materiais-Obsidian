---
titulo: "SIMD e Vetorização - Cpp"
tags: [cpp, performance, simd, avx]
aliases: ["Vetorização", "AVX2", "AVX-512", "NEON", "SSE", "Intrinsics", "std::simd", "auto-vetorização", "Highway", "xsimd"]
tipo: conceito
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Cache e Localidade de Dados]]", "[[Otimizações do Compilador LTO e PGO]]", "[[Algoritmos Paralelos]]"]
---

# SIMD e Vetorização - Cpp

**SIMD** (*Single Instruction, Multiple Data*): uma instrução opera em **vários elementos** de uma vez (registradores de 128/256/512 bits).

| Arquitetura | Extensões | Largura |
|---|---|---|
| x86-64 | SSE2 (base), **AVX2**, AVX-512 | 128 / 256 / 512 bits |
| ARM64 | **NEON**, SVE/SVE2 | 128 bits / escalável |
| WebAssembly | SIMD128 | 128 bits |

Com AVX2, `float` (32 bits) → **8 somas por instrução**.

## Três caminhos (do mais fácil ao mais controlado)

1. **Auto-vetorização** pelo compilador (`-O3`, ou `-O2` em GCC 12+/Clang): escreva laços simples sobre dados contíguos.
2. **Bibliotecas/abstrações**: `std::simd` (C++26, `<simd>`), **xsimd**, **Highway**, **Eigen**, OpenMP `#pragma omp simd`.
3. **Intrinsics** (`<immintrin.h>`): máximo controle, código específico da arquitetura.

### 1. Ajude o compilador

```cpp
// g++ -std=c++20 -O3 -march=x86-64-v3 -fopt-info-vec -Wall -Wextra
#include <cstddef>
#include <iostream>
#include <vector>

// __restrict (extensão) promete que a e b não se sobrepõem
void saxpy(float a, const float* __restrict x, float* __restrict y, std::size_t n) {
    for (std::size_t i = 0; i < n; ++i) y[i] += a * x[i];          // laço vetorizável: sem dependência entre iterações
}

int main() {
    std::vector<float> x(1024, 1.0f), y(1024, 2.0f);
    saxpy(3.0f, x.data(), y.data(), x.size());
    std::cout << y[0] << '\n';                                      // 5
}
```

`-fopt-info-vec` (GCC) ou `-Rpass=loop-vectorize` (Clang) informam o que foi vetorizado; veja o assembly no [[Compiler Explorer]].

### 3. Intrinsics AVX2

```cpp
// g++ -std=c++20 -O2 -mavx2 -mfma -Wall -Wextra
// ATENÇÃO: só execute em CPUs com AVX2/FMA. O exemplo verifica o suporte em tempo de execução.
#include <cstddef>
#include <immintrin.h>
#include <iostream>
#include <vector>

float soma_avx2(const float* p, std::size_t n) {
    __m256 acc = _mm256_setzero_ps();
    std::size_t i = 0;
    for (; i + 8 <= n; i += 8) acc = _mm256_add_ps(acc, _mm256_loadu_ps(p + i));   // 8 floats por vez
    alignas(32) float tmp[8];
    _mm256_store_ps(tmp, acc);
    float s = 0;
    for (float v : tmp) s += v;
    for (; i < n; ++i) s += p[i];                                                    // resto
    return s;
}

int main() {
    std::vector<float> v(1000, 1.0f);
    if (__builtin_cpu_supports("avx2")) std::cout << soma_avx2(v.data(), v.size()) << '\n';   // 1000
    else std::cout << "AVX2 indisponível\n";
}
```

## `std::simd` (C++26)

```cpp
// [nv] g++ -std=c++26 -O2 -Wall -Wextra   (ilustrativo; <simd> só em compiladores/bibliotecas muito recentes)
#include <simd>
#include <iostream>

int main() {
    namespace dx = std::datapar;                                       // nomes finais podem variar entre versões do rascunho
    // Ideia: dx::vec<float> v = 1.0f; v += v; reduzir com dx::reduce(v)
}
```

> [!question] Verificar na documentação oficial
> A API final de `<simd>` (C++26) e sua disponibilidade nos compiladores: consulte cppreference e as notas de versão.

## Detecção em execução e portabilidade

| Técnica | Uso |
|---|---|
| `__builtin_cpu_supports("avx2")` | Escolher implementação em runtime (GCC/Clang) |
| *Function multiversioning* (`__attribute__((target_clones("avx2","default")))`) | O compilador gera várias versões e despacha |
| **Highway/xsimd** | Dispatch dinâmico portátil |
| `-march=x86-64-v3` | Define um piso moderno (AVX2) para todo o binário |

> [!warning] Cuidados
> - Dados **não alinhados** e *tails* (resto do laço) exigem tratamento.
> - Ponto flutuante: reduzir em ordem diferente muda o resultado ([[Algoritmos Paralelos]]).
> - **AVX-512** pode reduzir a frequência em algumas CPUs: meça.
> - Prefira **SoA** para vetorizar ([[Cache e Localidade de Dados]]).

## Veja também

- [[Cache e Localidade de Dados]]
- [[Otimizações do Compilador LTO e PGO]]
- [[Eigen e Álgebra Linear]]
- [[Cpp em HPC e GPU]]
- [[Compiler Explorer]]

## Exercício

1. Veja o assembly de `saxpy` em `-O2` e `-O3 -march=x86-64-v3` e identifique instruções `vfmadd`.
2. Implemente produto escalar com AVX2 e compare com `std::inner_product`.
