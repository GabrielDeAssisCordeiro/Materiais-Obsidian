---
tags: [rust, basico, tipos]
aliases: ["fatias", "&[T]"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Arrays]]", "[[Strings String vs str]]", "[[Ranges]]"]
---

# Slices

Um **slice** é uma *visão* (referência) para uma sequência contígua de elementos. O tipo é `&[T]` (ou `&mut [T]`) e carrega ponteiro + tamanho.

```rust
fn soma(valores: &[i32]) -> i32 {
    valores.iter().sum()
}

fn main() {
    let v = vec![1, 2, 3, 4, 5];
    let a = [10, 20, 30];

    println!("{}", soma(&v));        // &Vec<i32> vira &[i32]
    println!("{}", soma(&a));        // &[i32; 3] vira &[i32]
    println!("{}", soma(&v[1..4]));  // fatia dos índices 1, 2, 3
}
```

| Sintaxe | Resultado |
|---|---|
| `&v[..]` | tudo |
| `&v[2..]` | do índice 2 ao fim |
| `&v[..3]` | do início até o índice 2 |
| `&v[1..=3]` | índices 1, 2 e 3 |

> [!tip] Aceite slices nos parâmetros
> Receber `&[T]` em vez de `&Vec<T>` torna a função mais genérica. O mesmo vale para `&str` em vez de `&String`.

## Veja também

- [[Arrays]]
- [[Strings String vs str]]
- [[Ranges]]
