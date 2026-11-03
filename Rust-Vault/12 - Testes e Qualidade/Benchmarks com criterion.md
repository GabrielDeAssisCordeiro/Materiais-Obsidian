---
tags: [rust, testes, desempenho]
aliases: ["criterion", "benchmark", "cargo bench", "black_box"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Perfilamento]]", "[[Debug vs release]]", "[[Zero-cost abstractions]]"]
---

# Benchmarks com criterion

O **Criterion** faz benchmarks estatisticamente robustos (várias amostras, detecção de regressões, relatórios HTML).

```toml
[dev-dependencies]
criterion = "0.5"

[[bench]]
name = "fib"
harness = false     # usa o harness do criterion em vez do padrão
```

```rust
// requer crate: criterion
// benches/fib.rs
use criterion::{criterion_group, criterion_main, Criterion};
use std::hint::black_box;

fn fib(n: u64) -> u64 {
    if n < 2 { n } else { fib(n - 1) + fib(n - 2) }
}

fn bench(c: &mut Criterion) {
    // black_box impede o compilador de otimizar a entrada/saída
    c.bench_function("fib 20", |b| b.iter(|| fib(black_box(20))));
}

criterion_group!(benches, bench);
criterion_main!(benches);
```

```bash
cargo bench                      # compila em release e roda; relatórios em target/criterion
cargo bench -- --save-baseline antes
cargo bench -- --baseline antes  # compara com a execução anterior
```

> [!question] Verificar na documentação oficial
> Confira a versão atual do `criterion` e se o `black_box` recomendado é o da `std::hint` ou o do próprio crate.

> [!warning] Cuidados
> Benchmarks medem **release**; evite ruído (outros programas, modo economia de energia). Meça a função isolada e compare **antes/depois**, não valores absolutos.

> [!info] `#[bench]` nativo
> O atributo `#[bench]` da biblioteca padrão é instável (somente nightly); por isso se usa o criterion.

## Veja também

- [[Perfilamento]]
- [[Debug vs release]]
- [[Zero-cost abstractions]]
