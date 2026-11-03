---
tags:
  - docker
  - build-avancado
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Builders do Buildx]]"
  - "[[Padrão OCI]]"
  - "[[Docker Buildx Bake]]"
  - "[[Instalação no macOS]]"
---

# Build multiplataforma

Uma única referência de imagem pode servir várias arquiteturas (`linux/amd64`, `linux/arm64`, etc.) através de um **index OCI** (manifest list).

```bash
# 1. Habilita emulação QEMU (necessário para arquiteturas diferentes da nativa)
docker run --privileged --rm tonistiigi/binfmt --install all

# 2. Builder com driver docker-container (ou containerd image store)
docker buildx create --name multi --driver docker-container --use

# 3. Constrói e publica para várias plataformas
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t meuusuario/app:1.0 \
  --push .

# 4. Confere o índice
docker buildx imagetools inspect meuusuario/app:1.0
```

> [!info] Por que `--push`?
> Com o image store clássico, imagens multiplataforma não podem ser carregadas no daemon local. Use `--push` (registry) ou `--output type=oci,dest=app.tar`.

## Cross-compilation (mais rápido que emulação)

```dockerfile
# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM golang:1.24 AS build
ARG TARGETOS
ARG TARGETARCH
WORKDIR /src
COPY . .
# Compila nativamente para a plataforma de destino, sem emular
RUN CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /out/app ./cmd/app

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/app /app
ENTRYPOINT ["/app"]
```

| ARG automático | Significado |
|---|---|
| `BUILDPLATFORM` | Plataforma onde o build executa |
| `TARGETPLATFORM` | Plataforma de destino (ex.: `linux/arm64`) |
| `TARGETOS`, `TARGETARCH` | Partes de `TARGETPLATFORM` |

> [!warning] Emulação é lenta
> Compilar sob QEMU pode ser 5 a 20 vezes mais lento. Prefira cross-compilation ou **runners nativos** de cada arquitetura.

> [!bug] `exec format error` ao rodar
> A imagem não contém a arquitetura do host. Verifique `docker buildx imagetools inspect` e reconstrua com a plataforma correta.

## Exercício

Construa uma imagem simples para `linux/amd64,linux/arm64` com `--output type=oci,dest=app.tar` e inspecione o index dentro do tar.

## Veja também

- [[Builders do Buildx]]
- [[Padrão OCI]]
- [[Docker Buildx Bake]]
- [[Instalação no macOS]]
- [[MOC - Build Avançado]]
