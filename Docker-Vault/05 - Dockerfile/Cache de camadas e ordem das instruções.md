---
tags:
  - docker
  - dockerfile
  - build
  - cache
  - otimizacao
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Camadas de uma imagem]]"
  - "[[Instrução RUN]]"
  - "[[Instruções COPY e ADD]]"
  - "[[Cache mounts]]"
  - "[[Otimização de tamanho e tempo de build]]"
---

# Cache de camadas e ordem das instruções

O builder reutiliza uma camada do cache quando **a instrução e seus arquivos de entrada são idênticos**. Se uma camada é invalidada, **todas as seguintes** também são.

## Regra: do que muda menos para o que muda mais

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
WORKDIR /app

# 1) Dependências (mudam raramente)
COPY package.json package-lock.json ./
RUN npm ci

# 2) Código (muda a cada commit)
COPY . .

CMD ["node", "server.js"]
```

Alterar só o código **não** reinstala as dependências.

```dockerfile
# ❌ ANTIPADRÃO: qualquer alteração no código invalida o npm ci
COPY . .
RUN npm ci
```

## O que invalida o cache

| Situação | Efeito |
|---|---|
| Instrução `RUN`/`ENV` alterada | Invalida a camada e as seguintes |
| Arquivo copiado com `COPY` mudou (conteúdo/metadados) | Invalida |
| `ARG` usado pela instrução mudou | Invalida |
| Imagem base atualizada na mesma tag | Invalida (depois de `pull`) |
| `RUN apt-get update` sem alteração | **Cache pode ficar obsoleto** (use `--no-cache` quando necessário) |

```bash
docker build -t app .                    # usa cache
docker build --no-cache -t app .         # ignora o cache
docker build --pull -t app .             # atualiza a imagem base
docker build --progress=plain -t app .   # mostra CACHED por etapa
```

> [!tip] Cache em CI
> Em ambientes efêmeros, o cache local não existe. Use cache remoto: [[Cache remoto de build]].

## Exercício

Construa o exemplo Node duas vezes: após alterar só `server.js`, confira que `npm ci` aparece como CACHED. Inverta a ordem das cópias e repita o teste.

## Veja também

- [[Camadas de uma imagem]]
- [[Instrução RUN]]
- [[Instruções COPY e ADD]]
- [[Cache mounts]]
- [[Otimização de tamanho e tempo de build]]
- [[MOC - Dockerfile]]
