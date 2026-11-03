---
titulo: "Google Benchmark"
tags: [cpp, testes, benchmark, desempenho]
aliases: ["Google Benchmark", "benchmark::State", "DoNotOptimize", "Microbenchmark", "nanobench"]
tipo: biblioteca
nivel: intermediario
padrao: C++14
criado: 2026-10-24
relacionados: ["[[Profiling e Benchmarking]]", "[[Compiler Explorer]]", "[[Complexidade e Invalidação de Iteradores]]"]
---

# Google Benchmark

Biblioteca para **microbenchmarks**: executa o código muitas vezes até a medição estabilizar e reporta tempo por iteração, com suporte a parâmetros e complexidade assintótica.

```cpp
// [nv] g++ -std=c++20 -O2 -Wall -Wextra -lbenchmark -lbenchmark_main -pthread   (requer Google Benchmark; indisponível no ambiente de teste do vault)
#include <benchmark/benchmark.h>
#include <map>
#include <unordered_map>
#include <vector>

static void BM_VectorPushBack(benchmark::State& state) {
    for (auto _ : state) {                                   // o laço é medido
        std::vector<int> v;
        for (int i = 0; i < state.range(0); ++i) v.push_back(i);
        benchmark::DoNotOptimize(v.data());                  // impede que o compilador elimine o trabalho
        benchmark::ClobberMemory();
    }
    state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_VectorPushBack)->RangeMultiplier(10)->Range(10, 100000)->Complexity();

static void BM_VectorReserve(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        v.reserve(static_cast<std::size_t>(state.range(0)));
        for (int i = 0; i < state.range(0); ++i) v.push_back(i);
        benchmark::DoNotOptimize(v.data());
    }
}
BENCHMARK(BM_VectorReserve)->Arg(100000);

BENCHMARK_MAIN();
```

```cmake
find_package(benchmark REQUIRED)
add_executable(bench bench.cpp)
target_link_libraries(bench PRIVATE benchmark::benchmark)
```

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build
./build/bench --benchmark_filter=Vector --benchmark_repetitions=5 --benchmark_format=json
```

## Cuidados para medir corretamente

| Problema | Solução |
|---|---|
| Compilador elimina o código "morto" | `DoNotOptimize`, `ClobberMemory`, consumir resultado |
| Build em **Debug** | Sempre `-O2`/`-O3` (Release) |
| Frequência da CPU variável / ruído | Desative *turbo*, fixe governor `performance`, execute várias repetições, observe desvio padrão |
| Aquecimento de cache | Mesmos dados repetidos favorecem o cache: use tamanhos reais |
| Concluir sem entender | Combine com **profiler** ([[Profiling e Benchmarking]]) |
| Alternativas | **nanobench**, **Catch2 BENCHMARK**, Quick Bench (web) |

> [!warning] Microbenchmark não é desempenho do sistema
> Resultados isolados podem enganar (cache, predição de desvio, `-march`). Valide com carga real.

## Veja também

- [[Profiling e Benchmarking]]
- [[Compiler Explorer]]
- [[Escolhendo um Contêiner]]
- [[Cache e Localidade de Dados]]

## Exercício

1. Compare `std::vector` vs `std::list` para percorrer e somar N elementos com Google Benchmark.
2. Meça o efeito de `reserve` vs sem `reserve`.
