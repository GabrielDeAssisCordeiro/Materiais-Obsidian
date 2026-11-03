---
titulo: "Templates de variável"
tags: [cpp, templates]
aliases: ["Variable templates", "Templates de variável", "inline constexpr template"]
tipo: conceito
nivel: intermediario
padrao: C++14
criado: 2026-10-24
relacionados: ["[[static_assert e Type Traits]]", "[[Especialização de Templates]]", "[[Concepts e requires]]"]
---

# Templates de variável

> [!info] Introdução
> **C++14.** Suporte: GCC 5+, Clang 3.4+, MSVC 2015 U2+.

Uma **variável** pode ser um template: uma "constante" diferente para cada tipo (ou valor).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <limits>
#include <numbers>
#include <type_traits>

template <typename T>
inline constexpr T pi = static_cast<T>(3.14159265358979323846L);    // uma constante por tipo

template <typename T>
inline constexpr T maximo = std::numeric_limits<T>::max();

template <typename T>
inline constexpr bool e_inteiro_grande_v = std::is_integral_v<T> && (sizeof(T) >= 8);   // estilo "_v" das traits

int main() {
    std::cout << pi<double> << ' ' << pi<float> << '\n';
    std::cout << maximo<short> << ' ' << maximo<unsigned char> + 0 << '\n';
    static_assert(e_inteiro_grande_v<long long>);
    static_assert(!e_inteiro_grande_v<int>);

    // C++20 já traz constantes matemáticas como templates de variável
    std::cout << std::numbers::pi_v<float> << '\n';
}
```

## Especialização

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename T> constexpr const char* nome = "desconhecido";
template <> constexpr const char* nome<int> = "int";
template <> constexpr const char* nome<double> = "double";

// Fatorial por template de variável com NTTP
template <unsigned N> constexpr unsigned long fat = N * fat<N - 1>;
template <> constexpr unsigned long fat<0> = 1;

int main() {
    std::cout << nome<int> << nome<char> << ' ' << fat<5> << '\n';   // intdesconhecido 120
}
```

## Uso na biblioteca padrão

As variantes `_v` são templates de variável: `std::is_same_v<A, B>` equivale a `std::is_same<A, B>::value`. Também: `std::numbers::pi_v<T>`, `std::ranges::enable_borrowed_range`.

> [!tip] Sempre use `inline constexpr`
> Em cabeçalhos, `inline` evita múltiplas definições (ODR) em C++17+ ([[Argumentos Padrão e inline]]); `constexpr` garante valor em compilação.

## Veja também

- [[static_assert e Type Traits]]
- [[Especialização de Templates]]
- [[Parâmetros Não-Tipo]]
- [[constexpr consteval constinit]]

## Exercício

1. Crie `tamanho_em_bits<T>` como template de variável e use-o com `static_assert`.
2. Escreva `e_ponteiro_v<T>` por especialização parcial de variável.
