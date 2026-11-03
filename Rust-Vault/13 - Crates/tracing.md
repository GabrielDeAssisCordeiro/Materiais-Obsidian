---
tags: [rust, crates]
aliases: ["tracing", "tracing-subscriber", "instrument"]
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[Escolhendo e avaliando crates]]"]
---

# tracing

**tracing** é o framework de instrumentação (logs estruturados + *spans*) padrão no ecossistema assíncrono. O crate `log` é a alternativa mais simples.

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
```

```rust
// requer crate: tracing
use tracing::{debug, error, info, instrument, warn};

#[instrument] // cria um span com o nome e os argumentos da função
fn processa(id: u32) -> Result<(), String> {
    info!(id, "processando"); // campos estruturados
    if id == 0 {
        error!("id inválido");
        return Err("id zero".into());
    }
    debug!("detalhe interno");
    Ok(())
}

fn main() {
    // Configura o destino; o filtro vem de RUST_LOG (ex.: RUST_LOG=debug)
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    info!("aplicação iniciada");
    let _ = processa(42);
    let _ = processa(0);
    warn!("encerrando");
}
```

| Nível | Uso |
|---|---|
| `error!` | falhas |
| `warn!` | situações suspeitas |
| `info!` | eventos de alto nível |
| `debug!` / `trace!` | diagnóstico detalhado |

> [!tip] Spans em código assíncrono
> Em async, `#[instrument]` e `.instrument(span)` mantêm o contexto entre `.await`s, algo que logs simples não conseguem.

> [!question] Verificar na documentação oficial
> As APIs de crates externos mudam entre versões maiores. Confirme versão e exemplos em docs.rs/tracing antes de copiar para um projeto.

## Veja também

- [[Tokio]]
- [[Escolhendo e avaliando crates]]
