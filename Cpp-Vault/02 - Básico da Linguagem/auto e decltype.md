---
titulo: "auto e decltype"
tags: [cpp, basico, tipos]
aliases: ["auto", "decltype", "decltype(auto)", "Dedução de tipo", "Trailing return type"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Variáveis e Inicialização]]", "[[const e constexpr]]", "[[Funções - Cpp]]"]
---

# `auto` e `decltype`

> [!info] Introdução
> `auto` e `decltype` foram introduzidos no **C++11**. `auto` como tipo de retorno e `decltype(auto)` vieram no **C++14**. `auto` em parâmetros de função (*abbreviated function templates*) veio no **C++20**.

## `auto`: deixe o compilador deduzir

`auto` deduz o tipo a partir do inicializador. As regras seguem a dedução de argumentos de templates: **descarta `const` e referência de nível superior**, a menos que você os escreva.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <initializer_list>
#include <type_traits>

int g = 0;                                   // variável global para o exemplo de decltype(auto)
decltype(auto) ref_para_g() { return (g); }  // parênteses: decltype((g)) é int&  -> retorna int&

int main() {
    int x = 10;
    const int cx = x;

    auto a = cx;           // int         (const descartado)
    const auto b = cx;     // const int
    auto& r = cx;          // const int&  (const preservado ao ligar a referência)
    auto&& u = x;          // int&        (referência universal; x é lvalue)
    auto lst = {1, 2, 3};  // std::initializer_list<int>

    static_assert(std::is_same_v<decltype(a), int>);
    static_assert(std::is_same_v<decltype(b), const int>);
    static_assert(std::is_same_v<decltype(r), const int&>);
    static_assert(std::is_same_v<decltype(u), int&>);
    static_assert(std::is_same_v<decltype(lst), std::initializer_list<int>>);
    static_assert(std::is_same_v<decltype(ref_para_g()), int&>);

    (void)a; (void)b; (void)r; (void)u; (void)lst;   // silencia avisos de variável não usada
}
```

### Quando usar `auto`

| Use | Evite |
|---|---|
| Tipos verbosos (iteradores, retornos de `make_unique`, lambdas) | Quando o tipo concreto é essencial para leitura |
| Quando o tipo já é óbvio pela direita (`auto p = std::make_unique<Foo>()`) | Para tipos numéricos onde o tamanho importa (`auto n = 1` é `int`) |
| Laços range-for (`for (const auto& x : v)`) | Em interfaces públicas se o tipo faz parte do contrato |

> [!warning] `auto` copia por padrão
> `for (auto x : vetor_de_strings)` **copia** cada elemento. Use `const auto&` para leitura ou `auto&` para modificar.

## `decltype`: o tipo de uma expressão

`decltype(expr)` informa o tipo **exato** da expressão, sem descartar `const` ou referências.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <type_traits>
#include <vector>

template <typename A, typename B>
auto soma(A a, B b) -> decltype(a + b) {      // trailing return type (C++11)
    return a + b;
}

int main() {
    int i = 0;
    decltype(i) j = 5;                 // int
    decltype(i + 1.0) d = 2.5;         // double
    std::vector<int> v{1, 2, 3};
    decltype(v)::value_type primeiro = v[0];   // int

    std::cout << j << ' ' << d << ' ' << primeiro << ' ' << soma(1, 2.5) << '\n';   // 5 2.5 1 3.5
    static_assert(std::is_same_v<decltype(soma(1, 2.5)), double>);
}
```

## Retorno com `auto` (C++14) e `decltype(auto)`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

auto quadrado(int x) { return x * x; }                   // retorno int deduzido (C++14)

std::string nome = "Ana";
decltype(auto) acessa_nome() { return (nome); }          // std::string& (preserva referência)
auto copia_nome() { return nome; }                       // std::string  (cópia)

int main() {
    std::cout << quadrado(7) << '\n';                    // 49
    acessa_nome() += " Maria";                           // altera a global
    std::cout << nome << ' ' << copia_nome() << '\n';    // Ana Maria Ana Maria
}
```

> [!bug] Armadilha: `decltype(auto)` com parênteses
> `return x;` e `return (x);` podem retornar tipos diferentes com `decltype(auto)`. Retornar `(variável_local)` produz **referência pendente** (*dangling*):
> ```cpp
> decltype(auto) ruim() { int x = 1; return (x); }   // int& para variável local: UB ao usar
> ```

## `auto` em parâmetros (C++20)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

void mostra(const auto& valor) {          // equivale a template <typename T> void mostra(const T&)
    std::cout << valor << '\n';
}

int main() {
    mostra(42);
    mostra("texto");
    mostra(3.14);
}
```

## Veja também

- [[Variáveis e Inicialização]]
- [[const e constexpr]]
- [[Funções - Cpp]]
- [[Conversões e Casts]]

## Exercício

1. Qual é o tipo de `auto x = 5 / 2.0;`? E de `auto y = 'a' + 1;`?
2. Reescreva `std::vector<int>::iterator it = v.begin();` com `auto`.
