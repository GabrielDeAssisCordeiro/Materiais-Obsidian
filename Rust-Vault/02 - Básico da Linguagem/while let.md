---
tags: [rust, basico, controle-de-fluxo, pattern-matching]
aliases: ["while let"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[if let e let else]]", "[[match]]"]
---

# while let

`while let` repete enquanto o padrão casar. É ideal para consumir pilhas, filas e iteradores manualmente.

```rust
fn main() {
    let mut pilha = vec![1, 2, 3];

    // pop devolve Option<T>: Some enquanto houver elementos
    while let Some(topo) = pilha.pop() {
        println!("{topo}");
    }

    // Também com iteradores
    let mut it = "a b c".split(' ');
    while let Some(parte) = it.next() {
        print!("[{parte}]");
    }
    println!();
}
```

## Veja também

- [[if let e let else]]
- [[match]]
