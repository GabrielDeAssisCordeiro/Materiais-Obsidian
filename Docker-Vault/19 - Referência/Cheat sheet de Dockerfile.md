---
tags:
  - docker
  - referencia
  - cheat-sheet
  - dockerfile
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Introdução ao Dockerfile]]"
  - "[[Boas práticas de Dockerfile]]"
  - "[[Instruções CMD e ENTRYPOINT]]"
  - "[[Multi-stage builds]]"
---

# Cheat sheet de Dockerfile

| Instrução | Exemplo | Observação |
|---|---|---|
| `# syntax=` | `# syntax=docker/dockerfile:1` | Primeira linha; habilita recursos novos |
| `FROM` | `FROM python:3.12-slim AS base` | Inicia um estágio |
| `ARG` | `ARG VERSAO=1.0` | Só no build |
| `ENV` | `ENV PORT=8080` | Persiste na imagem |
| `WORKDIR` | `WORKDIR /app` | Cria o diretório |
| `COPY` | `COPY --chown=10001:10001 . .` | Preferir a `ADD` |
| `ADD` | `ADD --checksum=sha256:... URL /dest` | URLs e tar |
| `RUN` | `RUN apt-get update && apt-get install -y x && rm -rf /var/lib/apt/lists/*` | Camada nova |
| `RUN --mount` | `RUN --mount=type=cache,target=/root/.cache/pip pip install -r r.txt` | cache, secret, ssh |
| `USER` | `USER 10001` | Não-root |
| `EXPOSE` | `EXPOSE 8080` | Documenta |
| `VOLUME` | `VOLUME /dados` | Evitar em apps |
| `HEALTHCHECK` | `HEALTHCHECK CMD wget -qO- http://127.0.0.1:8080/health \|\| exit 1` | Saúde |
| `ENTRYPOINT` | `ENTRYPOINT ["/app"]` | Forma exec |
| `CMD` | `CMD ["--porta","8080"]` | Argumentos padrão |
| `LABEL` | `LABEL org.opencontainers.image.source="..."` | Metadados OCI |
| `SHELL` | `SHELL ["/bin/bash","-o","pipefail","-c"]` | Shell do `RUN` |
| `STOPSIGNAL` | `STOPSIGNAL SIGQUIT` | Sinal do `docker stop` |
| `ONBUILD` | `ONBUILD COPY . /app` | Evitar |

## Esqueleto recomendado

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

FROM deps AS build
COPY . .
RUN npm run build

FROM node:22-alpine AS prod
ENV NODE_ENV=production
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
HEALTHCHECK CMD wget -qO- http://127.0.0.1:3000/health || exit 1
CMD ["node", "dist/server.js"]
```

## Lembretes

- **Ordem**: dependências antes do código (cache).
- **Forma exec** em `CMD`/`ENTRYPOINT` para receber sinais.
- **Um `RUN`** para instalar **e** limpar.
- **Sem segredos** em `ARG`/`ENV`/`COPY`; use `--mount=type=secret`.
- **`.dockerignore`** sempre.

## Veja também

- [[Introdução ao Dockerfile]]
- [[Boas práticas de Dockerfile]]
- [[Instruções CMD e ENTRYPOINT]]
- [[Multi-stage builds]]
- [[MOC - Referência - Docker]]
