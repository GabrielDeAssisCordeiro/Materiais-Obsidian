---
tags: [rust, colecoes, ordenacao]
aliases: ["sort_by", "sort_by_key", "binary_search", "total_cmp"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Vec]]", "[[Closures]]", "[[Traits padrão]]"]
---

# Ordenação e busca

```rust
fn main() {
    let mut v = vec![5, 2, 9, 1];
    v.sort();                       // estável, O(n log n)
    println!("{:?}", v);
    v.sort_by(|a, b| b.cmp(a));     // decrescente
    println!("{:?}", v);
    v.sort_unstable();              // mais rápido, sem garantir ordem de iguais

    // Por chave
    let mut pessoas = vec![("Ana", 30), ("Bia", 25), ("Caio", 35)];
    pessoas.sort_by_key(|p| p.1);
    println!("{:?}", pessoas);

    // f64 não é Ord (por causa de NaN): use partial_cmp ou total_cmp
    let mut f: Vec<f64> = vec![3.2, 1.1, 2.5];
    f.sort_by(|a, b| a.partial_cmp(b).unwrap());
    println!("{:?}", f);
    f.sort_by(|a, b| b.total_cmp(a));
    println!("{:?}", f);

    // Busca binária (exige slice ordenado)
    let ordenado = [1, 3, 5, 7];
    println!("{:?} {:?}", ordenado.binary_search(&5), ordenado.binary_search(&4)); // Ok(2) Err(2)
}
```

| Método | Observação |
|---|---|
| `sort` | estável, usa `Ord` |
| `sort_unstable` | não aloca; costuma ser mais rápido |
| `sort_by` / `sort_by_key` | comparador / chave customizados |
| `binary_search` | `Ok(índice)` ou `Err(ponto de inserção)` |

> [!tip] Chave decrescente
> Use `std::cmp::Reverse`: `v.sort_by_key(|p| std::cmp::Reverse(p.1))`.

## Veja também

- [[Vec]]
- [[Closures]]
- [[Traits padrão]]
