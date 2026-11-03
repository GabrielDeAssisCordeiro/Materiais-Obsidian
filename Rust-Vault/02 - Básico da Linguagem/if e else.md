---
tags: [rust, basico, controle-de-fluxo]
aliases: ["condicional"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[match]]", "[[Expressões vs instruções]]", "[[if let e let else]]"]
---

# if e else

```rust
fn main() {
    let n = 15;

    if n % 15 == 0 {
        println!("FizzBuzz");
    } else if n % 3 == 0 {
        println!("Fizz");
    } else if n % 5 == 0 {
        println!("Buzz");
    } else {
        println!("{n}");
    }

    // if como expressão: ambos os ramos devem ter o mesmo tipo
    let abs = if n < 0 { -n } else { n };
    println!("{abs}");
}
```

> [!warning] A condição precisa ser `bool`
> `if n { ... }` com `n: i32` não compila: Rust não converte inteiros em booleanos.

## Veja também

- [[match]]
- [[Expressões vs instruções]]
- [[if let e let else]]
