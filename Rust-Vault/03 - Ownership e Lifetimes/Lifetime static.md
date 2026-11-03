---
tags: [rust, ownership, lifetimes]
aliases: ["'static", "static lifetime"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Lifetimes]]", "[[Constantes e statics]]"]
---

# Lifetime static

`'static` indica que a referência **pode** viver durante todo o programa.

```rust
fn mensagem() -> &'static str {
    "literais de string vivem no binário"
}

fn main() {
    let s: &'static str = "oi";
    println!("{s} {}", mensagem());
}
```

> [!warning] Cuidado com a sugestão do compilador
> Mensagens de erro às vezes sugerem `'static`. Na maioria dos casos, isso é um sintoma de design errado; prefira corrigir o ownership.

## `T: 'static` como bound

Significa "T não contém referências não-estáticas" (pode ser um tipo que possui seus dados). É exigido, por exemplo, por `std::thread::spawn`.

```rust
use std::thread;

fn main() {
    let dados = vec![1, 2, 3];
    // move transfere o ownership para a thread: Vec<i32> satisfaz 'static
    let h = thread::spawn(move || {
        println!("{dados:?}");
    });
    h.join().unwrap();
}
```

## Veja também

- [[Lifetimes]]
- [[Constantes e statics]]
