---
tags:
  - docker
  - exercicios
  - dockerfile
  - build
aliases: []
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Introdução ao Dockerfile]]"
  - "[[Multi-stage builds]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Instruções CMD e ENTRYPOINT]]"
  - "[[Boas práticas de Dockerfile]]"
---

# Exercícios de Dockerfile e Build

## Questões

1. Escreva um Dockerfile para uma aplicação Python de arquivo único (`app.py`), com imagem base `python:3.12-slim`, usuário não-root e `CMD` em forma exec.
2. Encontre **cinco problemas** neste Dockerfile e reescreva-o:

```dockerfile
# ❌ Dockerfile com problemas (propositalmente)
FROM node
ENV API_TOKEN=abc123
COPY . /app
RUN apt-get update
RUN apt-get install -y curl
WORKDIR /app
RUN npm install
CMD npm start
```

3. Converta o Dockerfile Go abaixo em **multi-stage** com imagem final `distroless`:

```dockerfile
FROM golang:1.24
WORKDIR /src
COPY . .
RUN go build -o /app .
CMD ["/app"]
```

4. Dado o Dockerfile abaixo, o que imprimem os comandos `docker run IMG`, `docker run IMG 1.1.1.1` e `docker run --entrypoint echo IMG oi`?

```dockerfile
FROM alpine:3.20
ENTRYPOINT ["ping", "-c", "1"]
CMD ["localhost"]
```

5. Escreva um `.dockerignore` adequado a um projeto Node.js.
6. Reordene as instruções para aproveitar o cache: `COPY . .` / `RUN pip install -r requirements.txt` / `COPY requirements.txt .`.
7. Qual a diferença entre `ARG` e `ENV`? Qual deles existe no container em execução?
8. Como usar um token privado durante o `npm ci` sem gravá-lo na imagem?
9. Qual comando constrói e publica uma imagem para `amd64` e `arm64`?
10. Por que o `docker stop` leva 10 segundos com `CMD python app.py` e como corrigir?

## Gabarito

**1.**

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py .
RUN useradd --system --uid 10001 --no-create-home app
USER 10001
CMD ["python", "app.py"]
```

**2. Problemas e correção:** (a) `FROM node` sem tag (usa `latest`); (b) segredo em `ENV`; (c) `COPY . /app` antes das dependências (cache ruim); (d) `apt-get update` separado e sem limpeza; (e) `CMD` em forma shell; também roda como root e `npm install` (prefira `npm ci`).

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev
COPY . .
USER node
CMD ["node", "server.js"]
```

(O `curl` só deve ser instalado se for realmente necessário; em Alpine, `apk add --no-cache curl`. O token virá por *secret* na execução, nunca por `ENV`.)

**3.**

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.24 AS build
WORKDIR /src
COPY go.mod go.sum* ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/app .

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

**4.** `docker run IMG` → `ping -c 1 localhost`; `docker run IMG 1.1.1.1` → `ping -c 1 1.1.1.1` (o `CMD` é substituído); `docker run --entrypoint echo IMG oi` → imprime `oi` (o `ENTRYPOINT` foi trocado e `oi` é argumento).

**5.**

```text
.git
node_modules
npm-debug.log
.env
.env.*
Dockerfile
compose*.yaml
dist
coverage
```

**6.** `COPY requirements.txt .` → `RUN pip install -r requirements.txt` → `COPY . .` (dependências antes do código).

**7.** `ARG` existe apenas durante o **build**; `ENV` persiste na imagem e existe no **container em execução**.

**8.** Com *secret mount*: `RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci`, construindo com `docker build --secret id=npmrc,src=$HOME/.npmrc .`.

**9.** `docker buildx build --platform linux/amd64,linux/arm64 -t usuario/app:1.0 --push .` (com um builder `docker-container` ou containerd image store).

**10.** Na forma shell, o `/bin/sh` é o PID 1 e não repassa o SIGTERM; o Docker espera o timeout e aplica SIGKILL. Use a forma exec (`CMD ["python", "app.py"]`) e, se necessário, `--init`.

## Veja também

- [[Introdução ao Dockerfile]]
- [[Multi-stage builds]]
- [[Cache de camadas e ordem das instruções]]
- [[Instruções CMD e ENTRYPOINT]]
- [[Boas práticas de Dockerfile]]
- [[MOC - Exercícios - Docker]]
