---
tags: [rust, erros, traits]
aliases: ["From para erros", "map_err", "conversão de erros"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Operador de interrogação]]", "[[Erros customizados]]", "[[From e Into]]"]
---

# Conversão de erros com From

Quando uma função faz várias operações com **erros de tipos diferentes**, o `?` converte cada um para o tipo de erro da função usando `From`.

```rust
use std::fmt;
use std::fs;
use std::io;
use std::num::ParseIntError;

#[derive(Debug)]
enum ErroApp {
    Io(io::Error),
    Parse(ParseIntError),
}

impl fmt::Display for ErroApp {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ErroApp::Io(e) => write!(f, "erro de E/S: {e}"),
            ErroApp::Parse(e) => write!(f, "erro de conversão: {e}"),
        }
    }
}

impl std::error::Error for ErroApp {}

impl From<io::Error> for ErroApp {
    fn from(e: io::Error) -> Self {
        ErroApp::Io(e)
    }
}

impl From<ParseIntError> for ErroApp {
    fn from(e: ParseIntError) -> Self {
        ErroApp::Parse(e)
    }
}

fn le_numero(caminho: &str) -> Result<i32, ErroApp> {
    let texto = fs::read_to_string(caminho)?;  // io::Error -> ErroApp
    let n = texto.trim().parse::<i32>()?;      // ParseIntError -> ErroApp
    Ok(n)
}

fn main() {
    match le_numero("inexistente.txt") {
        Ok(n) => println!("{n}"),
        Err(e) => println!("{e}"),
    }
}
```

## `map_err` para conversões pontuais

```rust
fn parse(s: &str) -> Result<u8, String> {
    s.parse::<u8>().map_err(|e| format!("'{s}' inválido: {e}"))
}

fn main() {
    println!("{:?} {:?}", parse("7"), parse("300"));
}
```

> [!info] Coerência
> Só pode haver **uma** implementação `From<X> for MeuErro` por tipo `X`. Se dois erros de origens diferentes têm o mesmo tipo (`io::Error` em dois contextos), use `map_err` para distinguir.

## Veja também

- [[Operador de interrogação]]
- [[Erros customizados]]
- [[From e Into]]
