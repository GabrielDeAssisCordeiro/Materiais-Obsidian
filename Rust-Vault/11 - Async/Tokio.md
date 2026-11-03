---
tags: [rust, async, crates, tokio]
aliases: ["#[tokio::main]", "tokio::spawn", "JoinSet"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Executores e runtimes]]", "[[join! e select!]]", "[[Canais assíncronos]]", "[[Armadilhas do async]]"]
---

# Tokio

**Tokio** é o runtime assíncrono mais usado.

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

> [!question] Verificar na documentação oficial
> Confirme a versão atual e as *features* necessárias em docs.rs/tokio.

```rust
// requer crate: tokio
use std::time::Duration;
use tokio::time::sleep;

#[tokio::main] // cria o runtime e executa a main assíncrona
async fn main() {
    // spawn: roda o future em outra tarefa (leve, não é thread do SO)
    let h = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        42
    });

    println!("esperando...");
    let valor = h.await.unwrap(); // JoinHandle devolve Result (falha se a tarefa der panic)
    println!("{valor}");
}
```

## Várias tarefas com `JoinSet`

```rust
// requer crate: tokio
use tokio::task::JoinSet;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    let mut set = JoinSet::new();
    for i in 0..5u64 {
        set.spawn(async move {
            sleep(Duration::from_millis(50 * (5 - i))).await;
            i * 10
        });
    }

    // Resultados chegam na ordem em que terminam
    while let Some(res) = set.join_next().await {
        println!("{}", res.unwrap());
    }
}
```

## Trabalho bloqueante

```rust
// requer crate: tokio
#[tokio::main]
async fn main() {
    // CPU pesada ou API bloqueante: use spawn_blocking para não travar o runtime
    let r = tokio::task::spawn_blocking(|| (1..=1_000_000u64).sum::<u64>())
        .await
        .unwrap();
    println!("{r}");
}
```

## Timeout e sono

```rust
// requer crate: tokio
use std::time::Duration;
use tokio::time::{sleep, timeout};

#[tokio::main]
async fn main() {
    let r = timeout(Duration::from_millis(50), sleep(Duration::from_secs(5))).await;
    println!("estourou o tempo: {}", r.is_err());
}
```

| Módulo | Conteúdo |
|---|---|
| `tokio::task` | `spawn`, `spawn_blocking`, `JoinSet` |
| `tokio::time` | `sleep`, `timeout`, `interval` |
| `tokio::sync` | `mpsc`, `oneshot`, `broadcast`, `watch`, `Mutex`, `RwLock`, `Semaphore` |
| `tokio::net` | `TcpListener`, `TcpStream`, `UdpSocket` |
| `tokio::fs` / `tokio::io` | arquivos e utilitários de E/S assíncrona |

> [!info] Flavor do runtime
> `#[tokio::main]` usa o executor multi-thread por padrão. Para uma thread só: `#[tokio::main(flavor = "current_thread")]`.

## Veja também

- [[Executores e runtimes]]
- [[join! e select!]]
- [[Canais assíncronos]]
- [[Armadilhas do async]]
