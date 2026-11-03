---
titulo: "Classes e structs"
tags: [cpp, poo, classes, structs]
aliases: ["Classes", "class vs struct", "Agregados", "Membros"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Construtores e Destrutores]]", "[[Encapsulamento e friend]]", "[[const em Métodos]]"]
---

# Classes e structs

Uma **classe** agrupa **dados** (membros) e **operações** (métodos) em um novo tipo. `struct` e `class` são quase idênticos: a única diferença é a **visibilidade padrão**.

| | `struct` | `class` |
|---|---|---|
| Membros por padrão | `public` | `private` |
| Herança por padrão | `public` | `private` |

> [!tip] Convenção
> `struct` para **dados simples** sem invariantes (pontos, configurações); `class` quando há **invariantes** a proteger e interface controlada.

## Exemplo

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

class ContaBancaria {
public:                                         // interface pública
    ContaBancaria(std::string titular, double saldo_inicial)
        : titular_(std::move(titular)), saldo_(saldo_inicial) {}

    void depositar(double v) {
        if (v > 0) saldo_ += v;                 // invariante: depósitos positivos
    }
    bool sacar(double v) {
        if (v <= 0 || v > saldo_) return false; // invariante: saldo nunca negativo
        saldo_ -= v;
        return true;
    }
    double saldo() const { return saldo_; }
    const std::string& titular() const { return titular_; }

private:                                        // detalhes de implementação
    std::string titular_;
    double saldo_;
};

struct Ponto {                                  // dados simples: struct
    double x = 0;
    double y = 0;
};

int main() {
    ContaBancaria c{"Ana", 100.0};
    c.depositar(50);
    std::cout << c.sacar(500) << ' ' << c.sacar(30) << ' ' << c.saldo() << '\n';   // 0 1 120
    // c.saldo_ = 1e9;     // erro: membro privado

    Ponto p{1.5, 2.5};
    Ponto q = p;                                // cópia membro a membro
    std::cout << q.x + q.y << '\n';             // 4
}
```

## Anatomia

| Elemento | Exemplo | Observação |
|---|---|---|
| Membros de dados | `double saldo_;` | Convenção: sufixo `_` para membros privados |
| Métodos | `void depositar(double)` | Definidos dentro (implicitamente `inline`) ou fora com `Classe::` |
| Controle de acesso | `public`, `protected`, `private` | Veja [[Encapsulamento e friend]] |
| Inicializadores de membro (NSDMI) | `double x = 0;` | C++11: valor padrão ao lado da declaração |
| Tipos aninhados e aliases | `using Id = int;` | Dentro da classe |

### Definindo métodos fora da classe

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Retangulo {
public:
    Retangulo(double l, double a);
    double area() const;
private:
    double largura_, altura_;
};

Retangulo::Retangulo(double l, double a) : largura_(l), altura_(a) {}   // 'Retangulo::' qualifica
double Retangulo::area() const { return largura_ * altura_; }

int main() { std::cout << Retangulo{3, 4}.area() << '\n'; }   // 12
```

Em projetos reais, a declaração fica no `.hpp` e as definições no `.cpp` ([[Pipeline de Compilação - Cpp]]).

## Agregados e inicialização designada

Uma `struct` sem construtores, sem membros privados e sem funções virtuais é um **agregado**: pode ser inicializada com chaves. Desde o C++20, também com **inicializadores designados**.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <string>

struct Config {
    std::string nome = "padrão";
    int porta = 8080;
    bool debug = false;
};

int main() {
    Config c1{};                                    // todos os padrões
    Config c2{"servidor", 9000, true};              // posicional
    Config c3{.nome = "api", .debug = true};        // designado (C++20): deve seguir a ordem de declaração
    std::cout << c1.porta << ' ' << c2.nome << ' ' << c3.porta << '\n';   // 8080 servidor 8080
}
```

## Tamanho e layout

Membros de dados são organizados em memória na ordem de declaração, com *padding* ([[sizeof e alignof]]). Uma classe vazia tem `sizeof` ≥ 1.

## Veja também

- [[Construtores e Destrutores]]
- [[Encapsulamento e friend]]
- [[const em Métodos]]
- [[this e Membros Estáticos]]
- [[sizeof e alignof]]

## Exercício

1. Crie uma classe `Temperatura` que guarde graus Celsius e ofereça `fahrenheit() const`, impedindo valores abaixo do zero absoluto (−273,15).
2. Transforme `Config` em uma `class` com construtor e explique o que muda na inicialização.
