---
tags: [rust, crates, web]
aliases: ["actix-web", "actix"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[axum]]", "[[Tokio]]", "[[serde e serde_json]]"]
---

# actix-web

**actix-web** é um framework web maduro e muito rápido, com runtime próprio baseado em Tokio.

```toml
[dependencies]
actix-web = "4"
serde = { version = "1", features = ["derive"] }
```

```rust
// requer crate: actix-web
use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use serde::Deserialize;

#[derive(Deserialize)]
struct NovoUsuario {
    nome: String,
}

#[get("/")]
async fn ola() -> impl Responder {
    "olá, actix!"
}

#[get("/usuarios/{id}")]
async fn busca(id: web::Path<u32>) -> impl Responder {
    format!("usuário {}", id.into_inner())
}

#[post("/usuarios")]
async fn cria(corpo: web::Json<NovoUsuario>) -> HttpResponse {
    HttpResponse::Created().body(format!("criado {}", corpo.nome))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(ola).service(busca).service(cria))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
```

| | axum | actix-web |
|---|---|---|
| Base | `tower` + `hyper` (Tokio) | runtime próprio sobre Tokio |
| Estilo | funções + extractors + `Router` | atributos de rota + `App` |
| Middleware | `tower::Layer` | `wrap(...)` próprio |
| Ecossistema | integra com tudo do Tokio | grande, independente |

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/actix-web antes de copiar para um projeto.

## Veja também

- [[axum]]
- [[Tokio]]
- [[serde e serde_json]]
