---
tags: [rust, cargo, publicacao]
aliases: ["cargo publish", "crates.io", "cargo yank"]
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Cargo.toml e dependências]]", "[[Versionamento semântico]]", "[[cargo doc]]"]
---

# Publicar no crates.io

## Metadados obrigatórios/recomendados

```toml
[package]
name = "meu_crate"            # único no crates.io
version = "0.1.0"
edition = "2024"
description = "Descrição curta"          # obrigatório
license = "MIT OR Apache-2.0"            # (ou license-file) obrigatório
repository = "https://github.com/voce/meu_crate"
readme = "README.md"
keywords = ["exemplo", "cli"]            # até 5
categories = ["command-line-utilities"]
```

## Passos

```bash
cargo login                       # cola o token gerado em crates.io (Account Settings)
cargo package --list              # confere quais arquivos entram no pacote
cargo publish --dry-run           # simula tudo sem publicar
cargo publish                     # publica (IRREVERSÍVEL: versão não pode ser apagada)
```

- Depois de publicado, o **docs.rs** compila a documentação automaticamente.
- `cargo yank --version 0.1.0` impede **novos** projetos de usarem a versão, sem quebrar quem já depende dela.
- Dependências por `path`/`git` precisam também ter `version` para publicar.

## Checklist

- [ ] README, licença e documentação pública (`#![warn(missing_docs)]`)
- [ ] Testes e `cargo clippy` passando; `cargo doc` sem avisos
- [ ] `CHANGELOG.md` atualizado
- [ ] SemVer respeitado; `cargo semver-checks` (ferramenta externa) ajuda a detectar quebras
- [ ] Versão `rust-version` (MSRV) declarada

> [!warning] Publicação é permanente
> O código publicado fica disponível para sempre. Nunca inclua segredos; confira `cargo package --list`.

## Veja também

- [[Cargo.toml e dependências]]
- [[Versionamento semântico]]
- [[cargo doc]]
