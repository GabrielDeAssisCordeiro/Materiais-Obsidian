---
titulo: "Idiomas e padrões de projeto em C++"
tags: [cpp, avancado, design-patterns, raii]
aliases: ["Idiomas C++", "Padrões de projeto", "Strategy", "Observer", "Factory", "Visitor", "Copy and swap", "Pass key"]
tipo: referencia
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[RAII]]", "[[CRTP e Mixins]]", "[[Type Erasure]]"]
---

# Idiomas e padrões de projeto em C++

**Idiomas** são soluções específicas da linguagem; **padrões de projeto** (GoF) são soluções de design gerais. Em C++ moderno, muitos padrões ficam menores graças a lambdas, templates, `variant` e RAII.

## Idiomas clássicos

| Idioma | Para quê | Nota |
|---|---|---|
| **RAII** | Recursos presos ao tempo de vida | [[RAII]] |
| **Regra do 0** | Deixar o compilador gerar tudo | [[Regra do 0, 3 e 5]] |
| **Copy-and-swap** | Atribuição com garantia forte | [[Segurança de Exceções]] |
| **Pimpl** | Isolar implementação | [[Pimpl]] |
| **CRTP** | Polimorfismo estático e mixins | [[CRTP e Mixins]] |
| **Type erasure** | Polimorfismo de valor | [[Type Erasure]] |
| **NVI** (*Non-Virtual Interface*) | Interface pública não virtual chama ganchos virtuais privados | Veja abaixo |
| **Scope guard** | Executar código na saída do escopo | `std::experimental::scope_exit`, `gsl::finally` |
| **Erase-remove** | Remover de contêineres | `std::erase_if` (C++20) |
| **Tag dispatch** | Escolher implementação por tipo | Hoje: `if constexpr`/concepts |
| **Passkey** | Restringir quem chama um método | Veja abaixo |
| **Named constructor / factory** | Construtores com nome expressivo | `static T criar_xyz()` |
| **Substituição por `std::variant` + `visit`** | Visitor sem hierarquia | [[variant]] |

## NVI e *scope guard*

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <functional>
#include <iostream>
#include <utility>

// NVI: a API pública é não virtual e impõe pré/pós-condições; as variações ficam em ganchos privados
class Relatorio {
public:
    virtual ~Relatorio() = default;
    void gerar() const {                                       // "método template" (GoF Template Method)
        std::cout << "[início]\n";
        corpo();                                                // ponto de variação
        std::cout << "[fim]\n";
    }
private:
    virtual void corpo() const = 0;
};

struct RelatorioVendas : Relatorio {
private:
    void corpo() const override { std::cout << "vendas: 42\n"; }
};

// Scope guard minimalista
template <typename F>
class ScopeExit {
public:
    explicit ScopeExit(F f) : f_{std::move(f)} {}
    ScopeExit(const ScopeExit&) = delete;
    ~ScopeExit() { if (ativo_) f_(); }
    void liberar() { ativo_ = false; }                         // cancela a ação
private:
    F f_;
    bool ativo_ = true;
};

int main() {
    RelatorioVendas{}.gerar();
    {
        ScopeExit limpa{[] { std::cout << "limpeza executada\n"; }};
        std::cout << "trabalhando...\n";
    }                                                           // limpeza ao sair, mesmo com exceção
}
```

## Padrões GoF e o C++ moderno

| Padrão | Implementação moderna |
|---|---|
| **Strategy** | `std::function`, lambdas ou parâmetro de template |
| **Observer** | `std::vector<std::function<void(Evento)>>` (cuidado com tempo de vida; `weak_ptr`) |
| **Command / Undo** | Objetos callable + pilha de comandos |
| **Factory / Abstract Factory** | Função que retorna `unique_ptr<Base>`; registro de construtores `std::map<string, std::function<...>>` |
| **Singleton** | *Meyers singleton* (`static T& instancia() { static T t; return t; }`, thread-safe desde C++11) — **evite** estado global |
| **Visitor** | `std::visit` com `overloaded` lambdas |
| **Adapter / Decorator** | Composição + templates |
| **State** | `std::variant` de estados + `visit` |
| **Iterator** | Iteradores/ranges/geradores ([[Iteradores e Categorias]], [[Corrotinas Cpp20]]) |
| **RAII Guard** | `lock_guard`, `unique_ptr` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>
#include <variant>

struct Circulo { double r; };
struct Retangulo { double l, a; };
using Forma = std::variant<Circulo, Retangulo>;

template <class... Ts> struct overloaded : Ts... { using Ts::operator()...; };   // C++17; guia de dedução automático no C++20

double area(const Forma& f) {
    return std::visit(overloaded{
        [](const Circulo& c) { return 3.14159 * c.r * c.r; },
        [](const Retangulo& r) { return r.l * r.a; }
    }, f);                                                                          // Visitor sem hierarquia virtual
}

int main() {
    std::cout << area(Circulo{1.0}) << ' ' << area(Retangulo{2, 3}) << '\n';         // 3.14159 6
}
```

> [!warning] Cuidado com padrões demais
> Não aplique GoF "por cartilha". Em C++ a simplicidade (valores, funções, composição) costuma bastar. **Singleton** e estado global dificultam testes ([[gMock e Dublês de Teste]]).

## Veja também

- [[RAII]]
- [[CRTP e Mixins]]
- [[Type Erasure]]
- [[Pimpl]]
- [[variant]]
- [[Core Guidelines]]

## Exercício

1. Implemente **Observer** com `std::function` e proteja contra *dangling* usando `weak_ptr`.
2. Reescreva uma hierarquia Visitor clássica com `std::variant` + `std::visit`.
