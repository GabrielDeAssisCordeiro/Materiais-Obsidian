---
tags:
  - docker
  - projetos
  - swarm
  - stack
  - secrets
  - rolling-update
aliases: []
tipo: projeto
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Swarm]]"
  - "[[Stacks com docker stack deploy]]"
  - "[[Secrets e configs do Swarm]]"
  - "[[Atualizações progressivas e rollback]]"
  - "[[Rede overlay]]"
---

# Projeto 08 - Cluster Swarm com stack de produção

## Objetivos

- Montar um **cluster Swarm** (3 nós em laboratório).
- Implantar uma **stack** com três serviços (web, api, banco), **config** e **secret** do Swarm.
- Praticar **escala**, **atualização progressiva**, **rollback** e **falha de nó** (drain).

**Nível:** avançado · **Tempo estimado:** 90 min

## Laboratório com 3 VMs (Multipass)

```bash
# Requer o Multipass (Ubuntu); alternativa: três VMs quaisquer com Docker
for no in manager worker1 worker2; do
  multipass launch 24.04 --name $no --cpus 2 --memory 2G --disk 12G
  multipass exec $no -- bash -c 'curl -fsSL https://get.docker.com | sudo sh && sudo usermod -aG docker ubuntu'
done
multipass list
```

> [!warning] Script de conveniência
> O `get.docker.com` é aceitável **apenas em laboratório descartável**. Em servidores reais, use o repositório oficial ([[Instalação no Linux]]).

## 1. Formando o cluster

```bash
IP_MANAGER=$(multipass info manager --format csv | tail -n 1 | cut -d, -f3)

multipass exec manager -- docker swarm init --advertise-addr "$IP_MANAGER"

TOKEN=$(multipass exec manager -- docker swarm join-token -q worker)
for no in worker1 worker2; do
  multipass exec $no -- docker swarm join --token "$TOKEN" "$IP_MANAGER":2377
done

multipass exec manager -- docker node ls
```

Rotule um nó para hospedar o banco:

```bash
multipass exec manager -- docker node update --label-add db=true worker1
```

## 2. Arquivos da stack

Trabalhe dentro do manager (`multipass shell manager`) em uma pasta `loja/`.

`nginx.conf`:

```nginx
events {}

http {
  server {
    listen 80;

    location / {
      proxy_pass http://api:80;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
    }

    location = /health {
      return 200 "ok\n";
    }
  }
}
```

`stack.yaml`:

```yaml
services:
  web:
    image: nginx:1.27
    ports:
      - "8080:80"
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf
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
      resources:
        limits:
          cpus: "0.25"
          memory: 64M

  api:
    image: traefik/whoami:v1.10      # eco da requisição: mostra qual réplica respondeu
    networks:
      - frontend
      - backend
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        order: start-first
        failure_action: rollback

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - backend
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.labels.db == true

configs:
  nginx_conf:
    file: ./nginx.conf

secrets:
  db_password:
    external: true

networks:
  frontend:
    driver: overlay
  backend:
    driver: overlay

volumes:
  pgdata:
```

## 3. Implantação

```bash
printf '%s' "$(openssl rand -base64 24)" | docker secret create db_password -

docker stack deploy -c stack.yaml loja
docker stack services loja
docker stack ps loja
```

## Verificação

```bash
# O routing mesh responde em QUALQUER nó do cluster
for ip in IP_MANAGER IP_WORKER1 IP_WORKER2; do curl -s http://$ip:8080 | grep -i hostname; done
# Repita várias vezes: o "Hostname" muda (balanceamento entre as réplicas da api)

# O banco ficou no nó rotulado?
docker service ps loja_db --format '{{.Name}} → {{.Node}}'

# O segredo chegou ao banco?
docker exec $(docker ps -q -f name=loja_db) ls /run/secrets    # execute no nó que hospeda o db
```

## Experimentos

```bash
# 1) Escalar
docker service scale loja_api=6
docker service ps loja_api

# 2) Atualização progressiva (observe uma réplica por vez)
docker service update --image traefik/whoami:latest loja_api
watch docker service ps loja_api

# 3) Rollback
docker service rollback loja_api

# 4) Falha de nó: esvazie o worker2 e veja as tasks migrarem
docker node update --availability drain worker2
docker service ps loja_web
docker node update --availability active worker2

# 5) Matar um container manualmente (execute no nó correspondente) e observar o self-healing
docker rm -f $(docker ps -q -f name=loja_web | head -n 1)
docker service ps loja_web
```

## Solução de problemas

| Sintoma | Causa provável | Solução |
|---|---|---|
| `docker swarm join` falha por rede | Portas 2377/7946/4789 bloqueadas | Libere entre os nós |
| Task `Pending` ("no suitable node") | Constraint sem nó correspondente ou recursos insuficientes | `docker node inspect` e rótulos |
| Task em `Rejected`/`Failed` repetido | Imagem inexistente ou erro da app | `docker service ps --no-trunc` e `docker service logs` |
| `secret not found` | Secret criado com outro nome | `docker secret ls`; nomes são exatos |
| Config não atualiza | Configs são imutáveis | Crie nova config com outro nome e `service update --config-rm/--config-add` |
| Banco perdeu dados ao migrar de nó | Volume local ao nó | Fixe o banco em um nó (constraint) ou use armazenamento compartilhado |

## Limpeza

```bash
docker stack rm loja
docker secret rm db_password
# Remova as VMs
multipass delete --purge manager worker1 worker2
```

## Extensões sugeridas

1. Colocar o **Traefik em modo Swarm** na frente da `web` com HTTPS ([[Projeto 05 - Proxy reverso com Traefik e HTTPS]]).
2. Adicionar um **segundo manager** (3 managers) e testar a tolerância a falhas do Raft.
3. Monitorar o cluster com Prometheus/cAdvisor em **modo global** ([[Projeto 06 - Monitoramento com Prometheus e Grafana]]).
4. Comparar com a mesma stack em **Kubernetes** ([[Swarm vs Kubernetes e quando migrar]]).

## Exercício

Derrube (desligue) a VM `worker1` que hospeda o banco e descreva o que acontece com o serviço `db`. Que estratégia você adotaria para um banco em Swarm sem perda de disponibilidade?

## Veja também

- [[Visão geral do Swarm]]
- [[Stacks com docker stack deploy]]
- [[Secrets e configs do Swarm]]
- [[Atualizações progressivas e rollback]]
- [[Rede overlay]]
- [[MOC - Projetos - Docker]]
