---
tags: [rust, traits]
aliases: ["trait", "comportamento compartilhado", "impl Trait for"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Trait bounds e where]]", "[[impl Trait e dyn Trait]]", "[[Traits padrão]]", "[[Supertraits]]", "[[Métodos e funções associadas]]"]
---

# Traits

Uma **trait** define um conjunto de métodos que tipos podem implementar: o mecanismo de comportamento compartilhado de Rust (parecido com interfaces).

```rust
trait Animal {
    fn nome(&self) -> String;
    fn som(&self) -> String;

    // Método com implementação padrão
    fn apresenta(&self) -> String {
        format!("{} faz {}", self.nome(), self.som())
    }
}

struct Cachorro;
struct Gato {
    nome: String,
}

impl Animal for Cachorro {
    fn nome(&self) -> String {
        "Rex".to_string()
    }
    fn som(&self) -> String {
        "au".to_string()
    }
}

impl Animal for Gato {
    fn nome(&self) -> String {
        self.nome.clone()
    }
    fn som(&self) -> String {
        "miau".to_string()
    }
    // sobrescrevendo o padrão
    fn apresenta(&self) -> String {
        format!("o gato {} diz {}", self.nome, self.som())
    }
}

fn main() {
    let g = Gato { nome: "Mimi".to_string() };
    println!("{}", Cachorro.apresenta());
    println!("{}", g.apresenta());
}
```

## Funções associadas em traits

```rust
trait Zero {
    fn zero() -> Self;
}

impl Zero for i32 {
    fn zero() -> Self {
        0
    }
}

impl Zero for f64 {
    fn zero() -> Self {
        0.0
    }
}

fn soma_todos<T: Zero + std::ops::Add<Output = T> + Copy>(v: &[T]) -> T {
    let mut acc = T::zero();
    for &x in v {
        acc = acc + x;
    }
    acc
}

fn main() {
    println!("{} {}", soma_todos(&[1, 2, 3]), soma_todos(&[0.5, 0.25]));
}
```

> [!info] Regra de coerência
> Você só pode implementar uma trait para um tipo se **a trait ou o tipo for seu**; veja [[Orphan rule]].

> [!tip] Traits em escopo
> Para chamar métodos de uma trait, ela precisa estar no escopo (`use meu_mod::MinhaTrait;`). Itens do *prelude* já estão.

## Exercício

Defina a trait `Area` com `fn area(&self) -> f64` e implemente-a para `Circulo` e `Retangulo`.

## Veja também

- [[Trait bounds e where]]
- [[impl Trait e dyn Trait]]
- [[Traits padrão]]
- [[Supertraits]]
- [[Métodos e funções associadas]]
