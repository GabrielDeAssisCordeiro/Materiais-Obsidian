---
tags: [rust, erros, crates]
aliases: ["thiserror", "anyhow"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Erros customizados]]", "[[Box dyn Error]]", "[[Boas práticas de tratamento de erros]]"]
---

# thiserror e anyhow

Dois crates se complementam:

| Crate | Para quem | O que faz |
|---|---|---|
| `thiserror` | **bibliotecas** | gera `Display`, `Error` e `From` por derive; mantém tipos de erro específicos |
| `anyhow` | **aplicações** | tipo `anyhow::Error` dinâmico, com contexto e backtrace |

```toml
[dependencies]
thiserror = "2"
anyhow = "1"
```

> [!question] Verificar na documentação oficial
> Confira as versões atuais no crates.io (docs.rs/thiserror e docs.rs/anyhow) antes de fixá-las no seu `Cargo.toml`.

## thiserror

```rust
// requer crate: thiserror
use thiserror::Error;

#[derive(Debug, Error)]
pub enum ErroApp {
    #[error("arquivo não encontrado: {0}")]
    NaoEncontrado(String),

    #[error("falha de E/S")]
    Io(#[from] std::io::Error),          // gera From<io::Error>

    #[error("número inválido")]
    Parse(#[from] std::num::ParseIntError),

    #[error("valor {valor} fora do limite {max}")]
    Limite { valor: i64, max: i64 },
}
```

## anyhow

```rust
// requer crate: anyhow
use anyhow::{bail, Context, Result};

fn le_config(caminho: &str) -> Result<u16> {
    let texto = std::fs::read_to_string(caminho)
        .with_context(|| format!("lendo {caminho}"))?;   // adiciona contexto
    let porta: u16 = texto.trim().parse().context("porta inválida")?;
    if porta < 1024 {
        bail!("porta {porta} é reservada");               // retorna Err(anyhow!(...))
    }
    Ok(porta)
}

fn main() -> Result<()> {
    let porta = le_config("porta.txt")?;
    println!("{porta}");
    Ok(())
}
```

> [!tip] Regra de bolso
> **Biblioteca** → `thiserror` (o chamador decide o que fazer com cada erro). **Aplicação** → `anyhow` (só quer reportar com contexto).

## Veja também

- [[Erros customizados]]
- [[Box dyn Error]]
- [[Boas práticas de tratamento de erros]]
