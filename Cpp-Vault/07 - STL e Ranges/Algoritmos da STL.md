---
titulo: "Algoritmos da STL"
tags: [cpp, stl, algoritmos]
aliases: ["Algoritmos", "<algorithm>", "accumulate", "erase-remove"]
tipo: referencia
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Iteradores e Categorias]]", "[[Ranges e Views]]", "[[Lambdas e Captura]]"]
---

# Algoritmos da STL

Funções genéricas de `<algorithm>`, `<numeric>` e `<ranges>` que operam sobre **intervalos**, independentes do contêiner. Prefira-os a laços "à mão": expressam a **intenção**, são testados e otimizados.

## Os mais usados

| Categoria | Algoritmos |
|---|---|
| **Busca** | `find`, `find_if`, `find_if_not`, `count`, `count_if`, `any_of`, `all_of`, `none_of`, `search`, `adjacent_find` |
| **Ordenação** | `sort`, `stable_sort`, `partial_sort`, `nth_element`, `is_sorted` |
| **Busca binária** (em ordenados) | `binary_search`, `lower_bound`, `upper_bound`, `equal_range` |
| **Transformação** | `transform`, `for_each`, `replace`, `fill`, `generate`, `iota` |
| **Remoção** | `remove`, `remove_if`, `unique`, `erase`/`erase_if` (C++20) |
| **Cópia/movimento** | `copy`, `copy_if`, `move`, `reverse`, `rotate`, `shuffle` |
| **Redução** (`<numeric>`) | `accumulate`, `reduce` (C++17), `transform_reduce`, `inner_product`, `partial_sum`, `inclusive_scan` |
| **Conjuntos/ordem** | `min`, `max`, `minmax`, `min_element`, `max_element`, `clamp` (C++17), `merge`, `set_union`, `includes` |
| **Partição** | `partition`, `stable_partition`, `partition_point` |

## Exemplos

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

struct Pessoa { std::string nome; int idade; };

int main() {
    std::vector<int> v{5, 2, 8, 1, 9, 3};

    std::sort(v.begin(), v.end());                                // 1 2 3 5 8 9
    std::cout << std::binary_search(v.begin(), v.end(), 8) << '\n';   // 1
    auto it = std::lower_bound(v.begin(), v.end(), 4);            // primeiro >= 4
    std::cout << *it << '\n';                                     // 5

    auto par = std::find_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
    std::cout << *par << '\n';                                    // 2

    std::cout << std::count_if(v.begin(), v.end(), [](int x) { return x > 3; }) << '\n';   // 3
    std::cout << std::accumulate(v.begin(), v.end(), 0) << '\n';  // 28

    std::vector<int> quad(v.size());
    std::transform(v.begin(), v.end(), quad.begin(), [](int x) { return x * x; });

    v.erase(std::remove_if(v.begin(), v.end(), [](int x) { return x < 4; }), v.end());   // erase-remove
    for (int x : v) std::cout << x << ' ';                        // 5 8 9
    std::cout << '\n';

    std::vector<Pessoa> ps{{"Ana", 30}, {"Bia", 25}, {"Caio", 30}};
    std::stable_sort(ps.begin(), ps.end(),                        // estável: mantém ordem relativa dos empates
        [](const Pessoa& a, const Pessoa& b) { return a.idade > b.idade; });
    std::cout << ps[0].nome << ps[1].nome << ps[2].nome << '\n';  // AnaCaioBia

    std::vector<int> seq(5);
    std::iota(seq.begin(), seq.end(), 10);                        // 10 11 12 13 14
    std::cout << std::clamp(20, 0, 15) << '\n';                   // 15
}
```

## A armadilha do `remove`

> [!bug] `remove`/`remove_if`/`unique` **não apagam**
> Eles apenas **movem** os elementos a manter para o início e devolvem o novo "fim lógico". O tamanho do contêiner não muda. Sempre combine com `erase`:
> ```cpp
> v.erase(std::remove(v.begin(), v.end(), x), v.end());   // idioma erase-remove
> std::erase(v, x);                                        // C++20: equivalente simples
> std::erase_if(v, pred);                                  // C++20
> ```

## Requisitos importantes

- Comparadores de `sort` precisam de **ordem fraca estrita** (use `<`, nunca `<=`): violar isso é UB e pode travar ou corromper memória.
- `lower_bound`/`binary_search` exigem intervalo **ordenado** pelo mesmo critério.
- Predicados não devem modificar elementos nem depender de estado externo mutável.

## Algoritmos paralelos (C++17)

Com uma **política de execução** o algoritmo pode rodar em paralelo/vetorizado.

```cpp
// [nv] g++ -std=c++20 -Wall -Wextra -ltbb   (libstdc++ exige Intel TBB instalado para políticas paralelas)
#include <algorithm>
#include <execution>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v(10'000'000, 1);
    std::sort(std::execution::par, v.begin(), v.end());
    long total = std::reduce(std::execution::par_unseq, v.begin(), v.end(), 0L);
    return total > 0 ? 0 : 1;
}
```

| Política | Significado |
|---|---|
| `seq` | Sequencial |
| `par` | Múltiplas threads |
| `unseq` (C++20) | Vetorização |
| `par_unseq` | Threads + vetorização |

> [!info] Mais sobre paralelismo
> Detalhes e *data races* na seção de concorrência. Versões *ranges* dos algoritmos (`std::ranges::sort(v)`) estão em [[Ranges e Views]].

## Veja também

- [[Iteradores e Categorias]]
- [[Ranges e Views]]
- [[Lambdas e Captura]]
- [[vector]]

## Exercício

1. Dado um `vector<string>`, remova as strings vazias, ordene por tamanho e depois alfabeticamente (use `stable_sort` em duas passagens).
2. Calcule a média e o desvio padrão de um vetor usando `accumulate` e `transform_reduce`.
