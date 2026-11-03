---
tags:
  - docker
  - swarm
  - secrets
  - configs
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Gerenciamento de segredos]]"
  - "[[configs e secrets no Compose]]"
  - "[[Stacks com docker stack deploy]]"
---

# Secrets e configs do Swarm

No Swarm, segredos e configurações são **objetos do cluster**: armazenados **criptografados** no log Raft dos managers, transmitidos por TLS mútuo e entregues apenas aos nós que executam tasks que os usam. No container, aparecem como **arquivos em memória** (`/run/secrets/NOME`).

```bash
# Criar segredo a partir da entrada padrão (não deixa em arquivo)
printf 'senha-de-laboratorio' | docker secret create db_password -
docker secret ls

# Usar em um serviço
docker service create --name db \
  --secret db_password \
  -e POSTGRES_PASSWORD_FILE=/run/secrets/db_password \
  postgres:16

# Configs (não sensíveis)
docker config create nginx_conf ./nginx.conf
docker service create --name proxy \
  --config source=nginx_conf,target=/etc/nginx/nginx.conf \
  nginx:1.27
```

## Em stack

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password

secrets:
  db_password:
    external: true          # criado antes com `docker secret create`
```

## Rotação

Segredos são **imutáveis**. Para trocar: crie um novo (com outro nome) e atualize o serviço.

```bash
printf 'nova-senha' | docker secret create db_password_v2 -
docker service update \
  --secret-rm db_password \
  --secret-add source=db_password_v2,target=db_password \
  db
docker secret rm db_password
```

> [!tip] Criptografia do Raft
> Ative `--autolock` ao iniciar o Swarm para proteger as chaves em disco após reinícios. Veja [[Inicializando um Swarm]].

> [!warning] Segredo não é mágica
> A aplicação precisa ler o arquivo, e quem tiver acesso ao container (ou `docker exec`) o verá. Restrinja acesso ao Docker nos nós.

## Exercício

Crie um segredo, use-o em um serviço Postgres via `POSTGRES_PASSWORD_FILE` e faça a rotação para uma nova versão do segredo.

## Veja também

- [[Gerenciamento de segredos]]
- [[configs e secrets no Compose]]
- [[Stacks com docker stack deploy]]
- [[MOC - Swarm e Orquestração]]
