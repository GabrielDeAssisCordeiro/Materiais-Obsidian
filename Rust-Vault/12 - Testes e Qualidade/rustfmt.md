---
tags: [rust, qualidade, formatacao]
aliases: ["rustfmt", "cargo fmt", "rustfmt.toml"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Clippy]]", "[[CI com GitHub Actions]]", "[[Editores e rust-analyzer]]"]
---

# rustfmt

**rustfmt** formata o código no estilo oficial, encerrando discussões de estilo.

```bash
rustup component add rustfmt
cargo fmt                  # formata o projeto
cargo fmt --check          # só verifica (exit code ≠ 0 se houver diferenças): ideal para CI
cargo fmt --all            # todo o workspace
```

```toml
# rustfmt.toml (opcional)
max_width = 100
edition = "2024"
```

> [!info] Opções instáveis
> Várias opções do rustfmt (como `imports_granularity`) exigem nightly (`cargo +nightly fmt`).

```rust
// Desativar a formatação de um trecho específico
#[rustfmt::skip]
const MATRIZ: [[u8; 3]; 3] = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
];

fn main() {
    println!("{:?}", MATRIZ);
}
```

> [!tip] Formatar ao salvar
> Configure no editor (rust-analyzer) para rodar o rustfmt ao salvar; veja [[Editores e rust-analyzer]].

## Veja também

- [[Clippy]]
- [[CI com GitHub Actions]]
- [[Editores e rust-analyzer]]
