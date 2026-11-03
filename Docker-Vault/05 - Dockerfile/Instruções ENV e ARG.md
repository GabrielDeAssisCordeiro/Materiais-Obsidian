---
tags:
  - docker
  - dockerfile
  - instrucao
  - env
  - comparativo
aliases:
  - ARG vs ENV
  - ENV
  - ARG
tipo: instrucao
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Instrução FROM]]"
  - "[[Variáveis de ambiente em containers]]"
  - "[[Secret mounts]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instruções ENV e ARG

## ARG vs ENV

| | `ARG` | `ENV` |
|---|---|---|
| Disponível durante o build | Sim | Sim |
| Disponível no container em execução | **Não** | **Sim** |
| Definido por | `--build-arg` ou valor padrão | Dockerfile; sobrescrevível com `-e` |
| Persiste na imagem | Aparece no histórico/metadados | Gravado nos metadados da imagem |
| Uso típico | Versões, flags de build | Configuração do runtime |

```dockerfile
# syntax=docker/dockerfile:1
ARG NODE_VERSION=22
FROM node:${NODE_VERSION}-alpine

ARG BUILD_DATE                      # só para o build
ENV NODE_ENV=production \
    PORT=3000                       # persiste na imagem

LABEL org.opencontainers.image.created=$BUILD_DATE
```

```bash
docker build --build-arg NODE_VERSION=22 --build-arg BUILD_DATE=$(date -u +%FT%TZ) -t app .
docker run --rm -e PORT=8080 app printenv PORT      # sobrescreve o ENV
```

> [!danger] `ARG` e `ENV` NÃO são lugar para segredos
> Valores de `ARG` aparecem em `docker history` e valores de `ENV` ficam na imagem e em `docker inspect`. Para segredos de build, use [[Secret mounts]].
> ```dockerfile
> # ❌ INSEGURO — didático
> ARG NPM_TOKEN
> RUN echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" > .npmrc && npm ci
> ```

> [!info] Escopo de ARG
> Um `ARG` declarado antes do `FROM` não existe dentro do estágio, a menos que seja redeclarado. Cada estágio tem seu próprio escopo.

> [!tip] Variáveis predefinidas
> Com BuildKit existem `ARG`s automáticos para multiplataforma: `BUILDPLATFORM`, `TARGETPLATFORM`, `TARGETOS`, `TARGETARCH`. Veja [[Build multiplataforma]].

## Exercício

Defina `ARG APP_VERSION` e `ENV APP_VERSION=$APP_VERSION`. Construa passando `--build-arg APP_VERSION=2.0` e verifique dentro do container.

## Veja também

- [[Instrução FROM]]
- [[Variáveis de ambiente em containers]]
- [[Secret mounts]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
