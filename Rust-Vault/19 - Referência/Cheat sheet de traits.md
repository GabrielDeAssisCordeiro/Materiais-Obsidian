---
tags: [rust, referencia, cheatsheet, traits]
aliases: ["Resumo de traits", "Traits padrão em uma página"]
tipo: cheatsheet
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Traits padrão]]", "[[derive]]", "[[Trait bounds e where]]", "[[impl Trait e dyn Trait]]", "[[From e Into]]", "[[Sobrecarga de operadores]]"]
---

# Cheat sheet de traits

## Traits padrão mais usadas

| Trait | Para quê | `derive`? | Exemplo de uso |
|---|---|---|---|
| `Debug` | formatar com `{:?}` (depuração) | sim | `println!("{x:?}")` |
| `Display` | formatar com `{}` (usuário final) | **não** | `impl fmt::Display` |
| `Clone` | duplicar explicitamente | sim | `x.clone()` |
| `Copy` | duplicar implicitamente | sim (exige `Clone`) | tipos pequenos |
| `PartialEq` / `Eq` | `==` / igualdade total | sim | comparar |
| `PartialOrd` / `Ord` | `<`, `>` / ordem total | sim | `sort()` exige `Ord` |
| `Hash` | chave de `HashMap`/`HashSet` | sim | com `Eq` |
| `Default` | valor padrão | sim | `T::default()` |
| `From` / `Into` | conversão infalível | manual | `let s: String = "a".into()` |
| `TryFrom` / `TryInto` | conversão falível | manual | `u8::try_from(300)` |
| `FromStr` | `str::parse` | manual | `"5".parse::<i32>()` |
| `AsRef` / `Borrow` | visão emprestada | manual | `fn f(p: impl AsRef<Path>)` |
| `Deref` | `*x` e coerção | manual | ponteiros inteligentes |
| `Drop` | limpeza | manual | RAII |
| `Iterator` / `IntoIterator` | iteração / `for` | manual | `impl Iterator for X` |
| `Fn` / `FnMut` / `FnOnce` | closures | automática | `impl Fn(i32) -> i32` |
| `Send` / `Sync` | segurança entre threads | automática | `thread::spawn` |
| `Error` | erros | manual | `Box<dyn Error>` |

## Despacho estático × dinâmico

| | `impl Trait` / genérico | `dyn Trait` |
|---|---|---|
| Resolução | em compilação (monomorfização) | em execução (vtable) |
| Velocidade | mais rápido, *inline* | indireção |
| Tamanho do binário | pode crescer | menor |
| Coleção heterogênea | não | **sim** (`Vec<Box<dyn T>>`) |
| Requisito | — | trait *dyn compatible* ([[Object safety]]) |

## Sintaxe de limites

```rust
use std::fmt::{Debug, Display};

// Limites inline, com where e impl Trait: equivalentes
fn a<T: Display + Clone>(x: T) -> String {
    format!("{}", x.clone())
}

fn b<T>(x: T) -> String
where
    T: Display + Debug,
{
    format!("{x} / {x:?}")
}

fn c(x: impl Display) -> String {
    x.to_string()
}

// Retornar "algum tipo que implementa"
fn pares() -> impl Iterator<Item = u32> {
    (0..10).filter(|n| n % 2 == 0)
}

// Objeto de trait: tipos diferentes na mesma coleção
fn descricoes() -> Vec<Box<dyn Display>> {
    vec![Box::new(1), Box::new("dois"), Box::new(3.5)]
}

fn main() {
    println!("{} {} {}", a(1), b("x"), c(2.5));
    println!("{:?}", pares().collect::<Vec<_>>());
    for d in descricoes() {
        println!("{d}");
    }
}
```

## Receitas

| Quero... | Faça |
|---|---|
| Imprimir meu tipo com `{}` | `impl fmt::Display for T` |
| Converter `A -> B` | `impl From<A> for B` (e ganha `Into` de graça) |
| Ordenar structs | `#[derive(PartialEq, Eq, PartialOrd, Ord)]` (compara campo a campo) |
| Usar como chave de mapa | `#[derive(PartialEq, Eq, Hash)]` |
| Somar meu tipo com `+` | `impl Add for T` — [[Sobrecarga de operadores]] |
| Aceitar vários tipos de entrada | genérico com limite, ou `impl Into<T>` |
| Estender tipo alheio | *extension trait* — [[Traits avançadas]] |

## Veja também

- [[Traits]]
- [[Traits padrão]]
- [[derive]]
- [[Trait bounds e where]]
- [[impl Trait e dyn Trait]]
- [[From e Into]]
- [[Sobrecarga de operadores]]
