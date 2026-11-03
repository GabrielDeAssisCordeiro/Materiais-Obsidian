---
titulo: "this e membros estáticos"
tags: [cpp, poo, static]
aliases: ["this", "Membros estáticos", "static em classes"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Classes e Structs]]", "[[const em Métodos]]", "[[Escopo e Duração de Armazenamento]]"]
---

# `this` e membros estáticos

## `this`

Dentro de um método **não estático**, `this` é um **ponteiro para o objeto** sobre o qual o método foi chamado. Acessar `x` é o mesmo que `this->x`.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Contador {
public:
    explicit Contador(int valor) : valor_(valor) {}

    Contador& soma(int n) { valor_ += n; return *this; }     // devolve *this: encadeamento
    Contador& dobra()     { valor_ *= 2; return *this; }
    int valor() const { return valor_; }

    void define(int valor) { this->valor_ = valor; }         // 'this->' desambigua do parâmetro
    bool igual(const Contador& o) const { return this == &o || valor_ == o.valor_; }

private:
    int valor_;
};

int main() {
    Contador c{1};
    c.soma(2).dobra().soma(4);                               // ((1+2)*2)+4 = 10
    std::cout << c.valor() << '\n';
}
```

> [!info] *Deducing this* (C++23)
> Um parâmetro de objeto explícito (`void f(this Contador& self)`) elimina duplicações `const`/não-`const` e facilita CRTP e lambdas recursivas. Suporte: GCC 14, Clang 18, MSVC 17.2.
> [!question] Verificar na documentação oficial
> Confirme o suporte no seu compilador.

## Membros estáticos

Pertencem à **classe**, não a um objeto: existem **uma vez** para todo o programa.

| Tipo | Declaração | Acesso |
|---|---|---|
| Dado estático | `static int total;` | `Classe::total` |
| Método estático | `static int quantos();` | `Classe::quantos()` (sem `this`) |
| Constante estática | `static constexpr int MAX = 10;` | Direto, sem definição fora (C++17: implicitamente `inline`) |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Sensor {
public:
    Sensor() { ++total_; id_ = ++proximo_id_; }
    ~Sensor() { --total_; }

    int id() const { return id_; }
    static int total() { return total_; }                     // não acessa membros não estáticos

    static constexpr int kMaxSensores = 8;                    // constante de classe

private:
    int id_;
    inline static int total_ = 0;                             // C++17: definição na própria classe
    inline static int proximo_id_ = 0;
};

int main() {
    Sensor a, b;
    {
        Sensor c;
        std::cout << Sensor::total() << ' ' << c.id() << '\n';    // 3 3
    }
    std::cout << Sensor::total() << ' ' << Sensor::kMaxSensores << '\n';   // 2 8
}
```

> [!bug] Antes do C++17: definição fora da classe
> ```cpp
> class A { static int n; };
> int A::n = 0;      // obrigatória em UM .cpp; esquecer gera "undefined reference to A::n"
> ```
> Com `inline static` (C++17) isso não é necessário.

> [!warning] Estado estático compartilhado
> Dados estáticos são **estado global** disfarçado: dificultam testes e causam *data races* em programas com threads. Use com moderação e proteja com `std::atomic`/mutex quando necessário.

## Usos comuns

- Contadores de instâncias e geração de IDs.
- Constantes associadas ao tipo.
- **Fábricas** (*factory methods*): `static Pessoa de_json(const std::string&)`.
- Métodos utilitários que não dependem de estado.

## Veja também

- [[Classes e Structs]]
- [[const em Métodos]]
- [[Escopo e Duração de Armazenamento]]
- [[Argumentos Padrão e inline]]

## Exercício

1. Implemente um `StringBuilder` com métodos encadeáveis (`add`, `linha`) retornando `*this`.
2. Por que um método `static` não pode ser `const`?
