---
tags: [rust, referencia, cheatsheet, cargo]
aliases: ["Comandos do Cargo", "Cargo em uma página"]
tipo: cheatsheet
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Comandos úteis do Cargo]]", "[[Cargo.toml e dependências]]", "[[Features de Cargo]]", "[[Workspaces - Rust]]", "[[Debug vs release]]"]
---

# Cheat sheet de Cargo

## Projeto

| Comando | Faz |
|---|---|
| `cargo new nome` / `cargo new --lib nome` | cria binário / biblioteca |
| `cargo init` | inicializa na pasta atual |
| `cargo build` / `cargo build --release` | compila (debug / otimizado) |
| `cargo run` / `cargo run --release -- args` | compila e executa |
| `cargo check` | só verifica (rápido, sem gerar binário) |
| `cargo clean` | apaga `target/` |
| `cargo doc --open` | gera e abre a documentação |

## Qualidade

| Comando | Faz |
|---|---|
| `cargo test` | roda todos os testes ([[cargo test]]) |
| `cargo test nome -- --nocapture` | filtra e mostra `println!` |
| `cargo fmt` | formata ([[rustfmt]]) |
| `cargo clippy -- -D warnings` | lint estrito ([[Clippy]]) |
| `cargo bench` | benchmarks |
| `cargo audit` | vulnerabilidades em dependências (plugin) |

## Dependências

| Comando | Faz |
|---|---|
| `cargo add serde --features derive` | adiciona dependência |
| `cargo add --dev proptest` | dependência de desenvolvimento |
| `cargo remove serde` | remove |
| `cargo update` | atualiza `Cargo.lock` |
| `cargo tree` / `cargo tree -d` | árvore / duplicadas |
| `cargo outdated` | desatualizadas (plugin) |

## Publicação e instalação

| Comando | Faz |
|---|---|
| `cargo install nome` | instala um binário do crates.io |
| `cargo install --path .` | instala o projeto local |
| `cargo package` / `cargo publish --dry-run` | prepara / simula publicação |
| `cargo publish` | publica |

## Cargo.toml mínimo comentado

```toml
[package]
name = "meu-app"
version = "0.1.0"
edition = "2024"
rust-version = "1.85"          # versão mínima suportada (MSRV)

[dependencies]
serde = { version = "1", features = ["derive"] }

[dev-dependencies]
proptest = "1"

[features]
default = []
extra = []

[profile.release]
lto = "thin"
codegen-units = 1
```

## Variáveis de ambiente úteis

| Variável | Efeito |
|---|---|
| `RUST_BACKTRACE=1` (ou `full`) | mostra a pilha em panics |
| `RUST_LOG=debug` | nível de log (`env_logger`/`tracing-subscriber`) |
| `RUSTFLAGS="-C target-cpu=native"` | flags do compilador |
| `CARGO_TARGET_DIR=...` | pasta de saída compartilhada |

## Versões em `Cargo.toml`

| Escrita | Significa |
|---|---|
| `"1.2.3"` ou `"^1.2.3"` | `>=1.2.3, <2.0.0` |
| `"~1.2.3"` | `>=1.2.3, <1.3.0` |
| `"=1.2.3"` | exatamente |
| `"*"` | qualquer (evite) |

Veja [[Versionamento semântico]].

## Veja também

- [[Cargo básico]]
- [[Comandos úteis do Cargo]]
- [[Cargo.toml e dependências]]
- [[Features de Cargo]]
- [[Workspaces - Rust]]
- [[Debug vs release]]
