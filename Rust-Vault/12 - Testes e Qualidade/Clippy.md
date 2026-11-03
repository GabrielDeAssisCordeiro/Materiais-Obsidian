---
tags: [rust, qualidade]
aliases: ["clippy", "cargo clippy", "lints"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[rustfmt]]", "[[CI com GitHub Actions]]", "[[Iteradores]]"]
---

# Clippy

**Clippy** é o linter oficial: centenas de verificações sobre correção, desempenho e estilo idiomático.

```bash
rustup component add clippy
cargo clippy                                  # roda os lints
cargo clippy --all-targets --all-features -- -D warnings   # falha em qualquer aviso (CI)
cargo clippy --fix                            # aplica correções automáticas seguras
```

## Exemplo de melhoria sugerida

```rust
// Clippy: needless_range_loop e manual_sum
fn antes(v: &[i32]) -> i32 {
    let mut total = 0;
    for i in 0..v.len() {
        total += v[i];
    }
    total
}

// Versão idiomática
fn depois(v: &[i32]) -> i32 {
    v.iter().sum()
}

fn main() {
    let v = [1, 2, 3];
    assert_eq!(antes(&v), depois(&v));
}
```

## Grupos de lints

| Grupo | Conteúdo |
|---|---|
| `clippy::correctness` | código quase certamente errado (erro por padrão) |
| `clippy::suspicious` | provavelmente errado |
| `clippy::style` | estilo idiomático |
| `clippy::complexity` | código desnecessariamente complexo |
| `clippy::perf` | desempenho |
| `clippy::pedantic` | opinativo; ative seletivamente |

```rust
#![warn(clippy::pedantic)]       // ativa um grupo no crate inteiro

#[allow(clippy::too_many_arguments)]  // silencia um lint num item específico
fn muitos(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32, g: i32, h: i32) -> i32 {
    a + b + c + d + e + f + g + h
}

fn main() {
    println!("{}", muitos(1, 2, 3, 4, 5, 6, 7, 8));
}
```

> [!tip] Configuração no Cargo.toml
> Em `[lints.clippy]` você define níveis de lint para todo o package/workspace: `pedantic = "warn"`.

## Veja também

- [[rustfmt]]
- [[CI com GitHub Actions]]
- [[Iteradores]]
