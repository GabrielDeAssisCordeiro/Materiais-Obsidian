---
tags: [rust, cargo]
aliases: ["features", "cfg(feature)"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Workspaces - Rust]]", "[[Packages, crates e módulos]]"]
---

# Features de Cargo

**Features** permitem compilação condicional e dependências opcionais.

```toml
[package]
name = "minha_lib"
version = "0.1.0"
edition = "2024"

[features]
default = ["json"]               # ativadas por padrão
json = ["dep:serde_json"]        # ativa a dependência opcional
extra = []                       # feature sem dependência

[dependencies]
serde_json = { version = "1", optional = true }
```

```rust
// Código só compilado quando a feature "extra" está ativa
#[cfg(feature = "extra")]
pub fn recurso_extra() {
    println!("extra ligado");
}

fn main() {
    if cfg!(feature = "extra") {
        println!("com extra");
    } else {
        println!("sem extra");
    }
}
```

```bash
cargo build --features extra
cargo build --no-default-features
cargo build --all-features
```

> [!warning] Features devem ser aditivas
> Ativar uma feature nunca deve **remover** funcionalidade ou quebrar código. Como o Cargo unifica features de todo o grafo de dependências, features mutuamente exclusivas causam problemas.

> [!info] Aplicação típica
> Habilitar suporte opcional (`serde`, `tokio`), reduzir tempo de compilação e escolher backends.

## Veja também

- [[Workspaces - Rust]]
- [[Packages, crates e módulos]]
