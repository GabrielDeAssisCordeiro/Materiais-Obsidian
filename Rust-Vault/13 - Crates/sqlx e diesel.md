---
tags: [rust, crates, banco-de-dados]
aliases: ["sqlx", "diesel", "ORM", "banco de dados"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[serde e serde_json]]", "[[Erros customizados]]"]
---

# sqlx e diesel

| | **sqlx** | **Diesel** |
|---|---|---|
| Estilo | SQL puro, **assíncrono** | DSL de consultas em Rust (ORM/query builder), **síncrono** (há `diesel-async`) |
| Verificação | `query!` valida o SQL contra o banco em **compilação** | tipos gerados do schema validam a consulta |
| Bancos | PostgreSQL, MySQL, SQLite | PostgreSQL, MySQL, SQLite |
| Migrações | `sqlx migrate` | `diesel migration` |
| Indicado | quem prefere escrever SQL; stacks async | quem quer segurança de tipos forte via DSL |

## sqlx

```toml
[dependencies]
sqlx = { version = "0.8", features = ["runtime-tokio", "sqlite"] }
tokio = { version = "1", features = ["full"] }
```

```rust
// requer crate: sqlx
use sqlx::{sqlite::SqlitePoolOptions, FromRow};

#[derive(Debug, FromRow)]
struct Tarefa {
    id: i64,
    titulo: String,
    feita: bool,
}

#[tokio::main]
async fn main() -> Result<(), sqlx::Error> {
    let pool = SqlitePoolOptions::new().connect("sqlite::memory:").await?;

    sqlx::query("CREATE TABLE tarefas (id INTEGER PRIMARY KEY, titulo TEXT NOT NULL, feita BOOLEAN NOT NULL DEFAULT 0)")
        .execute(&pool)
        .await?;

    // Parâmetros ligados (?) evitam SQL injection
    sqlx::query("INSERT INTO tarefas (titulo) VALUES (?)")
        .bind("estudar Rust")
        .execute(&pool)
        .await?;

    let tarefas: Vec<Tarefa> = sqlx::query_as("SELECT id, titulo, feita FROM tarefas")
        .fetch_all(&pool)
        .await?;
    println!("{:?}", tarefas);
    Ok(())
}
```

> [!warning] Nunca concatene entrada do usuário em SQL
> Use sempre parâmetros (`.bind(...)` no sqlx; o Diesel já parametriza por construção).

## Diesel (visão geral)

```rust
// requer crate: diesel
// Com schema.rs gerado por `diesel print-schema`:
// use crate::schema::tarefas::dsl::*;
// let resultados = tarefas.filter(feita.eq(false)).limit(5).load::<Tarefa>(&mut conn)?;
```

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/sqlx antes de copiar para um projeto.

## Veja também

- [[Tokio]]
- [[serde e serde_json]]
- [[Erros customizados]]
