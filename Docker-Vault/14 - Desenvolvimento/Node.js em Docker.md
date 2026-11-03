---
tags:
  - docker
  - desenvolvimento
  - nodejs
  - dockerfile
  - multi-stage
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Hot reload em containers]]"
  - "[[Multi-stage builds]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Python em Docker]]"
---

# Node.js em Docker

## Dockerfile único com alvos de desenvolvimento e produção

```dockerfile
# syntax=docker/dockerfile:1

# ---------- Dependências ----------
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

# ---------- Desenvolvimento (hot reload) ----------
FROM deps AS dev
ENV NODE_ENV=development
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

# ---------- Build ----------
FROM deps AS build
COPY . .
RUN npm run build

# ---------- Produção ----------
FROM node:22-alpine AS prod
ENV NODE_ENV=production
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

## Compose de desenvolvimento

```yaml
services:
  web:
    build:
      context: .
      target: dev
    ports:
      - "3000:3000"
    volumes:
      - ./:/app
      - /app/node_modules
```

```bash
docker compose up --build                     # desenvolvimento
docker build --target prod -t meu-app:1.0 .   # produção
docker run --rm -p 3000:3000 meu-app:1.0
```

> [!tip] Boas práticas Node
> - Use `npm ci` (reprodutível) com `package-lock.json`.
> - `NODE_ENV=production` em produção; `USER node`.
> - Use `CMD ["node", ...]` (não `npm start`) para que o Node receba os sinais; ou use `--init`.
> - Em desenvolvimento, `node --watch` (Node 18.11+) substitui o nodemon em muitos casos.

> [!bug] Binários nativos e Alpine
> Módulos com addons nativos podem exigir `libc6-compat` ou compilação no Alpine; se houver problemas, use `node:22-slim`.

## Exercício

Crie uma API Express mínima e containerize com os alvos `dev` e `prod`. Compare os tamanhos das imagens.

## Veja também

- [[Hot reload em containers]]
- [[Multi-stage builds]]
- [[Cache de camadas e ordem das instruções]]
- [[Python em Docker]]
- [[MOC - Desenvolvimento]]
