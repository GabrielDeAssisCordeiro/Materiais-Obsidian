---
tags: [rust, projeto, avancado, web, async, banco-de-dados]
aliases: ["API REST", "CRUD com axum e sqlx", "Biblioteca de livros"]
tipo: projeto
nivel: avancado
criado: 2026-10-24
relacionados: ["[[axum]]", "[[sqlx e diesel]]", "[[serde e serde_json]]", "[[Tokio]]", "[[Backend web com Rust]]", "[[Async e await]]", "[[Box dyn Error]]"]
---

# Projeto 6 - API REST com banco de dados

## Objetivos

Uma API REST de CRUD para uma coleção de livros, com **axum** (HTTP), **sqlx** (SQLite) e **serde** (JSON).

| Método | Rota | Ação |
|---|---|---|
| `GET` | `/livros` | lista todos |
| `POST` | `/livros` | cria (`201 Created`) |
| `GET` | `/livros/{id}` | obtém um (`404` se não existir) |
| `DELETE` | `/livros/{id}` | remove (`204 No Content`) |

> [!question] Verificar na documentação oficial
> Este projeto usa crates externos que mudam de API entre versões: **axum 0.8** (sintaxe de rota `/{id}`), **sqlx 0.8** e **tokio 1**. Os blocos de código não são compilados automaticamente neste vault; confirme em docs.rs/axum e docs.rs/sqlx se houver divergência.

## Estrutura

```text
api-livros/
├── Cargo.toml
└── src/
    └── main.rs
```

```toml
[package]
name = "api-livros"
version = "0.1.0"
edition = "2024"

[dependencies]
axum = "0.8"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
sqlx = { version = "0.8", features = ["runtime-tokio", "sqlite"] }
```

## Código completo

```rust
// requer crate: axum, sqlx, tokio, serde
use axum::{
    extract::{Path, State},
    http::StatusCode,
    routing::get,
    Json, Router,
};
use serde::{Deserialize, Serialize};
use sqlx::{sqlite::SqlitePoolOptions, FromRow, SqlitePool};

/// Linha da tabela e também o JSON devolvido pela API.
#[derive(Serialize, FromRow)]
struct Livro {
    id: i64,
    titulo: String,
    autor: String,
}

/// Corpo esperado no POST.
#[derive(Deserialize)]
struct NovoLivro {
    titulo: String,
    autor: String,
}

/// Erro HTTP simples: (código, mensagem).
type ErroHttp = (StatusCode, String);

fn erro_interno(e: sqlx::Error) -> ErroHttp {
    (StatusCode::INTERNAL_SERVER_ERROR, e.to_string())
}

async fn listar(State(pool): State<SqlitePool>) -> Result<Json<Vec<Livro>>, ErroHttp> {
    let livros = sqlx::query_as::<_, Livro>("SELECT id, titulo, autor FROM livros ORDER BY id")
        .fetch_all(&pool)
        .await
        .map_err(erro_interno)?;
    Ok(Json(livros))
}

async fn criar(
    State(pool): State<SqlitePool>,
    Json(novo): Json<NovoLivro>,
) -> Result<(StatusCode, Json<Livro>), ErroHttp> {
    if novo.titulo.trim().is_empty() {
        return Err((StatusCode::BAD_REQUEST, "título obrigatório".to_string()));
    }
    // Parâmetros com `?` + bind(): protege contra SQL injection
    let livro = sqlx::query_as::<_, Livro>(
        "INSERT INTO livros (titulo, autor) VALUES (?, ?) RETURNING id, titulo, autor",
    )
    .bind(novo.titulo)
    .bind(novo.autor)
    .fetch_one(&pool)
    .await
    .map_err(erro_interno)?;
    Ok((StatusCode::CREATED, Json(livro)))
}

async fn obter(
    State(pool): State<SqlitePool>,
    Path(id): Path<i64>,
) -> Result<Json<Livro>, ErroHttp> {
    sqlx::query_as::<_, Livro>("SELECT id, titulo, autor FROM livros WHERE id = ?")
        .bind(id)
        .fetch_optional(&pool)
        .await
        .map_err(erro_interno)?
        .map(Json)
        .ok_or((StatusCode::NOT_FOUND, "livro não encontrado".to_string()))
}

async fn remover(
    State(pool): State<SqlitePool>,
    Path(id): Path<i64>,
) -> Result<StatusCode, ErroHttp> {
    let r = sqlx::query("DELETE FROM livros WHERE id = ?")
        .bind(id)
        .execute(&pool)
        .await
        .map_err(erro_interno)?;
    if r.rows_affected() == 0 {
        Err((StatusCode::NOT_FOUND, "livro não encontrado".to_string()))
    } else {
        Ok(StatusCode::NO_CONTENT)
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // mode=rwc: cria o arquivo do banco se ele não existir
    let pool = SqlitePoolOptions::new()
        .max_connections(5)
        .connect("sqlite://livros.db?mode=rwc")
        .await?;

    sqlx::query(
        "CREATE TABLE IF NOT EXISTS livros (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor  TEXT NOT NULL
        )",
    )
    .execute(&pool)
    .await?;

    let app = Router::new()
        .route("/livros", get(listar).post(criar))
        .route("/livros/{id}", get(obter).delete(remover))
        .with_state(pool); // o pool é compartilhado entre handlers (é um Arc por dentro)

    let listener = tokio::net::TcpListener::bind("127.0.0.1:3000").await?;
    println!("API em http://127.0.0.1:3000");
    axum::serve(listener, app).await?;
    Ok(())
}
```

## Testando com curl

```bash
cargo run

curl -X POST http://127.0.0.1:3000/livros \
     -H 'content-type: application/json' \
     -d '{"titulo":"The Rust Programming Language","autor":"Klabnik e Nichols"}'

curl http://127.0.0.1:3000/livros
curl http://127.0.0.1:3000/livros/1
curl -X DELETE http://127.0.0.1:3000/livros/1 -i
```

## Como funciona

- **Extractors** (`State`, `Path`, `Json`) transformam a requisição nos argumentos tipados do handler.
- Qualquer retorno `Result<T, (StatusCode, String)>` já implementa `IntoResponse`; o `?` encurta o tratamento de erros.
- `FromRow` mapeia colunas para campos; `Serialize`/`Deserialize` fazem o mesmo com JSON.
- `bind()` envia parâmetros separados do SQL — **nunca** concatene strings em consultas.

## Extensões

- [ ] `PUT /livros/{id}` para atualizar.
- [ ] Tipo de erro próprio que implemente `IntoResponse` ([[Erros customizados]]).
- [ ] Migrações com `sqlx migrate` e consultas verificadas em compilação (`query!`).
- [ ] Logs com [[tracing]] e testes de integração chamando o `Router` diretamente ([[Testes de integração]]).
- [ ] Paginação (`?pagina=1&por_pagina=20`) e filtro por autor.
- [ ] Trocar SQLite por PostgreSQL.

## Exercício

Implemente `PUT /livros/{id}` retornando 404 quando o id não existir e 200 com o livro atualizado.

## Veja também

- [[axum]]
- [[sqlx e diesel]]
- [[serde e serde_json]]
- [[Tokio]]
- [[Backend web com Rust]]
- [[Async e await]]
- [[Box dyn Error]]
