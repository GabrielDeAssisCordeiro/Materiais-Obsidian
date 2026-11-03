---
tags: [rust, erros, trait-objects]
aliases: ["Box<dyn Error>", "erro dinâmico", "downcast"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Operador de interrogação]]", "[[Erros customizados]]", "[[thiserror e anyhow]]"]
---

# Box dyn Error

`Box<dyn Error>` é um tipo de erro "qualquer coisa que implemente `Error`". Conveniente em aplicações e protótipos.

```rust
use std::error::Error;
use std::fmt;

#[derive(Debug)]
struct MeuErro;

impl fmt::Display for MeuErro {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "meu erro")
    }
}

impl Error for MeuErro {}

fn faz(passo: u8) -> Result<(), Box<dyn Error>> {
    match passo {
        0 => Err("erro como &str".into()),         // &str -> Box<dyn Error>
        1 => Err(Box::new(MeuErro)),
        2 => {
            let _n: i32 = "x".parse()?;           // ParseIntError -> Box<dyn Error>
            Ok(())
        }
        _ => Ok(()),
    }
}

fn main() {
    for p in 0..4 {
        match faz(p) {
            Ok(()) => println!("{p}: ok"),
            Err(e) => {
                // downcast_ref recupera o tipo concreto
                if e.downcast_ref::<MeuErro>().is_some() {
                    println!("{p}: era MeuErro");
                } else {
                    println!("{p}: {e}");
                }
            }
        }
    }
}
```

| Vantagem | Desvantagem |
|---|---|
| Aceita qualquer erro com `?` | Perde o tipo concreto (só via `downcast`) |
| Zero boilerplate | O chamador não consegue fazer `match` nas causas |
| Bom para `main` e scripts | Não recomendado como API de biblioteca |

> [!tip] Send + Sync
> Em código concorrente, use `Box<dyn Error + Send + Sync>` para poder enviar o erro entre threads.

## Veja também

- [[Operador de interrogação]]
- [[Erros customizados]]
- [[thiserror e anyhow]]
