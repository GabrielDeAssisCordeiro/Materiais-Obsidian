---
tags: [rust, cargo, ferramentas]
aliases: ["cargo add", "cargo update", "cargo tree", "cargo audit", "cargo deny", "cargo expand"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Versionamento semântico]]", "[[Publicar no crates.io]]", "[[Clippy]]"]
---

# Comandos úteis do Cargo

| Comando | Para quê |
|---|---|
| `cargo add <crate>` / `cargo remove <crate>` | gerenciar dependências |
| `cargo update` | atualizar o `Cargo.lock` |
| `cargo tree` | árvore de dependências (`-d` mostra duplicadas; `-i crate` mostra quem depende) |
| `cargo check` | verificação rápida |
| `cargo clippy` / `cargo fmt` | lint e formatação |
| `cargo doc --open` | documentação |
| `cargo clean` | apaga `target/` |
| `cargo fix` | aplica correções sugeridas (inclusive migração de edição) |
| `cargo metadata` | informações do projeto em JSON |
| `cargo install <crate>` | instala binários (em `~/.cargo/bin`) |

## Ferramentas externas muito usadas

```bash
cargo install cargo-audit cargo-deny cargo-edit cargo-expand cargo-outdated cargo-nextest cargo-watch

cargo audit                   # vulnerabilidades conhecidas (banco RustSec)
cargo deny check              # licenças, advisories, fontes e duplicatas (config em deny.toml)
cargo outdated                # dependências desatualizadas
cargo expand                  # mostra o código após expandir macros
cargo nextest run             # executor de testes mais rápido
cargo watch -x check -x test  # recompila ao salvar
```

> [!tip] Segurança da cadeia de suprimentos
> Rode `cargo audit` ou `cargo deny` na CI e revise dependências novas (`cargo tree`) antes de adicioná-las.

## Veja também

- [[Cargo básico]]
- [[Versionamento semântico]]
- [[Publicar no crates.io]]
- [[Clippy]]
