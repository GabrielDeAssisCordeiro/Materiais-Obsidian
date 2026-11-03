---
tags: [rust, basico, variaveis]
aliases: ["Sombreamento", "redeclaração"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Variáveis e mutabilidade]]", "[[Constantes e statics]]"]
---

# Shadowing

**Shadowing** é redeclarar uma variável com o mesmo nome usando `let`. A nova variável "esconde" a anterior e pode ter **outro tipo**.

```rust
fn main() {
    let espacos = "   ";          // &str
    let espacos = espacos.len();  // agora é usize: tipo diferente, mesmo nome
    println!("{espacos}");

    let x = 5;
    let x = x + 1;
    {
        let x = x * 2; // sombra apenas dentro do bloco
        println!("interno: {x}"); // 12
    }
    println!("externo: {x}");      // 6
}
```

| | `mut` | Shadowing |
|---|---|---|
| Altera o tipo? | Não | Sim |
| Cria nova variável? | Não | Sim |
| Mutabilidade após | Continua `mut` | Volta a ser imutável (se não usar `mut`) |

> [!tip] Uso comum
> Converter dados (texto para número) mantendo o mesmo nome conceitual: `let idade = idade.trim().parse::<u32>()`.

## Veja também

- [[Variáveis e mutabilidade]]
- [[Constantes e statics]]
