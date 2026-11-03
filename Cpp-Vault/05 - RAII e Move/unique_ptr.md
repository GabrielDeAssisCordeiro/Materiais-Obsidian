---
titulo: "std::unique_ptr"
tags: [cpp, smart-pointers]
aliases: ["std::unique_ptr", "unique_ptr", "Posse exclusiva", "Smart pointer"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[make_unique e make_shared]]", "[[shared_ptr]]", "[[Deleters Customizados]]"]
---

# `std::unique_ptr`

> [!info] Introdução
> **C++11** (`<memory>`). Substitui o obsoleto `std::auto_ptr` (removido no C++17). `std::make_unique` chegou no **C++14**.

`unique_ptr<T>` tem **posse exclusiva** de um objeto no heap: ao ser destruído, deleta o objeto. É **move-only** (não copiável) e tem **custo zero** em relação a um ponteiro bruto (com o *deleter* padrão).

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>
#include <utility>
#include <vector>

struct Widget {
    explicit Widget(int id) : id(id) { std::cout << "Widget " << id << " criado\n"; }
    ~Widget() { std::cout << "Widget " << id << " destruído\n"; }
    int id;
};

std::unique_ptr<Widget> cria(int id) { return std::make_unique<Widget>(id); }   // retorna por valor: move/elisão

void consome(std::unique_ptr<Widget> w) { std::cout << "consumindo " << w->id << '\n'; }   // toma posse
void observa(const Widget& w) { std::cout << "observando " << w.id << '\n'; }                // só observa

int main() {
    auto a = cria(1);
    // auto b = a;                    // erro: não copiável
    auto b = std::move(a);            // transfere a posse: a == nullptr
    std::cout << (a == nullptr) << '\n';   // 1

    observa(*b);                      // passe referência/ponteiro bruto para quem só usa
    b.reset();                        // destrói agora
    auto c = cria(2);
    consome(std::move(c));            // posse passa para a função; destruído ao sair dela
    std::cout << "depois\n";

    std::vector<std::unique_ptr<Widget>> v;     // contêiner de donos únicos
    v.push_back(cria(3));
    v.emplace_back(new Widget(4));              // ok, mas prefira make_unique
}
```

## Operações principais

| Operação | Efeito |
|---|---|
| `*p`, `p->m` | Acesso ao objeto |
| `p.get()` | Ponteiro bruto **sem** transferir posse |
| `p.release()` | Devolve o ponteiro bruto e **abre mão** da posse (você deve deletar) |
| `p.reset()` / `p.reset(novo)` | Deleta o atual (e, opcionalmente, adota outro) |
| `std::move(p)` | Transfere posse |
| `if (p)` | Teste de nulo |
| `p.swap(q)` | Troca |

## Arrays

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <memory>

int main() {
    auto arr = std::make_unique<int[]>(5);        // usa delete[] automaticamente
    arr[0] = 10;
    std::cout << arr[0] << arr[4] << '\n';        // 100 (valor-inicializado: zeros)
}
```
Mas prefira `std::vector`/`std::array` a `unique_ptr<T[]>`.

## Convenções de interface (Core Guidelines R.30 a R.34)

| Parâmetro | Significado |
|---|---|
| `std::unique_ptr<T>` por valor | A função **toma posse** |
| `std::unique_ptr<T>&` | A função pode **reatribuir** o ponteiro do chamador (raro) |
| `T*` / `T&` | A função apenas **usa** o objeto |
| Retorno `std::unique_ptr<T>` | Fábrica entregando posse |

> [!danger] Erros típicos
> ```cpp
> Widget* raw = new Widget(1);
> std::unique_ptr<Widget> a(raw);
> std::unique_ptr<Widget> b(raw);   // DOIS donos do mesmo objeto: double delete (UB)
>
> auto p = std::make_unique<Widget>(1);
> Widget* q = p.release();          // agora VOCÊ deve fazer delete q; esquecer vaza
> ```
> **Regra:** nunca crie dois `unique_ptr` a partir do mesmo ponteiro bruto; prefira `make_unique`.

> [!tip] `unique_ptr` primeiro
> Comece sempre com `unique_ptr`. Converter para `shared_ptr` depois é trivial (`std::shared_ptr<T> s = std::move(u);`); o inverso não.

## Usos clássicos

- Dono de objetos polimórficos (`std::unique_ptr<Base>`).
- Idioma **pimpl** (ponteiro para implementação) — seção de avançado.
- Dono de recursos C com *deleter* personalizado ([[Deleters Customizados]]).
- Nós de estruturas de dados (listas, árvores).

## Veja também

- [[make_unique e make_shared]]
- [[shared_ptr]]
- [[Deleters Customizados]]
- [[RAII]]
- [[Semântica de Movimento]]

## Exercício

1. Implemente uma lista encadeada simples com `std::unique_ptr<No> proximo` e verifique o que acontece ao destruir uma lista com 1 milhão de nós (risco de *stack overflow* na destruição recursiva).
2. Por que `std::unique_ptr` não pode ser usado em `std::initializer_list` para construir um `std::vector`?
