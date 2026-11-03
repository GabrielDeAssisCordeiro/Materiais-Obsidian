---
tags: [rust, crates, web]
aliases: ["axum", "Router", "extractors"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[serde e serde_json]]", "[[actix-web]]", "[[sqlx e diesel]]"]
---

# axum

**axum** é um framework web minimalista do projeto Tokio, construído sobre `tower` e `hyper`.

```toml
[dependencies]
axum = "0.8"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
```

```rust
// requer crate: axum
use axum::{
    extract::{Path, State},
    routing::{get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};
use std::sync::{Arc, Mutex};

#[derive(Clone, Serialize, Deserialize)]
struct Item {
    id: u32,
    nome: String,
}

type Estado = Arc<Mutex<Vec<Item>>>;

async fn ola() -> &'static str {
    "olá, axum!"
}

async fn lista(State(estado): State<Estado>) -> Json<Vec<Item>> {
    Json(estado.lock().unwrap().clone())
}

async fn busca(Path(id): Path<u32>, State(estado): State<Estado>) -> Option<Json<Item>> {
    estado.lock().unwrap().iter().find(|i| i.id == id).cloned().map(Json)
}

async fn cria(State(estado): State<Estado>, Json(item): Json<Item>) -> Json<Item> {
    estado.lock().unwrap().push(item.clone());
    Json(item)
}

#[tokio::main]
async fn main() {
    let estado: Estado = Arc::new(Mutex::new(Vec::new()));

    let app = Router::new()
        .route("/", get(ola))
        .route("/itens", get(lista).post(cria))
        .route("/itens/{id}", get(busca))
        .with_state(estado);

    let listener = tokio::net::TcpListener::bind("127.0.0.1:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

> [!question] Verificar na documentação oficial
> A sintaxe de parâmetros de caminho mudou entre versões (`/:id` nas séries antigas, `/{id}` na 0.8). Confirme em docs.rs/axum a versão que você usa.

- **Extractors** (`Path`, `Query`, `Json`, `State`) leem a requisição; retornos implementam `IntoResponse`.
- **Middleware** vem do ecossistema `tower`/`tower-http` (CORS, tracing, compressão).
- Estado compartilhado com `Arc<Mutex<T>>` (ou, melhor, um pool de banco de dados).

## Veja também

- [[Tokio]]
- [[serde e serde_json]]
- [[actix-web]]
- [[sqlx e diesel]]
