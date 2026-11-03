---
tags: [rust, colecoes]
aliases: ["BTreeMap", "BTreeSet", "mapa ordenado"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[HashMap]]", "[[Escolhendo uma coleção]]", "[[BinaryHeap]]"]
---

# BTreeMap

`BTreeMap<K, V>` mantém as chaves **ordenadas** (árvore B). Exige `Ord` e permite consultas por intervalo.

```rust
use std::collections::BTreeMap;

fn main() {
    let mut m = BTreeMap::new();
    m.insert(3, "c");
    m.insert(1, "a");
    m.insert(2, "b");
    m.insert(5, "e");

    for (k, v) in &m {
        print!("{k}{v} "); // sempre em ordem crescente de chave
    }
    println!();

    for (k, v) in m.range(2..5) {
        print!("{k}{v} ");
    }
    println!();

    println!("{:?} {:?}", m.first_key_value(), m.last_key_value());
}
```

`BTreeSet<T>` é o equivalente para conjuntos ordenados.

| | `HashMap` | `BTreeMap` |
|---|---|---|
| Ordem | Nenhuma | Por chave |
| Busca/inserção | O(1) médio | O(log n) |
| Intervalos | Não | Sim |
| Exige | `Eq + Hash` | `Ord` |

## Veja também

- [[HashMap]]
- [[Escolhendo uma coleção]]
- [[BinaryHeap]]
