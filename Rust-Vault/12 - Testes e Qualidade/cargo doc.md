---
tags: [rust, qualidade, documentacao, cargo]
aliases: ["cargo doc", "rustdoc", "docs.rs", "intra-doc links"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Comentários e doc comments]]", "[[Doc tests]]", "[[Publicar no crates.io]]"]
---

# cargo doc

```bash
cargo doc                 # gera HTML em target/doc (inclui dependências)
cargo doc --open          # gera e abre no navegador
cargo doc --no-deps       # só o seu crate (mais rápido)
```

```rust
//! # Meu Crate
//!
//! Documentação do crate (aparece na página inicial).

#![warn(missing_docs)] // avisa sobre itens públicos sem documentação

/// Uma pessoa.
///
/// Veja também [`Pessoa::nova`] e [`std::string::String`].
pub struct Pessoa {
    /// Nome completo.
    pub nome: String,
}

impl Pessoa {
    /// Cria uma [`Pessoa`] com o nome dado.
    pub fn nova(nome: impl Into<String>) -> Self {
        Self { nome: nome.into() }
    }
}
```

- **Intra-doc links:** ``[`Tipo`]`` e ``[`modulo::item`]`` criam links automáticos.
- `#[doc(hidden)]` esconde um item da documentação; `#[doc = include_str!("../README.md")]` reaproveita o README.
- Ao publicar no crates.io, o **docs.rs** compila e hospeda a documentação sozinho.

> [!tip] Padrão de qualidade
> Documente toda a API pública com exemplos testáveis; veja [[Doc tests]].

## Veja também

- [[Comentários e doc comments]]
- [[Doc tests]]
- [[Publicar no crates.io]]
