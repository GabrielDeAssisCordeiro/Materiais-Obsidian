---
tags:
  - docker
  - desenvolvimento
  - rust
  - cargo
  - dockerfile
  - distroless
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Go em Docker]]"
  - "[[Cache mounts]]"
  - "[[Superfície de ataque e imagens mínimas]]"
---

# Rust em Docker

Compilações Rust são pesadas; **cache mounts** e multi-stage são essenciais.

```dockerfile
# syntax=docker/dockerfile:1

# ---------- Build ----------
FROM rust:1.85 AS build
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN --mount=type=cache,target=/usr/local/cargo/registry \
    --mount=type=cache,target=/app/target \
    cargo build --release \
 && cp target/release/meuapp /app/meuapp

# ---------- Produção ----------
FROM gcr.io/distroless/cc-debian12:nonroot AS prod
COPY --from=build /app/meuapp /meuapp
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/meuapp"]
```

> [!info] Cópia dentro do mesmo `RUN`
> Como `target/` é um cache mount (não faz parte da camada), o binário precisa ser **copiado para fora** no mesmo `RUN`.

## Desenvolvimento com recarga

```dockerfile
FROM rust:1.85 AS dev
WORKDIR /app
RUN cargo install cargo-watch
CMD ["cargo", "watch", "-x", "run"]
```

```bash
docker build -t rust-demo:1.0 .
docker run --rm rust-demo:1.0
```

> [!tip] Alternativas
> - Binários **musl** estáticos (`x86_64-unknown-linux-musl`) permitem `FROM scratch`.
> - `cargo-chef` melhora o cache de dependências em builds de CI.
> - Troque `meuapp` pelo nome do crate (campo `name` do `Cargo.toml`).

> [!question] Verificar na documentação oficial
> Confirme a tag `rust:1.85` (ou mais recente) no Docker Hub e a compatibilidade da libc entre o estágio de build (Debian) e o runtime (`distroless/cc-debian12`).

## Exercício

Crie um programa Rust "olá mundo", containerize e compare o tamanho da imagem final com a imagem do estágio de build.

## Veja também

- [[Go em Docker]]
- [[Cache mounts]]
- [[Superfície de ataque e imagens mínimas]]
- [[MOC - Desenvolvimento]]
