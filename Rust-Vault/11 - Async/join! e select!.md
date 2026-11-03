---
tags: [rust, async, tokio]
aliases: ["join!", "select!", "try_join!"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[Armadilhas do async]]", "[[Canais assíncronos]]"]
---

# join! e select!

## `join!`: esperar **todos**

Executa vários Futures **concorrentemente** na mesma tarefa e devolve todos os resultados.

```rust
// requer crate: tokio
use std::time::Duration;
use tokio::time::sleep;

async fn busca(nome: &str, ms: u64) -> String {
    sleep(Duration::from_millis(ms)).await;
    format!("{nome} pronto")
}

#[tokio::main]
async fn main() {
    // Leva ~100ms (não 150ms): as esperas se sobrepõem
    let (a, b) = tokio::join!(busca("A", 100), busca("B", 50));
    println!("{a}, {b}");

    // try_join!: para no primeiro Err
    let r: Result<(i32, i32), String> = tokio::try_join!(async { Ok(1) }, async { Ok(2) });
    println!("{:?}", r);
}
```

## `select!`: esperar o **primeiro**

Aguarda vários Futures e executa o ramo do primeiro que concluir; os demais são **descartados (cancelados)**.

```rust
// requer crate: tokio
use std::time::Duration;
use tokio::sync::mpsc;
use tokio::time::sleep;

#[tokio::main]
async fn main() {
    let (tx, mut rx) = mpsc::channel::<String>(8);

    tokio::spawn(async move {
        sleep(Duration::from_millis(20)).await;
        tx.send("mensagem".to_string()).await.unwrap();
    });

    tokio::select! {
        Some(m) = rx.recv() => println!("recebi: {m}"),
        _ = sleep(Duration::from_secs(1)) => println!("timeout"),
    }
}
```

> [!warning] Cancel safety
> Ao vencer um ramo, os outros Futures são descartados no meio do caminho. Só use em `select!` operações **cancel-safe** (como `recv` de canais e `sleep`); outras podem perder dados (por exemplo, leituras parciais em buffers). A documentação de cada função informa isso.

> [!tip] `join!` vs `spawn`
> `join!` roda na **mesma tarefa** (sem paralelismo real entre os Futures). `tokio::spawn` cria tarefas independentes que podem rodar em paralelo no pool de threads.

## Veja também

- [[Tokio]]
- [[Armadilhas do async]]
- [[Canais assíncronos]]
