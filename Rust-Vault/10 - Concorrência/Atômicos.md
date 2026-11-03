---
tags: [rust, concorrencia]
aliases: ["AtomicUsize", "AtomicBool", "Ordering"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Mutex e RwLock]]", "[[Concorrência sem medo]]", "[[Constantes e statics]]"]
---

# Atômicos

Tipos **atômicos** (`std::sync::atomic`) permitem operações indivisíveis em inteiros e booleanos **sem lock**. São a base de contadores, flags e estruturas lock-free.

```rust
use std::sync::atomic::{AtomicBool, AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;

static CONTADOR: AtomicUsize = AtomicUsize::new(0);

fn main() {
    let mut handles = Vec::new();
    for _ in 0..4 {
        handles.push(thread::spawn(|| {
            for _ in 0..1000 {
                CONTADOR.fetch_add(1, Ordering::Relaxed);
            }
        }));
    }
    for h in handles {
        h.join().unwrap();
    }
    println!("{}", CONTADOR.load(Ordering::SeqCst)); // 4000

    // Flag de parada
    let parar = Arc::new(AtomicBool::new(false));
    let p = Arc::clone(&parar);
    let h = thread::spawn(move || {
        let mut voltas = 0u64;
        while !p.load(Ordering::Acquire) {
            voltas += 1;
            thread::yield_now();
        }
        voltas
    });
    parar.store(true, Ordering::Release);
    let _ = h.join().unwrap();

    // compare_exchange: atualiza só se o valor atual for o esperado
    let a = AtomicUsize::new(5);
    let r = a.compare_exchange(5, 10, Ordering::SeqCst, Ordering::SeqCst);
    println!("{:?} {}", r, a.load(Ordering::SeqCst)); // Ok(5) 10
}
```

## Ordenação de memória

| `Ordering` | Garantia | Quando usar |
|---|---|---|
| `Relaxed` | só a atomicidade; sem ordem em relação a outros acessos | contadores independentes |
| `Acquire` | leituras/escritas seguintes não sobem para antes | ler uma flag que "publica" dados |
| `Release` | anteriores não descem para depois | escrever a flag que publica dados |
| `AcqRel` | Acquire + Release | operações de leitura-modificação-escrita |
| `SeqCst` | ordem total global | padrão seguro quando em dúvida |

> [!warning] Cuidado
> Escolher `Ordering` errado gera bugs raros e difíceis de reproduzir. Se não tem certeza, use `SeqCst`. Para dados compostos, prefira `Mutex`.

> [!info] Globais sem `unsafe`
> Atômicos e `Mutex` em `static` substituem `static mut`, que exige `unsafe`; veja [[Constantes e statics]].

## Veja também

- [[Mutex e RwLock]]
- [[Concorrência sem medo]]
- [[Constantes e statics]]
