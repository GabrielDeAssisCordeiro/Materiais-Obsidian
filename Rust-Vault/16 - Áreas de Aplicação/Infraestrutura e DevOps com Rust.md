---
tags: [rust, areas, devops]
aliases: ["proxy", "tonic", "cloud native"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Tokio]]", "[[tracing]]", "[[CI com GitHub Actions]]", "[[Targets e cross-compilation]]", "[[Backend web com Rust]]"]
---

# Infraestrutura e DevOps com Rust

Rust é comum em software de infraestrutura: baixo consumo de recursos e ausência de pausas de GC são vantagens em componentes que rodam o tempo todo.

| Categoria | Exemplos |
|---|---|
| Proxies e rede | Pingora (Cloudflare), Linkerd2-proxy, Envoy alternatives |
| Bancos de dados | TiKV, SurrealDB, Materialize, Qdrant |
| Observabilidade | Vector, OpenTelemetry (SDK Rust) |
| Contêineres e VMs | Firecracker, youki, Cloud Hypervisor |
| Ferramentas de build | `cargo`, `uv`, `ruff`, `turbopack` |
| RPC | `tonic` (gRPC), `prost` (Protobuf) |

## Um servidor TCP "echo" assíncrono

```rust
// requer crate: tokio
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpListener;

#[tokio::main]
async fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:7000").await?;
    loop {
        let (mut socket, _) = listener.accept().await?;
        tokio::spawn(async move {
            let mut buf = [0u8; 1024];
            while let Ok(n) = socket.read(&mut buf).await {
                if n == 0 {
                    break;
                }
                if socket.write_all(&buf[..n]).await.is_err() {
                    break;
                }
            }
        });
    }
}
```

## Práticas operacionais

- **Binários estáticos** (`x86_64-unknown-linux-musl`) simplificam imagens Docker (`FROM scratch`): veja [[Targets e cross-compilation]].
- Logs estruturados e *spans* com [[tracing]].
- Integração contínua e releases automatizados: [[CI com GitHub Actions]].

```dockerfile
# Build em múltiplos estágios
FROM rust:1 AS build
WORKDIR /app
COPY . .
RUN cargo build --release

FROM debian:stable-slim
COPY --from=build /app/target/release/meu-servico /usr/local/bin/
CMD ["meu-servico"]
```

## Veja também

- [[Tokio]]
- [[tracing]]
- [[CI com GitHub Actions]]
- [[Targets e cross-compilation]]
- [[Backend web com Rust]]
