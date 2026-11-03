---
tags: [rust, traits, genericos]
aliases: ["trait bound", "cláusula where", "T: Trait"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Genéricos]]", "[[impl Trait e dyn Trait]]"]
---

# Trait bounds e where

**Trait bounds** restringem os tipos aceitos por um genérico.

```rust
use std::fmt::{Debug, Display};

// Sintaxe inline
fn mostra<T: Display + Clone>(x: &T) -> String {
    format!("<{}>", x.clone())
}

// Cláusula where: mais legível com muitos bounds
fn compara_e_mostra<T, U>(t: &T, u: &U) -> String
where
    T: Display + PartialOrd,
    U: Debug + Clone,
{
    format!("{} / {:?}", t, u.clone())
}

// impl Trait em argumento: açúcar sintático para um bound anônimo
fn imprime(x: impl Display) {
    println!("{x}");
}

fn main() {
    println!("{}", mostra(&5));
    println!("{}", compara_e_mostra(&1.5, &vec![1, 2]));
    imprime("olá");
}
```

## Implementações condicionais e blanket impls

```rust
use std::fmt::Debug;

trait Descreve {
    fn descreve(&self) -> String;
}

// Blanket impl: vale para QUALQUER tipo que implemente Debug
impl<T: Debug> Descreve for T {
    fn descreve(&self) -> String {
        format!("valor: {:?}", self)
    }
}

struct Embrulho<T>(T);

// Método só existe se T: Display
impl<T: std::fmt::Display> Embrulho<T> {
    fn mostra(&self) -> String {
        format!("[{}]", self.0)
    }
}

fn main() {
    println!("{}", 5i32.descreve());
    println!("{}", vec![1, 2].descreve());
    println!("{}", Embrulho("x").mostra());
}
```

> [!info] Exemplos na std
> `impl<T: Display> ToString for T` é o motivo de todo tipo `Display` ter `.to_string()`.

> [!tip] `?Sized`
> Por padrão, `T` precisa ter tamanho conhecido (`Sized`). Para aceitar `str` e `[T]`, use `T: ?Sized`.

## Veja também

- [[Traits]]
- [[Genéricos]]
- [[impl Trait e dyn Trait]]
