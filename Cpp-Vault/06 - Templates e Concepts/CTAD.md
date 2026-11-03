---
titulo: "CTAD — dedução de argumentos de template de classe"
tags: [cpp, templates, cpp17]
aliases: ["CTAD", "Class Template Argument Deduction", "Deduction guides", "Guias de dedução"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Templates de Classe]]", "[[auto e decltype]]", "[[Templates de Função]]"]
---

# CTAD — dedução de argumentos de template de classe

> [!info] Introdução
> **C++17.** Suporte: GCC 7+, Clang 5+, MSVC 2017 15.7+. CTAD para agregados e *aliases*: C++20 (GCC 11+/Clang 17+, com ressalvas).

Antes do C++17 era preciso escrever `std::pair<int, double> p{1, 2.5};` ou usar `std::make_pair`. Agora o compilador **deduz** os argumentos de template a partir dos argumentos do construtor.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>
#include <mutex>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

int main() {
    std::pair p{1, 2.5};                       // std::pair<int, double>
    std::tuple t{1, "a", 3.0};                 // std::tuple<int, const char*, double>
    std::vector v{1, 2, 3};                    // std::vector<int> (da lista de inicialização)
    std::array a{1, 2, 3, 4};                  // std::array<int, 4>: deduz o tipo E o tamanho
    std::mutex m;
    std::lock_guard g{m};                      // std::lock_guard<std::mutex>

    std::vector v2(3, 7);                      // std::vector<int>: {7, 7, 7}
    std::cout << p.first << std::get<1>(t) << v.size() << a.size() << v2[0] << '\n';
}
```

## Como funciona

O compilador gera **guias de dedução** implícitos a partir dos construtores. Você pode escrever **guias explícitos** quando a dedução automática não faz o que se quer.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <vector>

template <typename T>
struct Caixa {
    T valor;
    Caixa(T v) : valor(std::move(v)) {}
};

// Guia de dedução explícito: Caixa("texto") deduz Caixa<std::string>, não Caixa<const char*>
Caixa(const char*) -> Caixa<std::string>;

template <typename It>
struct Intervalo {
    It ini, fim;
    Intervalo(It a, It b) : ini(a), fim(b) {}
};
// Guia: constrói Intervalo<It> a partir de dois iteradores
template <typename It> Intervalo(It, It) -> Intervalo<It>;

int main() {
    Caixa c1{42};                       // Caixa<int>
    Caixa c2{"olá"};                    // Caixa<std::string> (pelo guia)
    std::vector<int> v{1, 2, 3};
    Intervalo r{v.begin(), v.end()};    // Intervalo<std::vector<int>::iterator>
    std::cout << c1.valor << c2.valor << (r.fim - r.ini) << '\n';
}
```

## Armadilhas

> [!bug] Parênteses vs chaves e *initializer_list*
> ```cpp
> std::vector a(3, 7);     // vector<int>: três elementos 7
> std::vector b{3, 7};     // vector<int>: dois elementos {3, 7}
> std::vector c{std::vector{1, 2}};   // CUIDADO: pode copiar (vector<int>) em vez de aninhar
> ```

> [!warning] A "cópia" tem prioridade
> `std::vector v{outro_vector};` deduz `std::vector<int>` (cópia), **não** `vector<vector<int>>`.

> [!warning] CTAD não é a mesma coisa que `auto`
> - Funciona só com **templates de classe** (e aliases em C++20).
> - Pode surpreender com `const char*` (veja o guia acima) ou com ponteiros inteligentes (`std::unique_ptr p{new int}` **não** deduz: construtor é `explicit` e o tipo seria ambíguo).

> [!tip] Quando usar
> Bom para tipos de biblioteca com argumentos óbvios (`std::pair`, `std::tuple`, `std::lock_guard`, `std::array`). Para tipos do seu domínio, prefira declarar explicitamente quando o leitor precisar saber o tipo.

## Veja também

- [[Templates de Classe]]
- [[Templates de Função]]
- [[auto e decltype]]
- [[Structured Bindings]]

## Exercício

1. Escreva `template<typename T> struct Embrulho { Embrulho(T) {} };` e um guia de dedução que faça `Embrulho{"x"}` virar `Embrulho<std::string>`.
2. Explique por que `std::vector{1, 2.5}` não compila.
