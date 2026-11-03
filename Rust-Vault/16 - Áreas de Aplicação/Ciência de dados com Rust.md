---
tags: [rust, areas, dados]
aliases: ["polars", "ndarray", "dataframes", "machine learning", "candle", "burn"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Rayon]]", "[[cxx e PyO3]]", "[[serde e serde_json]]", "[[Iteradores]]"]
---

# Ciência de dados com Rust

Rust não substitui Python para exploração interativa, mas é cada vez mais usado para o **motor de alta performance** por baixo: o **Polars** (dataframes) é escrito em Rust.

| Necessidade | Crate |
|---|---|
| DataFrames | `polars` |
| Arrays N-dimensionais | `ndarray` |
| Álgebra linear | `nalgebra`, `faer` |
| ML clássico | `linfa` |
| Deep learning | `candle`, `burn` |
| CSV / Parquet / Arrow | `csv`, `parquet`, `arrow` |
| Paralelismo | [[Rayon]] |
| Estatística | `statrs` |

## Estatística na biblioteca padrão

```rust
fn media(v: &[f64]) -> Option<f64> {
    if v.is_empty() {
        None
    } else {
        Some(v.iter().sum::<f64>() / v.len() as f64)
    }
}

fn desvio_padrao(v: &[f64]) -> Option<f64> {
    let m = media(v)?;
    let var = v.iter().map(|x| (x - m).powi(2)).sum::<f64>() / v.len() as f64;
    Some(var.sqrt())
}

fn main() {
    let dados = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0];
    println!("média = {:?}", media(&dados));
    println!("desvio = {:?}", desvio_padrao(&dados)); // Some(2.0)
}
```

## Polars (lazy)

```rust
// requer crate: polars
use polars::prelude::*;

fn main() -> PolarsResult<()> {
    let df = df!(
        "cidade" => ["SP", "RJ", "SP", "RJ"],
        "valor"  => [10, 20, 30, 40],
    )?;

    let resultado = df
        .lazy()
        .group_by([col("cidade")])
        .agg([col("valor").sum().alias("total")])
        .collect()?;

    println!("{resultado}");
    Ok(())
}
```

> [!tip] Combinação poderosa
> Escreva o gargalo em Rust e exponha-o a Python com **PyO3**/maturin: veja [[cxx e PyO3]].

> [!question] Verificar na documentação oficial
> A API do Polars muda com frequência (por exemplo, `group_by`). Confirme em docs.rs/polars.

## Veja também

- [[Rayon]]
- [[cxx e PyO3]]
- [[serde e serde_json]]
- [[Iteradores]]
