---
tags: [rust, pattern-matching, structs]
aliases: ["destructuring", "let com padrão"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Pattern matching avançado]]", "[[Tuplas]]", "[[Structs]]"]
---

# Desestruturação

Desestruturar é decompor um valor composto em partes com um padrão.

```rust
struct Ponto {
    x: i32,
    y: i32,
}

fn soma((a, b): (i32, i32)) -> i32 {
    a + b // desestruturação direto no parâmetro
}

fn main() {
    // Tuplas
    let (a, b, c) = (1, "dois", 3.0);
    println!("{a} {b} {c}");

    // Structs
    let p = Ponto { x: 3, y: -3 };
    let Ponto { x, y } = p;
    println!("{x} {y}");

    // Renomeando campos e ignorando o resto
    let p2 = Ponto { x: 10, y: 20 };
    let Ponto { x: horizontal, .. } = p2;
    println!("{horizontal}");

    // Arrays
    let [primeiro, segundo, _] = [10, 20, 30];
    println!("{primeiro} {segundo}");

    // Em closures e laços
    let pares = vec![(1, 'a'), (2, 'b')];
    for (n, c) in &pares {
        println!("{n}{c}");
    }

    println!("{}", soma((2, 3)));
}
```

> [!tip] Troca sem variável auxiliar
> `let (a, b) = (b, a);` troca valores; para variáveis existentes use `std::mem::swap(&mut a, &mut b)`.

## Veja também

- [[Pattern matching avançado]]
- [[Tuplas]]
- [[Structs]]
