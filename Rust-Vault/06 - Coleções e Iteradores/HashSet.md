---
tags: [rust, colecoes]
aliases: ["HashSet<T>", "conjunto"]
tipo: tipo-de-dado
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[HashMap]]", "[[BTreeMap]]", "[[Escolhendo uma coleção]]"]
---

# HashSet

`HashSet<T>` guarda valores **únicos**, sem ordem.

```rust
use std::collections::HashSet;

fn main() {
    let a: HashSet<i32> = [1, 2, 3].into_iter().collect();
    let b = HashSet::from([2, 3, 4]);

    let mut inter: Vec<_> = a.intersection(&b).cloned().collect();
    inter.sort();
    let mut uniao: Vec<_> = a.union(&b).copied().collect();
    uniao.sort();
    let mut dif: Vec<_> = a.difference(&b).copied().collect();
    dif.sort();

    println!("{:?} {:?} {:?}", inter, uniao, dif);

    let mut vistos = HashSet::new();
    println!("{}", vistos.insert("x")); // true: novo
    println!("{}", vistos.insert("x")); // false: já existia
    println!("{}", vistos.contains("x"));
}
```

> [!tip] Remover duplicatas mantendo a ordem
> Percorra o vetor e use o retorno de `insert` para filtrar: `v.into_iter().filter(|x| vistos.insert(*x))`.

## Veja também

- [[HashMap]]
- [[BTreeMap]]
- [[Escolhendo uma coleção]]
