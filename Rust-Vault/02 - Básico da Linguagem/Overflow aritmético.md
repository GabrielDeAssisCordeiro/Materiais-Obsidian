---
tags: [rust, basico, tipos]
aliases: ["overflow", "wrapping", "checked", "saturating"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Tipos escalares]]", "[[Operadores]]", "[[Conversão entre tipos]]"]
---

# Overflow aritmético

- Em **debug**, estouro de inteiro causa **panic**.
- Em **release**, o padrão é *wrapping* (dá a volta), sem panic (configurável no perfil).

Para controlar explicitamente, use os métodos:

| Família | Comportamento |
|---|---|
| `wrapping_*` | Dá a volta (módulo 2ⁿ) |
| `checked_*` | Devolve `Option` (`None` no estouro) |
| `saturating_*` | Satura no mínimo/máximo |
| `overflowing_*` | Devolve `(valor, estourou)` |

```rust
fn main() {
    let x: u8 = 250;
    println!("{}", x.wrapping_add(10));    // 4
    println!("{:?}", x.checked_add(10));   // None
    println!("{}", x.saturating_add(10));  // 255
    println!("{:?}", x.overflowing_add(10)); // (4, true)
}
```

> [!warning] Segurança
> Estouro de inteiros não corrompe memória em Rust seguro, mas pode gerar bugs lógicos; use `checked_*` em cálculos com dados externos.

## Veja também

- [[Tipos escalares]]
- [[Operadores]]
- [[Conversão entre tipos]]
