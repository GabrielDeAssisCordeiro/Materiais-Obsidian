---
tags:
  - docker
  - referencia
  - boas-praticas
  - seguranca
aliases:
  - Anti-patterns
  - O que não fazer
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Boas práticas de Dockerfile]]"
  - "[[Checklist de segurança de containers]]"
  - "[[Checklist de produção]]"
  - "[[Erros comuns e soluções]]"
---

# Antipadrões Docker

Cada item mostra o que **não** fazer (marcado com ❌), por que é um problema e a correção (✅).

> [!danger] Exemplos inseguros ou incorretos de propósito
> Os blocos ❌ existem apenas para ilustrar o problema. Não os use em projetos reais.

## 1. Usar `latest`

```dockerfile
# ❌ O build muda sem aviso
FROM python:latest
```

```dockerfile
# ✅ Versão fixa (e digest em produção)
FROM python:3.12-slim
```

## 2. Rodar como root

```dockerfile
# ❌ Sem USER: o processo roda como root
FROM node:22-alpine
COPY . /app
CMD ["node", "/app/server.js"]
```

```dockerfile
# ✅ Usuário sem privilégios
FROM node:22-alpine
COPY --chown=node:node . /app
USER node
CMD ["node", "/app/server.js"]
```

## 3. Segredos na imagem

```dockerfile
# ❌ Fica no histórico e nos metadados
ENV DB_PASSWORD=minha-senha
ARG API_TOKEN
RUN echo "$API_TOKEN" > /app/.token
```

✅ Use `RUN --mount=type=secret` no build e **secrets** na execução. Veja [[Gerenciamento de segredos]].

## 4. `apt-get update` separado e sem limpeza

```dockerfile
# ❌ Cache obsoleto e camada inchada
RUN apt-get update
RUN apt-get install -y curl
```

```dockerfile
# ✅ Uma camada, sem lixo
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*
```

## 5. `COPY . .` antes das dependências

```dockerfile
# ❌ Qualquer mudança no código reinstala tudo
COPY . .
RUN npm ci
```

```dockerfile
# ✅ Dependências primeiro, código depois
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
```

## 6. Forma shell no `CMD`

```dockerfile
# ❌ O shell é o PID 1 e engole o SIGTERM
CMD python app.py
```

```dockerfile
# ✅ Forma exec
CMD ["python", "app.py"]
```

## 7. Dados na camada gravável

```bash
# ❌ Banco de dados sem volume: os dados somem com o container
docker run -d postgres:16
```

```bash
# ✅ Volume nomeado
docker run -d -v pgdata:/var/lib/postgresql/data postgres:16
```

## 8. `--privileged` e `docker.sock` por conveniência

```bash
# ❌ Entrega o host ao container
docker run --privileged -v /var/run/docker.sock:/var/run/docker.sock ferramenta
```

✅ Capabilities específicas, proxy de socket, sem socket. Veja [[Riscos do --privileged]] e [[Proteção do docker.sock]].

## 9. Publicar o banco para o mundo

```yaml
# ❌ Banco acessível em todas as interfaces
services:
  db:
    image: postgres:16
    ports:
      - "5432:5432"
```

```yaml
# ✅ Sem porta publicada, ou apenas em loopback
services:
  db:
    image: postgres:16
    ports:
      - "127.0.0.1:5432:5432"
```

## 10. `depends_on` achando que garante prontidão

```yaml
# ❌ Só espera o container iniciar
depends_on:
  - db
```

```yaml
# ✅ Espera o healthcheck
depends_on:
  db:
    condition: service_healthy
```

## 11. Outros antipadrões frequentes

| Antipadrão | Por que é ruim | Alternativa |
|---|---|---|
| `docker commit` como forma de "construir" | Não reproduzível | Dockerfile |
| `ADD` para copiar arquivos locais | Comportamento implícito | `COPY` |
| Sem `.dockerignore` | Contexto gigante, vazamento de `.env` | Criar `.dockerignore` |
| Sem limites de recursos | Um serviço derruba o host | `--memory`, `--cpus` |
| Sem healthcheck | Falhas silenciosas | `HEALTHCHECK` |
| `restart: always` para "consertar" crashes | Mascara bugs | Corrija e alerte reinícios |
| `container_name` fixo | Impede escala e cópias | Deixe o Compose nomear |
| `chmod 777` nos volumes | Abre brecha | UID/GID corretos |
| SSH dentro do container | Superfície extra | `docker exec`/debug |
| Logs em arquivos no container | Enche a camada gravável | stdout/stderr |
| Reconstruir a imagem por ambiente | Artefato diferente do testado | Uma imagem, config por ambiente |
| Imagem enorme com tudo | Lenta e vulnerável | Multi-stage e base mínima |

## Exercício

Revise um Dockerfile/compose seu e encontre ao menos três antipadrões desta lista. Corrija e meça o efeito (tamanho, tempo de build, segurança).

## Veja também

- [[Boas práticas de Dockerfile]]
- [[Checklist de segurança de containers]]
- [[Checklist de produção]]
- [[Erros comuns e soluções]]
- [[MOC - Referência - Docker]]
