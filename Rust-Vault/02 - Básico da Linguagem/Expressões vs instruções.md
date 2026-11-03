---
tags: [rust, basico, sintaxe]
aliases: ["expression", "statement"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Funções]]", "[[if e else]]", "[[match]]"]
---

# Expressões vs instruções

- **Instrução** (*statement*): executa algo e **não** devolve valor (`let x = 1;`).
- **Expressão**: avalia para um valor. Quase tudo em Rust é expressão: blocos, `if`, `match`, `loop`.

```rust
fn main() {
    let y = {
        let x = 3;
        x + 1       // sem ; : valor do bloco
    };
    println!("{y}"); // 4

    let tipo = if y % 2 == 0 { "par" } else { "ímpar" };
    println!("{tipo}");

    let nota = 7;
    let conceito = match nota {
        9..=10 => 'A',
        7..=8 => 'B',
        _ => 'C',
    };
    println!("{conceito}");
}
```

> [!tip] Estilo idiomático
> Prefira atribuir o resultado de `if`/`match` diretamente à variável em vez de declará-la `mut` e alterá-la dentro dos ramos.

## Veja também

- [[Funções]]
- [[if e else]]
- [[match]]
