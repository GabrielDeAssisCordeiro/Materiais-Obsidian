---
tags: [rust, avancado, traits]
aliases: ["blanket impl", "impl genérico", "extension trait", "sealed trait", "marker trait"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Trait bounds e where]]", "[[Orphan rule]]", "[[Tipos associados]]", "[[Object safety]]"]
---

# Traits avançadas

## Blanket implementations

Implementa uma trait para **todos** os tipos que satisfazem um limite. A `std` faz isto, por exemplo, em `impl<T: Display> ToString for T`.

```rust
use std::fmt::Display;

trait Anunciar {
    fn anunciar(&self) -> String;
}

impl<T: Display> Anunciar for T {
    fn anunciar(&self) -> String {
        format!("Atenção: {self}")
    }
}

fn main() {
    println!("{}", 42.anunciar());
    println!("{}", "olá".anunciar());
}
```

## Extension traits

Adicionam métodos a tipos que você não controla (combinado com blanket impl):

```rust
trait StrExt {
    fn eh_palindromo(&self) -> bool;
}

impl StrExt for str {
    fn eh_palindromo(&self) -> bool {
        let c: Vec<char> = self.chars().filter(|c| c.is_alphanumeric()).collect();
        c.iter().eq(c.iter().rev())
    }
}

fn main() {
    println!("{}", "arara".eh_palindromo());
    println!("{}", "rust".eh_palindromo());
}
```

## Sealed traits

Impedem que código externo implemente sua trait, permitindo evoluí-la sem quebrar compatibilidade:

```rust
mod selado {
    pub trait Selo {}
}

pub trait Formato: selado::Selo {
    fn extensao(&self) -> &'static str;
}

pub struct Json;
pub struct Toml;

impl selado::Selo for Json {}
impl selado::Selo for Toml {}

impl Formato for Json {
    fn extensao(&self) -> &'static str {
        "json"
    }
}
impl Formato for Toml {
    fn extensao(&self) -> &'static str {
        "toml"
    }
}

fn main() {
    println!("{} {}", Json.extensao(), Toml.extensao());
}
```

## Outras técnicas

| Técnica | Descrição |
|---|---|
| **Marker traits** | sem métodos; só sinalizam propriedades (`Copy`, `Send`, `Eq`) |
| **Traits com `const`** | `trait T { const NOME: &'static str; }` |
| **Métodos com `where Self: Sized`** | mantêm a trait compatível com `dyn` — veja [[Object safety]] |
| **Implementação padrão com especialização** | especialização (`min_specialization`) ainda é instável |

> [!warning] Coerência
> Blanket impls interagem com a [[Orphan rule]]: adicionar um blanket impl a uma biblioteca pública pode ser uma **mudança incompatível**, pois pode colidir com impls de usuários.

## Veja também

- [[Traits]]
- [[Trait bounds e where]]
- [[Orphan rule]]
- [[Tipos associados]]
- [[Object safety]]
