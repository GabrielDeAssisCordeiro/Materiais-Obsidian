---
tags: [rust, basico, controle-de-fluxo]
aliases: ["intervalos", "..", "..="]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[while e for]]", "[[Slices]]", "[[match]]"]
---

# Ranges

| Sintaxe | Tipo | Significado |
|---|---|---|
| `a..b` | `Range` | de `a` até `b - 1` |
| `a..=b` | `RangeInclusive` | de `a` até `b` |
| `a..` | `RangeFrom` | de `a` sem limite superior |
| `..b` | `RangeTo` | até `b - 1` |
| `..` | `RangeFull` | tudo |

```rust
fn main() {
    let soma: i32 = (1..=100).sum();
    println!("{soma}"); // 5050

    println!("{}", (0..10).contains(&5)); // true
    println!("{}", (0..10).len());        // 10

    for c in 'a'..='e' {
        print!("{c}");
    }
    println!();

    // Passo com step_by
    for n in (0..20).step_by(5) {
        print!("{n} ");
    }
    println!();
}
```

## Veja também

- [[while e for]]
- [[Slices]]
- [[match]]
