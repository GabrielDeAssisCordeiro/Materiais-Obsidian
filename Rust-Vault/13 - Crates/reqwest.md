---
tags: [rust, crates]
aliases: ["reqwest", "cliente HTTP", "HTTP client"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[serde e serde_json]]", "[[Escolhendo e avaliando crates]]"]
---

# reqwest

**reqwest** é o cliente HTTP mais usado (assíncrono, com variante `blocking`).

```toml
[dependencies]
reqwest = { version = "0.12", features = ["json"] }
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
```

```rust
// requer crate: reqwest
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct Post {
    id: u32,
    title: String,
}

#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {
    // GET simples
    let corpo = reqwest::get("https://httpbin.org/get").await?.text().await?;
    println!("{} bytes", corpo.len());

    // Reutilize o Client: mantém pool de conexões
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(10))
        .build()?;

    let post: Post = client
        .get("https://jsonplaceholder.typicode.com/posts/1")
        .send()
        .await?
        .error_for_status()?   // transforma 4xx/5xx em Err
        .json()
        .await?;
    println!("{:?}", post);

    // POST com JSON
    let resp = client
        .post("https://httpbin.org/post")
        .json(&serde_json::json!({ "nome": "Ana" }))
        .send()
        .await?;
    println!("{}", resp.status());
    Ok(())
}
```

> [!info] Sem async
> Com a feature `blocking`, use `reqwest::blocking::get(url)?.text()?` em programas simples.

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/reqwest antes de copiar para um projeto.

## Veja também

- [[Tokio]]
- [[serde e serde_json]]
- [[Escolhendo e avaliando crates]]
