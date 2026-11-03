---
tags: [rust, areas]
aliases: ["Solana", "Substrate", "contratos inteligentes", "cadeia de blocos"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Structs]]", "[[Zero-cost abstractions]]", "[[Áreas de Aplicação]]"]
---

# Blockchain com Rust

Rust é muito usado em blockchains por oferecer **segurança de memória**, **determinismo** e **desempenho**. Ecossistemas notáveis: **Solana** (programas on-chain em Rust), **Polkadot/Substrate**, **NEAR**, **Aptos/Sui** (Move, com nós em Rust) e clientes Ethereum como **Reth**.

## Uma cadeia de hashes mínima

```rust
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

#[derive(Debug)]
struct Bloco {
    indice: u64,
    dados: String,
    hash_anterior: u64,
    hash: u64,
}

impl Bloco {
    fn novo(indice: u64, dados: &str, hash_anterior: u64) -> Self {
        let mut h = DefaultHasher::new();
        (indice, dados, hash_anterior).hash(&mut h);
        Bloco { indice, dados: dados.to_string(), hash_anterior, hash: h.finish() }
    }
}

fn valida(cadeia: &[Bloco]) -> bool {
    cadeia.windows(2).all(|par| par[1].hash_anterior == par[0].hash)
}

fn main() {
    let genese = Bloco::novo(0, "gênese", 0);
    let b1 = Bloco::novo(1, "Ana paga 5 a Bia", genese.hash);
    let b2 = Bloco::novo(2, "Bia paga 2 a Caio", b1.hash);
    let cadeia = vec![genese, b1, b2];
    println!("válida? {}", valida(&cadeia));
    println!("{:?}", cadeia.last().unwrap());
}
```

> [!warning] Isto é só didático
> `DefaultHasher` **não é criptográfico**. Em sistemas reais use SHA-256 ou BLAKE3 (crates `sha2`, `blake3`).

> [!info] Por que Rust
> Contratos inteligentes lidam com dinheiro: um bug de memória ou de *overflow* é um prejuízo real. O compilador elimina classes inteiras de falhas; ainda assim, **lógica** incorreta continua possível — audite e teste (veja [[Property-based testing com proptest]]).

> [!question] Verificar na documentação oficial
> Frameworks (Anchor, Substrate, ink!) mudam de versão rapidamente; consulte a documentação de cada rede.

## Veja também

- [[Traits]]
- [[Structs]]
- [[Zero-cost abstractions]]
- [[Áreas de Aplicação]]
