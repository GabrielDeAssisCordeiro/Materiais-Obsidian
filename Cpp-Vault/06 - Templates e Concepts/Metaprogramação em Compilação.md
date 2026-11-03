---
titulo: "Metaprogramação em tempo de compilação"
tags: [cpp, templates, metaprogramacao, constexpr]
aliases: ["Template metaprogramming", "TMP", "Metaprogramação", "Computação em tempo de compilação", "Type lists"]
tipo: conceito
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[constexpr consteval constinit]]", "[[Variadic Templates e Fold Expressions]]", "[[Concepts e requires]]"]
---

# Metaprogramação em tempo de compilação

**Metaprogramação** é escrever código que **computa tipos e valores durante a compilação**, reduzindo trabalho em execução e gerando código especializado.

## Três eras

| Era | Técnica | Exemplo |
|---|---|---|
| C++98 | **Template metaprogramming (TMP)**: recursão em templates e especialização | `Fatorial<N>::valor` |
| C++11/14/17 | **`constexpr`** + `if constexpr` + variadic templates | funções comuns executadas na compilação |
| C++20/23 | `consteval`, concepts, `std::is_constant_evaluated`, `constexpr` em `std::vector`/`std::string` | |
| C++26 | **Reflexão estática** | gerar código a partir de tipos |

## 1) TMP clássico (recursão em tipos)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <type_traits>

template <unsigned N> struct Fib { static constexpr unsigned long valor = Fib<N - 1>::valor + Fib<N - 2>::valor; };
template <> struct Fib<0> { static constexpr unsigned long valor = 0; };
template <> struct Fib<1> { static constexpr unsigned long valor = 1; };

// Lista de tipos e operações sobre ela
template <typename... Ts> struct Lista {};

template <typename L> struct Tamanho;
template <typename... Ts> struct Tamanho<Lista<Ts...>> : std::integral_constant<std::size_t, sizeof...(Ts)> {};

template <typename L, typename T> struct Prepend;
template <typename... Ts, typename T> struct Prepend<Lista<Ts...>, T> { using tipo = Lista<T, Ts...>; };

int main() {
    static_assert(Fib<10>::valor == 55);
    using L = Prepend<Lista<int, double>, char>::tipo;       // Lista<char, int, double>
    static_assert(Tamanho<L>::value == 3);
    std::cout << Fib<20>::valor << '\n';
}
```

## 2) `constexpr`: código normal executado na compilação

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <cstddef>
#include <iostream>

constexpr bool e_primo(unsigned n) {
    if (n < 2) return false;
    for (unsigned d = 2; d * d <= n; ++d)
        if (n % d == 0) return false;
    return true;
}

template <std::size_t N>
constexpr auto primos_ate() {                         // tabela gerada em compilação
    std::array<unsigned, N> r{};
    unsigned achados = 0;
    for (unsigned n = 2; achados < N; ++n)
        if (e_primo(n)) r[achados++] = n;
    return r;
}

constexpr auto tabela = primos_ate<10>();            // calculada durante a compilação
static_assert(tabela[9] == 29);

int main() {
    for (auto p : tabela) std::cout << p << ' ';     // 2 3 5 7 11 13 17 19 23 29
    std::cout << '\n';
}
```

> [!tip] Prefira `constexpr` ao TMP clássico
> Funções `constexpr` são código C++ comum, depuráveis e legíveis. Reserve a TMP para **manipular tipos** (listas de tipos, traits).

## 3) Computando com tipos: `std::conditional`, `std::integral_constant`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <type_traits>

// Escolhe o menor inteiro sem sinal que comporta N bits
template <unsigned Bits>
using UIntMinimo = std::conditional_t<(Bits <= 8), std::uint8_t,
                   std::conditional_t<(Bits <= 16), std::uint16_t,
                   std::conditional_t<(Bits <= 32), std::uint32_t, std::uint64_t>>>;

static_assert(std::is_same_v<UIntMinimo<12>, std::uint16_t>);
static_assert(sizeof(UIntMinimo<40>) == 8);

int main() {}
```

## 4) Geração de código com pacotes e sequências de índices

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <tuple>
#include <utility>

template <typename Tupla, std::size_t... Is>
void imprime_impl(const Tupla& t, std::index_sequence<Is...>) {
    ((std::cout << std::get<Is>(t) << ' '), ...);
}

template <typename... Ts>
void imprime(const std::tuple<Ts...>& t) { imprime_impl(t, std::index_sequence_for<Ts...>{}); }

int main() { imprime(std::tuple{1, 2.5, 'x'}); std::cout << '\n'; }
```

## Custos e riscos

| Aspecto | Observação |
|---|---|
| Tempo de compilação | Recursão profunda de templates é lenta (limite padrão ≈ 900 níveis, `-ftemplate-depth`) |
| Legibilidade | TMP clássico é difícil; prefira `constexpr`/concepts |
| Depuração | Erros extensos; use `static_assert` e `Compiler Explorer` |
| Memória do compilador | Muitas instanciações podem esgotar RAM |

> [!info] Reflexão (C++26)
> Reflexão estática (GCC 16.1 com `-freflection`) permitirá introspecção de membros e geração de código sem macros — ver [[Cpp26 Visão Geral]].

## Veja também

- [[constexpr consteval constinit]]
- [[Variadic Templates e Fold Expressions]]
- [[Concepts e requires]]
- [[static_assert e Type Traits]]
- [[Cpp26 Visão Geral]]

## Exercício

1. Gere em compilação uma tabela de senos de 0 a 359 graus usando `constexpr` e um `std::array<double, 360>` (dica: série de Taylor própria, pois `std::sin` só é `constexpr` em C++26).
2. Implemente `Reverter<Lista<...>>` que inverta uma lista de tipos.
