---
titulo: "Herança"
tags: [cpp, poo]
aliases: ["Herança", "Herança pública", "Composição vs herança", "Classe base e derivada", "Is-a"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Polimorfismo e Funções Virtuais]]", "[[Encapsulamento e friend]]", "[[Herança Múltipla e Virtual]]"]
---

# Herança

**Herança** permite definir uma classe (**derivada**) a partir de outra (**base**), reaproveitando e especializando comportamento.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

class Funcionario {                                   // base
public:
    Funcionario(std::string nome, double salario)
        : nome_(std::move(nome)), salario_(salario) {}
    std::string descricao() const { return nome_ + " (R$ " + std::to_string(salario_) + ")"; }
    double salario() const { return salario_; }
protected:
    std::string nome_;                                // visível às derivadas
private:
    double salario_;
};

class Gerente : public Funcionario {                  // herança PÚBLICA: "Gerente É UM Funcionario"
public:
    Gerente(std::string nome, double salario, int equipe)
        : Funcionario(std::move(nome), salario),      // construtor da base primeiro
          equipe_(equipe) {}
    int equipe() const { return equipe_; }
    std::string titulo() const { return "Gerente " + nome_; }   // acessa membro protected
private:
    int equipe_;
};

int main() {
    Gerente g{"Ana", 9000.0, 5};
    std::cout << g.descricao() << '\n';               // herdado
    std::cout << g.titulo() << ' ' << g.equipe() << '\n';

    Funcionario& f = g;                               // conversão derivada -> base (upcast): implícita
    std::cout << f.salario() << '\n';
}
```

## Tipos de herança

| Forma | `public` da base vira | Significado |
|---|---|---|
| `class D : public B` | `public` | Relação **é-um** (substituição). O caso comum |
| `class D : protected B` | `protected` | Raro |
| `class D : private B` | `private` | **Implementado-em-termos-de**; prefira composição |

> [!tip] Composição antes de herança
> Pergunte: *D **é um** B em **todos** os contextos?* (Princípio da Substituição de Liskov). Se for só "usa um" ou "tem um", use **composição** (membro). Herança cria o acoplamento mais forte da linguagem.

| Critério | Herança | Composição |
|---|---|---|
| Relação | é-um | tem-um / usa-um |
| Acoplamento | Alto | Baixo |
| Flexibilidade em runtime | Só com `virtual` | Fácil trocar membros |
| Reuso | Do comportamento da base | Delegação explícita |

## Ocultação de nomes

Um método na derivada **oculta** todos os métodos de mesmo nome da base (mesmo com assinaturas diferentes).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

struct B { void f(int) { std::cout << "B::f(int)\n"; } };
struct D : B {
    using B::f;                       // traz B::f de volta ao escopo de D
    void f(double) { std::cout << "D::f(double)\n"; }
};

int main() {
    D d;
    d.f(1);       // B::f(int) graças ao using; sem ele chamaria D::f(double)
    d.f(1.0);     // D::f(double)
}
```

## Construtores e herança

- A base é construída **antes** da derivada e destruída **depois**.
- Construtores não são herdados automaticamente; `using B::B;` (C++11) **herda construtores**.

> [!bug] Exemplo inválido proposital: base sem construtor padrão
> ```cpp
> struct Base { explicit Base(int) {} };
> struct Derivada : Base { Derivada() {} };   // erro: Base não tem construtor padrão
> ```
> **Correção:** `Derivada() : Base(0) {}`.

## Veja também

- [[Polimorfismo e Funções Virtuais]]
- [[Herança Múltipla e Virtual]]
- [[Slicing]]
- [[Encapsulamento e friend]]
- [[override e final]]

## Exercício

1. Modele `Animal` → `Cachorro`/`Gato` e depois reescreva com composição de um `Comportamento`. Compare.
2. Por que `class Pilha : public std::vector<int>` é considerada má ideia?
