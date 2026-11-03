---
tags:
  - docker
  - compose
  - build
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Estrutura do compose.yaml e Compose Specification]]"
  - "[[Introdução ao Dockerfile]]"
  - "[[Comandos do Docker Compose]]"
  - "[[Multi-stage builds]]"
---

# Serviços com image e build

Cada serviço usa uma **imagem pronta** (`image`) ou uma **construída localmente** (`build`) — ou ambas (constrói e dá nome à imagem).

```yaml
services:
  # Imagem pronta
  cache:
    image: redis:7

  # Construída do Dockerfile local
  api:
    build: ./api                  # forma curta: caminho do contexto

  # Forma longa com opções
  web:
    image: meuusuario/web:1.0     # nome da imagem resultante
    build:
      context: ./web
      dockerfile: Dockerfile.prod
      target: runtime             # estágio de um multi-stage
      args:
        NODE_ENV: production
      cache_from:
        - meuusuario/web:buildcache
      platforms:
        - linux/amd64
        - linux/arm64
    pull_policy: missing          # always | never | missing | build
```

```bash
docker compose build              # constrói todos os serviços com build
docker compose build api          # apenas um
docker compose up -d --build      # reconstrói antes de subir
docker compose pull               # baixa imagens
```

> [!info] `image` + `build`
> Quando ambos existem, o Compose **constrói** e etiqueta o resultado com o nome de `image`, útil para publicar com `docker compose push`.

> [!tip] `docker compose up` não reconstrói sozinho
> Se o código mudou, use `--build`. Sem isso, o Compose reutiliza a imagem existente.

## Exercício

Crie um serviço `api` com `build: ./api` (Dockerfile simples) e rode `docker compose up -d --build`. Altere o código e suba novamente com e sem `--build`.

## Veja também

- [[Estrutura do compose.yaml e Compose Specification]]
- [[Introdução ao Dockerfile]]
- [[Comandos do Docker Compose]]
- [[Multi-stage builds]]
- [[MOC - Docker Compose]]
