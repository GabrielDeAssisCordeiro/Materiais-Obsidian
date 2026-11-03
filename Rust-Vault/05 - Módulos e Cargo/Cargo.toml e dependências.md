---
tags: [rust, cargo]
aliases: ["Cargo.toml", "manifesto", "dependencies", "dev-dependencies", "build-dependencies"]
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Versionamento semântico]]", "[[Features de Cargo]]", "[[Workspaces - Rust]]"]
---

# Cargo.toml e dependências

O **`Cargo.toml`** é o manifesto do package.

```toml
[package]
name = "meu_app"
version = "0.1.0"
edition = "2024"
rust-version = "1.85"          # MSRV: versão mínima suportada do compilador
description = "Um exemplo"
license = "MIT OR Apache-2.0"

[dependencies]
serde = { version = "1", features = ["derive"] }     # do crates.io
rand = "0.9"                                          # forma abreviada
nucleo = { path = "../nucleo" }                       # local
algo = { git = "https://github.com/exemplo/algo" }    # repositório Git
opcional = { version = "2", optional = true }         # ativada por feature

[dev-dependencies]           # só para testes, exemplos e benchmarks
proptest = "1"

[build-dependencies]         # só para o build.rs
cc = "1"

[[bin]]                      # binário adicional ou renomeado
name = "ferramenta"
path = "src/bin/ferramenta.rs"

[lib]
name = "meu_app"
path = "src/lib.rs"
```

| Seção | Função |
|---|---|
| `[package]` | metadados e edição |
| `[dependencies]` | usadas pelo código |
| `[dev-dependencies]` | testes/exemplos/benches |
| `[build-dependencies]` | `build.rs` |
| `[features]` | recursos opcionais ([[Features de Cargo]]) |
| `[profile.*]` | otimização ([[Debug vs release]]) |
| `[workspace]` | monorepo ([[Workspaces - Rust]]) |
| `[target.'cfg(...)'.dependencies]` | dependências por plataforma |

> [!tip] Adicionando dependências
> `cargo add serde --features derive` edita o `Cargo.toml` por você.

## Veja também

- [[Cargo básico]]
- [[Versionamento semântico]]
- [[Features de Cargo]]
- [[Workspaces - Rust]]
