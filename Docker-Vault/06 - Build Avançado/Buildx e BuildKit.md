---
tags:
  - docker
  - build-avancado
  - buildkit
  - buildx
aliases:
  - BuildKit
  - Buildx
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Builders do Buildx]]"
  - "[[Cache mounts]]"
  - "[[Build multiplataforma]]"
  - "[[Docker Buildx Bake]]"
  - "[[Sintaxe do Dockerfile e syntax directive]]"
---

# Buildx e BuildKit

## BuildKit

**BuildKit** é o motor de build moderno do Docker (builder padrão desde o Engine 23.0 e no Docker Desktop). Substitui o builder clássico.

| Recurso | Benefício |
|---|---|
| Execução paralela de estágios | Builds mais rápidos |
| Pula estágios não usados | Menos trabalho |
| Cache mounts, secret mounts, SSH mounts | Cache e segredos sem vazar nas camadas |
| Cache remoto e exportação de cache | CI mais rápido |
| Builds multiplataforma | amd64, arm64 etc. |
| SBOM e provenance | Cadeia de suprimentos |
| Saída detalhada (`--progress`) | Depuração |

## Buildx

**Buildx** é o plugin da CLI (`docker buildx`) que expõe todo o poder do BuildKit: múltiplos builders, multiplataforma, cache, bake.

```bash
docker buildx version
docker buildx build -t app:1.0 .             # mesmo que docker build (com BuildKit)
docker buildx build --progress=plain -t app .
docker buildx ls                             # builders disponíveis
docker buildx du                             # uso de cache
docker buildx prune                          # limpa cache
```

> [!info] `docker build` já usa Buildx
> Em instalações modernas, `docker build` é um atalho para `docker buildx build` com o builder padrão.

> [!tip] Variável legada
> `DOCKER_BUILDKIT=1` só é necessária em instalações antigas do builder clássico. Hoje o padrão é BuildKit.

## Exercício

Execute `docker buildx ls` e `docker buildx version`. Construa qualquer imagem com `--progress=plain` e identifique as etapas em paralelo.

## Veja também

- [[Builders do Buildx]]
- [[Cache mounts]]
- [[Build multiplataforma]]
- [[Docker Buildx Bake]]
- [[Sintaxe do Dockerfile e syntax directive]]
- [[MOC - Build Avançado]]
