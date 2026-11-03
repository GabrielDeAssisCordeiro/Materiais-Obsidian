---
titulo: "std::any"
tags: [cpp, stl, type-erasure, cpp17]
aliases: ["std::any", "any", "Contêiner de qualquer tipo", "any_cast"]
tipo: conceito
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[variant]]", "[[optional]]", "[[std function e Functors]]"]
---

# `std::any`

> [!info] Introdução
> **C++17** (`<any>`). Guarda **um valor de qualquer tipo copiável**, apagando o tipo em tempo de compilação (*type erasure*) e permitindo recuperá-lo com `std::any_cast`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <any>
#include <iostream>
#include <string>
#include <typeinfo>
#include <vector>

int main() {
    std::any a = 42;
    std::cout << a.type().name() << ' ' << a.has_value() << '\n';      // i 1 (nome depende do compilador)

    std::cout << std::any_cast<int>(a) << '\n';                        // 42
    a = std::string("texto");                                          // troca o tipo
    a.emplace<double>(2.5);

    try {
        std::cout << std::any_cast<int>(a);                            // tipo errado
    } catch (const std::bad_any_cast& e) {
        std::cout << "bad_any_cast\n";
    }

    if (auto* p = std::any_cast<double>(&a)) std::cout << *p << '\n';  // ponteiro: sem exceção; 2.5

    std::vector<std::any> mix{1, std::string("dois"), 3.0};            // lista heterogênea
    for (const auto& x : mix) {
        if (x.type() == typeid(int)) std::cout << "int ";
        else if (x.type() == typeid(std::string)) std::cout << "string ";
        else std::cout << "outro ";
    }
    std::cout << '\n';
}
```

## `any` vs alternativas

| Necessidade | Ferramenta |
|---|---|
| Conjunto **fechado** e conhecido de tipos | [[variant]] (verificação em compilação) |
| Interface comum com comportamento | Herança/`virtual` ou *type erasure* próprio |
| Chamáveis | `std::function` |
| **Qualquer** tipo, decidido em runtime (plugins, configuração, bindings) | `std::any` |

> [!warning] Custos e limites
> - Exige **copiabilidade** (use `std::unique_ptr` dentro de `any` ou outro mecanismo para *move-only*; C++26 não muda isso, `std::move_only_any` é discutido).
> - Pode alocar no heap (otimização para objetos pequenos é opcional).
> - Perde-se a verificação em compilação: erros viram `bad_any_cast` em execução.
> - Depende de **RTTI** (`-fno-rtti` desabilita `type()`).

> [!tip] Use pouco
> `any` é um sinal de projeto: antes, pergunte se `variant`, templates ou uma interface comum resolvem melhor.

## Veja também

- [[variant]]
- [[optional]]
- [[std function e Functors]]
- [[vtable]]

## Exercício

1. Crie um "dicionário de configuração" `std::map<std::string, std::any>` e uma função `template<class T> std::optional<T> obter(...)` que usa `any_cast` com ponteiro.
2. Em que `variant<int, std::string>` é superior a `any` para o mesmo caso?
