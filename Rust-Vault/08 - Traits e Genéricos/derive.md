---
tags: [rust, traits]
aliases: ["#[derive]", "implementação automática"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Traits padrão]]", "[[Default]]", "[[Macros procedurais]]"]
---

# derive

`#[derive(...)]` gera a implementação de uma trait automaticamente, desde que **todos os campos** também a implementem.

```rust
#[derive(Debug, Clone, PartialEq, Default)]
struct Config {
    nome: String,
    porta: u16,
    debug: bool,
}

#[derive(Debug, Default, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord)]
enum Nivel {
    Baixo,
    #[default]
    Medio, // variante escolhida por Default
    Alto,
}

fn main() {
    let c = Config { porta: 8080, ..Default::default() };
    println!("{:?}", c);
    println!("{:#?}", Nivel::default());
    println!("{}", Nivel::Baixo < Nivel::Alto); // ordem pela posição da variante
    println!("{}", c == c.clone());
}
```

- Em structs, `PartialOrd`/`Ord` comparam campo a campo na ordem de declaração; em enums, pela ordem das variantes.
- `derive(Debug)` em tipos genéricos exige `T: Debug` automaticamente.
- Para `Display`, `Error` e outras, existem crates como `thiserror` e `derive_more`.

> [!tip] Quando escrever à mão
> Quando o comportamento não for o estrutural: por exemplo, `PartialEq` que ignora um campo de cache, ou `Debug` que oculta segredos.

## Veja também

- [[Traits padrão]]
- [[Default]]
- [[Macros procedurais]]
