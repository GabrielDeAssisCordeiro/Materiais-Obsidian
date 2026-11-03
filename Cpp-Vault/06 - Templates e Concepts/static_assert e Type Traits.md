---
titulo: "static_assert e *type traits*"
tags: [cpp, templates, static_assert]
aliases: ["static_assert", "Type traits", "<type_traits>", "is_same", "remove_reference", "decay"]
tipo: referencia
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Concepts e requires]]", "[[SFINAE e enable_if]]", "[[if constexpr]]"]
---

# `static_assert` e *type traits*

## `static_assert`

Verifica uma condição **em tempo de compilação**; se falsa, o programa **não compila** e a mensagem aparece como erro.

> [!info] Versões
> `static_assert(cond, "msg")`: C++11. Mensagem **opcional**: C++17. Mensagem dinâmica (`constexpr` string-like): C++26.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdint>
#include <type_traits>

static_assert(sizeof(std::int32_t) == 4, "int32_t deve ter 4 bytes");
static_assert(sizeof(void*) >= 4);                         // C++17: sem mensagem

template <typename T>
struct Contador {
    static_assert(std::is_arithmetic_v<T>, "Contador exige tipo aritmético");   // restrição simples
    T valor{};
};

int main() {
    Contador<int> ok;
    (void)ok;
    // Contador<std::string> ruim;   // erro de compilação com a mensagem acima
}
```

## *Type traits* (`<type_traits>`, C++11 em diante)

Metafunções que **consultam** ou **transformam** tipos em tempo de compilação.

### Consultas (resultam em `bool`; use `_v`)

| Trait | Verdadeiro se... |
|---|---|
| `is_integral_v<T>` / `is_floating_point_v<T>` / `is_arithmetic_v<T>` | Tipo numérico |
| `is_pointer_v<T>` / `is_reference_v<T>` / `is_array_v<T>` | Categoria composta |
| `is_class_v<T>` / `is_enum_v<T>` | Classe / enumeração |
| `is_const_v<T>` / `is_signed_v<T>` | Qualificadores/propriedades |
| `is_same_v<A, B>` | Mesmo tipo |
| `is_base_of_v<B, D>` | `D` deriva de `B` |
| `is_convertible_v<From, To>` | Conversão implícita existe |
| `is_constructible_v<T, Args...>` | `T(args...)` é válido |
| `is_trivially_copyable_v<T>` | Pode ser copiado com `memcpy` |
| `is_nothrow_move_constructible_v<T>` | Movimento não lança ([[noexcept e Movimento]]) |
| `is_invocable_v<F, Args...>` (C++17) | `F` pode ser chamado com `Args...` |

### Transformações (resultam em tipo; use `_t`)

| Trait | Resultado |
|---|---|
| `remove_const_t<T>`, `remove_reference_t<T>`, `remove_cv_t<T>`, `remove_pointer_t<T>` | Remove qualificador |
| `add_const_t<T>`, `add_pointer_t<T>`, `add_lvalue_reference_t<T>` | Adiciona |
| `decay_t<T>` | O que acontece ao passar por valor (remove ref/cv, array→ponteiro) |
| `common_type_t<A, B>` | Tipo comum aritmético |
| `conditional_t<cond, A, B>` | `A` se `cond`, senão `B` |
| `underlying_type_t<E>` | Tipo base de um `enum` |
| `invoke_result_t<F, Args...>` (C++17) | Tipo do retorno de `F(args...)` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

struct Base {};
struct Derivada : Base {};
enum class Cor : unsigned char { Vermelho };

static_assert(std::is_same_v<std::remove_reference_t<int&>, int>);
static_assert(std::is_same_v<std::decay_t<const int(&)[3]>, const int*>);
static_assert(std::is_same_v<std::conditional_t<(sizeof(int) > 2), long, short>, long>);
static_assert(std::is_base_of_v<Base, Derivada>);
static_assert(std::is_convertible_v<int, double>);
static_assert(!std::is_convertible_v<std::string, int>);
static_assert(std::is_same_v<std::underlying_type_t<Cor>, unsigned char>);
static_assert(std::is_invocable_v<decltype([](int) {}), int>);

template <typename T>
using SemRef = std::remove_cvref_t<T>;                    // C++20: remove const, volatile e referência

static_assert(std::is_same_v<SemRef<const std::vector<int>&>, std::vector<int>>);

int main() { std::cout << "tudo verificado em compilação\n"; }
```

## Convenções de nomes

| Sufixo | Significado | Exemplo |
|---|---|---|
| `::value` | Constante `bool` (ou valor) | `std::is_integral<int>::value` |
| `_v` (C++17) | Atalho de `::value` | `std::is_integral_v<int>` |
| `::type` | Tipo resultante | `std::remove_const<T>::type` |
| `_t` (C++14) | Atalho de `::type` | `std::remove_const_t<T>` |

## Escrevendo uma trait própria

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <type_traits>
#include <vector>

template <typename T> struct e_vector : std::false_type {};
template <typename T, typename A> struct e_vector<std::vector<T, A>> : std::true_type {};
template <typename T> inline constexpr bool e_vector_v = e_vector<T>::value;

static_assert(e_vector_v<std::vector<int>>);
static_assert(!e_vector_v<int>);

int main() {}
```

> [!tip] Use traits dentro de concepts
> `template <typename T> concept Numero = std::is_arithmetic_v<T>;` — ou use os conceitos prontos de `<concepts>` ([[Concepts e requires]]).

## Veja também

- [[Concepts e requires]]
- [[SFINAE e enable_if]]
- [[Especialização de Templates]]
- [[if constexpr]]

## Exercício

1. Escreva `static_assert`s que garantam que `MeuTipo` é *nothrow move constructible* e *trivially destructible*.
2. Implemente `e_ponteiro_para_const<T>` por especialização parcial.
