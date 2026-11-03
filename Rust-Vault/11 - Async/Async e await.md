---
tags: [rust, async]
aliases: ["async/await", "async fn", "programação assíncrona"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Future e Poll]]", "[[Executores e runtimes]]", "[[Async vs threads]]", "[[Armadilhas do async]]"]
---

# Async e await

**Programação assíncrona** permite que muitas tarefas de E/S progridam em poucas threads: quando uma tarefa precisa esperar (rede, disco, timer), ela **cede** a vez em vez de bloquear a thread.

## Os três ingredientes

| Peça | Papel |
|---|---|
| `async fn` / `async { }` | cria um **Future** (uma máquina de estados) |
| `.await` | suspende até o Future terminar, cedendo a thread |
| **Executor** (runtime) | chama `poll` nos Futures até concluírem; ex.: Tokio |

```rust
use std::future::Future;
use std::pin::pin;
use std::task::{Context, Poll, Waker};

// Mini executor didático: roda um Future até terminar (sem runtime externo)
fn block_on<F: Future>(fut: F) -> F::Output {
    let mut fut = pin!(fut);
    let mut cx = Context::from_waker(Waker::noop());
    loop {
        if let Poll::Ready(v) = fut.as_mut().poll(&mut cx) {
            return v;
        }
    }
}

async fn soma(a: i32, b: i32) -> i32 {
    a + b
}

async fn principal() -> i32 {
    let x = soma(1, 2).await;   // espera o outro future
    let y = soma(x, 10).await;
    y * 2
}

fn main() {
    // Chamar uma async fn NÃO executa nada: só cria o Future (preguiçoso)
    let fut = principal();
    println!("{}", block_on(fut)); // 26
}
```

> [!info] Futures são preguiçosos
> Um `Future` só progride quando é *polled*. `let f = soma(1, 2);` não calcula nada até alguém chamar `.await` ou o executor fazer `poll`.

## Novidades estáveis úteis

- `async fn` em **traits** (estável desde o Rust 1.75).
- **Closures assíncronas** (`async || { ... }`), estáveis desde o Rust 1.85.

```rust
trait Fonte {
    async fn busca(&self, id: u32) -> String;
}

struct Fixa;

impl Fonte for Fixa {
    async fn busca(&self, id: u32) -> String {
        format!("item {id}")
    }
}

fn main() {
    let _ = Fixa;
}
```

> [!question] Verificar na documentação oficial
> Confirme em release notes as versões em que `async fn` em traits e closures assíncronas foram estabilizadas, e as restrições para uso com `dyn Trait`.

> [!tip] Onde `.await` é permitido
> Apenas dentro de `async fn`/blocos `async`. Em `main`, use um runtime: `#[tokio::main]`; veja [[Tokio]].

## Veja também

- [[Future e Poll]]
- [[Executores e runtimes]]
- [[Async vs threads]]
- [[Armadilhas do async]]
