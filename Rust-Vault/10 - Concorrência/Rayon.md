---
tags: [rust, concorrencia, crates]
aliases: ["rayon", "par_iter", "paralelismo de dados"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Threads]]", "[[Crossbeam]]"]
---

# Rayon

**Rayon** transforma iteradores sequenciais em **paralelos** trocando `iter()` por `par_iter()`, usando um pool de threads com *work stealing*.

```toml
[dependencies]
rayon = "1"
```

```rust
// requer crate: rayon
use rayon::prelude::*;

fn main() {
    let v: Vec<u64> = (1..=1_000_000).collect();

    // Soma dos quadrados em paralelo
    let soma: u64 = v.par_iter().map(|x| x * x).sum();
    println!("{soma}");

    // Ordenação paralela
    let mut dados: Vec<u32> = (0..100_000).rev().collect();
    dados.par_sort();

    // Modificação em paralelo
    let mut vals = vec![1, 2, 3, 4];
    vals.par_iter_mut().for_each(|x| *x *= 10);

    // join: duas tarefas em paralelo
    let (a, b) = rayon::join(|| (1..100).sum::<i32>(), || (100..200).sum::<i32>());
    println!("{a} {b}");
}
```

| API | Equivalente sequencial |
|---|---|
| `par_iter()` | `iter()` |
| `par_iter_mut()` | `iter_mut()` |
| `into_par_iter()` | `into_iter()` |
| `par_chunks(n)` | `chunks(n)` |
| `rayon::join` | duas chamadas em sequência |

> [!warning] Nem sempre compensa
> Para trabalho pequeno, o custo de dividir tarefas supera o ganho. Meça com `criterion` ou `std::time::Instant`.

> [!info] Segurança preservada
> As closures precisam ser `Send + Sync`: o compilador continua impedindo data races.

## Veja também

- [[Iteradores]]
- [[Threads]]
- [[Crossbeam]]
