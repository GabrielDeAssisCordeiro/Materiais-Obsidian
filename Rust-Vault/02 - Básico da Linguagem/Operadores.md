---
tags: [rust, basico, operadores]
aliases: ["aritméticos", "lógicos", "bit a bit"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Tipos escalares]]", "[[Overflow aritmético]]", "[[Conversão entre tipos]]"]
---

# Operadores

| Categoria | Operadores |
|---|---|
| Aritméticos | `+ - * / %` |
| Comparação | `== != < > <= >=` |
| Lógicos | `&& \|\| !` |
| Bit a bit | `& \| ^ ! << >>` |
| Atribuição composta | `+= -= *= /= %= &= \|= ^= <<= >>=` |
| Intervalo | `..` `..=` |
| Conversão | `as` |

```rust
fn main() {
    println!("{}", 7 / 2);      // 3 (divisão inteira)
    println!("{}", 7.0 / 2.0);  // 3.5
    println!("{}", -7 % 3);     // -1 (resto mantém o sinal do dividendo)
    println!("{}", (-7i32).rem_euclid(3)); // 2

    let a = 0b1100u8;
    let b = 0b1010u8;
    println!("{:04b} {:04b} {:04b}", a & b, a | b, a ^ b);

    // Curto-circuito
    let ok = true || panic!("nunca executa");
    println!("{ok}");
}
```

> [!warning] Sem conversão implícita
> `let x: i64 = 1i32 + 2i64;` não compila. Converta explicitamente; veja [[Conversão entre tipos]].

## Veja também

- [[Tipos escalares]]
- [[Overflow aritmético]]
- [[Conversão entre tipos]]
