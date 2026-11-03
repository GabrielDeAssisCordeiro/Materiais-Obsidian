---
tags: [rust, testes, qualidade]
aliases: ["tests/", "integration tests", "testes de integração"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Testes unitários]]", "[[Estrutura de projetos binário e biblioteca]]", "[[cargo test]]"]
---

# Testes de integração

Testes de integração ficam na pasta `tests/` e usam **apenas a API pública** do crate, como um usuário externo faria. Cada arquivo em `tests/` é compilado como um crate separado.

```text
meu_crate/
├── Cargo.toml
├── src/
│   └── lib.rs
└── tests/
    ├── integracao.rs
    └── comum/
        └── mod.rs        # helpers compartilhados (não vira um teste)
```

```rust
// trecho: tests/integracao.rs
use meu_crate::soma;

mod comum;

#[test]
fn soma_pela_api_publica() {
    comum::prepara();
    assert_eq!(soma(2, 2), 4);
}
```

```rust
// trecho: tests/comum/mod.rs
pub fn prepara() {
    // inicializa dados de teste, diretórios temporários etc.
}
```

```bash
cargo test --test integracao      # roda só o arquivo tests/integracao.rs
cargo test --lib                  # só testes unitários da biblioteca
cargo test --doc                  # só doc tests
```

> [!warning] Crates binários
> Não é possível importar `src/main.rs` em `tests/`. Por isso o padrão **lib + bin fino** (veja [[Estrutura de projetos binário e biblioteca]]): coloque a lógica em `lib.rs`.

> [!tip] Recursos temporários
> Use o crate `tempfile` para criar diretórios/arquivos descartáveis e `assert_cmd` para testar o binário de CLI de ponta a ponta.

## Veja também

- [[Testes unitários]]
- [[Estrutura de projetos binário e biblioteca]]
- [[cargo test]]
