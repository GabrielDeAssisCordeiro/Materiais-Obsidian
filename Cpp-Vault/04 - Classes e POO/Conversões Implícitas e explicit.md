---
titulo: "Conversões implícitas e explicit"
tags: [cpp, poo, conversoes, construtores]
aliases: ["explicit", "Conversão implícita definida pelo usuário", "Operador de conversão", "explicit(bool)"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Construtores e Destrutores]]", "[[Conversões e Casts]]", "[[Sobrecarga de Operadores - Cpp]]"]
---

# Conversões implícitas e `explicit`

Um **construtor com um único parâmetro** (ou todos os demais com valor padrão) e um **operador de conversão** definem **conversões implícitas** entre tipos. Isso é conveniente, mas pode causar chamadas surpreendentes.

## O problema

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Buffer {
public:
    Buffer(std::size_t n) : tamanho_(n) {}              // sem explicit: int -> Buffer implícito!
    std::size_t tamanho() const { return tamanho_; }
private:
    std::size_t tamanho_;
};

void processa(const Buffer& b) { std::cout << "buffer de " << b.tamanho() << '\n'; }

int main() {
    processa(1024);        // compila: 1024 vira Buffer(1024). Intencional? Muitas vezes, não.
    Buffer b = 7;          // inicialização por cópia com conversão
    (void)b;
}
```

## A solução: `explicit`

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Buffer {
public:
    explicit Buffer(std::size_t n) : tamanho_(n) {}     // exige conversão explícita
    std::size_t tamanho() const { return tamanho_; }
private:
    std::size_t tamanho_;
};

void processa(const Buffer& b) { std::cout << "buffer de " << b.tamanho() << '\n'; }

int main() {
    processa(Buffer{1024});    // OK: explícito
    // processa(1024);         // erro: sem conversão implícita
    // Buffer b = 7;           // erro (inicialização por cópia)
    Buffer c{7};               // OK: inicialização direta
    (void)c;
}
```

> [!tip] Regra de ouro (Core Guidelines C.46)
> **Marque `explicit` em todo construtor de um argumento**, salvo quando a conversão implícita for uma decisão consciente (por exemplo, `std::string` a partir de `const char*`, `std::function` a partir de um chamável).

## `explicit` em operadores de conversão

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>

class Handle {
public:
    explicit Handle(int fd) : fd_(fd) {}
    explicit operator bool() const { return fd_ >= 0; }   // utilizável em condições, mas não em aritmética
    operator int() const { return fd_; }                  // conversão implícita para int (use com cuidado)
private:
    int fd_;
};

int main() {
    Handle h{3};
    if (h) std::cout << "válido\n";              // contexto booleano: permitido com explicit operator bool
    // bool b = h;                                // erro: conversão implícita não permitida
    bool b = static_cast<bool>(h);                // explícito: OK
    int n = h;                                    // usa operator int() implícito
    std::cout << b << ' ' << n << '\n';
}
```

## `explicit(bool)` condicional (C++20)

Torna o `explicit` dependente de uma constante de compilação: útil em tipos genéricos (por exemplo, `std::pair` e `std::tuple`).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <type_traits>

template <typename T>
struct Caixa {
    T valor;
    // implícito se T for aritmético; explícito caso contrário
    template <typename U>
    explicit(!std::is_arithmetic_v<U>) Caixa(U v) : valor(static_cast<T>(v)) {}
};

int main() {
    Caixa<double> c = 3;       // OK: int é aritmético, conversão implícita permitida
    std::cout << c.valor << '\n';
}
```

## Regra das conversões definidas pelo usuário

Uma sequência de conversão implícita pode conter **no máximo uma** conversão definida pelo usuário (por construtor ou operador), mais conversões padrão antes e depois.

> [!bug] Exemplo inválido proposital
> ```cpp
> struct A { A(int) {} };
> struct B { B(const A&) {} };
> void f(B);
> f(1);      // erro: int -> A -> B exigiria DUAS conversões definidas pelo usuário
> f(A{1});   // OK
> ```

## Veja também

- [[Construtores e Destrutores]]
- [[Conversões e Casts]]
- [[Sobrecarga de Operadores - Cpp]]
- [[Sobrecarga de Funções]]

## Exercício

1. Ache um construtor de um argumento na biblioteca padrão que **não** é `explicit` e explique por que isso é útil.
2. Por que `explicit operator bool` é preferido a `operator bool`?
