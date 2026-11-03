---
tags: [rust, referencia, cheatsheet, iteradores]
aliases: ["Resumo de iteradores", "Iterator methods"]
tipo: cheatsheet
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Adaptadores de iterador]]", "[[Consumidores de iterador]]", "[[Closures]]", "[[Vec]]", "[[itertools]]"]
---

# Cheat sheet de iteradores

## Criar

| Forma | Itens |
|---|---|
| `v.iter()` | `&T` |
| `v.iter_mut()` | `&mut T` |
| `v.into_iter()` / `for x in v` | `T` (consome) |
| `a..b`, `a..=b` | números |
| `s.chars()` / `s.bytes()` / `s.lines()` / `s.split_whitespace()` | `char` / `u8` / `&str` |
| `std::iter::repeat(x).take(n)` | `x` repetido |
| `std::iter::once(x)`, `empty()` | um item / nenhum |
| `std::iter::from_fn(f)` / `successors(ini, f)` | geradores |

## Adaptadores (preguiçosos: só rodam quando consumidos)

| Método | O que faz |
|---|---|
| `map(f)` | transforma cada item |
| `filter(p)` | mantém os que satisfazem `p` |
| `filter_map(f)` | `map` + descarta `None` |
| `flat_map(f)` / `flatten()` | achata iteradores aninhados |
| `enumerate()` | `(índice, item)` |
| `zip(outro)` | pares |
| `chain(outro)` | concatena |
| `take(n)` / `skip(n)` | primeiros n / pula n |
| `take_while(p)` / `skip_while(p)` | enquanto `p` |
| `step_by(n)` | de n em n |
| `rev()` | invertido (iteradores de duas pontas) |
| `peekable()` | permite `peek()` |
| `windows(n)` / `chunks(n)` | (em fatias) janelas / blocos |
| `inspect(f)` | espia, para depuração |
| `cloned()` / `copied()` | `&T` → `T` |

## Consumidores

| Método | Resultado |
|---|---|
| `collect::<C>()` | `Vec`, `HashMap`, `String`, `Result<Vec<_>, _>`... |
| `sum()` / `product()` | soma / produto |
| `count()` | quantidade |
| `min()` / `max()` / `min_by_key(f)` / `max_by(f)` | extremos |
| `fold(init, f)` / `reduce(f)` | acumulação |
| `any(p)` / `all(p)` | testes |
| `find(p)` / `position(p)` | primeiro item / índice |
| `last()` / `nth(n)` | itens específicos |
| `for_each(f)` | efeito colateral |
| `partition(p)` | divide em dois grupos |
| `unzip()` | pares → duas coleções |

## Exemplos prontos

```rust
use std::collections::HashMap;

fn main() {
    let palavras = ["rust", "é", "rápido", "e", "seguro"];

    // contar frequência de letras iniciais
    let mut freq: HashMap<char, usize> = HashMap::new();
    for p in palavras {
        if let Some(c) = p.chars().next() {
            *freq.entry(c).or_default() += 1;
        }
    }

    // transformar, filtrar e juntar em String
    let frase: String = palavras
        .iter()
        .filter(|p| p.len() > 1)
        .map(|p| p.to_uppercase())
        .collect::<Vec<_>>()
        .join(" ");

    // collect em Result: falha no primeiro erro
    let numeros: Result<Vec<i32>, _> = "1,2,x".split(',').map(str::parse::<i32>).collect();

    // fold e partition
    let soma_quadrados = (1..=4).fold(0, |acc, n| acc + n * n);
    let (pares, impares): (Vec<i32>, Vec<i32>) = (1..=6).partition(|n| n % 2 == 0);

    // zip + unzip, enumerate, windows
    let (a, b): (Vec<i32>, Vec<char>) = [(1, 'a'), (2, 'b')].into_iter().unzip();
    let subiu = [1, 3, 2, 5].windows(2).filter(|w| w[1] > w[0]).count();

    println!("{} {frase}", freq.len());
    println!("{:?}", numeros.is_err());
    println!("{soma_quadrados} {pares:?} {impares:?} {a:?} {b:?} {subiu}");
}
```

> [!tip] Regra prática
> Se você escreveu um `for` que só empilha em um `Vec` ou acumula um valor, provavelmente existe um adaptador (`map`, `filter`, `fold`) mais direto. Mas legibilidade vem primeiro: um `for` simples também é idiomático.

## Veja também

- [[Iteradores]]
- [[Adaptadores de iterador]]
- [[Consumidores de iterador]]
- [[Closures]]
- [[Vec]]
- [[itertools]]
