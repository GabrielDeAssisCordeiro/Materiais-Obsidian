---
tags: [rust, basico, tipos]
aliases: ["tipo unitário"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Arrays]]", "[[Tipos escalares]]", "[[Desestruturação]]"]
---

# Tuplas

Uma **tupla** agrupa valores de tipos possivelmente diferentes, com tamanho fixo.

```rust
fn main() {
    let t: (i32, f64, &str) = (500, 6.4, "oi");

    // Desestruturação
    let (a, b, c) = t;
    println!("{a} {b} {c}");

    // Acesso por índice
    println!("{} {}", t.0, t.2);
}
```

A tupla vazia `()` é o tipo **unit**, retornado por funções sem valor explícito.

```rust
fn principal() -> () {}      // equivale a: fn principal() {}

fn main() {
    let u = principal();
    println!("{:?}", u); // ()
}
```

> [!tip] Retornar múltiplos valores
> Tuplas são práticas para devolver mais de um valor, mas `struct` com campos nomeados é mais legível quando há mais de dois.

## Veja também

- [[Arrays]]
- [[Tipos escalares]]
- [[Desestruturação]]
