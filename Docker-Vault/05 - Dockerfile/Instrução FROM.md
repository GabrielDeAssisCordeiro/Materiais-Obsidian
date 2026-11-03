---
tags:
  - docker
  - dockerfile
  - instrucao
aliases: []
tipo: instrucao
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Multi-stage builds]]"
  - "[[Escolha da imagem base]]"
  - "[[Instruções ENV e ARG]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instrução FROM

`FROM` inicia um **estágio de build** e define a imagem base. Todo Dockerfile começa com ele (ou com `ARG` antes dele).

```dockerfile
FROM alpine:3.20                          # tag fixa
FROM python:3.12-slim@sha256:<digest>     # tag + digest
FROM --platform=linux/amd64 node:22-alpine
FROM golang:1.24 AS build                 # nomeia o estágio
FROM scratch                              # imagem vazia
```

## `ARG` antes de `FROM`

Permite parametrizar a imagem base. O valor só vale para o `FROM`; para usá-lo depois, redeclare `ARG` dentro do estágio.

```dockerfile
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim
ARG PYTHON_VERSION          # redeclarado: agora disponível neste estágio
RUN echo "Python ${PYTHON_VERSION}"
```

```bash
docker build --build-arg PYTHON_VERSION=3.13 -t teste .
```

> [!warning] Evite `latest`
> Sem tag, `FROM python` equivale a `python:latest`. O build deixa de ser reproduzível. Veja [[Tags e digests de imagens]].

> [!tip] Várias instruções FROM
> Cada `FROM` abre um novo estágio. Isso é a base dos [[Multi-stage builds]].

## Exercício

Parametrize a versão do Python do seu Dockerfile com `ARG` antes do `FROM` e construa com duas versões diferentes, confirmando com `docker run --rm IMAGEM python --version`.

## Veja também

- [[Multi-stage builds]]
- [[Escolha da imagem base]]
- [[Instruções ENV e ARG]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
