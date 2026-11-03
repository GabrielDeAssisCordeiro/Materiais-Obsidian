---
tags:
  - docker
  - swarm
  - stack
  - compose
  - deploy
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comando docker service]]"
  - "[[Secrets e configs do Swarm]]"
  - "[[Estrutura do compose.yaml e Compose Specification]]"
  - "[[deploy.resources e limites]]"
---

# Stacks com docker stack deploy

Um **stack** usa o mesmo formato Compose, mas a seção `deploy:` passa a ter efeito de orquestração.

`stack.yaml`:

```yaml
services:
  web:
    image: nginx:1.27
    ports:
      - "8080:80"
    networks:
      - frontend
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
        failure_action: rollback
      rollback_config:
        parallelism: 1
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
      resources:
        limits:
          cpus: "0.50"
          memory: 128M
        reservations:
          memory: 64M

  api:
    image: traefik/whoami:v1.10
    networks:
      - frontend
    deploy:
      replicas: 2

networks:
  frontend:
    driver: overlay
```

```bash
docker swarm init                          # se ainda não existir
docker stack deploy -c stack.yaml loja

docker stack ls
docker stack services loja
docker stack ps loja
docker service logs loja_web

# Atualizar: edite o arquivo e rode deploy novamente
docker stack deploy -c stack.yaml loja

docker stack rm loja
```

## Diferenças em relação ao `docker compose`

| Aspecto | `docker compose` | `docker stack deploy` |
|---|---|---|
| `build:` | Suportado | **Ignorado**: use imagens de um registry |
| `deploy:` | Parcial (resources etc.) | **Totalmente aplicado** |
| `depends_on` | Ordem e condições | Ignorado (use retry/healthchecks) |
| `container_name` | Suportado | Não suportado |
| Secrets/configs | Arquivos locais | Objetos do Swarm (`external` ou `file`) |
| Alvo | Um host | Cluster |

> [!bug] "image could not be accessed by the registry"
> Em cluster de vários nós, **todos os nós** precisam baixar a imagem. Use um registry acessível e `docker stack deploy --with-registry-auth` para repassar credenciais.

> [!tip] Placement
> Em cluster de um nó, não use `node.role == worker`; só há um manager. Em clusters reais, use `placement.constraints` para separar cargas.

## Exercício

Implante o stack acima, edite a imagem do `web` para outra tag, faça o deploy novamente e acompanhe a atualização progressiva com `docker service ps loja_web`.

## Veja também

- [[Comando docker service]]
- [[Secrets e configs do Swarm]]
- [[Estrutura do compose.yaml e Compose Specification]]
- [[deploy.resources e limites]]
- [[MOC - Swarm e Orquestração]]
