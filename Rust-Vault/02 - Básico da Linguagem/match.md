---
tags: [rust, basico, controle-de-fluxo, pattern-matching]
aliases: ["pattern matching", "casamento de padrões"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[if let e let else]]", "[[Enums]]", "[[Pattern matching avançado]]"]
---

# match

`match` compara um valor com padrões e executa o primeiro que casar. A checagem é **exaustiva**: todos os casos precisam ser cobertos.

```rust
fn descreve(n: i32) -> &'static str {
    match n {
        0 => "zero",
        1 | 2 | 3 => "pequeno",
        4..=9 => "médio",
        x if x < 0 => "negativo", // guard
        _ => "grande",            // curinga
    }
}

fn main() {
    for n in [0, 2, 7, -5, 100] {
        println!("{n}: {}", descreve(n));
    }

    let par = (3, -3);
    match par {
        (x, y) if x + y == 0 => println!("opostos"),
        (x, _) if x % 2 == 1 => println!("x ímpar"),
        _ => println!("outro"),
    }
}
```

> [!bug] Exaustividade
> Remover o ramo `_` acima gera `error[E0004]: non-exhaustive patterns`. É uma proteção: ao adicionar uma variante a um `enum`, o compilador mostra todos os `match` que precisam ser atualizados.

## Veja também

- [[if let e let else]]
- [[Enums]]
- [[Pattern matching avançado]]
