---
titulo: "Ranges e views"
tags: [cpp, stl, ranges, views, cpp20, cpp23]
aliases: ["Views", "std::ranges", "std::views", "Pipelines", "Adaptadores de range", "ranges::to"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Algoritmos da STL]]", "[[Iteradores e Categorias]]", "[[Concepts e requires]]"]
---

# Ranges e views

> [!info] Introdução
> **C++20** (`<ranges>`). Suporte: GCC 10+ (maduro em 12+), Clang 15+ (com libc++ 15+), MSVC 2019 16.10+. Várias adições são do **C++23** (`ranges::to`, `zip`, `enumerate`, `chunk`, `join_with`...).
> [!question] Verificar na documentação oficial
> Confirme em cppreference (*Compiler support* → C++23) a versão do seu compilador para as views de C++23.

## Ideias principais

- **Range**: qualquer coisa com `begin()` e `end()` (contêineres, arrays, strings, views).
- **Algoritmos de ranges** (`std::ranges::sort(v)`) recebem o contêiner direto, sem pares de iteradores, aceitam **projeções** e são restritos por concepts.
- **View**: um range **leve e preguiçoso** (*lazy*), que não guarda dados: custo O(1) para criar/copiar; os elementos são calculados ao iterar.
- **Pipelines** com `|` compõem transformações como um *shell*.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <vector>

namespace rv = std::views;

int main() {
    std::vector<int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Pipeline preguiçoso: nada é calculado até iterar
    auto resultado = v
        | rv::filter([](int x) { return x % 2 == 0; })     // mantém pares
        | rv::transform([](int x) { return x * x; })       // eleva ao quadrado
        | rv::take(3);                                      // só os 3 primeiros

    for (int x : resultado) std::cout << x << ' ';          // 4 16 36
    std::cout << '\n';

    // Algoritmo de ranges com projeção: ordena pessoas pelo nome sem escrever lambda
    struct P { std::string nome; int idade; };
    std::vector<P> ps{{"Caio", 30}, {"Ana", 25}, {"Bia", 28}};
    std::ranges::sort(ps, {}, &P::nome);                    // comparador padrão, projeção = nome
    for (const auto& p : ps) std::cout << p.nome << ' ';    // Ana Bia Caio
    std::cout << '\n';

    // Views fontes e utilitárias
    for (int i : rv::iota(1, 4)) std::cout << i;            // 123
    for (int i : rv::iota(0) | rv::take(3)) std::cout << i; // 012 (iota infinita + take)
    std::cout << '\n';
    for (int x : v | rv::reverse | rv::drop(7)) std::cout << x << ' ';   // 3 2 1
    std::cout << '\n';

    auto [min, max] = std::ranges::minmax(v);
    std::cout << min << max << '\n';                        // 110
}
```

## Views mais úteis

| View | Efeito | Padrão |
|---|---|---|
| `views::filter(pred)` | Mantém elementos que satisfazem | C++20 |
| `views::transform(f)` | Aplica `f` a cada elemento | C++20 |
| `views::take(n)`, `drop(n)` | Primeiros n / descarta n | C++20 |
| `take_while`, `drop_while` | Enquanto o predicado vale | C++20 |
| `views::reverse` | Inverte | C++20 |
| `views::iota(a, b)` | Sequência de inteiros | C++20 |
| `views::keys`, `values`, `elements<N>` | Componentes de pares/tuplas | C++20 |
| `views::split`, `lazy_split` | Divide por delimitador | C++20 |
| `views::join` | Achata ranges de ranges | C++20 |
| `views::common`, `all` | Adaptações | C++20 |
| `views::zip`, `enumerate`, `chunk`, `slide`, `stride`, `join_with`, `cartesian_product`, `adjacent` | Combinações | **C++23** |
| `ranges::to<Contêiner>()` | Materializa um range em contêiner | **C++23** |

## Materializando o resultado

Views são **preguiçosas**: para obter um contêiner use `ranges::to` (C++23) ou construa manualmente.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>
#include <iterator>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> v{1, 2, 3, 4, 5, 6};
    auto pares = v | std::views::filter([](int x) { return x % 2 == 0; });

    std::vector<int> copia;                                       // C++20: copiar manualmente
    std::ranges::copy(pares, std::back_inserter(copia));
    std::cout << copia.size() << '\n';                            // 3

    // C++23: auto copia2 = pares | std::ranges::to<std::vector>();
}
```

## Armadilhas

> [!danger] Views não possuem dados: cuidado com dangling
> ```cpp
> auto f() {
>     std::vector<int> v{1, 2, 3};
>     return v | std::views::transform([](int x) { return x * 2; });   // v morre: view pendente
> }
> ```
> Rvalues de contêiner não podem ser "pipados" (`std::vector{1,2,3} | views::...` não compila por segurança, exceto via `views::all` com `owning_view` em C++20+ para rvalues move-only).

> [!warning] Outras pegadinhas
> - `views::filter` **cacheia** o `begin()`: modificar o range subjacente depois de iterar pode dar resultados errados.
> - `views::filter` não é *const-iterable*: iterar uma view `const` pode não compilar.
> - A avaliação preguiçosa **reexecuta** o pipeline a cada iteração: materialize se for reutilizar muitas vezes.
> - Mensagens de erro de ranges podem ser longas: confie nos **concepts** (`std::ranges::range`, `input_range`...).

> [!tip] Ranges vs algoritmos clássicos
> Para código novo, prefira `std::ranges::` (mais seguro e legível). Ainda assim `std::sort(first, last)` continua válido e é necessário para intervalos parciais por iteradores.

## Veja também

- [[Algoritmos da STL]]
- [[Iteradores e Categorias]]
- [[Concepts e requires]]
- [[Lambdas e Captura]]
- [[Visão Geral da STL]]

## Exercício

1. Dado um texto, obtenha as 5 palavras de mais de 3 letras mais frequentes usando `views::split`, `transform` e `filter` (materialize para contar).
2. Gere os 10 primeiros quadrados perfeitos pares com `iota`, `transform`, `filter` e `take`.
