---
tags: [rust, testes, qualidade]
aliases: ["cargo-llvm-cov", "tarpaulin"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[cargo test]]", "[[CI com GitHub Actions]]"]
---

# Cobertura de testes

```bash
# Opção recomendada: cargo-llvm-cov (usa a instrumentação do LLVM)
rustup component add llvm-tools-preview
cargo install cargo-llvm-cov

cargo llvm-cov                        # resumo no terminal
cargo llvm-cov --html --open          # relatório HTML navegável
cargo llvm-cov --lcov --output-path lcov.info   # para Codecov/Coveralls

# Alternativa: cargo-tarpaulin (Linux)
cargo install cargo-tarpaulin
cargo tarpaulin --out Html
```

| Ferramenta | Plataformas | Observação |
|---|---|---|
| `cargo-llvm-cov` | Linux, macOS, Windows | precisa do componente `llvm-tools-preview` |
| `cargo-tarpaulin` | principalmente Linux | simples de usar |

> [!warning] Cobertura não é qualidade
> 100% de linhas cobertas não garante testes bons. Use a métrica para **achar buracos**, não como meta absoluta.

## Veja também

- [[cargo test]]
- [[CI com GitHub Actions]]
