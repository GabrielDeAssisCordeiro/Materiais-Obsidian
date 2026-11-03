---
titulo: "std::list e std::forward_list"
tags: [cpp, stl, conteineres]
aliases: ["std::list", "std::forward_list", "list", "forward_list", "Lista encadeada", "splice"]
tipo: conceito
nivel: intermediario
padrao: C++11
criado: 2026-10-24
relacionados: ["[[vector]]", "[[deque]]", "[[Escolhendo um Contêiner]]"]
---

# `std::list` e `std::forward_list`

| | `std::list` | `std::forward_list` (C++11) |
|---|---|---|
| Estrutura | Lista **duplamente** encadeada | Lista **simplesmente** encadeada |
| Iteração | Ambas as direções | Só para frente |
| Overhead por nó | 2 ponteiros | 1 ponteiro |
| `size()` | O(1) | **Não existe** |
| Inserção após/antes de uma posição | O(1) | `insert_after` O(1) |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <forward_list>
#include <iostream>
#include <list>

int main() {
    std::list<int> a{3, 1, 2};
    a.push_front(0);
    a.push_back(9);

    auto it = std::next(a.begin(), 2);        // avançar iterador é O(n): não há acesso aleatório
    a.insert(it, 100);                        // O(1) dado o iterador
    a.remove(9);                              // remove todos com valor 9
    a.sort();                                 // sort é MÉTODO (std::sort exige acesso aleatório)
    a.unique();                               // remove duplicados consecutivos
    for (int x : a) std::cout << x << ' ';
    std::cout << '\n';

    std::list<int> b{7, 8};
    a.splice(a.end(), b);                     // move os nós de b para a em O(1): sem cópia
    std::cout << a.size() << b.size() << '\n';

    std::forward_list<int> f{1, 2, 3};
    f.push_front(0);
    f.insert_after(f.begin(), 42);
    for (int x : f) std::cout << x << ' ';
    std::cout << '\n';
}
```

## Pontos fortes

- **Iteradores e referências estáveis**: inserir/remover não invalida os demais elementos.
- `splice`, `merge`, `reverse`, `sort`, `unique`, `remove_if` **sem mover valores** (religa nós).
- Inserção/remoção em O(1) quando se tem o iterador.

## Pontos fracos (por que raramente são a melhor escolha)

> [!warning] Listas encadeadas costumam ser lentas na prática
> - Cada nó é uma **alocação separada** → mais custo e fragmentação.
> - Nós espalhados na memória → **cache misses**; percorrer uma lista pode ser ordens de grandeza mais lento que um `vector`.
> - Sem acesso aleatório, busca é O(n).
>
> Muitas vezes `std::vector` com `erase`/`insert` em O(n) **vence** `std::list` até para milhares de elementos. Meça antes de escolher.

## Quando usar

| Situação | Escolha |
|---|---|
| Precisa de iteradores/referências **estáveis** ao inserir/remover no meio | `list` |
| Precisa de `splice` entre contêineres em O(1) | `list` |
| Memória mínima, só `push_front` e travessia | `forward_list` |
| Qualquer outro caso | `vector` |

> [!bug] Armadilha: invalidar o iterador ao apagar
> ```cpp
> for (auto it = l.begin(); it != l.end(); ++it)
>     if (*it == 0) l.erase(it);     // 'it' inválido depois do erase: UB
> ```
> **Correção:** `it = l.erase(it);` (e só incremente no `else`), ou `l.remove(0);`.

## Veja também

- [[vector]]
- [[deque]]
- [[Complexidade e Invalidação de Iteradores]]
- [[Escolhendo um Contêiner]]

## Exercício

1. Remova de uma `std::list<int>` todos os pares percorrendo com iteradores e tratando corretamente `erase`.
2. Compare o tempo de percorrer e somar 10 milhões de inteiros em `vector<int>` e `list<int>`.
