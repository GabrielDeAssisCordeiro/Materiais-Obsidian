---
titulo: "Cheat sheet: templates e concepts"
tags: [cpp, referencia, cheat-sheet, templates, concepts]
aliases: ["Cheat sheet templates", "Resumo de templates", "Folha de consulta de templates"]
tipo: referencia
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Templates de Função]]", "[[Concepts e requires]]", "[[Variadic Templates e Fold Expressions]]"]
---

# Cheat sheet: templates e concepts

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

// 1) Template de função e dedução
template <typename T>
T maior(T a, T b) { return a > b ? a : b; }

// 2) Template de classe + CTAD
template <typename T, std::size_t N = 4>
struct Buffer {
    T dados[N]{};
    constexpr std::size_t tamanho() const { return N; }
};

// 3) Especialização total e parcial
template <typename T> struct Nome { static constexpr const char* valor = "outro"; };
template <> struct Nome<int> { static constexpr const char* valor = "int"; };
template <typename T> struct Nome<T*> { static constexpr const char* valor = "ponteiro"; };

// 4) Concepts: três sintaxes equivalentes
template <typename T> concept Numero = std::integral<T> || std::floating_point<T>;

template <Numero T> T dobro1(T x) { return x * 2; }                 // restrição no parâmetro
template <typename T> requires Numero<T> T dobro2(T x) { return x * 2; }   // cláusula requires
auto dobro3(Numero auto x) { return x * 2; }                        // função abreviada

// 5) requires-expression
template <typename T>
concept TemSize = requires(T t) { { t.size() } -> std::convertible_to<std::size_t>; };

// 6) Variádicos e fold expressions
template <typename... Args>
auto soma(Args... args) { return (args + ...); }                    // fold à direita

template <typename... Args>
void imprime(const Args&... args) { ((std::cout << args << ' '), ...); }   // fold com vírgula

// 7) if constexpr
template <typename T>
std::string descreve(const T& v) {
    if constexpr (std::is_integral_v<T>) return "inteiro " + std::to_string(v);
    else if constexpr (TemSize<T>) return "contêiner de " + std::to_string(v.size());
    else return "outro";
}

// 8) Template de variável e alias
template <typename T> constexpr bool eh_ptr_v = std::is_pointer_v<T>;
template <typename T> using Vec = std::vector<T>;

int main() {
    Buffer<int> b;                                                  // N = 4
    Buffer<char, 8> c;
    static_assert(eh_ptr_v<int*> && !eh_ptr_v<int>);
    std::cout << maior(3, 7) << maior<double>(2, 2.5) << b.tamanho() << c.tamanho() << '\n';
    std::cout << Nome<int>::valor << Nome<char*>::valor << Nome<double>::valor << '\n';
    std::cout << dobro1(2) << dobro2(2.5) << dobro3(4) << soma(1, 2, 3) << '\n';
    imprime("a", 1, 2.5);
    std::cout << '\n' << descreve(5) << ' ' << descreve(std::string{"abc"}) << ' ' << descreve(2.5) << '\n';
    Vec<int> v{1, 2};
    std::cout << v.size() << '\n';
}
```

## Quadro-resumo

| Recurso | Sintaxe | Desde |
|---|---|---|
| Template de função/classe | `template <typename T>` | C++98 |
| Parâmetro não-tipo | `template <int N>` | C++98 |
| Alias de template | `template <class T> using V = vector<T>;` | C++11 |
| Variádicos | `template <typename... Ts>` | C++11 |
| Fold expressions | `(args + ...)` | C++17 |
| CTAD | `std::pair p{1, 2.0};` | C++17 |
| `if constexpr` | decisão em compilação | C++17 |
| Template de variável | `template <class T> constexpr T pi = ...;` | C++14 |
| Concepts / `requires` | `template <Concept T>` | C++20 |
| Parâmetros não-tipo de classe/float | `template <auto V>` com literais de classe | C++20 |
| *Deducing this* | `void f(this Self&& self)` | C++23 |

## Type traits úteis (`<type_traits>`)

`is_same_v`, `is_integral_v`, `is_floating_point_v`, `is_pointer_v`, `is_class_v`, `is_base_of_v`, `is_convertible_v`, `is_invocable_v`, `remove_cv_t`, `remove_reference_t`, `decay_t`, `conditional_t`, `enable_if_t`, `common_type_t`, `invoke_result_t`.

> [!warning] Armadilhas
> - Definições de template precisam estar **visíveis** onde são instanciadas (geralmente no header).
> - Erros de template sem concepts geram mensagens longas: restrinja com `requires`.
> - `template <typename T> void f(T&&)` é uma *forwarding reference*; `void f(std::vector<T>&&)` **não** é.
> - Especialização parcial de **função** não existe: use sobrecarga ou `if constexpr`.

## Veja também

- [[Templates de Função]]
- [[Templates de Classe]]
- [[Concepts e requires]]
- [[Variadic Templates e Fold Expressions]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Escreva o *concept* `Somavel<T>` (requer `a + b` convertível para `T`) e use-o em uma função `soma_todos`.
2. Reescreva uma função com `enable_if` usando `requires`.
