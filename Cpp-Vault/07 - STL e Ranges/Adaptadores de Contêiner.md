---
titulo: "Adaptadores: stack, queue, priority_queue"
tags: [cpp, stl, stack]
aliases: ["std::stack", "std::queue", "std::priority_queue", "Adaptadores"]
tipo: conceito
nivel: iniciante
padrao: C++98
criado: 2026-10-24
relacionados: ["[[deque]]", "[[vector]]", "[[Escolhendo um Contêiner]]"]
---

# Adaptadores: `stack`, `queue`, `priority_queue`

Adaptadores **restringem a interface** de um contêiner subjacente para expressar uma estrutura de dados clássica. Não têm iteradores.

| Adaptador | Disciplina | Contêiner padrão | Operações |
|---|---|---|---|
| `std::stack<T>` | LIFO (último a entrar, primeiro a sair) | `deque` | `push`, `pop`, `top` |
| `std::queue<T>` | FIFO | `deque` | `push`, `pop`, `front`, `back` |
| `std::priority_queue<T>` | Maior prioridade primeiro | `vector` + heap | `push`, `pop`, `top` |

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <functional>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>

int main() {
    std::stack<int> pilha;
    pilha.push(1); pilha.push(2); pilha.push(3);
    std::cout << pilha.top() << '\n';            // 3
    pilha.pop();                                 // pop NÃO retorna valor (segurança de exceções)

    std::queue<std::string> fila;
    fila.push("a"); fila.push("b");
    std::cout << fila.front() << fila.back() << '\n';   // ab
    fila.pop();

    std::priority_queue<int> maxheap;            // maior no topo
    for (int x : {5, 1, 8, 3}) maxheap.push(x);
    std::cout << maxheap.top() << '\n';          // 8

    std::priority_queue<int, std::vector<int>, std::greater<>> minheap;   // menor no topo
    for (int x : {5, 1, 8, 3}) minheap.push(x);
    while (!minheap.empty()) { std::cout << minheap.top() << ' '; minheap.pop(); }   // 1 3 5 8
    std::cout << '\n';
}
```

## `priority_queue` com tipo próprio

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <queue>
#include <string>
#include <vector>

struct Tarefa {
    int prioridade;
    std::string nome;
    bool operator<(const Tarefa& o) const { return prioridade < o.prioridade; }   // maior prioridade sai primeiro
};

int main() {
    std::priority_queue<Tarefa> fila;
    fila.push({2, "relatório"});
    fila.push({9, "incidente"});
    fila.push({5, "reunião"});
    while (!fila.empty()) { std::cout << fila.top().nome << '\n'; fila.pop(); }   // incidente, reunião, relatório
}
```

## Complexidade

| Operação | `stack`/`queue` | `priority_queue` |
|---|---|---|
| `push` / `emplace` | O(1) | O(log n) |
| `pop` | O(1) | O(log n) |
| `top`/`front` | O(1) | O(1) |
| Construção a partir de n elementos | O(n) | O(n) (heapify) |

> [!warning] Sem iteração
> Não é possível percorrer ou buscar em um adaptador. Se precisar, use diretamente o contêiner subjacente.

> [!tip] Usos típicos
> `stack`: avaliação de expressões, DFS, desfazer. `queue`: BFS, filas de tarefas (mono-thread). `priority_queue`: Dijkstra, agendadores, "top-k".

## Veja também

- [[deque]]
- [[vector]]
- [[Escolhendo um Contêiner]]
- [[Complexidade e Invalidação de Iteradores]]

## Exercício

1. Verifique parênteses balanceados em uma expressão com `std::stack<char>`.
2. Encontre os k maiores elementos de um vetor com uma `priority_queue` de tamanho k.
