---
tags: [rust, erros, boas-praticas]
aliases: ["error handling"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Panic]]", "[[Operador de interrogação]]", "[[Erros customizados]]", "[[thiserror e anyhow]]"]
---

# Boas práticas de tratamento de erros

| Prática | Por quê |
|---|---|
| Devolva `Result`, não use `panic!` para falhas esperadas | O chamador decide como reagir |
| Evite `unwrap()` fora de testes e protótipos | Cada `unwrap` é um possível panic |
| Use `expect("invariante...")` para invariantes | A mensagem explica por que "não pode falhar" |
| Adicione **contexto** ao propagar | "lendo config.toml: permissão negada" é melhor que "permissão negada" |
| Mensagens de erro em minúsculas, sem ponto final | Convenção da biblioteca padrão; facilita encadear |
| Bibliotecas: tipos de erro próprios (`thiserror`) | Permite `match` nas causas |
| Aplicações: `anyhow` ou `Box<dyn Error>` | Menos cerimônia |
| Marque enums de erro públicos com `#[non_exhaustive]` | Adicionar variantes não quebra clientes |
| Defina `type Result<T> = std::result::Result<T, MeuErro>;` | Menos ruído nas assinaturas |
| Documente `# Errors` e `# Panics` | Faz parte do contrato da função |

```rust
use std::fmt;

#[derive(Debug)]
#[non_exhaustive]
pub enum MeuErro {
    Entrada(String),
}

impl fmt::Display for MeuErro {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MeuErro::Entrada(m) => write!(f, "entrada inválida: {m}"),
        }
    }
}

impl std::error::Error for MeuErro {}

pub type Result<T> = std::result::Result<T, MeuErro>;

/// Divide `a` por `b`.
///
/// # Errors
///
/// Devolve [`MeuErro::Entrada`] se `b` for zero.
pub fn divide(a: i32, b: i32) -> Result<i32> {
    if b == 0 {
        return Err(MeuErro::Entrada("divisor zero".to_string()));
    }
    Ok(a / b)
}

fn main() {
    println!("{:?}", divide(6, 3));
    if let Err(e) = divide(1, 0) {
        eprintln!("erro: {e}");
    }
}
```

> [!info] Erros como valores
> Tratar erros explicitamente deixa o fluxo visível no código e no sistema de tipos, em vez de escondido em exceções.

## Veja também

- [[Panic]]
- [[Operador de interrogação]]
- [[Erros customizados]]
- [[thiserror e anyhow]]
