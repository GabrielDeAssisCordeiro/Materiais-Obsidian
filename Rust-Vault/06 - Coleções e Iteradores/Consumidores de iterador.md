---
tags: [rust, iteradores]
aliases: ["collect", "sum", "fold", "count", "all", "position", "partition"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Adaptadores de iterador]]", "[[Option e Result]]"]
---

# Consumidores de iterador

Consumidores **executam** a cadeia e produzem um resultado.

| Consumidor | Resultado |
|---|---|
| `collect()` | constrói uma coleção (`Vec`, `String`, `HashMap`, `Result<Vec<_>, _>`...) |
| `sum()` / `product()` | soma / produto |
| `count()` | número de itens |
| `fold(init, f)` | reduz a um valor acumulado |
| `min()` / `max()` | extremos (`Option`) |
| `min_by_key` / `max_by_key` | extremos por chave |
| `any(p)` / `all(p)` | existe / todos |
| `find(p)` / `position(p)` | primeiro item / índice |
| `last()` / `nth(n)` | último / n-ésimo |
| `for_each(f)` | efeito colateral por item |
| `partition(p)` | divide em duas coleções |
| `unzip()` | separa pares em duas coleções |

```rust
use std::collections::HashMap;

fn main() {
    let nums = vec![3, 8, 1, 9, 4];

    let soma: i32 = nums.iter().sum();
    let total = nums.iter().fold(0, |acc, x| acc + x);
    println!("{soma} {total} {}", nums.iter().count());
    println!("{:?} {:?}", nums.iter().max(), nums.iter().min());
    println!("{} {}", nums.iter().any(|&x| x > 8), nums.iter().all(|&x| x > 0));
    println!("{:?} {:?}", nums.iter().find(|&&x| x > 5), nums.iter().position(|&x| x == 1));

    let palavras = ["casa", "ou", "elefante"];
    println!("{:?}", palavras.iter().max_by_key(|p| p.len()));

    let (pares, impares): (Vec<i32>, Vec<i32>) = nums.iter().copied().partition(|x| x % 2 == 0);
    println!("{:?} {:?}", pares, impares);

    // collect para vários tipos
    let texto: String = vec!['r', 'u', 's', 't'].into_iter().collect();
    let mapa: HashMap<&str, i32> = [("a", 1), ("b", 2)].into_iter().collect();
    println!("{texto} {}", mapa.len());

    // collect em Result: para no primeiro erro
    let ok: Result<Vec<i32>, _> = ["1", "2"].iter().map(|s| s.parse::<i32>()).collect();
    let erro: Result<Vec<i32>, _> = ["1", "x"].iter().map(|s| s.parse::<i32>()).collect();
    println!("{:?} {}", ok, erro.is_err());

    // unzip
    let (a, b): (Vec<i32>, Vec<char>) = vec![(1, 'a'), (2, 'b')].into_iter().unzip();
    println!("{:?} {:?}", a, b);
}
```

> [!tip] Anotação de tipo
> `collect` precisa saber o destino: `let v: Vec<_> = ...` ou `.collect::<Vec<_>>()` (o "turbofish").

## Exercício

Dado um texto, obtenha as palavras com mais de 3 letras, em maiúsculas, num `Vec<String>`.

## Veja também

- [[Iteradores]]
- [[Adaptadores de iterador]]
- [[Option e Result]]
