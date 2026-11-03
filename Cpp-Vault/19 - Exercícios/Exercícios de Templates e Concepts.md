---
titulo: "Exercícios de Templates e Concepts"
tags: [cpp, exercicios, templates, concepts]
aliases: ["Exercícios de templates"]
tipo: exercicio
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[MOC - Templates e Concepts]]", "[[MOC - Exercícios - Cpp]]"]
---

# Exercícios de Templates e Concepts

Teoria: [[Templates de Função]], [[Templates de Classe]], [[Variadic Templates e Fold Expressions]], [[Concepts e requires]].

## 1. `maximo` com concept

Escreva `maximo(a, b)` restrito a tipos comparáveis com `<` (use `std::totally_ordered`).

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>
#include <string>

template <std::totally_ordered T>
const T& maximo(const T& a, const T& b) { return (a < b) ? b : a; }

int main() {
    std::cout << maximo(3, 7) << ' ' << maximo(std::string("a"), std::string("b")) << '\n';
}
```

## 2. `Pilha<T>`

Implemente `Pilha<T>` com `push`, `pop`, `topo`, `vazia`, usando `std::vector<T>` internamente. `pop` em pilha vazia lança exceção.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

template <typename T>
class Pilha {
    std::vector<T> d_;
public:
    void push(T v) { d_.push_back(std::move(v)); }
    void pop() {
        if (d_.empty()) throw std::out_of_range("pilha vazia");
        d_.pop_back();
    }
    const T& topo() const { return d_.back(); }
    bool vazia() const noexcept { return d_.empty(); }
};

int main() {
    Pilha<int> p;
    p.push(1);
    p.push(2);
    p.pop();
    std::cout << p.topo() << '\n';   // 1
    p.pop();
    try { p.pop(); } catch (const std::out_of_range& e) { std::cout << e.what() << '\n'; }
}
```

## 3. `soma` variádica

Escreva `soma(args...)` com *fold expression* que funcione com qualquer quantidade de argumentos numéricos (inclusive zero).

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

template <typename... Ts>
constexpr auto soma(Ts... xs) { return (0 + ... + xs); }   // fold com valor inicial: funciona com 0 argumentos

static_assert(soma() == 0);
static_assert(soma(1, 2, 3) == 6);

int main() { std::cout << soma(1, 2.5, 3) << '\n'; }       // 6.5
```

## 4. Concept `Imprimivel`

Defina um concept para tipos que podem ser enviados a `std::ostream` e uma função `mostrar` restrita a ele.

> [!success] Gabarito

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>
#include <vector>

template <typename T>
concept Imprimivel = requires(std::ostream& os, const T& v) {
    { os << v } -> std::same_as<std::ostream&>;
};

template <Imprimivel T>
void mostrar(const T& v) { std::cout << v << '\n'; }

int main() {
    mostrar(42);
    mostrar("texto");
    // mostrar(std::vector<int>{1});   // ERRO de compilação: vector não é Imprimivel (mensagem clara do concept)
}
```

> [!info] Mensagem de erro
> Com o concept, o erro de `mostrar(std::vector<int>{1})` diz que a restrição `Imprimivel` não foi satisfeita, em vez de dezenas de linhas de template ([[Concepts e requires]]).

## Veja também

- [[Templates de Função]]
- [[Concepts e requires]]
- [[static_assert e Type Traits]]
- [[MOC - Exercícios - Cpp]]

## Exercício

Faça `Pilha<T>` exigir `std::movable T` com um concept e tente instanciá-la com um tipo não movível.
