---
tags: [rust, async, erros, boas-praticas]
aliases: ["async pitfalls", "bloqueio no runtime", "Mutex através de await", "cancel safety"]
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[join! e select!]]", "[[Async vs threads]]", "[[Send e Sync]]"]
---

# Armadilhas do async

| Armadilha | Sintoma | Correção |
|---|---|---|
| **Esquecer `.await`** | nada executa; aviso `unused_must_use` | sempre `await` (ou `spawn`) |
| **Bloquear o runtime** (`std::thread::sleep`, leitura de arquivo síncrona, CPU pesada) | outras tarefas travam | `tokio::time::sleep`, `spawn_blocking`, `tokio::fs` |
| **Segurar `std::sync::MutexGuard` através de `.await`** | erro "future is not `Send`" ou deadlock | soltar o guard antes do `await` ou usar `tokio::sync::Mutex` |
| **Cancelamento** (futures descartados em `select!`/timeout) | dados perdidos pela metade | operações cancel-safe; documentar |
| **Recursão async** | erro de tamanho infinito | `Box::pin(async move { ... })` |
| **Tarefas órfãs** | trabalho continua sem dono | guardar `JoinHandle`/`JoinSet`, usar sinais de parada |
| **Futures enormes na pilha** | estouro ou lentidão | `Box::pin`, dividir em funções menores |
| **Misturar runtimes** | panics "no reactor running" | um runtime por programa |

## Exemplo: guard através de await

```rust
use std::sync::Mutex;

async fn passo() {}

// OK: o guard é solto ANTES do await
async fn bom(m: &Mutex<i32>) {
    {
        let mut g = m.lock().unwrap();
        *g += 1;
    } // guard liberado aqui
    passo().await;
}

fn main() {
    let m = Mutex::new(0);
    let _f = bom(&m);
}
```

```rust
// requer crate: tokio
// Problema: std MutexGuard não é Send; manter através de await impede tokio::spawn
use std::sync::Mutex;
use std::sync::Arc;

async fn ruim(m: Arc<Mutex<i32>>) {
    let mut g = m.lock().unwrap();
    *g += 1;
    tokio::time::sleep(std::time::Duration::from_millis(1)).await; // g ainda vivo aqui
}

#[tokio::main]
async fn main() {
    let m = Arc::new(Mutex::new(0));
    // tokio::spawn(ruim(m)); // erro: o future não é Send
    let _ = ruim(m).await;
}
```

## Recursão

```rust
use std::future::Future;
use std::pin::{pin, Pin};
use std::task::{Context, Poll, Waker};

fn fatorial(n: u64) -> Pin<Box<dyn Future<Output = u64>>> {
    Box::pin(async move {
        if n <= 1 { 1 } else { n * fatorial(n - 1).await }
    })
}

fn block_on<F: Future>(fut: F) -> F::Output {
    let mut fut = pin!(fut);
    let mut cx = Context::from_waker(Waker::noop());
    loop {
        if let Poll::Ready(v) = fut.as_mut().poll(&mut cx) {
            return v;
        }
    }
}

fn main() {
    println!("{}", block_on(fatorial(10))); // 3628800
}
```

## Veja também

- [[Tokio]]
- [[join! e select!]]
- [[Async vs threads]]
- [[Send e Sync]]
