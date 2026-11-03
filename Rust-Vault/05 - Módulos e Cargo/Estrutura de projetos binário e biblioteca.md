---
tags: [rust, modulos, cargo, projeto]
aliases: ["lib.rs", "main.rs", "src/bin", "binário e lib"]
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Packages, crates e módulos]]", "[[Cargo básico]]", "[[Workspaces - Rust]]", "[[Testes de integração]]"]
---

# Estrutura de projetos binário e biblioteca

## Binário

```bash
cargo new app          # binário (src/main.rs)
cargo new minha_lib --lib   # biblioteca (src/lib.rs)
```

## Layout completo de um package

```text
meu_pacote/
├── Cargo.toml
├── Cargo.lock
├── src/
│   ├── lib.rs          # crate de biblioteca (opcional)
│   ├── main.rs         # binário principal (opcional)
│   └── bin/
│       └── outra.rs    # binários extras: cargo run --bin outra
├── tests/              # testes de integração
├── benches/            # benchmarks
├── examples/           # exemplos: cargo run --example nome
└── build.rs            # script de build (opcional)
```

## Padrão recomendado: lib + bin finos

Coloque a lógica em `lib.rs` e deixe `main.rs` só com a entrada. Isso facilita testes e reuso.

```rust
// trecho: src/lib.rs
pub fn executa(args: &[String]) -> Result<(), String> {
    if args.is_empty() {
        return Err("faltam argumentos".into());
    }
    println!("rodando com {} argumentos", args.len());
    Ok(())
}
```

```rust
// trecho: src/main.rs (o nome do crate lib é o do package, com _ no lugar de -)
use std::process;

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    if let Err(e) = meu_pacote::executa(&args) {
        eprintln!("erro: {e}");
        process::exit(1);
    }
}
```

> [!tip] Testabilidade
> Testes de integração em `tests/` só enxergam a API **pública** da biblioteca, o que força um bom design.

## Veja também

- [[Packages, crates e módulos]]
- [[Cargo básico]]
- [[Workspaces - Rust]]
- [[Testes de integração]]
