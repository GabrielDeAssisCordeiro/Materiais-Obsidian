---
tags: [rust, async]
aliases: ["Stream", "StreamExt", "iterador assíncrono", "futures"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Iteradores]]", "[[Tokio]]", "[[Async e await]]"]
---

# Streams

Um **Stream** é o análogo assíncrono de um iterador: produz vários valores ao longo do tempo (`poll_next`).

| | Iterator | Stream |
|---|---|---|
| Próximo item | `next()` → `Option<T>` | `next().await` → `Option<T>` |
| Esperas | bloqueia a thread | cede a thread |
| Fonte | `std` | `futures` / `tokio-stream` |

> [!info] Estado na biblioteca padrão
> A trait `Stream` (também chamada de *async iterator*) ainda não faz parte da `std` estável; é fornecida pelo crate `futures`.
> [!question] Verificar na documentação oficial
> Confira o estado atual de `AsyncIterator`/`Stream` na biblioteca padrão antes de depender apenas da `std`.

```rust
// requer crate: futures
use futures::stream::{self, StreamExt};

#[tokio::main]
async fn main() {
    let mut s = stream::iter(1..=6)
        .map(|x| x * 2)
        .filter(|x| futures::future::ready(*x > 4));

    while let Some(v) = s.next().await {
        println!("{v}");
    }

    // Processar com concorrência limitada
    let somas: Vec<i32> = stream::iter(1..=5)
        .map(|n| async move { n * n })
        .buffer_unordered(3) // até 3 futures ao mesmo tempo
        .collect()
        .await;
    println!("{}", somas.len());
}
```

> [!tip] Casos típicos
> Leitura de linhas de um socket, eventos de WebSocket, paginação de APIs e processamento em lote com limite de concorrência.

## Veja também

- [[Iteradores]]
- [[Tokio]]
- [[Async e await]]
