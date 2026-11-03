---
tags: [rust, colecoes]
aliases: ["BinaryHeap", "fila de prioridade"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Escolhendo uma coleção]]", "[[VecDeque]]"]
---

# BinaryHeap

`BinaryHeap<T>` é uma **fila de prioridade** que devolve sempre o **maior** elemento (max-heap).

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn main() {
    let mut h = BinaryHeap::new();
    h.push(3);
    h.push(9);
    h.push(1);
    println!("{:?}", h.peek()); // Some(9)
    while let Some(x) = h.pop() {
        print!("{x} ");
    }
    println!();

    // Min-heap com Reverse
    let mut mh = BinaryHeap::new();
    mh.push(Reverse(5));
    mh.push(Reverse(2));
    mh.push(Reverse(8));
    if let Some(Reverse(menor)) = mh.pop() {
        println!("menor = {menor}");
    }

    // Tuplas comparam lexicograficamente: (prioridade, tarefa)
    let mut tarefas = BinaryHeap::new();
    tarefas.push((2, "escrever"));
    tarefas.push((5, "urgente"));
    tarefas.push((1, "descansar"));
    println!("{:?}", tarefas.pop());
}
```

> [!info] Aplicações
> Algoritmo de Dijkstra, agendadores de tarefas e "top-K".

## Veja também

- [[Escolhendo uma coleção]]
- [[VecDeque]]
