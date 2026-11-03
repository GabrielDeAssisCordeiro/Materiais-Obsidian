---
tags: [rust, iteradores]
aliases: ["map", "filter", "enumerate", "zip", "take", "skip", "chain", "flat_map", "rev", "peekable"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Consumidores de iterador]]", "[[Closures]]"]
---

# Adaptadores de iterador

Adaptadores transformam um iterador em outro (preguiçosamente).

| Adaptador | Efeito |
|---|---|
| `map(f)` | transforma cada item |
| `filter(p)` | mantém itens que satisfazem `p` |
| `filter_map(f)` | `map` + descarta `None` |
| `enumerate()` | `(índice, item)` |
| `zip(outro)` | pares de dois iteradores |
| `chain(outro)` | concatena |
| `take(n)` / `skip(n)` | primeiros n / pula n |
| `take_while` / `skip_while` | enquanto o predicado valer |
| `step_by(n)` | de n em n |
| `rev()` | inverte (precisa ser de duas pontas) |
| `flat_map(f)` / `flatten()` | achata iteradores aninhados |
| `peekable()` | permite espiar o próximo item |
| `copied()` / `cloned()` | de `&T` para `T` |
| `inspect(f)` | espia (depuração) |

```rust
fn main() {
    let nums = vec![1, 2, 3, 4, 5, 6];

    let quadrados: Vec<i32> = nums.iter().map(|x| x * x).collect();
    let pares: Vec<i32> = nums.iter().copied().filter(|x| x % 2 == 0).collect();
    println!("{:?} {:?}", quadrados, pares);

    for (i, n) in nums.iter().enumerate().skip(1).step_by(2) {
        print!("{i}:{n} ");
    }
    println!();

    let nomes = ["Ana", "Bia"];
    let idades = [30, 25];
    let juntos: Vec<(&str, i32)> = nomes.iter().copied().zip(idades.iter().copied()).collect();
    println!("{:?}", juntos);

    let achatado: Vec<i32> = vec![vec![1, 2], vec![3], vec![]].into_iter().flatten().collect();
    println!("{:?}", achatado);

    // filter_map: converte e descarta falhas
    let validos: Vec<i32> = ["1", "x", "3"].iter().filter_map(|s| s.parse().ok()).collect();
    println!("{:?}", validos);

    // take_while
    let ate_cinco: Vec<i32> = (1..).take_while(|n| *n <= 5).collect();
    println!("{:?}", ate_cinco);

    // peekable: agrupa dígitos consecutivos
    let mut it = "123+45".chars().peekable();
    let mut numero = String::new();
    while let Some(c) = it.peek() {
        if c.is_ascii_digit() {
            numero.push(*c);
            it.next();
        } else {
            break;
        }
    }
    println!("{numero}");
}
```

## Veja também

- [[Iteradores]]
- [[Consumidores de iterador]]
- [[Closures]]
