---
tags: [rust, modulos, cargo]
aliases: ["workspace", "monorepo Rust"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Packages, crates e módulos]]", "[[Features de Cargo]]", "[[Estrutura de projetos binário e biblioteca]]"]
---

# Workspaces - Rust

Um **workspace** reúne vários packages com um único `Cargo.lock` e um diretório `target/` compartilhado.

```text
meu_workspace/
├── Cargo.toml          # raiz do workspace
├── nucleo/
│   ├── Cargo.toml
│   └── src/lib.rs
├── cli/
│   ├── Cargo.toml
│   └── src/main.rs
└── api/
    ├── Cargo.toml
    └── src/main.rs
```

```toml
# Cargo.toml da raiz
[workspace]
resolver = "3"          # padrão para a edição 2024
members = ["nucleo", "cli", "api"]

# Dependências compartilhadas entre os membros
[workspace.dependencies]
serde = { version = "1", features = ["derive"] }

[workspace.package]
version = "0.1.0"
edition = "2024"
```

```toml
# cli/Cargo.toml
[package]
name = "cli"
version.workspace = true
edition.workspace = true

[dependencies]
nucleo = { path = "../nucleo" }   # dependência local
serde.workspace = true             # herda do workspace
```

```bash
cargo build --workspace         # compila tudo
cargo test -p nucleo            # testa um package
cargo run -p cli
```

> [!question] Verificar na documentação oficial
> Confirme o `resolver` padrão para a edição 2024 e a sintaxe de herança `workspace = true` na versão do Cargo que você usa.

## Veja também

- [[Packages, crates e módulos]]
- [[Features de Cargo]]
- [[Estrutura de projetos binário e biblioteca]]
