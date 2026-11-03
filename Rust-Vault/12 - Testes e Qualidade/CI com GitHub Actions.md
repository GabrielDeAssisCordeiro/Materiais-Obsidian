---
tags: [rust, qualidade]
aliases: ["workflow"]
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[cargo test]]", "[[Clippy]]", "[[rustfmt]]", "[[Cobertura de testes]]"]
---

# CI com GitHub Actions

Workflow típico de CI para Rust: formatação, lint e testes.

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

env:
  CARGO_TERM_COLOR: always
  RUSTFLAGS: "-D warnings"

jobs:
  verificacao:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
        with:
          components: rustfmt, clippy
      - uses: Swatinem/rust-cache@v2     # cache de dependências e target/
      - name: Formatação
        run: cargo fmt --all -- --check
      - name: Clippy
        run: cargo clippy --all-targets --all-features -- -D warnings
      - name: Testes
        run: cargo test --all-features

  matriz:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        rust: [stable, beta]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@master
        with:
          toolchain: ${{ matrix.rust }}
      - run: cargo test
```

> [!question] Verificar na documentação oficial
> Confira as versões atuais das actions (`actions/checkout`, `dtolnay/rust-toolchain`, `Swatinem/rust-cache`) nos repositórios oficiais.

## Passos úteis

| Verificação | Comando |
|---|---|
| Vulnerabilidades em dependências | `cargo audit` ou `cargo deny check advisories` |
| Licenças e duplicatas | `cargo deny check` |
| MSRV (versão mínima do Rust) | job com `toolchain: "1.85"` |
| Documentação sem erros | `RUSTDOCFLAGS="-D warnings" cargo doc --no-deps` |
| Cobertura | `cargo llvm-cov --lcov` |

> [!tip] Velocidade
> Cache de `target/` e `~/.cargo` reduz muito o tempo; use `cargo nextest` para testes rápidos.

## Veja também

- [[cargo test]]
- [[Clippy]]
- [[rustfmt]]
- [[Cobertura de testes]]
