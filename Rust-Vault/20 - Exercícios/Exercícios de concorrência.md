---
tags: [rust, exercicios, concorrencia]
aliases: []
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Threads]]", "[[Canais mpsc]]", "[[Mutex e RwLock]]", "[[Atômicos]]", "[[Exercícios de erros, traits e genéricos]]", "[[Flashcards de fundamentos e ownership]]"]
---

# Exercícios de concorrência

## Exercícios

1. **Soma paralela.** `soma_paralela(&[u64], partes)` divide o vetor em `partes` blocos e soma cada um em uma thread, usando `std::thread::scope` (sem `Arc`, pois as threads emprestam o vetor).
2. **Contador compartilhado.** 8 threads incrementam 1000 vezes um `Arc<Mutex<u32>>`. O resultado final deve ser 8000.
3. **Canal.** 4 threads produtoras enviam 5 números cada por um `mpsc::channel`; a thread principal soma tudo. *Dica:* lembre de `drop(tx)` do transmissor original.
4. **Atômico.** Refaça o contador com `AtomicUsize` em um `static`, sem `Mutex`.

Notas relacionadas: [[Threads]], [[Canais mpsc]], [[Mutex e RwLock]], [[Atômicos]], [[Send e Sync]], [[Arc]], [[Concorrência sem medo]].

> [!tip] Desafio
> Meça a soma paralela contra a sequencial em `--release` para vetores de 100 milhões de elementos. Quando a paralela compensa? Compare com [[Rayon]].

## Gabarito

<details>
<summary>Solução 1</summary>

```rust
use std::thread;

fn soma_paralela(v: &[u64], partes: usize) -> u64 {
    let tam = v.len().div_ceil(partes).max(1);
    // `scope` garante que as threads terminam antes de `v` deixar de existir,
    // então elas podem emprestar `v` sem Arc nem 'static.
    thread::scope(|s| {
        let handles: Vec<_> = v
            .chunks(tam)
            .map(|bloco| s.spawn(move || bloco.iter().sum::<u64>()))
            .collect();
        handles.into_iter().map(|h| h.join().unwrap()).sum::<u64>()
    })
}

fn main() {
    let v: Vec<u64> = (1..=1_000).collect();
    assert_eq!(soma_paralela(&v, 4), 500_500);
    assert_eq!(soma_paralela(&v, 7), 500_500);
    assert_eq!(soma_paralela(&[], 4), 0);
    println!("{}", soma_paralela(&v, 4));
}
```

</details>
<details>
<summary>Solução 2</summary>

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let contador = Arc::new(Mutex::new(0u32));
    let mut handles = Vec::new();

    for _ in 0..8 {
        let contador = Arc::clone(&contador);
        handles.push(thread::spawn(move || {
            for _ in 0..1000 {
                *contador.lock().unwrap() += 1;
            }
        }));
    }
    for h in handles {
        h.join().unwrap();
    }

    assert_eq!(*contador.lock().unwrap(), 8000);
    println!("total = {}", *contador.lock().unwrap());
}
```

</details>
<details>
<summary>Solução 3</summary>

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel::<u32>();
    let mut handles = Vec::new();

    for id in 0..4u32 {
        let tx = tx.clone();
        handles.push(thread::spawn(move || {
            for i in 1..=5 {
                tx.send(id * 10 + i).unwrap();
            }
        }));
    }
    // Sem este drop, `rx.iter()` nunca terminaria: o tx original ainda existiria.
    drop(tx);

    let total: u32 = rx.iter().sum();
    for h in handles {
        h.join().unwrap();
    }

    // cada id soma 50*id + 15; ids 0..=3: 50*6 + 60 = 360
    assert_eq!(total, 360);
    println!("total = {total}");
}
```

</details>
<details>
<summary>Solução 4</summary>

```rust
use std::sync::atomic::{AtomicUsize, Ordering};
use std::thread;

static CONTADOR: AtomicUsize = AtomicUsize::new(0);

fn main() {
    thread::scope(|s| {
        for _ in 0..4 {
            s.spawn(|| {
                for _ in 0..500 {
                    // Relaxed basta: só precisamos da atomicidade do incremento
                    CONTADOR.fetch_add(1, Ordering::Relaxed);
                }
            });
        }
    });
    assert_eq!(CONTADOR.load(Ordering::SeqCst), 2000);
    println!("total = {}", CONTADOR.load(Ordering::SeqCst));
}
```

</details>

## Veja também

- [[Threads]]
- [[Canais mpsc]]
- [[Mutex e RwLock]]
- [[Atômicos]]
- [[Exercícios de erros, traits e genéricos]]
- [[Flashcards de fundamentos e ownership]]
