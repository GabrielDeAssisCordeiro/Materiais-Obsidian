---
tags: [rust, fundamentos]
aliases: ["Edition 2024", "Edição 2021", "editions"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[História do Rust]]", "[[Cargo básico]]", "[[Toolchains stable beta nightly]]"]
---

# Edições do Rust

Uma **edição** é um mecanismo para introduzir mudanças que, de outra forma, quebrariam compatibilidade, de forma **opt-in** por crate.

| Edição | Versão que a estabilizou |
|---|---|
| 2015 | 1.0 |
| 2018 | 1.31 |
| 2021 | 1.56 |
| **2024** | **1.85** (edição usada neste vault) |

```toml
[package]
name = "exemplo"
version = "0.1.0"
edition = "2024"
```

- Crates de edições diferentes interoperam normalmente.
- `cargo fix --edition` migra o código automaticamente na maior parte dos casos.
- O `cargo new` usa a edição mais recente.

> [!info] Versão vs edição
> A **versão** do compilador (1.99, por exemplo) é independente da **edição** da linguagem (2024). Uma versão nova do compilador suporta todas as edições.

> [!tip] Consulta
> O Edition Guide oficial descreve cada mudança e como migrar.

## Veja também

- [[História do Rust]]
- [[Cargo básico]]
- [[Toolchains stable beta nightly]]
