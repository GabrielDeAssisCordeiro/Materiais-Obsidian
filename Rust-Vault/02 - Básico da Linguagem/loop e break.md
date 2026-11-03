---
tags: [rust, basico, controle-de-fluxo]
aliases: ["loop", "break com valor", "rótulos"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[while e for]]", "[[Expressões vs instruções]]"]
---

# loop e break

`loop` repete para sempre até um `break`. Diferente de `while` e `for`, o `loop` pode **devolver um valor** via `break valor`.

```rust
fn main() {
    let mut contador = 0;
    let resultado = loop {
        contador += 1;
        if contador == 10 {
            break contador * 2; // valor do loop
        }
    };
    println!("{resultado}"); // 20

    // Rótulos para sair de laços aninhados
    'externo: for i in 0..5 {
        for j in 0..5 {
            if i * j == 6 {
                println!("achei {i} * {j}");
                break 'externo;
            }
            if j > i {
                continue 'externo;
            }
        }
    }
}
```

## Veja também

- [[while e for]]
- [[Expressões vs instruções]]
