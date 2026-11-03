---
tags: [rust, concorrencia]
aliases: ["RwLock", "lock", "MutexGuard", "poisoning", "Arc<Mutex<T>>"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Arc]]", "[[Concorrência sem medo]]", "[[Send e Sync]]", "[[Atômicos]]"]
---

# Mutex e RwLock

`Mutex<T>` garante **exclusão mútua**: só uma thread acessa o dado por vez. O dado fica **dentro** do mutex, então é impossível esquecer de travar.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let contador = Arc::new(Mutex::new(0));
    let mut handles = Vec::new();

    for _ in 0..8 {
        let c = Arc::clone(&contador);
        handles.push(thread::spawn(move || {
            for _ in 0..1000 {
                // lock() devolve um MutexGuard; ao sair do escopo, destrava (RAII)
                *c.lock().unwrap() += 1;
            }
        }));
    }
    for h in handles {
        h.join().unwrap();
    }
    println!("{}", *contador.lock().unwrap()); // 8000
}
```

## Envenenamento (*poisoning*)

Se uma thread entra em pânico segurando o lock, o mutex fica "envenenado" e `lock()` devolve `Err`. Para ignorar: `lock().unwrap_or_else(|e| e.into_inner())`.

## RwLock: vários leitores ou um escritor

```rust
use std::sync::RwLock;

fn main() {
    let l = RwLock::new(5);
    {
        let r1 = l.read().unwrap();
        let r2 = l.read().unwrap(); // vários leitores simultâneos
        println!("{} {}", *r1, *r2);
    } // leitores liberados
    {
        let mut w = l.write().unwrap(); // um único escritor
        *w += 1;
    }
    println!("{:?}", l);
}
```

## Mutex global

```rust
use std::sync::Mutex;

static LOG: Mutex<Vec<String>> = Mutex::new(Vec::new());

fn registra(msg: &str) {
    LOG.lock().unwrap().push(msg.to_string());
}

fn main() {
    registra("início");
    registra("fim");
    println!("{:?}", LOG.lock().unwrap());
}
```

> [!warning] Deadlock
> Duas threads que travam `A` e `B` em ordens opostas podem se bloquear para sempre. Defina uma **ordem global** de aquisição e mantenha as seções críticas curtas. Não segure o guard durante operações demoradas.

> [!tip] Reduza o escopo do lock
> Use blocos `{ let g = m.lock().unwrap(); ... }` ou copie o dado e solte o guard antes de trabalho caro.

## Veja também

- [[Arc]]
- [[Concorrência sem medo]]
- [[Send e Sync]]
- [[Atômicos]]
