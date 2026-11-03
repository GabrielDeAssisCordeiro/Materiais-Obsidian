---
tags:
  - docker
  - desenvolvimento
  - python
  - dockerfile
  - fastapi
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Hot reload em containers]]"
  - "[[Cache mounts]]"
  - "[[Node.js em Docker]]"
  - "[[Boas práticas de Dockerfile]]"
---

# Python em Docker

Exemplo com **FastAPI**.

`requirements.txt`:

```text
fastapi==0.115.0
uvicorn[standard]==0.30.6
```

`main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem": "Olá, Docker!"}

@app.get("/health")
def saude():
    return {"status": "ok"}
```

`Dockerfile`:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

# ---------- Dependências ----------
FROM base AS deps
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# ---------- Desenvolvimento ----------
FROM deps AS dev
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# ---------- Produção ----------
FROM deps AS prod
COPY . .
RUN useradd --system --uid 10001 --no-create-home app
USER 10001
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build --target prod -t fastapi-demo:1.0 .
docker run -d --name api -p 8000:8000 fastapi-demo:1.0
curl http://localhost:8000/health
docker rm -f api
```

```yaml
# compose.yaml de desenvolvimento
services:
  api:
    build:
      context: .
      target: dev
    ports:
      - "8000:8000"
    develop:
      watch:
        - action: sync
          path: .
          target: /app
        - action: rebuild
          path: requirements.txt
```

> [!tip] Boas práticas Python
> - `PYTHONUNBUFFERED=1` para logs imediatos; `PYTHONDONTWRITEBYTECODE=1` evita `.pyc`.
> - Fixe versões (`requirements.txt` com versões ou lockfile com hashes).
> - Em produção, prefira vários workers (Gunicorn + Uvicorn workers) conforme a CPU.
> - Pacotes com extensões C podem exigir `build-essential`: instale em um estágio de build e copie o resultado.

> [!question] Verificar na documentação oficial
> As versões fixadas em `requirements.txt` são exemplos; atualize para versões atuais e compatíveis.

## Exercício

Containerize uma API Flask ou FastAPI com os alvos `dev` e `prod`; confirme `GET /health` e o usuário não-root com `docker exec api id`.

## Veja também

- [[Hot reload em containers]]
- [[Cache mounts]]
- [[Node.js em Docker]]
- [[Boas práticas de Dockerfile]]
- [[MOC - Desenvolvimento]]
