---
tags: [rust, concorrencia, canais]
aliases: ["mpsc", "channel", "Sender", "Receiver", "passagem de mensagens"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Concorrência sem medo]]", "[[Threads]]", "[[Crossbeam]]", "[[Canais assíncronos]]"]
---

# Canais mpsc

`std::sync::mpsc` = *multiple producer, single consumer*. Um canal tem um `Sender` (clonável) e um `Receiver`.

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();
    let tx2 = tx.clone(); // segundo produtor

    thread::spawn(move || {
        for i in 0..3 {
            tx.send(format!("a{i}")).unwrap();
        }
    });
    thread::spawn(move || {
        for i in 0..3 {
            tx2.send(format!("b{i}")).unwrap();
        }
    });

    // rx.iter() termina quando TODOS os Senders forem descartados
    let mut recebidas: Vec<String> = rx.iter().collect();
    recebidas.sort(); // a ordem de chegada varia
    println!("{:?}", recebidas);
}
```

Enviar um valor **move** o ownership para o receptor:

```rust
// ❌ NÃO COMPILA: s foi movida ao enviar
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
    let s = String::from("oi");
    tx.send(s).unwrap();
    println!("{s}");
    drop(rx);
}
```

```text
error[E0382]: borrow of moved value: `s`
```

## Variantes

| API | Comportamento |
|---|---|
| `channel()` | fila **ilimitada**; `send` nunca bloqueia |
| `sync_channel(n)` | fila **limitada**; `send` bloqueia quando cheia (contrapressão) |
| `recv()` | bloqueia até chegar valor |
| `try_recv()` | não bloqueia; `Err(Empty)` se não há valor |
| `recv_timeout(d)` | bloqueia por no máximo `d` |

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::sync_channel::<u32>(2);

    let produtor = thread::spawn(move || {
        for i in 0..5 {
            tx.send(i).unwrap(); // bloqueia se houver 2 itens pendentes
        }
    });

    while let Ok(v) = rx.recv_timeout(Duration::from_secs(1)) {
        println!("recebi {v}");
    }
    produtor.join().unwrap();
}
```

> [!tip] Encerramento limpo
> Quando todos os `Sender` são descartados, `recv` devolve `Err` e o laço do consumidor termina naturalmente.

## Veja também

- [[Concorrência sem medo]]
- [[Threads]]
- [[Crossbeam]]
- [[Canais assíncronos]]
