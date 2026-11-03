---
tags: [rust, async, canais, tokio]
aliases: ["tokio::sync::mpsc", "oneshot", "broadcast", "watch"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[Canais mpsc]]", "[[join! e select!]]"]
---

# Canais assíncronos

O módulo `tokio::sync` oferece canais cujos `send`/`recv` são `async` (não bloqueiam a thread).

| Canal | Padrão | Uso |
|---|---|---|
| `mpsc` | N produtores → 1 consumidor | filas de trabalho, atores |
| `oneshot` | 1 valor, 1 vez | resposta de uma requisição |
| `broadcast` | N produtores → N consumidores (todos recebem tudo) | eventos, chat |
| `watch` | último valor; consumidores veem o mais recente | configuração, estado |

```rust
// requer crate: tokio
use tokio::sync::{mpsc, oneshot};

// Padrão "ator": uma tarefa dona do estado; comandos chegam por mpsc
enum Comando {
    Soma(i32),
    Consulta(oneshot::Sender<i32>),
}

#[tokio::main]
async fn main() {
    let (tx, mut rx) = mpsc::channel::<Comando>(16);

    // Ator: único dono do contador (sem Mutex)
    let ator = tokio::spawn(async move {
        let mut total = 0;
        while let Some(cmd) = rx.recv().await {
            match cmd {
                Comando::Soma(n) => total += n,
                Comando::Consulta(resp) => {
                    let _ = resp.send(total);
                }
            }
        }
    });

    for n in 1..=4 {
        tx.send(Comando::Soma(n)).await.unwrap();
    }
    let (resp_tx, resp_rx) = oneshot::channel();
    tx.send(Comando::Consulta(resp_tx)).await.unwrap();
    println!("total = {}", resp_rx.await.unwrap()); // 10

    drop(tx); // fecha o canal: o ator termina
    ator.await.unwrap();
}
```

> [!info] Canal limitado
> `mpsc::channel(n)` é limitado: `send().await` espera quando cheio (contrapressão). Prefira-o ao `unbounded_channel`, que pode crescer sem limite.

## Veja também

- [[Tokio]]
- [[Canais mpsc]]
- [[join! e select!]]
