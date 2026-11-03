---
titulo: "Concepts e requires"
tags: [cpp, templates, concepts, cpp20]
aliases: ["Concepts", "requires", "requires-expression", "requires-clause", "Conceitos", "<concepts>"]
tipo: conceito
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[SFINAE e enable_if]]", "[[Templates de Função]]", "[[if constexpr]]"]
---

# Concepts e `requires`

> [!info] Introdução
> **C++20.** Suporte: GCC 10+ (`-std=c++20`; GCC 9 com `-fconcepts`), Clang 10+, MSVC 2019 16.3+. Biblioteca `<concepts>` completa em GCC 10+/Clang 13+ (libc++)/MSVC 2019 16.3+.

Um **concept** é um **predicado em tempo de compilação** sobre tipos: nomeia uma **exigência** (interface/operações) que um argumento de template deve satisfazer. Substitui [[SFINAE e enable_if|SFINAE]] com sintaxe legível e erros claros.

## Primeiro exemplo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>
#include <string>

template <typename T>
concept Numero = std::integral<T> || std::floating_point<T>;     // combina conceitos da biblioteca

template <Numero T>                                               // 1) forma "constrained parameter"
T dobro(T x) { return x * 2; }

template <typename T>
    requires std::integral<T>                                     // 2) requires-clause após o template
T metade(T x) { return x / 2; }

template <typename T>
T quadrado(T x) requires Numero<T> { return x * x; }              // 3) requires-clause à direita

auto triplo(Numero auto x) { return x * 3; }                      // 4) abbreviated: auto restrito

int main() {
    std::cout << dobro(21) << dobro(1.5) << metade(9) << quadrado(3) << triplo(2) << '\n';
    // dobro(std::string{"a"});    // erro CLARO: 'std::string' não satisfaz 'Numero'
}
```

Mensagem de erro típica (GCC):
```
error: no matching function for call to 'dobro(std::string)'
note: constraints not satisfied ... the required expression 'std::integral<T>' evaluated to 'false'
```

## `requires`-expression

Descreve **operações exigidas** do tipo.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>
#include <string>
#include <vector>

template <typename T>
concept Imprimivel = requires(const T& x, std::ostream& os) {
    { os << x } -> std::same_as<std::ostream&>;                  // expressão válida E tipo do resultado
};

template <typename C>
concept Conteiner = requires(C c) {
    typename C::value_type;                                      // requisito de tipo aninhado
    { c.size() } -> std::convertible_to<std::size_t>;
    { c.begin() } -> std::input_or_output_iterator;
    c.push_back(std::declval<typename C::value_type>());         // requisito simples: expressão válida
    requires std::default_initializable<C>;                      // requisito aninhado (condição bool)
};

template <Imprimivel T>
void mostra(const T& x) { std::cout << x << '\n'; }

template <Conteiner C>
std::size_t tamanho(const C& c) { return c.size(); }

struct SemSaida {};

int main() {
    mostra(5);
    mostra(std::string("ok"));
    std::cout << tamanho(std::vector<int>{1, 2, 3}) << '\n';
    static_assert(!Imprimivel<SemSaida>);
    static_assert(Conteiner<std::vector<int>>);
    static_assert(!Conteiner<int>);
}
```

## Conceitos da biblioteca padrão (`<concepts>`, `<iterator>`, `<ranges>`)

| Categoria | Conceitos |
|---|---|
| Tipos | `same_as`, `derived_from`, `convertible_to`, `integral`, `floating_point`, `signed_integral` |
| Objetos | `movable`, `copyable`, `semiregular`, `regular`, `default_initializable`, `destructible` |
| Comparação | `equality_comparable`, `totally_ordered`, `three_way_comparable` |
| Chamáveis | `invocable`, `predicate`, `regular_invocable`, `relation` |
| Iteradores | `input_iterator`, `forward_iterator`, `bidirectional_iterator`, `random_access_iterator` |
| Ranges | `range`, `sized_range`, `input_range`, `contiguous_range`, `view` |

## Sobrecarga e subsunção

Quando dois templates são viáveis, vence o **mais restrito** (subsunção por conjunção de conceitos).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <concepts>
#include <iostream>

template <typename T>
concept Inteiro = std::integral<T>;
template <typename T>
concept InteiroComSinal = Inteiro<T> && std::signed_integral<T>;

void f(Inteiro auto)          { std::cout << "inteiro\n"; }
void f(InteiroComSinal auto)  { std::cout << "inteiro com sinal (mais restrito)\n"; }
void f(auto)                  { std::cout << "qualquer\n"; }

int main() {
    f(1);          // inteiro com sinal
    f(1u);         // inteiro
    f(1.5);        // qualquer
}
```

> [!warning] Subsunção é sintática
> Só reconhece restrições escritas com os **mesmos conceitos nomeados** combinados por `&&`/`||`. Duas expressões idênticas em `requires` anônimos **não** se subsumem. Nomeie os conceitos.

## Boas práticas

- Defina conceitos pequenos, com **semântica** (axiomas) além da sintaxe: `Ordenavel`, `Serializavel`.
- Prefira conceitos da biblioteca padrão a reinventar.
- Use `static_assert(Conceito<Tipo>)` em testes para documentar que seus tipos o satisfazem.
- Não restrinja demais: exija só o que o algoritmo **usa**.

> [!tip] Concepts em lambdas e `auto`
> `[](std::integral auto x) { return x + 1; }` — funções e lambdas genéricas restritas.

## Veja também

- [[SFINAE e enable_if]]
- [[static_assert e Type Traits]]
- [[Templates de Função]]
- [[Ranges e Views]]
- [[if constexpr]]

## Exercício

1. Defina o conceito `Somavel` (exige `a + b` do mesmo tipo) e escreva `soma_todos(const std::vector<T>&)` restrita a ele.
2. Qual sobrecarga é escolhida em `f(short{})` no exemplo de subsunção? Por quê?
