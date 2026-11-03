---
tags: [rust, memoria, ponteiros, rc]
aliases: ["Rc<T>", "ownership compartilhado"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Arc]]", "[[Cell e RefCell]]", "[[Weak e ciclos de referência]]", "[[Escolhendo ponteiro inteligente]]"]
---

# Rc

`Rc<T>` (*Reference Counted*) permite **vários donos** do mesmo dado em **uma única thread**. O dado é liberado quando a contagem chega a zero.

```rust
use std::rc::Rc;

fn main() {
    let a = Rc::new(String::from("compartilhado"));
    println!("contagem = {}", Rc::strong_count(&a)); // 1

    let b = Rc::clone(&a); // incrementa a contagem; não copia o dado
    {
        let _c = Rc::clone(&a);
        println!("contagem = {}", Rc::strong_count(&a)); // 3
    } // _c sai de escopo: contagem volta a 2
    println!("contagem = {}", Rc::strong_count(&a));
    println!("{b}");
}
```

## Lista com cauda compartilhada

```rust
use std::rc::Rc;

enum Lista {
    Cons(i32, Rc<Lista>),
    Nil,
}

use Lista::{Cons, Nil};

fn tamanho(l: &Lista) -> usize {
    match l {
        Cons(_, resto) => 1 + tamanho(resto),
        Nil => 0,
    }
}

fn main() {
    let cauda = Rc::new(Cons(10, Rc::new(Cons(20, Rc::new(Nil)))));
    let a = Cons(1, Rc::clone(&cauda));
    let b = Cons(2, Rc::clone(&cauda)); // duas listas compartilham a mesma cauda
    println!("{} {} (cauda com {} donos)", tamanho(&a), tamanho(&b), Rc::strong_count(&cauda));
}
```

> [!warning] `Rc` é somente leitura e não é thread-safe
> `Rc<T>` dá apenas `&T`. Para mutação, combine com [[Cell e RefCell]]. Para threads, use [[Arc]]; o compilador impede enviar `Rc` entre threads:

```rust
// ❌ NÃO COMPILA: Rc não implementa Send
use std::rc::Rc;
use std::thread;

fn main() {
    let r = Rc::new(1);
    thread::spawn(move || println!("{r}")).join().unwrap();
}
```

```text
error[E0277]: `Rc<i32>` cannot be sent between threads safely
```

## Veja também

- [[Arc]]
- [[Cell e RefCell]]
- [[Weak e ciclos de referência]]
- [[Escolhendo ponteiro inteligente]]
