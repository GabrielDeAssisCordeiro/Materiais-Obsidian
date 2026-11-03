---
tags: [rust, basico, conversao]
aliases: ["as", "parse"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Tipos escalares]]", "[[Overflow aritmético]]", "[[From e Into]]"]
---

# Conversão entre tipos

Rust não faz conversões numéricas implícitas.

```rust
use std::convert::TryFrom;

fn main() {
    // as: conversão "crua" (pode truncar!)
    let grande: i32 = 300;
    let pequeno = grande as u8; // 44: truncou
    println!("{pequeno}");
    println!("{}", -1i32 as u32); // 4294967295
    println!("{}", 3.99f64 as i32); // 3 (trunca; satura nos limites)

    // From/Into: conversões que nunca falham
    let a: i64 = i64::from(10i32);
    let b: f64 = 5u8.into();
    println!("{a} {b}");

    // TryFrom: conversões que podem falhar
    println!("{:?}", u8::try_from(300i32).is_err()); // true
    println!("{:?}", u8::try_from(200i32));          // Ok(200)

    // Texto para número
    let n: Result<u32, _> = "42".parse();
    println!("{:?}", n);
}
```

> [!tip] Prefira `From`/`TryFrom` a `as`
> `as` pode perder informação silenciosamente; as traits tornam a intenção explícita.

## Veja também

- [[Tipos escalares]]
- [[Overflow aritmético]]
- [[From e Into]]
