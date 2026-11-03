---
tags: [rust, basico, controle-de-fluxo]
aliases: ["while", "for", "iteração"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[loop e break]]", "[[Ranges]]", "[[Iteradores]]"]
---

# while e for

```rust
fn main() {
    // while: condição avaliada a cada volta
    let mut n = 3;
    while n > 0 {
        println!("{n}...");
        n -= 1;
    }

    // for: itera sobre qualquer IntoIterator
    for i in 0..3 {
        println!("i = {i}");
    }

    let nomes = ["Ana", "Bia", "Caio"];
    for (indice, nome) in nomes.iter().enumerate() {
        println!("{indice}: {nome}");
    }

    // Em ordem inversa
    for i in (1..=3).rev() {
        print!("{i} ");
    }
    println!();
}
```

> [!tip] Prefira `for`
> `for` evita erros de índice e costuma ser tão rápido quanto laços manuais, pois o compilador elimina as checagens (zero-cost).

## Veja também

- [[loop e break]]
- [[Ranges]]
- [[Iteradores]]
