---
titulo: "Algoritmos paralelos"
tags: [cpp, concorrencia, paralelismo, stl, cpp17]
aliases: ["Execution policies", "std::execution::par", "par_unseq", "reduce", "transform_reduce"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Algoritmos da STL]]", "[[TBB e OpenMP]]", "[[Data Races e Deadlocks]]"]
---

# Algoritmos paralelos

> [!info] Introdução
> **C++17**, `<execution>`. Muitos algoritmos da [[Algoritmos da STL|STL]] aceitam uma **política de execução** como primeiro argumento.
> - GCC/libstdc++: implementados sobre **oneTBB** — instale `libtbb-dev` e linke com `-ltbb`.
> - MSVC: suporte nativo. libc++ (Clang): suporte parcial/experimental (confirmar na documentação).
> [!question] Verificar na documentação oficial
> Verifique o suporte de `<execution>` na versão da sua biblioteca padrão.

| Política | Significado |
|---|---|
| `std::execution::seq` | Sequencial |
| `std::execution::par` | Pode usar várias threads |
| `std::execution::par_unseq` | Threads **e** vetorização (as funções não podem usar locks) |
| `std::execution::unseq` | Só vetorização (C++20) |

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -O2 -ltbb   (precisa de oneTBB; indisponível no ambiente de teste do vault)
#include <algorithm>
#include <execution>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

int main() {
    std::vector<double> v(10'000'000);
    std::mt19937 rng{42};
    std::uniform_real_distribution<double> d{0.0, 1.0};
    std::generate(v.begin(), v.end(), [&] { return d(rng); });

    std::sort(std::execution::par, v.begin(), v.end());                   // ordenação paralela

    double soma = std::reduce(std::execution::par, v.begin(), v.end(), 0.0);           // reduce: associativo/comutativo
    double sq = std::transform_reduce(std::execution::par_unseq, v.begin(), v.end(), 0.0,
                                      std::plus<>{}, [](double x) { return x * x; });
    std::cout << soma << ' ' << sq << '\n';
}
```

## `reduce` vs `accumulate`

`std::accumulate` é **sequencial e ordenado**; `std::reduce` pode somar em qualquer ordem — exige operação **associativa e comutativa**. Em ponto flutuante o resultado pode **variar levemente** entre execuções.

> [!warning] Regras
> - As funções passadas **não podem causar data races** nem lançar exceções (exceção em política paralela → `std::terminate`).
> - `par_unseq`: sem mutex, alocação bloqueante ou qualquer sincronização na função.
> - Só vale a pena com **dados grandes** (milhares+ de elementos) e trabalho por elemento não trivial; meça!
> - Iteradores devem ser *forward* ou melhores.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v(100, 1);
    std::cout << std::reduce(v.begin(), v.end(), 0) << '\n';   // versão sem política compila sem TBB: 100
    std::cout << std::transform_reduce(v.begin(), v.end(), v.begin(), 0) << '\n';   // produto escalar: 100
}
```

## Veja também

- [[Algoritmos da STL]]
- [[TBB e OpenMP]]
- [[Data Races e Deadlocks]]
- [[Ranges e Views]]

## Exercício

1. Compare `std::sort` sequencial vs `par` em 10⁷ elementos (use `std::chrono`).
2. Mostre que `std::reduce` em `float` pode produzir resultados distintos de `accumulate`.
