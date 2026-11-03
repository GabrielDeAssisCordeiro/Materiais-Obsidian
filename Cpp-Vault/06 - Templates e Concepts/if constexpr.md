---
titulo: "if constexpr"
tags: [cpp, templates, cpp17]
aliases: ["if constexpr", "Compile-time if", "if consteval", "Ramificação em tempo de compilação"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[SFINAE e enable_if]]", "[[Concepts e requires]]", "[[constexpr consteval constinit]]"]
---

# `if constexpr`

> [!info] Introdução
> **C++17.** Suporte: GCC 7+, Clang 3.9+, MSVC 2017 15.3+. `if consteval` chegou no **C++23**.

`if constexpr (condição)` decide **em tempo de compilação** qual ramo é compilado. O ramo **descartado não é instanciado**, então pode conter código que seria **inválido** para aquele tipo.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <type_traits>
#include <vector>

template <typename T>
std::string descreve(const T& v) {
    if constexpr (std::is_integral_v<T>) {
        return "inteiro: " + std::to_string(v);
    } else if constexpr (std::is_floating_point_v<T>) {
        return "decimal: " + std::to_string(v);
    } else if constexpr (std::is_same_v<T, std::string>) {
        return "texto: " + v;
    } else {
        return "outro tipo";
    }
}

template <typename T>
auto tamanho(const T& x) {
    if constexpr (requires { x.size(); })       // C++20: requires-expression como condição
        return x.size();
    else
        return sizeof(x);
}

int main() {
    std::cout << descreve(42) << '\n' << descreve(3.5) << '\n'
              << descreve(std::string("oi")) << '\n' << descreve('c') << '\n';
    std::cout << tamanho(std::vector<int>{1, 2, 3}) << ' ' << tamanho(5) << '\n';
}
```

## `if` normal vs `if constexpr`

```cpp
template <typename T>
void f(T x) {
    if (std::is_pointer_v<T>)  { std::cout << *x; }       // ERRO para T = int: *x é inválido, mesmo no ramo "morto"
    if constexpr (std::is_pointer_v<T>) { std::cout << *x; }   // OK: ramo descartado não é compilado
}
```

> [!bug] Exemplo inválido proposital
> ```cpp
> template <typename T> void f(T x) { if (std::is_pointer_v<T>) std::cout << *x; }
> f(5);   // erro: invalid type argument of unary '*'
> ```
> **Correção:** `if constexpr`.

> [!warning] O ramo descartado só é ignorado em **templates**, e só se a condição **depender de parâmetros de template**. Fora de um template, `if constexpr` ainda compila os dois ramos (apenas não os executa).

## Recursão em compilação sem especialização

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <int N>
constexpr long fatorial() {
    if constexpr (N <= 1) return 1;
    else return N * fatorial<N - 1>();       // N-1 só é instanciado se N > 1
}

int main() {
    static_assert(fatorial<5>() == 120);
    std::cout << fatorial<10>() << '\n';
}
```

## Substitui SFINAE em muitos casos

Antes do C++17, escolher código por categoria de tipo exigia sobrecargas com `enable_if` ([[SFINAE e enable_if]]). Hoje, um único corpo com `if constexpr` é mais legível. Para **restringir a interface** (aceitar/rejeitar tipos), use **concepts** ([[Concepts e requires]]).

## `if consteval` (C++23)

Detecta se a função está sendo avaliada **em tempo de compilação**:

```cpp
// [nv] g++ -std=c++23 -Wall -Wextra   (GCC 12+)
#include <cmath>

constexpr double potencia(double x, int n) {
    if consteval {                         // avaliação em compilação: algoritmo constexpr
        double r = 1;
        for (int i = 0; i < n; ++i) r *= x;
        return r;
    } else {                               // execução: pode usar função otimizada não constexpr
        return std::pow(x, n);
    }
}

static_assert(potencia(2.0, 10) == 1024.0);
int main() {}
```

## Veja também

- [[SFINAE e enable_if]]
- [[Concepts e requires]]
- [[static_assert e Type Traits]]
- [[constexpr consteval constinit]]

## Exercício

1. Escreva `converte_para_string(T)` que usa `std::to_string` para números, retorna o próprio valor para `std::string` e `.c_str()` indireto para `const char*`.
2. Explique por que `if constexpr` dentro de uma função **não** template não evita erros de compilação no ramo descartado.
