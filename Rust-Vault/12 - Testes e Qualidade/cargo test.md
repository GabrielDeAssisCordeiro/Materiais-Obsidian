---
tags: [rust, testes, cargo]
aliases: ["--nocapture", "--test-threads", "filtro de testes"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Testes unitários]]", "[[Testes de integração]]", "[[Doc tests]]", "[[CI com GitHub Actions]]"]
---

# cargo test

```bash
cargo test                       # roda tudo (unitários, integração, doc tests)
cargo test soma                  # só testes cujo nome contém "soma"
cargo test -- --exact tests::soma_basica   # nome exato
cargo test -- --nocapture        # mostra println! mesmo de testes que passam
cargo test -- --test-threads=1   # sequencial (útil com estado compartilhado)
cargo test -- --ignored          # só os marcados com #[ignore]
cargo test -- --include-ignored  # todos, incluindo ignorados
cargo test --lib                 # só a biblioteca
cargo test --release             # em modo otimizado
cargo test --workspace           # todo o workspace
cargo test --all-features
```

> [!info] Separador `--`
> Argumentos antes de `--` são do **Cargo**; depois, do **executável de teste**.

> [!tip] Testes mais rápidos
> `cargo nextest run` (ferramenta externa) executa cada teste em processo próprio, com relatório melhor e geralmente mais rápido.

## Veja também

- [[Testes unitários]]
- [[Testes de integração]]
- [[Doc tests]]
- [[CI com GitHub Actions]]
