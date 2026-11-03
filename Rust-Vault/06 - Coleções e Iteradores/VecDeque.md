---
tags: [rust, colecoes]
aliases: ["VecDeque", "fila", "buffer circular"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Escolhendo uma coleção]]", "[[Vec]]"]
---

# VecDeque

`VecDeque<T>` é um deque (fila de duas pontas) implementado como buffer circular: inserir e remover nas **duas extremidades** é O(1).

```rust
use std::collections::VecDeque;

fn main() {
    let mut fila = VecDeque::new();
    fila.push_back(1);
    fila.push_back(2);
    fila.push_front(0);

    println!("{:?}", fila); // [0, 1, 2]

    while let Some(x) = fila.pop_front() {
        print!("{x} ");
    }
    println!();

    // BFS: uso clássico de fila
    let mut a_visitar = VecDeque::from([1]);
    let mut ordem = Vec::new();
    while let Some(n) = a_visitar.pop_front() {
        ordem.push(n);
        if n < 4 {
            a_visitar.push_back(n * 2);
            a_visitar.push_back(n * 2 + 1);
        }
    }
    println!("{:?}", ordem);
}
```

> [!tip] Use em filas
> Para filas (FIFO), `VecDeque` é bem mais adequado que `Vec`, onde `remove(0)` custa O(n).

## Veja também

- [[Escolhendo uma coleção]]
- [[Vec]]
