---
tags: [rust, avancado, padroes, tipos]
aliases: ["newtype pattern", "wrapper", "tipos fortes"]
tipo: padrao
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Structs]]", "[[Orphan rule]]", "[[Deref e AsRef]]", "[[Sobrecarga de operadores]]", "[[PhantomData]]"]
---

# Newtype

O padrão **newtype** é uma struct de tupla com um único campo: um tipo novo, **distinto** do original, sem custo em tempo de execução.

```rust
use std::fmt;

// 1) Segurança de tipos: impossível confundir unidades
#[derive(Debug, Clone, Copy, PartialEq, PartialOrd)]
struct Metros(f64);

#[derive(Debug, Clone, Copy, PartialEq, PartialOrd)]
struct Pes(f64);

impl From<Pes> for Metros {
    fn from(p: Pes) -> Self {
        Metros(p.0 * 0.3048)
    }
}

fn altura_maxima(m: Metros) -> Metros {
    m
}

// 2) Contornar a regra do órfão: implementar trait externa em tipo externo
struct Lista(Vec<String>);

impl fmt::Display for Lista {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

// 3) Invariantes: só se constrói um valor válido
#[derive(Debug)]
struct Email(String);

impl Email {
    fn novo(s: &str) -> Result<Self, String> {
        if s.contains('@') {
            Ok(Email(s.to_string()))
        } else {
            Err(format!("e-mail inválido: {s}"))
        }
    }
}

fn main() {
    let altura = altura_maxima(Pes(6.0).into());
    println!("{:.2} m", altura.0);

    println!("{}", Lista(vec!["a".into(), "b".into()]));

    println!("{:?}", Email::novo("ana@exemplo.com"));
    println!("{:?}", Email::novo("sem-arroba"));
}
```

| Vantagem | Exemplo |
|---|---|
| Evita misturar valores do mesmo tipo primitivo | `UserId(u64)` vs `OrderId(u64)` |
| Contorna a [[Orphan rule]] | `Display` para `Vec<T>` |
| Esconde a representação interna | pode trocar o campo sem quebrar a API |
| Garante invariantes via construtor | `Email`, `NonEmptyString` |

> [!tip] Menos boilerplate
> Se quiser que o wrapper se comporte como o interior, implemente [[Deref e AsRef]] com cuidado (não abuse de `Deref` para herança). Crates como `derive_more` automatizam a repetição.

## Exercício

Crie `Porcentagem(u8)` que só aceita valores de 0 a 100 e implemente `Display` imprimindo `42%`.

## Veja também

- [[Structs]]
- [[Orphan rule]]
- [[Deref e AsRef]]
- [[Sobrecarga de operadores]]
- [[PhantomData]]
