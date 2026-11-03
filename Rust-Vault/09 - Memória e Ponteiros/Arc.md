---
tags: [rust, memoria, ponteiros, concorrencia]
aliases: ["Arc<T>", "Rc atômico", "ownership compartilhado entre threads"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Rc]]", "[[Escolhendo ponteiro inteligente]]", "[[Cell e RefCell]]"]
---

# Arc

`Arc<T>` (*Atomically Reference Counted*) é o `Rc` **seguro entre threads**: a contagem usa operações atômicas (um pouco mais caro).

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let dados = Arc::new(vec![1, 2, 3]);
    let mut handles = Vec::new();

    for i in 0..3 {
        let d = Arc::clone(&dados); // cada thread recebe seu próprio Arc
        handles.push(thread::spawn(move || d[i] * 2));
    }

    for h in handles {
        println!("{}", h.join().unwrap());
    }
    println!("donos restantes: {}", Arc::strong_count(&dados));
}
```

- `Arc<T>` só dá acesso **imutável** a `T`. Para mutar compartilhado entre threads, combine `Arc<Mutex<T>>` ou `Arc<RwLock<T>>`.
- `Arc<T>` é `Send + Sync` **se** `T: Send + Sync`.

> [!tip] Rc ou Arc?
> Use `Rc` em código de thread única e `Arc` quando o dado cruzar threads. O compilador avisa se você errar a escolha.

## Veja também

- [[Rc]]
- [[Escolhendo ponteiro inteligente]]
- [[Cell e RefCell]]
