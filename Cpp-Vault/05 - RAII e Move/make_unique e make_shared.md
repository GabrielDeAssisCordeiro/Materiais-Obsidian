---
titulo: "make_unique e make_shared"
tags: [cpp, smart-pointers]
aliases: ["make_unique", "make_shared", "allocate_shared", "make_unique_for_overwrite"]
tipo: conceito
nivel: intermediario
padrao: C++14
criado: 2026-10-24
relacionados: ["[[unique_ptr]]", "[[shared_ptr]]", "[[Referências Universais e Perfect Forwarding]]"]
---

# `make_unique` e `make_shared`

> [!info] Versões
> `std::make_shared`: **C++11**. `std::make_unique`: **C++14**. Variantes para arrays em `make_shared`: C++20. `make_unique_for_overwrite`/`make_shared_for_overwrite`: C++20.

São **fábricas** que constroem o objeto **e** o smart pointer em um passo, com *perfect forwarding* dos argumentos.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <string>

struct Cliente {
    Cliente(std::string nome, int id) : nome(std::move(nome)), id(id) {}
    std::string nome;
    int id;
};

int main() {
    auto u = std::make_unique<Cliente>("Ana", 1);          // unique_ptr<Cliente>
    auto s = std::make_shared<Cliente>("Bia", 2);          // shared_ptr<Cliente>
    auto v = std::make_unique<int[]>(10);                  // array valor-inicializado
    std::cout << u->nome << s->nome << v[9] << '\n';
}
```

## Vantagens

| Vantagem | Explicação |
|---|---|
| **Segurança contra exceções** | Evita vazamentos em `f(unique_ptr<A>(new A), g())` (pré-C++17, a ordem de avaliação podia vazar se `g()` lançasse) |
| **Sem `new` explícito** | Código mais curto, zero `delete` |
| **`make_shared` é mais eficiente** | **Uma** alocação para o objeto **e** o bloco de controle (melhor cache) |
| **Deduz o tipo** | `auto p = std::make_unique<T>(...)` evita repetir `T` |

## Quando **não** usar `make_*`

| Situação | Alternativa |
|---|---|
| **Deleter customizado** | `std::unique_ptr<T, D>(p, d)` ([[Deleters Customizados]]) |
| Construtor **privado/protegido** | `std::unique_ptr<T>(new T(...))` dentro de membro estático |
| Inicializar com `{}` (lista) | `make_unique<T>(T{...})` ou construtor explícito |
| `make_shared` com objetos grandes e `weak_ptr` longevos | A memória do objeto só é liberada quando a contagem **fraca** zera (bloco único) |
| Adotar ponteiro bruto vindo de API C | Construtor do smart pointer |

> [!warning] `make_shared` e `weak_ptr`
> Com alocação única, mesmo depois que o último `shared_ptr` morre (objeto destruído), o **bloco inteiro** (objeto + controle) só é desalocado quando o último `weak_ptr` desaparece. Para objetos grandes com `weak_ptr` de vida longa, considere `shared_ptr<T>(new T)`.

## Segurança de exceções (por que importava)

```cpp
// Antes do C++17 — PODE vazar:
// f(std::unique_ptr<A>(new A), g());   // ordem possível: new A; g() lança; unique_ptr nunca construído

// Correto em todas as versões:
// f(std::make_unique<A>(), g());
```
Desde o C++17 a avaliação de argumentos de função não intercala mais com `new` dessa forma, mas `make_unique` continua sendo o estilo recomendado.

## Veja também

- [[unique_ptr]]
- [[shared_ptr]]
- [[Deleters Customizados]]
- [[Referências Universais e Perfect Forwarding]]

## Exercício

1. Compare `sizeof` e número de alocações (sobrescrevendo `operator new`) de `shared_ptr<T>(new T)` e `make_shared<T>()`.
2. Escreva uma classe com construtor privado e uma função estática `criar()` que retorne `unique_ptr`.
