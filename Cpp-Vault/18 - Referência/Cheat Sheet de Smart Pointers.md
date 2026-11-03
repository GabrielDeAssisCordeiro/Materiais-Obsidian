---
titulo: "Cheat sheet: smart pointers e posse"
tags: [cpp, referencia, cheat-sheet, smart-pointers, raii]
aliases: ["Cheat sheet smart pointers", "Resumo smart pointers", "unique_ptr shared_ptr weak_ptr resumo"]
tipo: referencia
nivel: iniciante
padrao: C++20
criado: 2026-10-24
relacionados: ["[[unique_ptr]]", "[[shared_ptr]]", "[[weak_ptr]]"]
---

# Cheat sheet: smart pointers e posse

## Regra de ouro

| Pergunta | Resposta |
|---|---|
| Quem é o dono do objeto? | Se há **um** dono: `unique_ptr`. Vários donos: `shared_ptr`. Sem posse: ponteiro/referência cru(a) ou `weak_ptr` |
| Preciso de um objeto em heap? | Talvez não: prefira **valores** (`std::vector`, membros por valor) |
| Posso usar `new`/`delete` direto? | Quase nunca: use `make_unique` / `make_shared` |

| Tipo | Posse | Cópia | Custo | Uso típico |
|---|---|---|---|---|
| `T` (valor) | Escopo | Copia | Nenhum | Padrão |
| `std::unique_ptr<T>` | **Exclusiva** | Só movimento | ≈ ponteiro cru | Polimorfismo, *factories*, pimpl |
| `std::shared_ptr<T>` | Compartilhada (contagem atômica) | Copia (incrementa) | Bloco de controle + atômicos | Grafos, caches, async |
| `std::weak_ptr<T>` | Observador de `shared_ptr` | Copia | Pequeno | Quebrar ciclos, caches |
| `T*` / `T&` | **Nenhuma** | Copia o ponteiro | Nenhum | Parâmetros "emprestados" |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <cstdio>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Forma {
    virtual ~Forma() = default;
    virtual double area() const = 0;
};
struct Quadrado : Forma {
    explicit Quadrado(double l) : l_{l} {}
    double area() const override { return l_ * l_; }
    double l_;
};

// Factory: retorna posse exclusiva
std::unique_ptr<Forma> criar(double l) { return std::make_unique<Quadrado>(l); }

// Parâmetros: "emprestar" = referência; "assumir posse" = unique_ptr por valor
double mostra(const Forma& f) { return f.area(); }
void guarda(std::vector<std::unique_ptr<Forma>>& v, std::unique_ptr<Forma> f) { v.push_back(std::move(f)); }

struct No {
    std::string nome;
    std::shared_ptr<No> proximo;
    std::weak_ptr<No> anterior;                                 // weak evita ciclo shared ↔ shared
};

int main() {
    auto f = criar(3);                                          // unique_ptr
    std::cout << mostra(*f) << '\n';                            // 9
    std::vector<std::unique_ptr<Forma>> v;
    guarda(v, std::move(f));                                    // f agora é nulo
    std::cout << (f == nullptr) << v.size() << '\n';            // 11

    auto a = std::make_shared<No>(No{"a", nullptr, {}});
    auto b = std::make_shared<No>(No{"b", nullptr, a});         // b observa a
    a->proximo = b;
    std::cout << a.use_count() << b.use_count() << '\n';        // 1 2
    if (auto p = b->anterior.lock()) std::cout << p->nome << '\n';   // lock(): vira shared_ptr se ainda existir

    // Deleter customizado (recurso C)
    std::unique_ptr<FILE, decltype(&fclose)> arq{std::fopen("/dev/null", "r"), &fclose};
    std::cout << (arq != nullptr) << '\n';
}
```

## O que evitar

| Antipadrão | Alternativa |
|---|---|
| `shared_ptr` por padrão | `unique_ptr` e valores |
| `f(std::shared_ptr<T>)` só para usar o objeto | `f(const T&)` ou `f(T*)` |
| `shared_ptr<T>(new T)` | `make_shared<T>()` (uma alocação, exceção-seguro) |
| Dois `shared_ptr` do **mesmo ponteiro cru** | Copie o `shared_ptr`, use `enable_shared_from_this` |
| `get()` guardado para depois | Não guarde: o objeto pode morrer |
| Ciclos `shared` ↔ `shared` | `weak_ptr` para o lado "não-dono" |
| `delete` em ponteiro de `unique_ptr` | Deixe o destrutor agir |

> [!info] C++26
> `std::unique_ptr` e `shared_ptr` são parte do vocabulário padrão desde C++11; `std::make_unique` desde C++14. `make_shared` e `make_unique` para arrays: C++20 (`make_shared<T[]>`).

## Veja também

- [[unique_ptr]]
- [[shared_ptr]]
- [[weak_ptr]]
- [[make_unique e make_shared]]
- [[Ciclos de Referência]]
- [[MOC - Referência - Cpp]]

## Exercício

1. Transforme uma lista encadeada com `new/delete` em uma com `unique_ptr`, cuidando do destrutor recursivo (e do risco de estouro de pilha).
2. Reescreva uma função `void f(std::shared_ptr<Foo>)` para a assinatura mais adequada e justifique.
