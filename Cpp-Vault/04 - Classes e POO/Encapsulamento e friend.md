---
titulo: "Encapsulamento e friend"
tags: [cpp, poo, encapsulamento]
aliases: ["Encapsulamento", "friend", "public private protected"]
tipo: conceito
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Classes e Structs]]", "[[Herança]]", "[[Sobrecarga de Operadores - Cpp]]"]
---

# Encapsulamento e `friend`

**Encapsulamento** é esconder a representação interna e expor apenas uma **interface** que preserve as **invariantes** da classe (condições que sempre devem valer).

## Níveis de acesso

| Especificador | Classe | Derivadas | Código externo |
|---|---|---|---|
| `public` | ✓ | ✓ | ✓ |
| `protected` | ✓ | ✓ | ✗ |
| `private` | ✓ | ✗ | ✗ |

> [!tip] Regra prática
> Dados **privados**, interface **pública** mínima. Evite `protected` para dados: o acoplamento com subclasses fica forte demais.

## Exemplo com invariante

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <stdexcept>

class Intervalo {                          // invariante: inicio <= fim
public:
    Intervalo(int inicio, int fim) : inicio_(inicio), fim_(fim) {
        if (inicio > fim) throw std::invalid_argument("inicio > fim");
    }
    int inicio() const { return inicio_; }
    int fim() const { return fim_; }
    int tamanho() const { return fim_ - inicio_; }

    void mover_fim(int novo_fim) {
        if (novo_fim < inicio_) throw std::invalid_argument("fim < inicio");
        fim_ = novo_fim;                   // única porta de modificação: invariante preservada
    }

private:
    int inicio_;
    int fim_;
};

int main() {
    Intervalo i{2, 10};
    i.mover_fim(5);
    std::cout << i.tamanho() << '\n';      // 3
    try { Intervalo{5, 1}; } catch (const std::exception& e) { std::cout << e.what() << '\n'; }
}
```

> [!bug] Getters/setters triviais não são encapsulamento
> Uma classe com `get_x()`/`set_x()` para cada campo e nenhuma invariante é só uma `struct` verbosa. Se não há invariante, use `struct` com membros públicos.

## `friend`

`friend` concede a uma função ou classe **acesso aos membros privados**. Não é herdado nem transitivo.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Cofre {
public:
    explicit Cofre(int valor) : valor_(valor) {}

    friend std::ostream& operator<<(std::ostream& os, const Cofre& c) {   // função amiga definida na classe
        return os << "Cofre(" << c.valor_ << ")";
    }
    friend class Auditor;                                                  // classe amiga
    friend bool operator==(const Cofre&, const Cofre&) = default;          // C++20: comparação padrão como amiga

private:
    int valor_;
};

class Auditor {
public:
    static int espiar(const Cofre& c) { return c.valor_; }                 // acesso privilegiado
};

int main() {
    Cofre a{10}, b{10};
    std::cout << a << ' ' << Auditor::espiar(a) << ' ' << (a == b) << '\n';   // Cofre(10) 10 1
}
```

### Quando usar `friend`

| Uso legítimo | Alternativa |
|---|---|
| `operator<<` e operadores simétricos ([[Sobrecarga de Operadores - Cpp]]) | — |
| Classes fortemente acopladas (iterador e contêiner) | Tipo aninhado |
| Testes de unidade que precisam inspecionar internos | Testar pela interface pública (preferido) |

> [!warning] `friend` quebra o encapsulamento
> Use pouco. Cada `friend` é um novo cliente que depende da representação interna.

## Veja também

- [[Classes e Structs]]
- [[Herança]]
- [[Sobrecarga de Operadores - Cpp]]
- [[const em Métodos]]

## Exercício

1. Crie uma classe `Fracao` que nunca aceita denominador zero e sempre mantém a fração simplificada.
2. Explique por que `friend` não é herdado: se `A` é amiga de `B` e `C` herda de `B`, `A` acessa privados de `C`?
