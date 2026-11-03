---
titulo: "TBB e OpenMP"
tags: [cpp, concorrencia, paralelismo, bibliotecas]
aliases: ["TBB", "oneTBB", "OpenMP", "parallel_for", "task_group", "#pragma omp", "Paralelismo por dados"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Algoritmos Paralelos]]", "[[Threads e jthread]]", "[[Data Races e Deadlocks]]"]
---

# TBB e OpenMP

Duas formas populares de paralelismo **de alto nível**, mais produtivas que gerenciar threads à mão.

| | **oneTBB** (Intel/UXL) | **OpenMP** |
|---|---|---|
| Tipo | Biblioteca C++ (templates, lambdas) | Diretivas `#pragma omp` + runtime (suporte do compilador) |
| Modelo | Tarefas com *work-stealing* | Regiões paralelas, laços, tarefas |
| Destaques | `parallel_for`, `parallel_reduce`, `task_group`, `concurrent_vector/queue/hash_map`, fluxo de dados (`flow::graph`) | `parallel for`, `reduction`, `simd`, `task`, `target` (GPU) |
| Ativar | Linke `-ltbb` / CMake `TBB::tbb` | `-fopenmp` (GCC/Clang), `/openmp` (MSVC) |
| Base de | `std::execution::par` do GCC | Muito usado em HPC e Fortran/C |

## OpenMP

```cpp
// g++ -std=c++20 -Wall -Wextra -fopenmp
#include <iostream>
#include <vector>

int main() {
    const int n = 1'000'000;
    std::vector<double> v(n, 0.5);
    double soma = 0.0;

    #pragma omp parallel for reduction(+ : soma)       // cada thread acumula uma cópia privada, combinada no fim
    for (int i = 0; i < n; ++i) soma += v[i];

    std::cout << soma << '\n';                          // 500000
}
```

```cmake
find_package(OpenMP REQUIRED)
target_link_libraries(app PRIVATE OpenMP::OpenMP_CXX)
```

## oneTBB

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -ltbb   (requer oneTBB instalado: libtbb-dev / vcpkg install tbb)
#include <oneapi/tbb/parallel_for.h>
#include <oneapi/tbb/parallel_reduce.h>
#include <oneapi/tbb/blocked_range.h>
#include <iostream>
#include <vector>

int main() {
    std::vector<double> v(1'000'000, 0.5);

    double soma = oneapi::tbb::parallel_reduce(
        oneapi::tbb::blocked_range<std::size_t>(0, v.size()), 0.0,
        [&](const auto& r, double acc) {                         // corpo sobre um sub-intervalo
            for (auto i = r.begin(); i != r.end(); ++i) acc += v[i];
            return acc;
        },
        std::plus<>{});                                           // combina parciais
    std::cout << soma << '\n';
}
```

```cmake
find_package(TBB REQUIRED)
target_link_libraries(app PRIVATE TBB::tbb)
```

> [!warning] Cuidados
> - **Sobre-inscrição**: não misture muitos pools (OpenMP + TBB + threads próprias) sem controle.
> - Laços com dependência entre iterações **não** são paralelizáveis diretamente.
> - Em `reduction`, ponto flutuante pode dar resultados ligeiramente diferentes por ordem de soma.
> - Use `-fsanitize=thread` com cuidado (OpenMP pode gerar falsos positivos sem runtime instrumentado).

> [!tip] Qual escolher?
> Laços numéricos simples e código C-like → OpenMP. Tarefas irregulares, estruturas concorrentes e C++ idiomático → oneTBB. Para algoritmos da STL → [[Algoritmos Paralelos]].

## Veja também

- [[Algoritmos Paralelos]]
- [[Threads e jthread]]
- [[Data Races e Deadlocks]]
- [[std execution Senders e Receivers]]

## Exercício

1. Paralelize a multiplicação de matrizes 512×512 com OpenMP e meça o *speedup*.
2. Reimplemente com TBB (`parallel_for`) e compare.
