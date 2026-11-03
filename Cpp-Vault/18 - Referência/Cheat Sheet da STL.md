---
titulo: "Cheat sheet: STL"
tags: [cpp, referencia, cheat-sheet, stl, algoritmos]
aliases: ["Cheat sheet STL", "Resumo STL", "Folha de consulta STL"]
tipo: referencia
nivel: iniciante
padrao: C++23
criado: 2026-10-24
relacionados: ["[[Visão Geral da STL]]", "[[Escolhendo um Contêiner]]", "[[Algoritmos da STL]]"]
---

# Cheat sheet: STL

## Contêineres: escolha rápida

| Preciso de... | Use | Complexidade-chave |
|---|---|---|
| Sequência contígua (padrão) | `std::vector` | acesso O(1), `push_back` O(1) amort., inserir no meio O(n) |
| Tamanho fixo em compilação | `std::array` | O(1) |
| Fila dupla | `std::deque` | `push` nas pontas O(1) |
| Inserção/remoção O(1) com iterador | `std::list` / `forward_list` | busca O(n) |
| Ordenado por chave | `std::map` / `set` (`multi*`) | O(log n) |
| Busca média O(1) | `std::unordered_map` / `unordered_set` | O(1) médio, O(n) pior |
| Ordenado, compacto (C++23) | `std::flat_map` / `flat_set` | busca O(log n), inserção O(n) |
| Pilha / fila / prioridade | `std::stack` / `queue` / `priority_queue` | O(1) / O(1) / O(log n) |
| Visão contígua | `std::span` | O(1) |
| Visão de texto | `std::string_view` | O(1) |
| Bits | `std::bitset<N>` / `vector<bool>` | — |

## Operações essenciais

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <optional>
#include <ranges>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    std::vector<int> v{5, 3, 8, 1, 9, 2};
    v.push_back(7);  v.emplace_back(4);  v.insert(v.begin(), 0);  v.erase(v.begin());
    v.reserve(100);  v.shrink_to_fit();

    std::sort(v.begin(), v.end());                                          // ordena
    auto it = std::lower_bound(v.begin(), v.end(), 5);                      // busca binária (precisa estar ordenado)
    bool existe = std::binary_search(v.begin(), v.end(), 8);
    auto f = std::find(v.begin(), v.end(), 9);
    auto cnt = std::count_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });
    int soma = std::accumulate(v.begin(), v.end(), 0);
    auto [mn, mx] = std::minmax_element(v.begin(), v.end());
    v.erase(std::remove_if(v.begin(), v.end(), [](int x) { return x > 8; }), v.end());   // erase-remove
    std::reverse(v.begin(), v.end());
    std::vector<int> d(v.size());
    std::transform(v.begin(), v.end(), d.begin(), [](int x) { return x * x; });

    // Ranges (C++20)
    auto pares = v | std::views::filter([](int x) { return x % 2 == 0; }) | std::views::transform([](int x) { return x * 10; });
    for (int x : pares) std::cout << x << ' ';
    std::ranges::sort(v, std::greater{});

    std::map<std::string, int> m{{"a", 1}};
    m["b"] = 2;  m.emplace("c", 3);
    if (auto p = m.find("a"); p != m.end()) std::cout << p->second;
    for (const auto& [k, val] : m) std::cout << k << val;
    std::unordered_map<std::string, int> h;  ++h["x"];  h.contains("x");     // contains: C++20
    std::set<int> s{3, 1, 2};  s.insert(2);                                  // sem duplicatas
    std::optional<int> o = f != v.end() ? std::optional<int>{*f} : std::nullopt;

    std::cout << *it << existe << cnt << soma << *mn << *mx << o.value_or(-1) << '\n';
}
```

## Invalidação de iteradores (resumo)

| Contêiner | Inserção | Remoção |
|---|---|---|
| `vector` | Invalida **tudo** se realocar; senão do ponto em diante | Do ponto em diante |
| `deque` | Invalida tudo (inserção no meio); nas pontas invalida iteradores (referências ok) | Pontas: só o removido |
| `list` / `forward_list` | **Nunca** | Só o removido |
| `map`/`set` | Nunca | Só o removido |
| `unordered_*` | Rehash invalida iteradores (referências ok) | Só o removido |

Detalhes em [[Complexidade e Invalidação de Iteradores]].

## Algoritmos mais usados

| Categoria | Funções |
|---|---|
| Busca | `find`, `find_if`, `count`, `any_of`/`all_of`/`none_of`, `binary_search`, `lower_bound`, `search` |
| Modificação | `copy`, `copy_if`, `transform`, `replace`, `fill`, `remove`/`remove_if` + `erase`, `unique`, `reverse`, `rotate`, `shuffle` |
| Ordenação | `sort`, `stable_sort`, `partial_sort`, `nth_element`, `is_sorted` |
| Numéricos | `accumulate`, `reduce`, `inner_product`, `partial_sum`, `iota`, `gcd`, `lcm` |
| Conjuntos (ordenados) | `merge`, `set_union`, `set_intersection`, `set_difference` |
| Heap | `make_heap`, `push_heap`, `pop_heap` |

> [!tip] Dica
> Prefira `std::ranges::` (C++20) quando possível; use projeções (`std::ranges::sort(v, {}, &T::campo)`).

## Veja também

- [[Visão Geral da STL]]
- [[Escolhendo um Contêiner]]
- [[Algoritmos da STL]]
- [[Ranges e Views]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Dado um `vector<string>`, remova duplicatas mantendo a ordem original (use `unordered_set`).
2. Escreva um *one-liner* com ranges que retorne os 3 maiores números pares.
