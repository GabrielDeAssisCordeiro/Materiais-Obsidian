---
tags: [rust, anexo, checklist, projeto]
aliases: ["Novo projeto Rust"]
tipo: checklist
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Estrutura de projetos binário e biblioteca]]", "[[CI com GitHub Actions]]", "[[Clippy]]", "[[rustfmt]]"]
---

# Checklist de novo projeto

Passos para começar um projeto Rust bem estruturado.

## Criação

- [ ] `cargo new meu-projeto` (ou `--lib`) — veja [[Cargo básico]] e [[Estrutura de projetos binário e biblioteca]].
- [ ] Definir `edition = "2024"` e `rust-version` no `Cargo.toml`.
- [ ] `git init` e um `.gitignore` com `/target` (mantenha o `Cargo.lock` em binários).
- [ ] Escrever o `README.md` com o objetivo do projeto.

## Qualidade desde o início

- [ ] `rustfmt.toml` (opcional) e `cargo fmt` no editor ao salvar ([[rustfmt]]).
- [ ] `cargo clippy` sem avisos ([[Clippy]]).
- [ ] Um primeiro teste que falha e depois passa ([[Testes unitários]]).
- [ ] CI com fmt, clippy e test ([[CI com GitHub Actions]]).

## Arquitetura

- [ ] Separar `main.rs` (fino) de `lib.rs` (lógica testável).
- [ ] Definir o tipo de erro do crate ([[Erros customizados]]).
- [ ] Escolher dependências com critério ([[Escolhendo e avaliando crates]]).
- [ ] Documentar decisões em um `docs/` ou no README.

## Quando crescer

- [ ] Dividir em [[Workspaces - Rust]].
- [ ] Introduzir [[Features de Cargo]] para partes opcionais.
- [ ] Adicionar [[Testes de integração]] e [[Benchmarks com criterion]].

## Veja também

- [[Cargo básico]]
- [[Estrutura de projetos binário e biblioteca]]
- [[CI com GitHub Actions]]
- [[Clippy]]
- [[rustfmt]]
