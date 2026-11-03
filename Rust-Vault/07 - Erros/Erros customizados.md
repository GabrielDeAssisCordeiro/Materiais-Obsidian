---
tags: [rust, erros, traits]
aliases: ["std::error::Error", "enum de erros", "source"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Operador de interrogação]]", "[[Conversão de erros com From]]", "[[thiserror e anyhow]]", "[[Boas práticas de tratamento de erros]]"]
---

# Erros customizados

Um bom tipo de erro implementa `Debug`, `Display` e `std::error::Error`, e costuma ser um **enum** com as causas possíveis.

```rust
use std::error::Error;
use std::fmt;
use std::num::ParseIntError;

#[derive(Debug)]
enum ErroPorta {
    Vazio,
    Invalido(ParseIntError),
    ForaDoIntervalo(i64),
}

impl fmt::Display for ErroPorta {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Vazio => write!(f, "valor vazio"),
            Self::Invalido(e) => write!(f, "número inválido: {e}"),
            Self::ForaDoIntervalo(n) => write!(f, "{n} fora do intervalo 1..=65535"),
        }
    }
}

impl Error for ErroPorta {
    // Encadeia a causa original
    fn source(&self) -> Option<&(dyn Error + 'static)> {
        match self {
            Self::Invalido(e) => Some(e),
            _ => None,
        }
    }
}

impl From<ParseIntError> for ErroPorta {
    fn from(e: ParseIntError) -> Self {
        Self::Invalido(e)
    }
}

fn le_porta(s: &str) -> Result<u16, ErroPorta> {
    if s.is_empty() {
        return Err(ErroPorta::Vazio);
    }
    let n: i64 = s.trim().parse()?; // ParseIntError vira ErroPorta via From
    if !(1..=65535).contains(&n) {
        return Err(ErroPorta::ForaDoIntervalo(n));
    }
    Ok(n as u16)
}

fn main() {
    for entrada in ["", "x", "70000", "8080"] {
        match le_porta(entrada) {
            Ok(p) => println!("porta {p}"),
            Err(e) => println!("erro: {e}"),
        }
    }
}
```

| Trait | Papel |
|---|---|
| `Debug` | para desenvolvedores (`derive`) |
| `Display` | mensagem para o usuário |
| `Error` | marca o tipo como erro; `source()` encadeia causas |

> [!tip] Muito boilerplate?
> Em bibliotecas, o crate `thiserror` gera `Display`, `Error` e `From` por você. Veja [[thiserror e anyhow]].

## Veja também

- [[Operador de interrogação]]
- [[Conversão de erros com From]]
- [[thiserror e anyhow]]
- [[Boas práticas de tratamento de erros]]
