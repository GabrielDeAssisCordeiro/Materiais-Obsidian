---
tags: [rust, iteradores, desempenho]
aliases: ["custo zero", "zero-cost"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Closures]]", "[[Pipeline de compilação]]"]
---

# Zero-cost abstractions

"O que você não usa, não paga; o que você usa, não conseguiria escrever melhor à mão" (Bjarne Stroustrup, adotado pela comunidade Rust).

Uma cadeia de iteradores é **monomorfizada** e **inlined**: o compilador gera um único laço sem alocações intermediárias.

```rust
fn soma_quadrados_pares_laco(v: &[i32]) -> i32 {
    let mut total = 0;
    for &x in v {
        if x % 2 == 0 {
            total += x * x;
        }
    }
    total
}

fn soma_quadrados_pares_iter(v: &[i32]) -> i32 {
    v.iter().filter(|&&x| x % 2 == 0).map(|&x| x * x).sum()
}

fn main() {
    let v: Vec<i32> = (1..=10).collect();
    assert_eq!(soma_quadrados_pares_laco(&v), soma_quadrados_pares_iter(&v));
    println!("{}", soma_quadrados_pares_iter(&v)); // 220
}
```

Em `--release`, as duas versões costumam gerar código de máquina equivalente (inclusive vetorizado).

| Abstração | Mecanismo |
|---|---|
| Genéricos | monomorfização: uma cópia por tipo |
| Iteradores/closures | inlining + eliminação de código morto |
| `Option<&T>` | otimização de nicho: mesmo tamanho de um ponteiro |

> [!warning] Mas não é mágica
> Em modo **debug** iteradores podem ser bem mais lentos. Faça medições em `--release`; veja [[Debug vs release]].

## Veja também

- [[Iteradores]]
- [[Closures]]
- [[Pipeline de compilação]]
