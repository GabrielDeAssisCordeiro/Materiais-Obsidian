---
tags: [rust, enums, erros, option, result]
aliases: ["Option", "Result", "Some", "None", "Ok", "Err"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Enums]]", "[[Combinadores de Option e Result]]", "[[if let e let else]]", "[[match]]"]
---

# Option e Result

Rust não tem `null` nem exceções. Usa dois enums da biblioteca padrão:

```rust
// trecho: definições simplificadas (já existem na biblioteca padrão)
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

## Option: "talvez haja um valor"

```rust
fn divide(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 { None } else { Some(a / b) }
}

fn main() {
    match divide(10.0, 2.0) {
        Some(v) => println!("resultado {v}"),
        None => println!("divisão por zero"),
    }

    let v = vec![1, 2, 3];
    println!("{:?} {:?}", v.first(), v.get(9));
}
```

## Result: "deu certo ou deu erro"

```rust
use std::num::ParseIntError;

fn dobra(texto: &str) -> Result<i32, ParseIntError> {
    let n = texto.trim().parse::<i32>()?; // ? propaga o erro
    Ok(n * 2)
}

fn main() {
    println!("{:?}", dobra("21"));
    match dobra("x") {
        Ok(v) => println!("{v}"),
        Err(e) => println!("erro: {e}"),
    }
}
```

| | `Option<T>` | `Result<T, E>` |
|---|---|---|
| Quando usar | ausência é normal | falha com informação |
| "Sucesso" | `Some(t)` | `Ok(t)` |
| "Ausência/falha" | `None` | `Err(e)` |

> [!warning] `unwrap` e `expect`
> `unwrap()` causa *panic* em `None`/`Err`. Aceitável em protótipos e testes; em código real prefira `match`, `?` ou combinadores. Veja [[Operador de interrogação]] e [[Combinadores de Option e Result]].

## Exercício

Escreva `fn raiz(x: f64) -> Result<f64, String>` que devolve erro para números negativos.

## Veja também

- [[Enums]]
- [[Combinadores de Option e Result]]
- [[if let e let else]]
- [[match]]
