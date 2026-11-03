---
tags:
  - docker
  - projetos
  - nodejs
  - api
  - multi-stage
aliases: []
tipo: projeto
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Node.js em Docker]]"
  - "[[Multi-stage builds]]"
  - "[[Init, PID 1 e sinais]]"
  - "[[Boas práticas de Dockerfile]]"
  - "[[Projeto 03 - WordPress com MySQL]]"
---

# Projeto 02 - API Node.js containerizada

## Objetivos

- Containerizar uma API Node.js (Express) com **multi-stage**, usuário não-root e *graceful shutdown*.
- Ter alvos separados de **desenvolvimento** (hot reload) e **produção**.
- Rodar testes dentro de um container.

**Nível:** iniciante · **Tempo estimado:** 45 min

## Estrutura

```text
api-node/
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── package.json
├── package-lock.json     (gerado no passo 1)
├── server.js
└── test/
    └── server.test.js
```

## Arquivos

`package.json`:

```json
{
  "name": "api-node",
  "version": "1.0.0",
  "private": true,
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "node --watch server.js",
    "test": "node --test"
  },
  "dependencies": {
    "express": "^4.21.0"
  }
}
```

`server.js`:

```javascript
const express = require("express");

const app = express();
const PORT = Number(process.env.PORT ?? 3000);
const SAUDACAO = process.env.SAUDACAO || "Olá";

app.get("/", (req, res) => {
  res.json({ mensagem: `${SAUDACAO} do container!`, host: require("os").hostname() });
});

app.get("/health", (req, res) => res.status(200).json({ status: "ok" }));

const server = app.listen(PORT, "0.0.0.0", () => {
  console.log(JSON.stringify({ nivel: "info", msg: `escutando em ${PORT}` }));
});

// Encerramento gracioso: o Docker envia SIGTERM no "docker stop"
function encerrar(sinal) {
  console.log(JSON.stringify({ nivel: "info", msg: `recebido ${sinal}, encerrando` }));
  server.close(() => process.exit(0));
  setTimeout(() => process.exit(1), 8000).unref();
}
process.on("SIGTERM", () => encerrar("SIGTERM"));
process.on("SIGINT", () => encerrar("SIGINT"));

module.exports = { app, server };
```

`test/server.test.js`:

```javascript
const test = require("node:test");
const assert = require("node:assert");
const { once } = require("node:events");

test("GET /health responde 200", async () => {
  process.env.PORT = "0";                       // porta aleatória durante o teste
  const { server } = require("../server.js");
  if (!server.listening) await once(server, "listening");

  const resposta = await fetch(`http://127.0.0.1:${server.address().port}/health`);
  assert.strictEqual(resposta.status, 200);

  server.close();
});
```

`.dockerignore`:

```text
node_modules
npm-debug.log
.git
Dockerfile
compose*.yaml
```

`Dockerfile`:

```dockerfile
# syntax=docker/dockerfile:1

FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

# ---------- desenvolvimento ----------
FROM deps AS dev
ENV NODE_ENV=development
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]

# ---------- testes ----------
FROM deps AS test
COPY . .
CMD ["npm", "test"]

# ---------- produção ----------
FROM node:22-alpine AS prod
ENV NODE_ENV=production
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev
COPY server.js ./
USER node
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD wget -qO- http://127.0.0.1:3000/health || exit 1
CMD ["node", "server.js"]
```

`compose.yaml`:

```yaml
services:
  api:
    build:
      context: .
      target: prod
    image: api-node:1.0
    environment:
      SAUDACAO: Olá
    ports:
      - "127.0.0.1:3000:3000"
    restart: unless-stopped
    init: true
    read_only: true
    cap_drop: [ALL]
    security_opt:
      - no-new-privileges:true
    deploy:
      resources:
        limits:
          cpus: "0.5"
          memory: 256M

  api-dev:
    profiles: ["dev"]
    build:
      context: .
      target: dev
    ports:
      - "127.0.0.1:3001:3000"
    volumes:
      - ./:/app
      - /app/node_modules
```

## Passo a passo

```bash
# 1) Gera o package-lock.json usando um container (nada instalado no host)
docker run --rm -v "$PWD":/app -w /app node:22-alpine npm install

# 2) Roda os testes dentro de um container
docker build --target test -t api-node:test .
docker run --rm api-node:test

# 3) Produção
docker compose up -d --build api

# 4) Desenvolvimento com hot reload (edite server.js e observe o reinício)
docker compose --profile dev up --build api-dev
```

## Verificação

```bash
curl http://localhost:3000/                   # {"mensagem":"Olá do container!", ...}
curl http://localhost:3000/health             # {"status":"ok"}
docker compose exec api id                    # uid=1000(node)
docker images api-node                        # tamanho enxuto

# Encerramento gracioso: deve ser rápido (< 2 s) e logar "recebido SIGTERM"
time docker compose stop api
docker compose logs --tail 5 api
```

## Solução de problemas

| Sintoma | Causa provável | Solução |
|---|---|---|
| `npm ci` falha: "package-lock.json not found" | Lockfile ausente | Execute o passo 1 |
| `docker stop` leva 10 s | A app é o PID 1 e não trata sinais, ou `CMD` em forma shell | Use a forma exec e o tratamento de SIGTERM (já no exemplo) |
| `EADDRINUSE` | Porta ocupada | Mude a porta publicada |
| Hot reload não detecta mudanças | Montagem sem eventos (Windows/macOS) | Use `develop.watch` ou *polling* |
| `read-only file system` | A app grava em disco | Adicione `tmpfs` ou volume |

## Extensões sugeridas

1. Adicionar um **banco** (veja o [[Projeto 04 - Stack com Postgres, API e frontend]]).
2. Trocar para **Compose Watch** em vez de bind mount ([[Compose Watch]]).
3. Gerar **SBOM e provenance** e escanear a imagem ([[Varredura de vulnerabilidades com Trivy e Grype]]).
4. Publicar com GitHub Actions e fazer deploy em Cloud Run ([[Google Cloud Run]]).

## Exercício

Adicione uma rota `GET /info` que retorna a versão do Node (`process.version`) e a variável `APP_VERSION`; passe `APP_VERSION` por `ARG`/`ENV` no build.

## Veja também

- [[Node.js em Docker]]
- [[Multi-stage builds]]
- [[Init, PID 1 e sinais]]
- [[Boas práticas de Dockerfile]]
- [[Projeto 03 - WordPress com MySQL]]
- [[MOC - Projetos - Docker]]
