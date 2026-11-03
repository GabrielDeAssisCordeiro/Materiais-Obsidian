---
tags: [rust, areas, cli]
aliases: ["argumentos", "std::env::args", "exit code"]
tipo: pratica
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[clap]]", "[[Operador de interrogação]]", "[[Erros customizados]]", "[[ratatui]]", "[[Cargo básico]]"]
---

# CLI com Rust

Rust é excelente para ferramentas de linha de comando: compila para um **binário único**, inicia instantaneamente e roda em Windows, macOS e Linux. Exemplos famosos: `ripgrep`, `fd`, `bat`, `eza`, `starship`.

## Só com a biblioteca padrão

```rust
use std::env;
use std::process::ExitCode;

fn main() -> ExitCode {
    let args: Vec<String> = env::args().skip(1).collect();

    match args.as_slice() {
        [] => {
            eprintln!("uso: saudar <nome> [--maiusculas]");
            ExitCode::from(2) // 2 = erro de uso, por convenção
        }
        [nome] => {
            println!("Olá, {nome}!");
            ExitCode::SUCCESS
        }
        [nome, flag] if flag == "--maiusculas" => {
            println!("OLÁ, {}!", nome.to_uppercase());
            ExitCode::SUCCESS
        }
        _ => {
            eprintln!("argumentos inválidos");
            ExitCode::FAILURE
        }
    }
}
```

## Com `clap` (recomendado)

```rust
// requer crate: clap
use clap::Parser;

/// Saúda alguém.
#[derive(Parser)]
#[command(version, about)]
struct Args {
    /// Nome da pessoa
    nome: String,
    /// Quantas vezes repetir
    #[arg(short, long, default_value_t = 1)]
    vezes: u32,
}

fn main() {
    let args = Args::parse();
    for _ in 0..args.vezes {
        println!("Olá, {}!", args.nome);
    }
}
```

Veja [[clap]] para subcomandos, validação e *completions*.

## Boas práticas de CLI

| Prática | Como |
|---|---|
| Saída normal em **stdout**, erros em **stderr** | `println!` / `eprintln!` |
| Códigos de saída significativos | `ExitCode`, `std::process::exit` |
| Retornar `Result` de `main` | combina com [[Operador de interrogação]] |
| Ler de stdin quando não houver arquivo | `std::io::stdin().lines()` |
| Detectar terminal | crate `is-terminal` (cores só em TTY) |
| Distribuir | `cargo install`, GitHub Releases, `cargo-dist` |

```rust
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    // Conta linhas e palavras da entrada padrão: `echo "a b" | prog`
    let (mut linhas, mut palavras) = (0usize, 0usize);
    for linha in io::stdin().lock().lines() {
        let linha = linha?;
        linhas += 1;
        palavras += linha.split_whitespace().count();
    }
    println!("{linhas} linhas, {palavras} palavras");
    Ok(())
}
```

> [!tip] Interface de terminal
> Para interfaces interativas em tela cheia, veja [[ratatui]].

## Exercício

Escreva uma CLI `contar` que receba um arquivo como argumento, imprima linhas/palavras/bytes e retorne código de saída 1 se o arquivo não existir.

## Veja também

- [[clap]]
- [[Operador de interrogação]]
- [[Erros customizados]]
- [[ratatui]]
- [[Cargo básico]]
