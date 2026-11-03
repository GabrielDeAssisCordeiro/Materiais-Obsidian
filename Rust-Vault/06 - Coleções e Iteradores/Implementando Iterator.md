---
tags: [rust, iteradores, traits]
aliases: ["impl Iterator", "IntoIterator", "iterador próprio"]
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Adaptadores de iterador]]", "[[Traits padrão]]"]
---

# Implementando Iterator

Basta implementar `next` para ganhar **todos** os adaptadores e consumidores de graça.

```rust
struct Fibonacci {
    a: u64,
    b: u64,
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<u64> {
        let atual = self.a;
        self.a = self.b;
        self.b += atual;
        Some(atual) // iterador infinito: nunca devolve None
    }
}

fn main() {
    let primeiros: Vec<u64> = Fibonacci { a: 0, b: 1 }.take(10).collect();
    println!("{:?}", primeiros);

    let soma_pares: u64 = Fibonacci { a: 0, b: 1 }
        .take_while(|&n| n < 100)
        .filter(|n| n % 2 == 0)
        .sum();
    println!("{soma_pares}");
}
```

## Tornando uma coleção iterável com `IntoIterator`

```rust
struct Pilha {
    itens: Vec<i32>,
}

// for x in pilha   (consome)
impl IntoIterator for Pilha {
    type Item = i32;
    type IntoIter = std::vec::IntoIter<i32>;

    fn into_iter(self) -> Self::IntoIter {
        self.itens.into_iter()
    }
}

// for x in &pilha  (empresta)
impl<'a> IntoIterator for &'a Pilha {
    type Item = &'a i32;
    type IntoIter = std::slice::Iter<'a, i32>;

    fn into_iter(self) -> Self::IntoIter {
        self.itens.iter()
    }
}

fn main() {
    let p = Pilha { itens: vec![1, 2, 3] };
    for x in &p {
        print!("{x} ");
    }
    for x in p {
        print!("{x} ");
    }
    println!();
}
```

> [!tip] Retornando iteradores
> Para devolver uma cadeia sem nomear o tipo, use `fn pares(v: &[i32]) -> impl Iterator<Item = &i32> { v.iter().filter(|x| *x % 2 == 0) }`. Veja [[impl Trait e dyn Trait]].

## Veja também

- [[Iteradores]]
- [[Adaptadores de iterador]]
- [[Traits padrão]]
