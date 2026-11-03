---
tags: [rust, fundamentos, cargo]
aliases: ["cargo new", "cargo build", "cargo run", "cargo check"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Primeiro programa Hello World]]", "[[Pipeline de compilação]]", "[[Instalação com rustup]]"]
---

# Cargo básico

O **Cargo** é o gerenciador de pacotes e sistema de build do Rust.

```bash
cargo new meu_projeto        # cria um binário (use --lib para biblioteca)
cd meu_projeto
cargo build                  # compila em modo debug (target/debug)
cargo build --release        # compila otimizado (target/release)
cargo run                    # compila e executa
cargo check                  # só verifica tipos: muito mais rápido que build
cargo test                   # roda os testes
cargo fmt                    # formata o código (rustfmt)
cargo clippy                 # lints sugeridos
cargo doc --open             # gera e abre a documentação
```

## Estrutura criada por `cargo new`

```text
meu_projeto/
├── Cargo.toml     # manifesto: nome, versão, edição, dependências
└── src/
    └── main.rs    # código inicial com Hello World
```

```toml
# Cargo.toml gerado
[package]
name = "meu_projeto"
version = "0.1.0"
edition = "2024"

[dependencies]
```

> [!tip] Ciclo de trabalho
> Use `cargo check` com frequência (rápido) e `cargo run` para ver o resultado. Reserve `--release` para medir desempenho.

> [!info] Cargo.lock
> O `Cargo.lock` fixa as versões exatas. Em binários, versione-o no Git.

## Exercício

Crie um projeto com `cargo new`, rode `cargo run`, depois `cargo build --release` e compare o tamanho dos diretórios `target/debug` e `target/release`.

## Veja também

- [[Primeiro programa Hello World]]
- [[Pipeline de compilação]]
- [[Instalação com rustup]]
