---
titulo: "Regra do 0, 3 e 5"
tags: [cpp, raii]
aliases: ["Regra do 0", "Regra do 3", "Regra do 5", "Rule of Zero", "Rule of Three", "Rule of Five"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[RAII]]", "[[Semântica de Movimento]]", "[[default e delete]]"]
---

# Regra do 0, 3 e 5

Seis funções membro especiais controlam como um tipo é criado, copiado, movido e destruído. A regra diz **quais declarar juntas**.

| Função | Assinatura |
|---|---|
| Destrutor | `~T()` |
| Construtor de cópia | `T(const T&)` |
| Atribuição de cópia | `T& operator=(const T&)` |
| Construtor de movimento | `T(T&&) noexcept` |
| Atribuição de movimento | `T& operator=(T&&) noexcept` |
| (Construtor padrão) | `T()` |

## Regra do 0 (preferida)

> **Se sua classe não gerencia recursos diretamente, não declare nenhuma delas.** Use membros que já são RAII (`std::string`, `std::vector`, `std::unique_ptr`...) e o compilador gera tudo corretamente.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <memory>
#include <string>
#include <vector>

class Pedido {                                   // Regra do 0: nenhuma função especial escrita
    std::string cliente_;
    std::vector<int> itens_;
    std::unique_ptr<int> cupom_;                 // torna a classe movível e NÃO copiável, automaticamente
public:
    Pedido(std::string c) : cliente_(std::move(c)) {}
};

int main() {
    Pedido a{"ana"};
    Pedido b = std::move(a);                     // movimento gerado pelo compilador
}
```

## Regra do 3 (C++98)

Se você declara **destrutor**, **construtor de cópia** ou **atribuição de cópia**, quase certamente precisa declarar **os três**: o tipo gerencia um recurso (por exemplo, memória bruta) e a cópia padrão (rasa) seria um bug (dupla liberação).

## Regra do 5 (C++11)

Com semântica de movimento, acrescente **construtor e atribuição de movimento**: **cinco** funções. Se declarar qualquer uma, declare (ou `= default`/`= delete`) as cinco.

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <cstddef>
#include <iostream>
#include <utility>

class Buffer {
public:
    explicit Buffer(std::size_t n = 0) : n_(n), dados_(n ? new int[n]{} : nullptr) {}

    ~Buffer() { delete[] dados_; }                                      // 1) destrutor

    Buffer(const Buffer& o) : n_(o.n_), dados_(o.n_ ? new int[o.n_] : nullptr) {   // 2) cópia profunda
        std::copy(o.dados_, o.dados_ + n_, dados_);
    }

    Buffer& operator=(const Buffer& o) {                                // 3) atribuição de cópia
        if (this != &o) {                                               // proteção contra autoatribuição
            Buffer tmp(o);                                              // copy-and-swap
            swap(tmp);
        }
        return *this;
    }

    Buffer(Buffer&& o) noexcept : n_(std::exchange(o.n_, 0)),           // 4) movimento: rouba os recursos
                                  dados_(std::exchange(o.dados_, nullptr)) {}

    Buffer& operator=(Buffer&& o) noexcept {                            // 5) atribuição de movimento
        if (this != &o) {
            delete[] dados_;
            n_ = std::exchange(o.n_, 0);
            dados_ = std::exchange(o.dados_, nullptr);
        }
        return *this;
    }

    void swap(Buffer& o) noexcept { std::swap(n_, o.n_); std::swap(dados_, o.dados_); }
    std::size_t tamanho() const { return n_; }
    int& operator[](std::size_t i) { return dados_[i]; }

private:
    std::size_t n_;
    int* dados_;
};

int main() {
    Buffer a{4};
    a[0] = 42;
    Buffer b = a;                 // cópia profunda
    Buffer c = std::move(a);      // movimento: a fica vazio
    b[0] = 7;
    std::cout << c[0] << ' ' << b[0] << ' ' << a.tamanho() << '\n';   // 42 7 0
}
```

> [!danger] Cópia rasa gera *double free*
> ```cpp
> class Ruim { int* p = new int(1); public: ~Ruim() { delete p; } };
> Ruim a; Ruim b = a;      // cópia padrão copia o ponteiro: dois donos
> // ao sair do escopo: delete duplo do mesmo bloco -> UB
> ```
> **Correção:** Regra do 0 (`std::unique_ptr<int>`/`std::vector<int>`) ou Regra do 3/5.

## Como o compilador decide gerar

| Se você declara... | Cópia | Movimento |
|---|---|---|
| Nada | gerada | gerado |
| Destrutor | gerada (obsoleto) | **não** gerado (usa cópia) |
| Cópia | gerada | **não** gerado |
| Movimento | **deletada** | declarado |

## Guia rápido

1. Pode usar membros RAII? **Regra do 0**.
2. Gerencia recurso bruto? **Regra do 5**, com `noexcept` nos movimentos.
3. Não deve ser copiável? `= delete` cópia, movimento permitido (como `unique_ptr`).
4. Classe base polimórfica? Destrutor `virtual` e cópia protegida/deletada ([[Slicing]]).

## Veja também

- [[RAII]]
- [[Semântica de Movimento]]
- [[Construtores de Cópia e Atribuição]]
- [[noexcept e Movimento]]
- [[default e delete]]

## Exercício

1. Remova a atribuição de movimento do `Buffer` e verifique (com saídas de depuração) que `b = std::move(c)` passa a usar a cópia.
2. Reescreva `Buffer` aplicando a Regra do 0 com `std::vector<int>`.
