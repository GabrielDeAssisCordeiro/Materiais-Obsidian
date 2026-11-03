---
titulo: "std::variant"
tags: [cpp, stl, variant, vocabulary-types, cpp17]
aliases: ["std::variant", "variant", "Union segura", "std::visit", "Tipo soma", "Sum type", "overloaded"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[optional]]", "[[std any]]", "[[Polimorfismo e Funções Virtuais]]"]
---

# `std::variant`

> [!info] Introdução
> **C++17** (`<variant>`). Uma *union* **segura em tipos** (tipo-soma): guarda **exatamente um** valor dentre uma lista fixa de tipos e sabe qual.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <variant>
#include <vector>

int main() {
    std::variant<int, double, std::string> v = 42;           // guarda int
    std::cout << v.index() << '\n';                           // 0 (posição do tipo ativo)

    v = std::string("texto");                                 // agora string
    std::cout << std::holds_alternative<std::string>(v) << '\n';   // 1

    std::cout << std::get<std::string>(v) << '\n';            // lança std::bad_variant_access se tipo errado
    if (auto* p = std::get_if<int>(&v)) std::cout << *p;      // ponteiro ou nullptr: sem exceção
    else std::cout << "não é int\n";

    v.emplace<double>(3.14);                                  // constrói no lugar
    std::cout << std::get<double>(v) << '\n';
}
```

## `std::visit`: tratar cada alternativa

`std::visit` aplica um **visitante** que precisa cobrir **todos** os tipos (verificado em compilação).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <variant>

// Utilitário clássico: junta várias lambdas em um único visitante
template <class... Ts> struct sobrecarga : Ts... { using Ts::operator()...; };
template <class... Ts> sobrecarga(Ts...) -> sobrecarga<Ts...>;   // guia de dedução (desnecessário no C++20)

using Valor = std::variant<int, double, std::string>;

std::string descreve(const Valor& v) {
    return std::visit(sobrecarga{
        [](int i)                { return "int " + std::to_string(i); },
        [](double d)             { return "double " + std::to_string(d); },
        [](const std::string& s) { return "string " + s; },
    }, v);
}

int main() {
    std::cout << descreve(7) << '\n' << descreve(2.5) << '\n' << descreve(std::string("oi")) << '\n';
}
```

## Modelando estados e mensagens (substitui hierarquias)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <variant>
#include <vector>

struct Circulo   { double r; };
struct Retangulo { double l, a; };
struct Triangulo { double b, h; };
using Forma = std::variant<Circulo, Retangulo, Triangulo>;     // conjunto FECHADO de formas

double area(const Forma& f) {
    return std::visit([](const auto& s) -> double {
        using T = std::decay_t<decltype(s)>;
        if constexpr (std::is_same_v<T, Circulo>)        return 3.14159 * s.r * s.r;
        else if constexpr (std::is_same_v<T, Retangulo>) return s.l * s.a;
        else                                             return s.b * s.h / 2;
    }, f);
}

int main() {
    std::vector<Forma> formas{Circulo{1}, Retangulo{2, 3}, Triangulo{4, 5}};   // sem ponteiros, sem heap
    double total = 0;
    for (const auto& f : formas) total += area(f);
    std::cout << total << '\n';
}
```

## `variant` vs herança

| | `std::variant` | Hierarquia com `virtual` |
|---|---|---|
| Conjunto de tipos | **Fechado** (conhecido em compilação) | **Aberto** (novas derivadas depois) |
| Armazenamento | Em linha (sem heap), tamanho = maior tipo + índice | Ponteiros no heap |
| Adicionar **operação** | Fácil (novo visitante) | Difícil (mexe em todas as classes) |
| Adicionar **tipo** | Difícil (muda o `variant` e visitantes) | Fácil |
| Desempenho | Sem indireção de vtable; cache-friendly | Chamada virtual |

## Cuidados

> [!bug] `valueless_by_exception`
> Se a construção do novo valor lançar exceção durante uma atribuição, o `variant` pode ficar **sem valor** (`v.valueless_by_exception()`). Tipos com construtores `noexcept` evitam isso.

> [!warning] Primeiro tipo precisa ser construtível por padrão
> `std::variant<A, B>` só tem construtor padrão se `A` tiver; senão use `std::monostate` como primeiro tipo: `std::variant<std::monostate, A, B>` ("vazio").

> [!warning] Tipos repetidos e conversões
> `std::variant<int, long> v = 3L;` funciona, mas `variant<int, bool>` e inicialização com ponteiros podem escolher alternativas inesperadas (veja P0608 corrigido no C++20). Use `std::in_place_type<T>` para ser explícito.

## Veja também

- [[optional]]
- [[std any]]
- [[expected]]
- [[Polimorfismo e Funções Virtuais]]
- [[if constexpr]]

## Exercício

1. Implemente um avaliador de expressões com `std::variant<double, Soma, Produto>` onde `Soma`/`Produto` guardam `std::unique_ptr<Expr>`, e avalie recursivamente com `visit`.
2. Por que `std::visit` com um visitante que não cobre todos os tipos é erro de compilação?
