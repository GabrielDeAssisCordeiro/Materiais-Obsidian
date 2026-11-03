---
titulo: "Slicing* (fatiamento)"
tags: [cpp, poo, copia, polimorfismo]
aliases: ["Object slicing", "Fatiamento de objetos", "Slicing"]
tipo: conceito
nivel: intermediario
padrao: C++98
criado: 2026-10-24
relacionados: ["[[Herança]]", "[[Polimorfismo e Funções Virtuais]]", "[[Construtores e Destrutores]]"]
---

# *Slicing* (fatiamento)

Copiar um objeto derivado para uma variável **do tipo base, por valor**, copia só a parte da base: o restante é "fatiado" e o comportamento polimórfico se perde.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <vector>

struct Animal {
    virtual ~Animal() = default;
    virtual const char* som() const { return "..."; }
};
struct Cachorro : Animal {
    int fome = 10;
    const char* som() const override { return "au"; }
};

void por_valor(Animal a)          { std::cout << a.som() << '\n'; }   // fatiamento!
void por_ref(const Animal& a)     { std::cout << a.som() << '\n'; }   // polimorfismo preservado

int main() {
    Cachorro c;
    por_valor(c);                 // "..."  (virou Animal)
    por_ref(c);                   // "au"

    Animal a = c;                 // fatiado: perde 'fome' e o tipo dinâmico
    std::cout << a.som() << '\n'; // "..."

    std::vector<Animal> ruim;     // contêiner de valores: fatia cada elemento
    ruim.push_back(c);
    std::cout << ruim[0].som() << '\n';       // "..."

    std::vector<std::unique_ptr<Animal>> bom; // ponteiros: preserva o tipo dinâmico
    bom.push_back(std::make_unique<Cachorro>());
    std::cout << bom[0]->som() << '\n';       // "au"
}
```

## Como evitar

| Técnica | Detalhe |
|---|---|
| Passe por **referência** ou ponteiro | `const Animal&` |
| Contêineres de **ponteiros inteligentes** | `std::vector<std::unique_ptr<Base>>` |
| Impeça cópia da base | `Animal(const Animal&) = delete;` (copie com método `clone()` virtual) |
| Classes abstratas | Impossível instanciar por valor |
| `-Wall` + `clang-tidy` | `cppcoreguidelines-slicing` |

## `clone()` virtual (construtor virtual)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>

struct Animal {
    virtual ~Animal() = default;
    virtual std::unique_ptr<Animal> clone() const = 0;       // cópia polimórfica
    virtual const char* som() const = 0;
protected:
    Animal() = default;
    Animal(const Animal&) = default;                         // só derivadas podem copiar: sem slicing externo
};

struct Gato : Animal {
    std::unique_ptr<Animal> clone() const override { return std::make_unique<Gato>(*this); }
    const char* som() const override { return "miau"; }
};

int main() {
    std::unique_ptr<Animal> a = std::make_unique<Gato>();
    auto b = a->clone();                                      // cópia do tipo dinâmico real
    std::cout << b->som() << '\n';                            // miau
}
```

> [!warning] Slicing também afeta atribuição
> `base = derivada;` atribui apenas a parte base. Por isso, em hierarquias polimórficas, desabilite cópia/atribuição pública (Core Guidelines C.67).

## Veja também

- [[Herança]]
- [[Polimorfismo e Funções Virtuais]]
- [[Construtores e Destrutores]]
- [[default e delete]]

## Exercício

1. Reproduza o slicing com `std::vector<Animal>` e corrija com `unique_ptr`.
2. Escreva `clone()` para três classes derivadas e use-o para duplicar um `vector<unique_ptr<Animal>>`.
