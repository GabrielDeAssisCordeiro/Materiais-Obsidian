---
tags: [rust, closures, funcoes]
aliases: ["closure", "lambda", "função anônima"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Fn, FnMut e FnOnce]]", "[[Adaptadores de iterador]]", "[[Funções]]"]
---

# Closures

Uma **closure** é uma função anônima que pode **capturar** variáveis do ambiente.

```rust
fn main() {
    let fator = 3;
    let triplica = |x: i32| x * fator;       // captura fator por referência
    let soma = |a: i32, b: i32| -> i32 { a + b };
    println!("{} {}", triplica(5), soma(1, 2));

    // Captura mutável
    let mut contador = 0;
    let mut incrementa = || contador += 1;
    incrementa();
    incrementa();
    println!("{contador}");

    // move: a closure toma posse do que usa
    let nome = String::from("Ana");
    let saudacao = move || println!("Olá, {nome}");
    saudacao();
    // println!("{nome}"); // erro: nome foi movido para a closure
}
```

## Quando `move` é obrigatório

```rust
// ❌ NÃO COMPILA: a thread pode viver mais que v
use std::thread;

fn main() {
    let v = vec![1, 2, 3];
    let h = thread::spawn(|| println!("{v:?}"));
    h.join().unwrap();
}
```

```text
error[E0373]: closure may outlive the current function, but it borrows `v`
help: to force the closure to take ownership of `v`, use the `move` keyword
```

**Correção:** `thread::spawn(move || ...)`.

> [!info] Tipos
> Cada closure tem um **tipo único e anônimo**. Para recebê-la ou devolvê-la use genéricos (`F: Fn(...)`), `impl Fn` ou `Box<dyn Fn>`; veja [[Fn, FnMut e FnOnce]].

## Veja também

- [[Fn, FnMut e FnOnce]]
- [[Adaptadores de iterador]]
- [[Funções]]
