---
titulo: "Variadic templates e *fold expressions*"
tags: [cpp, templates]
aliases: ["Variadic templates", "Parameter pack", "Fold expressions", "sizeof...", "Pack indexing"]
tipo: conceito
nivel: avancado
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Templates de Função]]", "[[Referências Universais e Perfect Forwarding]]", "[[if constexpr]]"]
---

# Variadic templates e *fold expressions*

> [!info] Versões
> **Variadic templates**: C++11. **Fold expressions**: **C++17**. **Pack indexing** (`Ts...[N]`): **C++26** (GCC 15+).
> [!question] Verificar na documentação oficial
> Confirme o suporte a *pack indexing* no seu compilador.

Um **pacote de parâmetros** (*parameter pack*) representa **zero ou mais** tipos/valores.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename... Ts>            // pacote de tipos
void conta(Ts... args) {             // pacote de argumentos
    std::cout << sizeof...(Ts) << " tipos, " << sizeof...(args) << " args\n";   // sizeof... mede o pacote
}

int main() {
    conta();                          // 0 tipos, 0 args
    conta(1, 2.5, "a");               // 3 tipos, 3 args
}
```

## Recursão (estilo C++11)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void imprime() { std::cout << '\n'; }                      // caso base

template <typename T, typename... Resto>
void imprime(const T& primeiro, const Resto&... resto) {
    std::cout << primeiro << ' ';
    imprime(resto...);                                      // expande o resto: recursão em compilação
}

int main() { imprime(1, "dois", 3.0); }
```

## *Fold expressions* (C++17)

Reduzem o pacote com um operador **sem recursão**.

| Forma | Expansão |
|---|---|
| `(... op pack)` — fold esquerdo unário | `((p1 op p2) op p3) ...` |
| `(pack op ...)` — fold direito unário | `p1 op (p2 op (p3 ...))` |
| `(init op ... op pack)` — binário esquerdo | `((init op p1) op p2) ...` |
| `(pack op ... op init)` — binário direito | `p1 op (p2 op (... op init))` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

template <typename... Ts>
auto soma(Ts... xs) { return (xs + ...); }                       // fold direito unário

template <typename... Ts>
bool todos(Ts... xs) { return (... && xs); }                      // pacote vazio com && = true

template <typename... Ts>
void imprime(const Ts&... xs) {
    ((std::cout << xs << ' '), ...);                              // fold com operador vírgula
    std::cout << '\n';
}

template <typename... Ts>
auto soma_com_zero(Ts... xs) { return (0 + ... + xs); }           // binário: funciona com pacote vazio

int main() {
    std::cout << soma(1, 2, 3, 4) << '\n';                        // 10
    std::cout << todos(true, 1 > 0, 3 == 3) << '\n';              // 1
    imprime(1, "dois", 3.5, std::string("quatro"));
    std::cout << soma_com_zero() << '\n';                         // 0
}
```

> [!bug] Fold unário com pacote vazio
> Só `&&` (→ `true`), `||` (→ `false`) e `,` (→ `void()`) aceitam pacote vazio em fold **unário**. Para os demais operadores, use a forma binária com valor inicial, ou o compilador dá erro em `soma()` sem argumentos.

## Expansão em diferentes contextos

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <array>
#include <iostream>
#include <tuple>
#include <utility>

template <typename... Ts>
auto faz_array(Ts... xs) { return std::array<std::common_type_t<Ts...>, sizeof...(Ts)>{xs...}; }

template <typename F, typename... Args>
decltype(auto) chama(F&& f, Args&&... args) {
    return std::forward<F>(f)(std::forward<Args>(args)...);       // perfect forwarding de todo o pacote
}

template <typename... Ts>
struct Contador { static constexpr std::size_t valor = sizeof...(Ts); };

int main() {
    auto a = faz_array(1, 2, 3);
    std::cout << a.size() << chama([](int x, int y) { return x * y; }, 6, 7) << '\n';   // 342
    std::cout << Contador<int, double, char>::valor << '\n';                              // 3
    auto t = std::make_tuple(1, 2.5, 'c');
    std::apply([](auto... v) { ((std::cout << v << ';'), ...); }, t);                     // percorre tupla
    std::cout << '\n';
}
```

## Quando usar

- `std::make_unique`, `emplace_back`, `std::tuple`, `std::variant`, `std::format`: todos são variádicos.
- Funções de *log*, *callbacks* com número arbitrário de argumentos, utilitários genéricos.

> [!tip] Prefira fold expressions à recursão quando possível
> Menos código, compilação mais rápida e mensagens de erro mais curtas.

## Veja também

- [[Templates de Função]]
- [[Referências Universais e Perfect Forwarding]]
- [[if constexpr]]
- [[Metaprogramação em Compilação]]

## Exercício

1. Implemente `todos_iguais(xs...)` e `qualquer(xs...)` com fold expressions.
2. Escreva `media(xs...)` que retorna `double` e não compila com pacote vazio — como dar uma mensagem clara com `static_assert`?
