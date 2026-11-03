---
tags: [rust, basico, documentacao]
aliases: ["//", "///", "//!"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Funções]]", "[[Primeiro programa Hello World]]"]
---

# Comentários e doc comments

```rust
// trecho: comentários e doc comments (não compila isolado)
// Comentário de linha

/* Comentário
   de bloco */

/// Documentação de um item (aparece no `cargo doc`).
/// Suporta Markdown e exemplos que viram *doc tests*.
///
/// # Exemplos
///
/// ```
/// let r = meu_crate::dobra(4);
/// assert_eq!(r, 8);
/// ```
pub fn dobra(n: i32) -> i32 {
    n * 2
}

fn main() {
    println!("{}", dobra(2));
}
```

> [!info] `//!`
> Comentários `//!` documentam o item que os **contém** (módulo ou crate) e ficam no topo do arquivo.

> [!info] Doc tests
> Os blocos de código em `///` são compilados e executados por `cargo test`. Veja [[Doc tests]].

> [!tip] Seções convencionais
> `# Panics`, `# Errors`, `# Safety` e `# Examples` são padrões da documentação da biblioteca padrão.

## Veja também

- [[Funções]]
- [[Primeiro programa Hello World]]
