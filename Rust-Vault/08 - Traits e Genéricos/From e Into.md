---
tags: [rust, traits, conversao]
aliases: ["From", "Into", "TryFrom", "TryInto", "conversões"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Conversão entre tipos]]", "[[Conversão de erros com From]]", "[[Traits padrão]]", "[[Deref e AsRef]]"]
---

# From e Into

- `From<T> for U`: converte `T` em `U` sem falhar.
- `Into<U> for T` é **derivada automaticamente** de `From`; implemente sempre `From`.
- `TryFrom` / `TryInto` para conversões que podem falhar.

```rust
use std::convert::TryFrom;

struct Celsius(f64);
struct Fahrenheit(f64);

impl From<Celsius> for Fahrenheit {
    fn from(c: Celsius) -> Self {
        Fahrenheit(c.0 * 9.0 / 5.0 + 32.0)
    }
}

struct Par(u32);

impl TryFrom<i64> for Par {
    type Error = String;

    fn try_from(v: i64) -> Result<Self, Self::Error> {
        if v >= 0 && v % 2 == 0 {
            Ok(Par(v as u32))
        } else {
            Err(format!("{v} não é um par não negativo"))
        }
    }
}

// Parâmetro flexível: aceita &str, String, etc.
struct Pessoa {
    nome: String,
}

impl Pessoa {
    fn new(nome: impl Into<String>) -> Self {
        Self { nome: nome.into() }
    }
}

fn main() {
    let f: Fahrenheit = Celsius(100.0).into();
    println!("{}", f.0); // 212

    println!("{:?}", Par::try_from(8i64).map(|p| p.0));
    let r: Result<Par, _> = 7i64.try_into();
    println!("{}", r.is_err());

    let a = Pessoa::new("Ana");
    let b = Pessoa::new(String::from("Bia"));
    println!("{} {}", a.nome, b.nome);

    // Conversões da biblioteca padrão
    let s: String = "texto".into();
    let n: i64 = i64::from(7u8);
    let v: Vec<u8> = "oi".into();
    println!("{s} {n} {:?}", v);
}
```

> [!tip] Convenção de nomes
> `from`/`into` = conversão infalível; `as_*` = visão barata (empresta); `to_*` = cópia/cálculo custoso; `into_*` = consome.

## Veja também

- [[Conversão entre tipos]]
- [[Conversão de erros com From]]
- [[Traits padrão]]
- [[Deref e AsRef]]
