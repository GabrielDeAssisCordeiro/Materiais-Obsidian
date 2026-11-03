---
tags: [rust, memoria]
aliases: ["Cell", "RefCell", "interior mutability", "mutabilidade interior"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Rc]]", "[[Weak e ciclos de referência]]", "[[Regras do borrow checker]]", "[[Escolhendo ponteiro inteligente]]"]
---

# Cell e RefCell

**Mutabilidade interior** permite alterar dados através de uma referência compartilhada `&T`. As regras de empréstimo continuam valendo, mas são verificadas **em tempo de execução** em vez de em compilação.

| Tipo | Como funciona | Verificação |
|---|---|---|
| `Cell<T>` | troca o valor inteiro (`get`/`set`, para `T: Copy`) | nenhuma necessária |
| `RefCell<T>` | `borrow()` e `borrow_mut()` | em execução; **panic** se violar |

```rust
use std::cell::{Cell, RefCell};

fn main() {
    let c = Cell::new(5);
    c.set(c.get() + 1); // mutação com &c, sem mut
    println!("{}", c.get());

    let r = RefCell::new(vec![1]);
    r.borrow_mut().push(2);
    println!("{:?}", r.borrow());

    // Violação detectada em execução (aqui sem panic, usando try_)
    let r2 = RefCell::new(1);
    let _g = r2.borrow_mut();
    println!("{}", r2.try_borrow_mut().is_err()); // true: já emprestado
}
```

## `Rc<RefCell<T>>`: vários donos que podem mutar

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Conta {
    saldo: i64,
}

fn main() {
    let conta = Rc::new(RefCell::new(Conta { saldo: 100 }));
    let a = Rc::clone(&conta);
    let b = Rc::clone(&conta);

    a.borrow_mut().saldo += 50;
    b.borrow_mut().saldo -= 30;
    println!("{:?}", conta.borrow());
}
```

> [!warning] `RefCell` é uma saída de emergência
> Dois `borrow_mut()` ativos ao mesmo tempo causam **panic** em execução. Prefira a estrutura de ownership normal; use `RefCell` quando o design exigir (grafos, observadores, mocks em testes).

> [!info] Thread-safe equivalente
> `Mutex<T>` e `RwLock<T>` fazem o papel de `RefCell` entre threads.

## Veja também

- [[Rc]]
- [[Weak e ciclos de referência]]
- [[Regras do borrow checker]]
- [[Escolhendo ponteiro inteligente]]
