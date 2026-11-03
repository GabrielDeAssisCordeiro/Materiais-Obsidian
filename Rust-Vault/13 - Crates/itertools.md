---
tags: [rust, crates, itertools, iteradores]
aliases: ["itertools", "adaptadores extras de iterador"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Adaptadores de iterador]]"]
---

# itertools

**itertools** acrescenta dezenas de adaptadores e consumidores a todo `Iterator` por meio de uma trait de extensão.

```toml
[dependencies]
itertools = "0.14"
```

```rust
// requer crate: itertools
use itertools::Itertools;

fn main() {
    let v = vec![3, 1, 2, 3, 1];

    println!("{}", v.iter().join(", "));                  // "3, 1, 2, 3, 1"
    println!("{:?}", v.iter().unique().collect_vec());    // [3, 1, 2]
    println!("{:?}", v.iter().sorted().collect_vec());    // [1, 1, 2, 3, 3]

    // Pares consecutivos
    for (a, b) in v.iter().tuple_windows() {
        print!("({a},{b}) ");
    }
    println!();

    // Produto cartesiano e combinações
    let pares: Vec<(i32, char)> = (1..=2).cartesian_product("ab".chars()).collect();
    println!("{:?}", pares);
    println!("{:?}", (1..=4).combinations(2).count()); // 6

    // Mínimo e máximo em uma só passagem
    println!("{:?}", v.iter().minmax());
}
```

> [!tip] Antes de adicionar a dependência
> Parte do que o itertools oferece já existe na `std` (`chunks`, `windows`, `zip`, `flat_map`). Use-o quando o ganho de legibilidade compensar.

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/itertools antes de copiar para um projeto.

## Veja também

- [[Iteradores]]
- [[Adaptadores de iterador]]
