---
tags: [rust, fundamentos]
aliases: ["Rust", "Linguagem Rust"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Filosofia do Rust]]", "[[História do Rust]]", "[[Casos de uso do Rust]]", "[[Instalação com rustup]]"]
---

# O que é Rust

Rust é uma linguagem de programação **compilada**, **estaticamente tipada** e de **propósito geral**, criada para escrever software de sistemas com segurança de memória *sem* coletor de lixo (garbage collector).

> [!info] Em uma frase
> Rust entrega o desempenho de C/C++ com garantias de segurança verificadas **em tempo de compilação**.

## Características principais

| Característica | Significado prático |
|---|---|
| Segurança de memória | Sem *use-after-free*, sem ponteiros nulos "soltos", sem data races em código seguro |
| Sem GC | Memória é liberada de forma determinística (RAII + [[Ownership e regras]]) |
| Abstrações de custo zero | Iteradores, genéricos e closures compilam para código tão rápido quanto o escrito à mão |
| Sistema de tipos expressivo | `enum`, `Option`, `Result`, traits e pattern matching |
| Ferramentas integradas | `cargo`, `rustfmt`, `clippy`, `rustdoc`, testes embutidos |

## O que se constrói com Rust

Ferramentas de linha de comando, serviços web, navegadores e motores, sistemas embarcados, WebAssembly, jogos e infraestrutura. Veja [[Casos de uso do Rust]].

## Um primeiro olhar

```rust
// Um programa completo em Rust
fn main() {
    let linguagem = "Rust";
    println!("Olá, {linguagem}!");
}
```

> [!tip] Como estudar
> Siga a trilha do vault: Fundamentos → Básico → [[Ownership e regras]]. O ownership é a ideia central; o resto da linguagem se encaixa em torno dele.

## Exercício

Instale o Rust seguindo [[Instalação com rustup]] e rode `rustc --version` no terminal.

## Veja também

- [[Filosofia do Rust]]
- [[História do Rust]]
- [[Casos de uso do Rust]]
- [[Instalação com rustup]]
