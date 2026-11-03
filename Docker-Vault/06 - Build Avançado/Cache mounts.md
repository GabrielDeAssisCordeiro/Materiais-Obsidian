---
tags:
  - docker
  - build-avancado
  - buildkit
  - cache
  - otimizacao
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Instrução RUN]]"
  - "[[Otimização de tamanho e tempo de build]]"
---

# Cache mounts

Um **cache mount** fornece um diretório persistente **entre builds** para gerenciadores de pacotes, sem incluí-lo na imagem final.

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
# O cache de wheels do pip persiste entre builds, mas não vai para a imagem
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
COPY . .
```

## Exemplos por ecossistema

```dockerfile
# Node.js (npm)
RUN --mount=type=cache,target=/root/.npm npm ci

# Go
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go build -o /out/app ./cmd/app

# Debian apt (desativa a limpeza automática do cache de apt)
RUN rm -f /etc/apt/apt.conf.d/docker-clean && \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends curl
```

| Opção | Efeito |
|---|---|
| `target` | Diretório dentro do build |
| `id` | Identificador do cache (padrão: o `target`) |
| `sharing` | `shared`, `private` ou `locked` |

> [!warning] O conteúdo do cache não está na imagem
> Se o programa precisa dos arquivos em tempo de execução, copie-os para fora do mount dentro do mesmo `RUN`.

> [!info] Cache mounts não são exportados por padrão
> Em CI efêmero eles são perdidos, a menos que você use um mecanismo de persistência próprio.

## Exercício

Construa uma imagem Python com `--mount=type=cache` para o pip, altere uma dependência e compare o tempo do segundo build com o de uma versão sem cache mount.

## Veja também

- [[Cache de camadas e ordem das instruções]]
- [[Instrução RUN]]
- [[Otimização de tamanho e tempo de build]]
- [[MOC - Build Avançado]]
