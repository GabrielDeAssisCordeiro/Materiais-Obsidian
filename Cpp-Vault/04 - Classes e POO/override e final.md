---
titulo: "override e final"
tags: [cpp, poo, virtual]
aliases: ["override", "final", "Sobrescrita", "Overriding"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Polimorfismo e Funções Virtuais]]", "[[Classes Abstratas e Interfaces]]", "[[Herança]]"]
---

# `override` e `final`

> [!info] Introdução
> **C++11.** Suporte completo em GCC 4.7+, Clang 3.0+, MSVC 2012+.

## `override`

Marca uma função como **sobrescrita** de uma virtual da base. Se nada for sobrescrito, o compilador **emite erro**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Base {
    virtual void f(int) const { std::cout << "Base::f\n"; }
    virtual ~Base() = default;
};

struct Boa : Base {
    void f(int) const override { std::cout << "Boa::f\n"; }
};

struct Ruim : Base {
    void f(int) { std::cout << "Ruim::f\n"; }     // SEM const e SEM override: NÃO sobrescreve! oculta
};

int main() {
    Boa boa; Ruim ruim;
    const Base& a = boa;
    const Base& b = ruim;
    a.f(1);        // Boa::f
    b.f(1);        // Base::f  <-- bug silencioso
}
```

> [!bug] O bug que `override` evita
> Esquecer `const`, errar o tipo do parâmetro ou o nome cria uma **nova** função em vez de sobrescrever. Com `override`:
> ```cpp
> void f(int) override;     // erro: marked 'override' but does not override
> ```
> **Regra:** use `override` em **toda** sobrescrita. Com `-Wsuggest-override` (GCC) o compilador avisa quando faltar.

## `final`

| Uso | Efeito |
|---|---|
| `void f() final;` | Impede que **derivadas** sobrescrevam `f` |
| `class D final : public B` | Impede que alguém **herde** de `D` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Base {
    virtual void a() { std::cout << "Base::a\n"; }
    virtual void b() { std::cout << "Base::b\n"; }
    virtual ~Base() = default;
};

struct Meio : Base {
    void a() override { std::cout << "Meio::a\n"; }
    void b() override final { std::cout << "Meio::b (final)\n"; }   // ninguém mais sobrescreve b
};

struct Folha final : Meio {                    // ninguém herda de Folha
    void a() override { std::cout << "Folha::a\n"; }
    // void b() override {}                    // erro: Meio::b é final
};

// struct Outra : Folha {};                    // erro: Folha é final

int main() {
    Folha f;
    Base& r = f;
    r.a(); r.b();      // Folha::a e Meio::b (final)
}
```

### Para que serve `final`

- **Segurança de projeto**: documentar que a classe não foi pensada para extensão.
- **Desempenho**: se o tipo dinâmico é conhecido e é `final`, o compilador pode **desvirtualizar** a chamada (chamada direta, *inlining*).

> [!tip] Padrão sugerido
> Classes folha de hierarquias: `class X final`. Sobrescritas: `override` (e `final` quando fizer sentido).

## Palavras contextuais

`override` e `final` só são palavras-chave **em contexto**: ainda é válido (embora desaconselhável) usá-las como identificadores.

## Veja também

- [[Polimorfismo e Funções Virtuais]]
- [[Classes Abstratas e Interfaces]]
- [[Herança]]
- [[vtable]]

## Exercício

1. Remova `override` do exemplo `Boa`, mude o parâmetro para `double` e observe o que ocorre sem e com `override`.
2. Marque uma classe como `final` e meça (via Compiler Explorer) se uma chamada virtual é desvirtualizada com `-O2`.
