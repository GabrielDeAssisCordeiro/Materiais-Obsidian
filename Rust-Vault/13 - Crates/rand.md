---
tags: [rust, crates]
aliases: ["rand", "números aleatórios", "random"]
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Escolhendo e avaliando crates]]", "[[Vec]]"]
---

# rand

Rust não tem gerador aleatório na `std`; o crate **rand** é o padrão.

```toml
[dependencies]
rand = "0.9"
```

```rust
// requer crate: rand
use rand::seq::IndexedRandom;
use rand::Rng;

fn main() {
    let mut rng = rand::rng(); // gerador local da thread

    let dado: u8 = rng.random_range(1..=6);
    let prob: f64 = rng.random(); // [0.0, 1.0)
    println!("{dado} {prob:.3}");

    let opcoes = ["pedra", "papel", "tesoura"];
    println!("{:?}", opcoes.choose(&mut rng));

    let moeda = rng.random_bool(0.5);
    println!("{moeda}");

    // Atalho global
    let x: u32 = rand::random();
    println!("{x}");
}
```

> [!question] Verificar na documentação oficial
> Os nomes mudaram na série 0.9 (`rand::rng()`, `random_range`, `random`); em versões 0.8 eram `thread_rng()`, `gen_range`, `gen`. Confirme em docs.rs/rand.

> [!warning] Segurança
> `rand::rng()` serve para jogos/simulações. Para chaves e tokens criptográficos use `rand::rngs::OsRng` ou o crate `getrandom`, e bibliotecas de criptografia dedicadas.

## Veja também

- [[Escolhendo e avaliando crates]]
- [[Vec]]
