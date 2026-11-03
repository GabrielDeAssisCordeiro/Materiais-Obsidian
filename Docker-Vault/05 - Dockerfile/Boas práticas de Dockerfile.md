---
tags:
  - docker
  - dockerfile
  - boas-praticas
  - checklist
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Multi-stage builds]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Instruções WORKDIR e USER]]"
  - "[[Arquivo .dockerignore]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Boas práticas de Dockerfile

Checklist de um bom Dockerfile:

- [ ] Imagem base **oficial**, mínima e com **tag fixa** (ou digest). Veja [[Escolha da imagem base]].
- [ ] `# syntax=docker/dockerfile:1` na primeira linha.
- [ ] **Multi-stage**: ferramentas de build fora da imagem final. Veja [[Multi-stage builds]].
- [ ] Ordem pensada para **cache**: dependências antes do código.
- [ ] `.dockerignore` presente.
- [ ] `COPY` em vez de `ADD`, copiando apenas o necessário.
- [ ] Comandos de instalação e limpeza no **mesmo** `RUN`.
- [ ] **Usuário não-root** (`USER` com UID numérico).
- [ ] Forma **exec** em `CMD`/`ENTRYPOINT`.
- [ ] **Sem segredos** em `ENV`, `ARG`, `COPY` ou `RUN`. Use [[Secret mounts]].
- [ ] `HEALTHCHECK` quando fizer sentido.
- [ ] `LABEL` OCI com origem e versão.
- [ ] Uma preocupação por container (um processo principal).
- [ ] Imagem varrida por vulnerabilidades ([[Docker Scout]]).

## Exemplo consolidado (Python)

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

FROM base AS deps
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --prefix=/install -r requirements.txt

FROM base AS runtime
COPY --from=deps /install /usr/local
COPY . .
RUN useradd --system --uid 10001 --no-create-home app
USER 10001
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request as u; u.urlopen('http://127.0.0.1:8000/health')" || exit 1
CMD ["python", "-m", "http.server", "8000"]
```

> [!info] Exemplo ilustrativo
> O `CMD` usa `http.server` apenas para manter o exemplo autocontido; em um projeto real, use seu servidor (gunicorn, uvicorn, etc.).

> [!tip] Linter de Dockerfile
> Use `docker build --check` ou ferramentas como Hadolint para detectar problemas automaticamente.

## Exercício

Pegue um Dockerfile antigo seu e marque quais itens do checklist ele viola. Corrija pelo menos três.

## Veja também

- [[Multi-stage builds]]
- [[Cache de camadas e ordem das instruções]]
- [[Instruções WORKDIR e USER]]
- [[Arquivo .dockerignore]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Dockerfile]]
