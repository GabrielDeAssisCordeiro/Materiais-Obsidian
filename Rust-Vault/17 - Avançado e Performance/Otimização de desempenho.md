---
tags: [rust, performance]
aliases: ["alocações", "cache", "with_capacity"]
tipo: pratica
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Perfilamento]]", "[[Zero-cost abstractions]]", "[[Vec]]", "[[Iteradores]]", "[[SIMD e vetorização]]", "[[Rayon]]"]
---

# Otimização de desempenho

Depois de [[Perfilamento]], as vitórias mais comuns são **algorítmicas** e de **alocação**, não truques de baixo nível.

## Lista de técnicas (da mais para a menos impactante)

1. **Algoritmo e estrutura de dados certos** — veja [[Escolhendo uma coleção]].
2. **Evitar alocações** em laços quentes: reutilize buffers, `Vec::with_capacity`, `String::clear`.
3. **Evitar `clone`** desnecessário; use referências e `Cow`.
4. **Iteradores** em vez de índices — o compilador elimina checagens de limites.
5. **Localidade de cache**: `Vec<T>` contíguo supera listas encadeadas; struct-of-arrays em dados numéricos.
6. **Paralelismo**: [[Rayon]].
7. **Flags de release**: veja [[Release profile LTO e codegen]].

## Exemplo: reutilizando alocação

```rust
use std::time::Instant;

fn com_alocacao(n: usize) -> usize {
    let mut total = 0;
    for i in 0..n {
        let s = format!("item-{i}"); // aloca a cada iteração
        total += s.len();
    }
    total
}

fn reutilizando(n: usize) -> usize {
    use std::fmt::Write;
    let mut total = 0;
    let mut s = String::with_capacity(32);
    for i in 0..n {
        s.clear();
        write!(s, "item-{i}").unwrap(); // reaproveita o mesmo buffer
        total += s.len();
    }
    total
}

fn main() {
    let n = 2_000_000;
    let t = Instant::now();
    let a = com_alocacao(n);
    println!("com alocação: {a} em {:?}", t.elapsed());

    let t = Instant::now();
    let b = reutilizando(n);
    println!("reutilizando: {b} em {:?}", t.elapsed());
    assert_eq!(a, b);
}
```

## `Cow`: clonar só quando preciso

```rust
use std::borrow::Cow;

fn normaliza(s: &str) -> Cow<'_, str> {
    if s.contains(' ') {
        Cow::Owned(s.replace(' ', "_")) // só aloca se necessário
    } else {
        Cow::Borrowed(s)
    }
}

fn main() {
    println!("{}", normaliza("sem_espaco"));
    println!("{}", normaliza("com espaco"));
}
```

## Evitar dispatch dinâmico no caminho quente

| Genéricos (`impl Trait`) | `dyn Trait` |
|---|---|
| monomorfização, inlining | indireção via vtable |
| binário maior | binário menor |
| mais rápido | mais flexível |

> [!tip] Mantenha a legibilidade
> Otimize só o que o perfil mostrou ser gargalo e mantenha um benchmark que comprove o ganho.

## Veja também

- [[Perfilamento]]
- [[Zero-cost abstractions]]
- [[Vec]]
- [[Iteradores]]
- [[SIMD e vetorização]]
- [[Rayon]]
