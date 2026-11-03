---
titulo: "Sobrecarga de Operadores - Cpp"
tags: [cpp, poo, operadores, sobrecarga]
aliases: ["operator+", "operator==", "operator<=>"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Encapsulamento e friend]]", "[[Operadores - Cpp]]", "[[Conversões Implícitas e explicit]]"]
---

# Sobrecarga de Operadores - Cpp

Permite que tipos definidos pelo usuário usem a sintaxe de operadores (`+`, `==`, `<<`, `[]`, `()`...) com semântica coerente.

## Regras gerais

- Só é possível **sobrecarregar** operadores existentes; não se criam novos.
- Não podem ser sobrecarregados: `::`, `.`, `.*`, `?:`, `sizeof`, `typeid`.
- **Preserve a semântica esperada**: `+` não deve modificar operandos; `==` deve ser relação de equivalência.
- Precedência e associatividade **não mudam**.

## Membro ou função livre?

| Operador | Forma recomendada |
|---|---|
| `=`, `[]`, `()`, `->`, `+=`, `-=`, ... (modificam o objeto) | **Membro** |
| `+`, `-`, `*`, `==`, `<` (simétricos, conversão nos dois lados) | **Livre** (ou `friend`) |
| `<<` e `>>` de streams | **Livre** (o operando esquerdo é o stream) |

## Exemplo completo: `Vetor2D`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <compare>
#include <iostream>

class Vetor2D {
public:
    constexpr Vetor2D(double x = 0, double y = 0) : x_(x), y_(y) {}

    // Operadores compostos: membros, modificam *this e retornam referência
    constexpr Vetor2D& operator+=(const Vetor2D& o) { x_ += o.x_; y_ += o.y_; return *this; }
    constexpr Vetor2D& operator*=(double k) { x_ *= k; y_ *= k; return *this; }

    // Unário
    constexpr Vetor2D operator-() const { return {-x_, -y_}; }

    // Acesso por índice (duas versões, como em const em Métodos)
    double& operator[](int i) { return i == 0 ? x_ : y_; }
    const double& operator[](int i) const { return i == 0 ? x_ : y_; }

    // C++20: gera ==, != automaticamente
    friend constexpr bool operator==(const Vetor2D&, const Vetor2D&) = default;

    friend std::ostream& operator<<(std::ostream& os, const Vetor2D& v) {
        return os << '(' << v.x_ << ", " << v.y_ << ')';
    }

private:
    double x_, y_;
};

// Simétricos como funções livres, implementados com os compostos
constexpr Vetor2D operator+(Vetor2D a, const Vetor2D& b) { return a += b; }   // 'a' por valor (cópia)
constexpr Vetor2D operator*(Vetor2D a, double k) { return a *= k; }
constexpr Vetor2D operator*(double k, const Vetor2D& v) { return v * k; }

int main() {
    Vetor2D a{1, 2}, b{3, 4};
    std::cout << a + b << ' ' << 2.0 * a << ' ' << -b << ' ' << (a == b) << '\n';
    a += b;
    a[0] = 10;
    std::cout << a << ' ' << a[1] << '\n';
    constexpr Vetor2D c = Vetor2D{1, 1} + Vetor2D{2, 2};
    static_assert(c == Vetor2D{3, 3});
}
```

## Operador de comparação *three-way* `<=>` (C++20)

Um único operador gera `<`, `<=`, `>`, `>=` (e, com `== default`, `==` e `!=`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <compare>
#include <iostream>
#include <set>
#include <string>

struct Versao {
    int maior, menor;
    std::string tag;
    auto operator<=>(const Versao&) const = default;     // compara membro a membro na ordem
    bool operator==(const Versao&) const = default;
};

int main() {
    Versao a{1, 2, "a"}, b{1, 3, "a"};
    std::cout << (a < b) << (a == b) << (a >= b) << '\n';   // 100
    std::set<Versao> s{b, a};
    std::cout << s.begin()->menor << '\n';                  // 2
}
```

## `operator()` e conversões

- `operator()` cria **functors** (objetos chamáveis) — veja a seção de lambdas e STL.
- `explicit operator bool() const` permite `if (obj)` sem conversões acidentais ([[Conversões Implícitas e explicit]]).

> [!bug] Armadilhas
> - Sobrecarregar `&&`, `||` e `,` **perde** o curto-circuito e a ordem de avaliação: não faça.
> - `operator=` deve tratar **autoatribuição** (`a = a`) com segurança (regra dos 5, seção de RAII e Move).
> - `operator<<` para `std::ostream&`: retorne o stream para permitir encadeamento.
> - `a + b` não deve retornar referência a objeto local.

> [!tip] Menos código
> Implemente `+=` como membro e `+` em termos de `+=`; implemente `<=>` e `==` (ou `= default`) e ganhe todos os relacionais.

## Veja também

- [[Operadores - Cpp]]
- [[Encapsulamento e friend]]
- [[Conversões Implícitas e explicit]]
- [[default e delete]]

## Exercício

1. Implemente `Fracao` com `+`, `-`, `*`, `/`, `<=>` e `operator<<`, mantendo a fração simplificada.
2. Por que `operator+` costuma receber o primeiro parâmetro **por valor**?
