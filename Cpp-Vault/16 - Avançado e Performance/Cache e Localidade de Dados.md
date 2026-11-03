---
titulo: "Cache e localidade de dados"
tags: [cpp, performance, cache]
aliases: ["Cache da CPU", "Localidade de dados", "Cache miss", "AoS vs SoA", "Prefetch", "Hierarquia de memória"]
tipo: conceito
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Stack vs Heap]]", "[[vector]]", "[[Escolhendo um Contêiner]]"]
---

# Cache e localidade de dados

A CPU é muito mais rápida que a memória principal. Para esconder a diferença há **caches** (L1, L2, L3). Um acesso que falha (*cache miss*) pode custar **dezenas a centenas de ciclos**. Em muitos programas, o desempenho é dominado por **como os dados estão dispostos**, não pelo número de instruções.

| Nível (ordem de grandeza) | Latência típica | Tamanho típico |
|---|---|---|
| Registrador | ~0–1 ciclo | bytes |
| L1 | ~4 ciclos | 32–64 KiB |
| L2 | ~12 ciclos | 256 KiB–2 MiB |
| L3 | ~40 ciclos | MiB (compartilhado) |
| RAM | ~200+ ciclos | GiB |

> [!info] Linha de cache
> A memória é transferida em **linhas de 64 bytes** (típico em x86-64 e muitos ARM). Ler 1 byte traz 64; acessos vizinhos saem "de graça" (**localidade espacial**). Reusar o mesmo dado logo em seguida é **localidade temporal**.

## Percorra memória em ordem

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <chrono>
#include <iostream>
#include <vector>

int main() {
    constexpr int N = 4096;
    std::vector<int> m(static_cast<std::size_t>(N) * N, 1);       // matriz N×N em ordem de linha (row-major)

    auto medir = [&](auto&& f) {
        auto t0 = std::chrono::steady_clock::now();
        long soma = f();
        auto t1 = std::chrono::steady_clock::now();
        std::cout << soma << ' ' << std::chrono::duration<double, std::milli>(t1 - t0).count() << " ms\n";
    };

    medir([&] {                                                    // linha por linha: sequencial → rápido
        long s = 0;
        for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) s += m[static_cast<std::size_t>(i) * N + j];
        return s;
    });
    medir([&] {                                                    // coluna por coluna: salta N*4 bytes → muitos misses
        long s = 0;
        for (int j = 0; j < N; ++j) for (int i = 0; i < N; ++i) s += m[static_cast<std::size_t>(i) * N + j];
        return s;
    });
}
```

O segundo laço costuma ser várias vezes mais lento, apesar de fazer o mesmo trabalho.

## AoS vs SoA

```cpp
// g++ -std=c++20 -O2 -Wall -Wextra
#include <iostream>
#include <vector>

struct ParticulaAoS { float x, y, z, massa; int id; char flags[44]; };   // "Array of Structs": 64 bytes por partícula

struct ParticulasSoA {                                                     // "Struct of Arrays"
    std::vector<float> x, y, z;
    explicit ParticulasSoA(std::size_t n) : x(n, 1.0f), y(n, 2.0f), z(n, 3.0f) {}
};

int main() {
    const std::size_t n = 1'000'000;
    std::vector<ParticulaAoS> aos(n);
    ParticulasSoA soa{n};

    float s1 = 0;
    for (const auto& p : aos) s1 += p.x;                                   // carrega 64 B para usar 4 B
    float s2 = 0;
    for (float v : soa.x) s2 += v;                                         // só os floats de x, contíguos (e vetorizável)
    std::cout << s1 << ' ' << s2 << '\n';
}
```

| Escolha | Quando |
|---|---|
| **AoS** | Acessa **todos** os campos juntos; poucos objetos |
| **SoA** | Processa **um campo** em muitos objetos; SIMD ([[SIMD e Vetorização - Cpp]]) |
| **AoSoA** | Híbrido (blocos de 8/16) para GPUs/SIMD |

## Regras práticas

1. Prefira **contêineres contíguos** (`std::vector`, `std::array`) a estruturas com ponteiros (`std::list`, `std::map`) — veja [[Escolhendo um Contêiner]].
2. **Compacte** structs: ordene membros por tamanho decrescente, use tipos menores ([[sizeof e alignof]]).
3. Separe dados **quentes** e **frios**.
4. Evite indireções (`vector<unique_ptr<T>>`, `vector<vector<T>>`) em laços críticos.
5. **Tile/bloqueie** laços para caber no cache (multiplicação de matrizes).
6. Dê *hints* só com medição: `__builtin_prefetch`.
7. Veja [[False Sharing]] para o problema oposto em multithreading.

> [!tip] Meça
> Use `perf stat -e cache-misses,cache-references ./prog` e ferramentas de [[Profiling e Benchmarking]] (cachegrind, VTune).

## Veja também

- [[False Sharing]]
- [[SIMD e Vetorização - Cpp]]
- [[Escolhendo um Contêiner]]
- [[sizeof e alignof]]
- [[Profiling e Benchmarking]]

## Exercício

1. Execute o primeiro exemplo e registre a razão entre os dois tempos.
2. Converta uma simulação de partículas de AoS para SoA e meça.
