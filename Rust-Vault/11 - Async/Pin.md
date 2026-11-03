---
tags: [rust, async]
aliases: ["Pin", "Unpin", "pin!", "Box::pin", "autorreferência"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Future e Poll]]", "[[Async e await]]", "[[Box]]"]
---

# Pin

**`Pin<P>`** garante que o valor apontado **não será movido na memória**. Isso é necessário porque a máquina de estados de uma `async fn` pode conter referências para si mesma (campos que apontam para outros campos); mover o Future invalidaria essas referências.

- `Unpin` é uma auto trait: tipos `Unpin` (quase todos, como `i32`, `String`) podem ser movidos mesmo "fixados". Futures gerados por `async` **não** são `Unpin`.
- Para chamar `poll`, é preciso ter um `Pin<&mut Self>`.

## Como fixar um valor

```rust
use std::future::Future;
use std::pin::{pin, Pin};
use std::task::{Context, Poll, Waker};

fn block_on<F: Future>(fut: F) -> F::Output {
    // pin! fixa na pilha, sem alocar
    let mut fut = pin!(fut);
    let mut cx = Context::from_waker(Waker::noop());
    loop {
        if let Poll::Ready(v) = fut.as_mut().poll(&mut cx) {
            return v;
        }
    }
}

// Box::pin fixa na heap: útil para guardar futures de tipos diferentes
fn tarefas() -> Vec<Pin<Box<dyn Future<Output = i32>>>> {
    vec![
        Box::pin(async { 1 }),
        Box::pin(async { 2 + 3 }),
    ]
}

fn main() {
    let total: i32 = tarefas().into_iter().map(block_on).sum();
    println!("{total}"); // 6
}
```

| Método | Onde fica | Quando usar |
|---|---|---|
| `std::pin::pin!(x)` | pilha | executar/consultar localmente |
| `Box::pin(x)` | heap | coleções, recursão, trait objects |

> [!tip] Na prática
> No dia a dia você raramente escreve `Pin` à mão: `.await`, `tokio::spawn` e `select!` cuidam disso. Ele aparece quando você implementa `Future` ou guarda futures em estruturas.

## Veja também

- [[Future e Poll]]
- [[Async e await]]
- [[Box]]
