---
titulo: "const em métodos"
tags: [cpp, poo, const]
aliases: ["Métodos const", "mutable", "Const em métodos"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[const e constexpr]]", "[[Classes e Structs]]", "[[this e Membros Estáticos]]"]
---

# `const` em métodos

Um método marcado com `const` **promete não modificar** o objeto (o tipo de `this` passa a ser `const T*`). Só métodos `const` podem ser chamados em objetos `const`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

class Livro {
public:
    explicit Livro(std::string titulo) : titulo_(std::move(titulo)) {}

    const std::string& titulo() const { return titulo_; }     // leitura: const
    void renomear(std::string t) { titulo_ = std::move(t); }  // modifica: não const

private:
    std::string titulo_;
};

void imprime(const Livro& l) {            // recebe const&: só enxerga métodos const
    std::cout << l.titulo() << '\n';
    // l.renomear("x");                   // erro: método não const em objeto const
}

int main() {
    Livro l{"C++ Moderno"};
    imprime(l);
    l.renomear("C++ Avançado");
    imprime(l);
}
```

## Sobrecarga por `const`

Uma versão para objetos `const` e outra para não-`const` é um padrão comum (como `operator[]` do `std::vector`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <vector>

class Grade {
public:
    explicit Grade(std::size_t n) : dados_(n) {}
    int& at(std::size_t i) { return dados_.at(i); }                 // leitura e escrita
    const int& at(std::size_t i) const { return dados_.at(i); }     // somente leitura
private:
    std::vector<int> dados_;
};

int main() {
    Grade g{3};
    g.at(0) = 7;                      // chama a versão não const
    const Grade& cg = g;
    std::cout << cg.at(0) << '\n';    // chama a versão const: 7
    // cg.at(0) = 1;                  // erro: retorno é const int&
}
```

## `mutable`

Permite modificar um membro **dentro de método `const`**. Use para estado que **não faz parte do valor lógico** do objeto: caches, contadores de acesso, mutexes.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <mutex>

class Calculadora {
public:
    explicit Calculadora(int base) : base_(base) {}

    int quadrado() const {
        std::lock_guard<std::mutex> g(m_);        // travar o mutex "modifica" m_
        ++chamadas_;                              // contador de uso
        if (!cache_valido_) { cache_ = base_ * base_; cache_valido_ = true; }
        return cache_;
    }
    int chamadas() const { return chamadas_; }

private:
    int base_;
    mutable std::mutex m_;
    mutable int chamadas_ = 0;
    mutable int cache_ = 0;
    mutable bool cache_valido_ = false;
};

int main() {
    const Calculadora c{7};
    std::cout << c.quadrado() << ' ' << c.quadrado() << ' ' << c.chamadas() << '\n';   // 49 49 2
}
```

> [!warning] `const` é **superficial** com ponteiros
> Em um método `const`, um membro `int* p` vira `int* const p` (o ponteiro é const, **o dado apontado não**). O compilador permite `*p = 1;`. Para constância profunda use `std::experimental::propagate_const` ou aplique disciplina de projeto.

> [!tip] Regra de ouro
> Marque **todo** método que não modifica o objeto como `const`. Isso documenta a intenção, habilita o uso com `const&` e é exigido pelos contêineres e algoritmos da biblioteca padrão em muitos casos.

## Veja também

- [[const e constexpr]]
- [[Classes e Structs]]
- [[this e Membros Estáticos]]
- [[Sobrecarga de Funções]]

## Exercício

1. Adicione a uma classe `Matriz` as sobrecargas `operator()(i, j)` com e sem `const`.
2. Dê dois exemplos de membros que justificam `mutable` e um exemplo em que `mutable` seria má prática.
