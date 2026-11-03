---
tags: [rust, anexo, checklist, cargo, publicacao]
aliases: ["Publicação de crate", "Release checklist"]
tipo: checklist
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Publicar no crates.io]]", "[[Versionamento semântico]]", "[[Rust API Guidelines]]", "[[CI com GitHub Actions]]", "[[Checklist de revisão de código]]"]
---

# Checklist para publicar um crate

Antes de rodar `cargo publish` (que é **irreversível**: versões publicadas não podem ser apagadas, apenas *yanked*).

## Metadados

- [ ] `Cargo.toml` com `name`, `version`, `edition`, `description`, `license` (ou `license-file`), `repository`, `readme`, `keywords` e `categories` ([[Cargo.toml e dependências]]).
- [ ] `rust-version` (MSRV) declarado e testado na CI.
- [ ] `README.md` com instalação, exemplo mínimo e licença.
- [ ] Arquivos `LICENSE` incluídos.
- [ ] `CHANGELOG.md` atualizado.

## Qualidade

- [ ] Checklist de [[Checklist de revisão de código]] cumprido.
- [ ] Documentação pública completa; `#![warn(missing_docs)]`.
- [ ] Testes, doc tests e exemplos (`examples/`) funcionam.
- [ ] CI verde em Linux, macOS e Windows ([[CI com GitHub Actions]]).
- [ ] Features documentadas e testadas em combinação ([[Features de Cargo]]).

## Versão e publicação

- [ ] Número de versão segue [[Versionamento semântico]] (mudança incompatível = nova versão maior; em `0.x`, nova versão menor).
- [ ] `cargo publish --dry-run` passa.
- [ ] `cargo package --list` não inclui segredos nem arquivos grandes.
- [ ] `cargo publish`; marque a versão no Git (`git tag v1.2.3`).
- [ ] Conferir a página em docs.rs.

> [!warning] Segredos
> Nunca publique tokens, chaves ou `.env`. Revise `cargo package --list` antes de publicar.

> [!question] Verificar na documentação oficial
> Confirme as regras vigentes (por exemplo, metadados obrigatórios e *trusted publishing*) em doc.rust-lang.org/cargo/reference/publishing.html.

## Veja também

- [[Publicar no crates.io]]
- [[Versionamento semântico]]
- [[Rust API Guidelines]]
- [[CI com GitHub Actions]]
- [[Checklist de revisão de código]]
