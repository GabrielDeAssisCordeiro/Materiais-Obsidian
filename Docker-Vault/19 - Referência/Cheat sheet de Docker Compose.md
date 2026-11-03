---
tags:
  - docker
  - referencia
  - cheat-sheet
  - compose
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Docker Compose]]"
  - "[[Comandos do Docker Compose]]"
  - "[[Interpolação e arquivo .env]]"
  - "[[depends_on com condition e healthcheck]]"
---

# Cheat sheet de Docker Compose

## Comandos

```bash
docker compose up -d [--build] [--wait]     # sobe a stack
docker compose down [-v]                    # derruba (-v apaga volumes!)
docker compose ps / logs -f [serviço]
docker compose exec serviço sh              # container existente
docker compose run --rm serviço comando     # container novo
docker compose build / pull / push
docker compose stop / start / restart
docker compose config                       # valida e mostra o modelo final
docker compose watch                        # desenvolvimento
docker compose ls                           # projetos
docker compose -p nome -f a.yaml -f b.yaml up -d
docker compose --profile debug up -d
```

## Modelo de `compose.yaml` (sem `version`)

```yaml
name: meu-projeto

services:
  api:
    build:
      context: ./api
      target: prod
    image: meu-projeto-api:1.0
    environment:
      LOG_LEVEL: info
    env_file:
      - path: .env
        required: false
    ports:
      - "127.0.0.1:8080:8080"
    volumes:
      - dados:/var/lib/app
      - ./config:/etc/app:ro
    networks: [backend, frontend]
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:8080/health || exit 1"]
      interval: 15s
      timeout: 3s
      retries: 3
    restart: unless-stopped
    init: true
    deploy:
      resources:
        limits: { cpus: "1.0", memory: 512M }
    profiles: []

  db:
    image: postgres:16
    secrets: [db_password]
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    volumes: [pgdata:/var/lib/postgresql/data]
    networks: [backend]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 10

networks:
  frontend:
  backend:
    internal: true

volumes:
  dados:
  pgdata:

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

## Interpolação

| Forma | Efeito |
|---|---|
| `${VAR}` | Valor da variável |
| `${VAR:-padrao}` | Padrão se vazia/indefinida |
| `${VAR:?erro}` | Erro se vazia/indefinida |
| `$$` | `$` literal |

## Condições de `depends_on`

`service_started` · `service_healthy` · `service_completed_successfully`

## Veja também

- [[Visão geral do Docker Compose]]
- [[Comandos do Docker Compose]]
- [[Interpolação e arquivo .env]]
- [[depends_on com condition e healthcheck]]
- [[MOC - Referência - Docker]]
