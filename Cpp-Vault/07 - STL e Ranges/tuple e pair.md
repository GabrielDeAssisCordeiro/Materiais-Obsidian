---
titulo: "std::pair e std::tuple"
tags: [cpp, stl]
aliases: ["std::tuple", "std::pair", "tuple", "pair", "std::tie", "std::apply", "make_pair"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Structured Bindings]]", "[[map e set]]", "[[Variadic Templates e Fold Expressions]]"]
---

# `std::pair` e `std::tuple`

## `std::pair<A, B>` (`<utility>`)

Dois valores heterogêneos: `.first` e `.second`. É o `value_type` de `std::map`.

## `std::tuple<Ts...>` (`<tuple>`, C++11)

Generalização para **qualquer quantidade** de valores.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

std::tuple<int, double, std::string> dados() { return {1, 2.5, "oi"}; }

int main() {
    std::pair<std::string, int> p{"Ana", 30};
    auto p2 = std::make_pair(1, 'x');
    std::cout << p.first << p.second << p2.second << '\n';

    auto t = dados();
    std::cout << std::get<0>(t) << std::get<2>(t) << '\n';          // acesso por índice (constante)
    std::cout << std::get<double>(t) << '\n';                        // por tipo (só se único)

    auto [i, d, s] = dados();                                        // structured bindings (preferido)
    std::cout << i << d << s << '\n';

    int a; std::string b;
    std::tie(a, b, std::ignore) = dados();                           // desempacota em variáveis existentes

    // Comparação lexicográfica pronta: ideal para ordenar por múltiplos campos
    std::vector<std::tuple<int, std::string>> v{{2, "b"}, {1, "z"}, {1, "a"}};
    std::sort(v.begin(), v.end());                                   // por int e depois string
    std::cout << std::get<1>(v[0]) << '\n';                          // a

    // Usar std::tie para comparar vários campos em operator<
    struct Aluno {
        std::string nome; int idade;
        bool operator<(const Aluno& o) const { return std::tie(idade, nome) < std::tie(o.idade, o.nome); }
    };
    std::cout << (Aluno{"Ana", 20} < Aluno{"Bia", 20}) << '\n';      // 1

    // std::apply: chama função com os elementos da tupla
    auto soma = [](int x, int y) { return x + y; };
    std::cout << std::apply(soma, std::make_tuple(3, 4)) << '\n';    // 7

    std::cout << std::tuple_size_v<decltype(t)> << '\n';             // 3
}
```

## Quando **não** usar

> [!tip] `struct` nomeada é mais legível que `tuple`
> `result.first`/`std::get<2>(t)` não dizem nada. Para retornos e dados persistentes, **prefira uma `struct` com nomes**:
> ```cpp
> struct Estatistica { double media; double desvio; std::size_t n; };
> Estatistica calcula(std::span<const double>);   // chamador: auto [m, d, n] = calcula(x);
> ```
> Use `tuple` em código **genérico** (pacotes de argumentos, retorno de funções-modelo).

## Utilidades

| Função | Uso |
|---|---|
| `std::make_tuple`, `std::forward_as_tuple` | Criar tuplas (com `ref`s) |
| `std::tuple_cat(t1, t2)` | Concatenar |
| `std::apply(f, t)` | Expandir como argumentos |
| `std::tie(a, b)` | Tupla de **referências** (desempacotar/comparar) |
| `std::ignore` | Descartar um elemento |
| `std::make_from_tuple<T>(t)` | Construir um objeto |

## Veja também

- [[Structured Bindings]]
- [[map e set]]
- [[Variadic Templates e Fold Expressions]]
- [[Funções - Cpp]]

## Exercício

1. Escreva uma função que retorne `std::tuple<bool, int, std::string>` e consuma com structured bindings; depois refatore para uma `struct` e compare a legibilidade.
2. Implemente `operator<=>` para uma struct usando `std::tie` (pré-C++20) e depois `= default` (C++20).
