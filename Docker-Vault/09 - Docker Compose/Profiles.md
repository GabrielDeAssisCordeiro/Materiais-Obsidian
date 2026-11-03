---
tags:
  - docker
  - compose
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Múltiplos arquivos e overrides]]"
  - "[[depends_on com condition e healthcheck]]"
  - "[[Comandos do Docker Compose]]"
---

# Profiles

**Profiles** permitem declarar serviços opcionais no mesmo arquivo e ativá-los só quando necessário (depuração, testes, ferramentas administrativas).

```yaml
services:
  app:
    image: traefik/whoami:v1.10          # sem profile: sempre sobe
    ports: ["8080:80"]

  adminer:
    image: adminer:4
    profiles: ["debug"]
    ports: ["8081:8080"]

  testes:
    image: alpine:3.20
    command: sh -c 'echo "executando testes" && exit 0'
    profiles: ["test"]
```

```bash
docker compose up -d                           # só "app"
docker compose --profile debug up -d           # app + adminer
docker compose --profile debug --profile test up -d
COMPOSE_PROFILES=debug docker compose up -d    # via variável

# Executar um serviço de profile diretamente (ativa o profile automaticamente)
docker compose run --rm testes
```

> [!info] Serviços sem `profiles`
> Sempre iniciam. Serviços com profile só iniciam se o profile estiver ativo ou se forem chamados explicitamente (`up adminer`, `run adminer`).

> [!tip] Padrão comum
> Um único `compose.yaml` com `profiles: [dev]` para ferramentas de desenvolvimento (Mailpit, Adminer), mantendo a stack de produção limpa.

## Exercício

Crie profiles `debug` e `test`, suba combinações diferentes e liste o resultado com `docker compose ps`.

## Veja também

- [[Múltiplos arquivos e overrides]]
- [[depends_on com condition e healthcheck]]
- [[Comandos do Docker Compose]]
- [[MOC - Docker Compose]]
