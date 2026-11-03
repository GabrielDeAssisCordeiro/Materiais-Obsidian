---
tags:
  - docker
  - compose
  - healthcheck
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Healthchecks em containers]]"
  - "[[Políticas de restart]]"
  - "[[Comandos do Docker Compose]]"
---

# depends_on com condition e healthcheck

`depends_on` controla a **ordem de inicialização**. Por padrão, só espera o container **iniciar**, não ficar **pronto**. Para esperar a aplicação, combine com `healthcheck` e `condition`.

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: senha-de-laboratorio
      POSTGRES_DB: appdb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d appdb"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 10s

  migracao:
    image: postgres:16
    depends_on:
      db:
        condition: service_healthy
    command: psql postgresql://postgres:senha-de-laboratorio@db/appdb -c "SELECT 1;"
    restart: "no"

  api:
    image: traefik/whoami:v1.10
    depends_on:
      db:
        condition: service_healthy        # espera o banco ficar saudável
        restart: true                     # reinicia a api se o db reiniciar
      migracao:
        condition: service_completed_successfully   # espera a migração terminar com sucesso
```

| `condition` | Significado |
|---|---|
| `service_started` | O container foi iniciado (padrão) |
| `service_healthy` | O healthcheck passou |
| `service_completed_successfully` | O serviço terminou com código 0 (tarefas únicas) |

```bash
docker compose up -d --wait      # aguarda os serviços ficarem saudáveis
```

> [!warning] `depends_on` não substitui resiliência
> Mesmo com a ordem correta, a aplicação deve **tentar reconectar** ao banco com *retry* e *backoff*; dependências podem cair depois do startup.

> [!info] `required: false`
> Na sintaxe longa, `required: false` (por exemplo, `depends_on: { cache: { condition: service_started, required: false } }`) evita falha se o serviço dependente estiver desativado, como quando pertence a um profile inativo.

## Exercício

Altere `retries` do healthcheck do banco para 1 com um comando que falha, e observe o comportamento da `api` com `condition: service_healthy`.

## Veja também

- [[Healthchecks em containers]]
- [[Políticas de restart]]
- [[Comandos do Docker Compose]]
- [[MOC - Docker Compose]]
