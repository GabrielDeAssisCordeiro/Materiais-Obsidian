---
titulo: "Polimorfismo e funções virtuais"
tags: [cpp, poo, polimorfismo, virtual]
aliases: ["Polimorfismo", "Funções virtuais", "virtual", "Despacho dinâmico", "Destrutor virtual"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Herança]]", "[[vtable]]", "[[override e final]]"]
---

# Polimorfismo e funções virtuais

**Polimorfismo** é tratar objetos de tipos diferentes por uma interface comum. Em C++ há dois tipos:

| Tipo | Quando é resolvido | Mecanismo |
|---|---|---|
| **Estático** (em compilação) | Compilação | Sobrecarga, templates, concepts |
| **Dinâmico** (em execução) | Execução | Funções **virtuais** + ponteiro/referência para base |

## Função virtual

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <vector>

class Forma {
public:
    virtual ~Forma() = default;                          // destrutor virtual: ESSENCIAL
    virtual double area() const = 0;                     // virtual puro: veja Classes Abstratas
    virtual void descreve() const { std::cout << "forma de área " << area() << '\n'; }
};

class Circulo : public Forma {
public:
    explicit Circulo(double r) : r_(r) {}
    double area() const override { return 3.14159 * r_ * r_; }
private:
    double r_;
};

class Quadrado : public Forma {
public:
    explicit Quadrado(double l) : l_(l) {}
    double area() const override { return l_ * l_; }
    void descreve() const override { std::cout << "quadrado " << l_ << "x" << l_ << '\n'; }
private:
    double l_;
};

int main() {
    std::vector<std::unique_ptr<Forma>> formas;          // coleção heterogênea
    formas.push_back(std::make_unique<Circulo>(1.0));
    formas.push_back(std::make_unique<Quadrado>(2.0));

    for (const auto& f : formas) f->descreve();          // a versão certa é escolhida em EXECUÇÃO
}
```

Saída:
```
forma de área 3.14159
quadrado 2x2
```

## Condições para o despacho dinâmico

1. A função é declarada `virtual` na base.
2. A chamada é feita por **ponteiro ou referência** para a base (não por valor).
3. A assinatura na derivada **coincide** (use `override` — veja [[override e final]]).

## Sem `virtual`: ocultação, não polimorfismo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct A { void f() const { std::cout << "A\n"; } virtual void g() const { std::cout << "A::g\n"; } virtual ~A() = default; };
struct B : A { void f() const { std::cout << "B\n"; } void g() const override { std::cout << "B::g\n"; } };

int main() {
    B b;
    A& r = b;
    r.f();     // A    (não virtual: decide o tipo ESTÁTICO da referência)
    r.g();     // B::g (virtual: decide o tipo DINÂMICO do objeto)
}
```

## Destrutor virtual

> [!danger] Destruir via ponteiro para base sem destrutor virtual é UB
> Toda classe projetada para ser **base polimórfica** deve ter destrutor `virtual` (ou `protected` não virtual, se objetos não forem destruídos pela base). Veja o exemplo em [[Construtores e Destrutores]].

> [!warning] Não chame virtuais em construtores/destrutores
> Durante a construção de `Base`, o objeto **ainda é uma `Base`**; uma chamada virtual resolve para a versão da base, não da derivada.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct Base {
    Base() { quem(); }                       // chama Base::quem, nunca Derivada::quem
    virtual void quem() const { std::cout << "Base\n"; }
    virtual ~Base() = default;
};
struct Derivada : Base {
    void quem() const override { std::cout << "Derivada\n"; }
};

int main() { Derivada d; d.quem(); }         // imprime "Base" e depois "Derivada"
```

## Custo

| Custo | Detalhe |
|---|---|
| Memória | +1 ponteiro (vptr) por objeto |
| Execução | Chamada indireta; dificulta *inlining* |
| Cache | Objetos em ponteiros espalhados (localidade pior) |

Veja [[vtable]]. Alternativas sem custo de virtual: templates/concepts, CRTP, `std::variant` + `std::visit`, *type erasure* (seção de avançado).

## Veja também

- [[Herança]]
- [[vtable]]
- [[override e final]]
- [[Classes Abstratas e Interfaces]]
- [[Slicing]]

## Exercício

1. Adicione `Triangulo` à hierarquia sem alterar `main`, e some as áreas de todas as formas.
2. O que ocorre se `Forma` não tiver destrutor virtual e destruirmos um `unique_ptr<Forma>` que guarda `Circulo`?
