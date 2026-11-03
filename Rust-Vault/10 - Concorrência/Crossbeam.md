---
tags: [rust, concorrencia, crates]
aliases: ["crossbeam", "crossbeam-channel", "ArrayQueue"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Canais mpsc]]", "[[Threads]]", "[[Rayon]]"]
---

# Crossbeam

O ecossistema **crossbeam** complementa a biblioteca padrão:

| Crate | Oferece |
|---|---|
| `crossbeam-channel` | canais **mpmc** (vários consumidores), `select!`, mais rápidos que `mpsc` |
| `crossbeam-utils` | `thread::scope`, `Backoff`, `CachePadded` |
| `crossbeam-queue` | filas lock-free (`ArrayQueue`, `SegQueue`) |
| `crossbeam-epoch` | reclamação de memória para estruturas lock-free |
| `crossbeam-deque` | deques *work-stealing* |

```toml
[dependencies]
crossbeam-channel = "0.5"
```

```rust
// requer crate: crossbeam-channel
use crossbeam_channel::{select, unbounded};
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = unbounded();
    let (tx_fim, rx_fim) = unbounded::<()>();

    // Dois consumidores compartilham o mesmo Receiver (mpmc)
    let rx2 = rx.clone();
    let c1 = thread::spawn(move || rx.iter().count());
    let c2 = thread::spawn(move || rx2.iter().count());

    for i in 0..10 {
        tx.send(i).unwrap();
    }
    drop(tx);
    println!("{}", c1.join().unwrap() + c2.join().unwrap()); // 10

    // select!: espera em vários canais
    thread::spawn(move || {
        thread::sleep(Duration::from_millis(10));
        tx_fim.send(()).unwrap();
    });
    select! {
        recv(rx_fim) -> _ => println!("fim recebido"),
        default(Duration::from_secs(1)) => println!("timeout"),
    }
}
```

> [!question] Verificar na documentação oficial
> Confirme a versão atual e os nomes dos crates em docs.rs/crossbeam antes de fixar no `Cargo.toml`.

> [!tip] Quando usar
> Se precisa de vários consumidores no mesmo canal, `select!` ou filas lock-free. Para o resto, `std::sync::mpsc` basta.

## Veja também

- [[Canais mpsc]]
- [[Threads]]
- [[Rayon]]
