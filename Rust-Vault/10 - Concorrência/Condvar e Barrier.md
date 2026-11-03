---
tags: [rust, concorrencia]
aliases: ["Condvar", "Barrier", "variável de condição"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Mutex e RwLock]]", "[[Threads]]"]
---

# Condvar e Barrier

## Condvar

Permite que uma thread **durma** até que outra sinalize que uma condição mudou (sempre usada junto com um `Mutex`).

```rust
use std::sync::{Arc, Condvar, Mutex};
use std::thread;

fn main() {
    let par = Arc::new((Mutex::new(false), Condvar::new()));
    let par2 = Arc::clone(&par);

    thread::spawn(move || {
        let (m, cv) = &*par2;
        *m.lock().unwrap() = true; // muda a condição
        cv.notify_one();           // acorda quem espera
    });

    let (m, cv) = &*par;
    let mut pronto = m.lock().unwrap();
    // O laço protege contra "despertares espúrios"
    while !*pronto {
        pronto = cv.wait(pronto).unwrap(); // libera o lock enquanto dorme
    }
    println!("condição satisfeita");
}
```

## Barrier

Faz várias threads **esperarem umas pelas outras** em um ponto de encontro.

```rust
use std::sync::{Arc, Barrier};
use std::thread;

fn main() {
    let barreira = Arc::new(Barrier::new(3));
    let mut handles = Vec::new();

    for i in 0..3 {
        let b = Arc::clone(&barreira);
        handles.push(thread::spawn(move || {
            println!("thread {i}: antes da barreira");
            b.wait(); // ninguém passa até as 3 chegarem
            println!("thread {i}: depois da barreira");
        }));
    }
    for h in handles {
        h.join().unwrap();
    }
}
```

> [!tip] Alternativas
> Para sincronizar por mensagens, [[Canais mpsc]] costumam ser mais simples. `std::sync::Once`/`OnceLock` cobrem inicialização única.

## Veja também

- [[Mutex e RwLock]]
- [[Threads]]
