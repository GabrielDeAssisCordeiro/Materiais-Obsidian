---
titulo: "Construtor de cópia e atribuição de cópia"
tags: [cpp, raii, copia]
aliases: ["Atribuição de cópia", "Cópia profunda", "Cópia rasa", "Copy-and-swap"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Regra do 0, 3 e 5]]", "[[Semântica de Movimento]]", "[[Construtores e Destrutores]]"]
---

# Construtor de cópia e atribuição de cópia

| Operação | Sintaxe | Quando acontece |
|---|---|---|
| Construção por cópia | `T b = a;`, `T b(a);`, `T b{a};` | Cria um objeto novo a partir de outro |
| Atribuição por cópia | `b = a;` | Substitui o conteúdo de um objeto **existente** |
| Cópia implícita | Passar/retornar por valor | Quando não há elisão ou movimento |

## Cópia rasa vs profunda

- **Rasa** (*shallow*): copia os membros bit a bit — ponteiros passam a apontar para o **mesmo** bloco (perigoso).
- **Profunda** (*deep*): cria uma **nova** alocação e copia o conteúdo.

O construtor de cópia gerado pelo compilador copia **cada membro** com sua própria semântica de cópia; é correto se todos os membros forem tipos RAII.

## Implementação com *copy-and-swap*

O idioma garante **segurança forte contra exceções** e trata autoatribuição sem verificação explícita.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <string>
#include <utility>

class Texto {
public:
    explicit Texto(const char* s = "")
        : n_(std::char_traits<char>::length(s)), p_(new char[n_ + 1]) {
        std::copy(s, s + n_ + 1, p_);
    }
    ~Texto() { delete[] p_; }

    Texto(const Texto& o) : n_(o.n_), p_(new char[o.n_ + 1]) {      // cópia profunda
        std::copy(o.p_, o.p_ + n_ + 1, p_);
    }

    Texto& operator=(Texto o) noexcept {                             // parâmetro POR VALOR: cópia (ou move) já feita
        swap(o);                                                     // troca: o antigo conteúdo vai para 'o' e morre
        return *this;
    }

    void swap(Texto& o) noexcept { std::swap(n_, o.n_); std::swap(p_, o.p_); }
    const char* c_str() const { return p_; }

private:
    std::size_t n_;
    char* p_;
};

int main() {
    Texto a{"olá"};
    Texto b;
    b = a;                         // copy-and-swap
    b = b;                         // autoatribuição segura
    std::cout << b.c_str() << '\n';
}
```

> [!tip] Uma única atribuição para cópia e movimento
> Com `operator=(Texto o)` por valor, a mesma função atende `b = a` (cópia) e `b = std::move(c)` (o parâmetro é construído por movimento). Trade-off: pode ter uma alocação a mais que implementações especializadas.

## Autoatribuição

```cpp
b = b;      // deve ser segura (e normalmente barata)
```
Se escrever a atribuição "à mão" (sem *copy-and-swap*), proteja com `if (this != &o)` e **não** libere antes de copiar.

> [!bug] Atribuição insegura
> ```cpp
> T& operator=(const T& o) {
>     delete[] p_;                 // se &o == this, perdeu os dados!
>     p_ = new char[o.n_ + 1];     // e se 'new' lançar? objeto fica inválido
>     std::copy(o.p_, o.p_ + o.n_ + 1, p_);
>     return *this;
> }
> ```

## Controlando a cópia

| Objetivo | Como |
|---|---|
| Proibir | `T(const T&) = delete; T& operator=(const T&) = delete;` |
| Padrão do compilador | `= default` |
| Cópia "barata" por contagem de referências | `std::shared_ptr` / *copy-on-write* (cuidado) |

## Cópia e herança

Em bases polimórficas a cópia por valor causa *slicing*. Use `clone()` ([[Slicing]]).

## Veja também

- [[Regra do 0, 3 e 5]]
- [[Semântica de Movimento]]
- [[Copy Elision e RVO]]
- [[Slicing]]

## Exercício

1. Adicione `std::cout` a cada operação especial de `Texto` e conte quantas cópias ocorrem ao passar `Texto` por valor a uma função.
2. Por que `operator=(Texto o)` é `noexcept` se a cópia pode lançar exceção?
