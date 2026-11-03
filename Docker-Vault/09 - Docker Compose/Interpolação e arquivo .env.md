---
tags:
  - docker
  - compose
  - variaveis
  - env
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Variáveis de ambiente e env_file]]"
  - "[[Múltiplos arquivos e overrides]]"
  - "[[Estrutura do compose.yaml e Compose Specification]]"
---

# Interpolação e arquivo .env

O Compose substitui `${VARIAVEL}` no `compose.yaml` usando variáveis do **shell** e do arquivo **`.env`** (na pasta do projeto).

`.env`:

```text
POSTGRES_VERSION=16
HTTP_PORT=8080
```

`compose.yaml`:

```yaml
services:
  db:
    image: postgres:${POSTGRES_VERSION:-16}
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD:?Defina DB_PASSWORD}
  web:
    image: nginx:1.27
    ports:
      - "${HTTP_PORT:-8080}:80"
```

## Sintaxe

| Forma | Significado |
|---|---|
| `${VAR}` | Valor de `VAR` (vazio se indefinida) |
| `${VAR:-padrao}` | `padrao` se `VAR` indefinida **ou vazia** |
| `${VAR-padrao}` | `padrao` apenas se indefinida |
| `${VAR:?mensagem}` | **Erro** com a mensagem se indefinida ou vazia |
| `${VAR:+alternativa}` | `alternativa` se `VAR` definida e não vazia |
| `$$` | Cifrão literal |

```bash
# Ver o resultado da interpolação
DB_PASSWORD=lab docker compose config

# Outro arquivo de variáveis
docker compose --env-file prod.env config
```

## Precedência para interpolação

Variáveis do **shell** sobrescrevem o `.env`; `--env-file` substitui o arquivo `.env` padrão.

> [!tip] Variáveis especiais
> `COMPOSE_PROJECT_NAME`, `COMPOSE_FILE`, `COMPOSE_PROFILES` e `COMPOSE_PATH_SEPARATOR` configuram o próprio Compose.

> [!bug] "variable is not set. Defaulting to a blank string"
> Aviso de variável indefinida. Defina-a ou use `${VAR:-padrao}` / `${VAR:?erro}` para falhar de forma clara.

## Exercício

Use `${DB_PASSWORD:?...}` e rode `docker compose config` sem e com a variável definida, observando o erro e o sucesso.

## Veja também

- [[Variáveis de ambiente e env_file]]
- [[Múltiplos arquivos e overrides]]
- [[Estrutura do compose.yaml e Compose Specification]]
- [[MOC - Docker Compose]]
