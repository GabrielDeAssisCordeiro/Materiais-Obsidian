---
tags: [rust, modulos, api]
aliases: ["pub use", "re-export", "facade"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[use e caminhos]]", "[[Estrutura de projetos binário e biblioteca]]"]
---

# Re-exports com pub use

`pub use` reexporta um item, permitindo que a **API pública** tenha uma estrutura diferente da organização interna.

```rust
mod interno {
    pub mod detalhes {
        pub fn ola() -> &'static str {
            "olá"
        }
        pub struct Config {
            pub nome: String,
        }
    }
}

// API pública plana: os usuários escrevem `minha_lib::ola`
pub use interno::detalhes::{ola, Config};

fn main() {
    println!("{}", ola());
    let c = Config { nome: "x".to_string() };
    println!("{}", c.nome);
}
```

> [!tip] Padrão em bibliotecas
> É comum ter `pub use` em `lib.rs` para expor tipos principais na raiz, escondendo a árvore de módulos interna. Também é usado em *preludes*: `pub mod prelude { pub use crate::{A, B}; }`.

## Veja também

- [[use e caminhos]]
- [[Estrutura de projetos binário e biblioteca]]
