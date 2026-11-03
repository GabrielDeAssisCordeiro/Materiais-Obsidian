---
tags: [rust, iteradores]
aliases: ["Iterator", "iter", "iter_mut", "into_iter", "next"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Adaptadores de iterador]]", "[[Consumidores de iterador]]", "[[Implementando Iterator]]", "[[Zero-cost abstractions]]", "[[while e for]]"]
---

# Iteradores

Um **iterador** produz uma sequência de valores, um por vez. É qualquer tipo que implementa a trait `Iterator` (método `next`). Iteradores são **preguiçosos**: nada acontece até serem consumidos.

```rust
fn main() {
    let v = vec![1, 2, 3];
    let mut it = v.iter();
    println!("{:?} {:?}", it.next(), it.next()); // Some(1) Some(2)
    println!("{:?} {:?}", it.next(), it.next()); // Some(3) None
}
```

## Três formas de iterar

| Método | Item | Efeito na coleção |
|---|---|---|
| `iter()` | `&T` | empresta |
| `iter_mut()` | `&mut T` | empresta mutavelmente |
| `into_iter()` | `T` | **consome** a coleção |

```rust
fn main() {
    let mut v = vec![String::from("a"), String::from("b")];

    for s in v.iter() {         // &String
        print!("{s} ");
    }
    for s in v.iter_mut() {     // &mut String
        s.push('!');
    }
    for s in v {                // String: v é movido
        print!("{s} ");
    }
    println!();
}
```

O laço `for x in expr` chama `IntoIterator::into_iter(expr)`: por isso `for x in &v` dá referências e `for x in v` dá valores.

```mermaid
graph LR
    A[Coleção] --> B["iter()"]
    B --> C["adaptadores: map, filter..."]
    C --> D["consumidor: collect, sum..."]
    D --> E[Resultado]
```

> [!info] Preguiça
> `v.iter().map(|x| x + 1);` sozinho não executa nada (o compilador avisa com `unused_must_use`). É preciso um consumidor.

## Veja também

- [[Adaptadores de iterador]]
- [[Consumidores de iterador]]
- [[Implementando Iterator]]
- [[Zero-cost abstractions]]
- [[while e for]]
