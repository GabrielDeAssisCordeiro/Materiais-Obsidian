---
tags:
  - docker
  - swarm
  - comandos
aliases: []
tipo: comando
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Inicializando um Swarm]]"
  - "[[Atualizações progressivas e rollback]]"
  - "[[Stacks com docker stack deploy]]"
---

# Comando docker service

```bash
# Cria um serviço replicado com porta publicada (routing mesh)
docker service create \
  --name web \
  --replicas 3 \
  --publish published=8080,target=80 \
  --limit-cpus 0.5 --limit-memory 128M \
  --health-cmd "wget -qO- http://127.0.0.1/ || exit 1" \
  nginx:1.27

docker service ls
docker service ps web                 # tarefas, nós e estados
docker service inspect --pretty web
docker service logs -f web

# Escalar
docker service scale web=5

# Restrições de posicionamento
docker service create --name db --constraint 'node.role==manager' \
  -e POSTGRES_PASSWORD=senha-de-laboratorio postgres:16

# Serviço global (um por nó)
docker service create --name agente --mode global alpine:3.20 sleep 3600

# Remover
docker service rm web
```

| Opção | Efeito |
|---|---|
| `--replicas` | Número de réplicas |
| `--mode global` | Uma tarefa por nó |
| `--publish` | Porta no *routing mesh* |
| `--constraint` | Onde pode rodar (`node.role`, `node.labels.zona==a`) |
| `--limit-*` / `--reserve-*` | Limites e reservas de CPU/memória |
| `--network` | Rede overlay |
| `--secret`, `--config` | Segredos e configurações |
| `--update-*` / `--rollback-*` | Estratégia de atualização |

> [!info] Routing mesh
> Ao publicar uma porta, **todos os nós** a escutam e direcionam o tráfego a uma réplica saudável, mesmo que ela esteja em outro nó. Para contornar, use `mode=host` em `--publish`.

> [!warning] Dados persistentes
> Volumes locais ficam no nó onde a task rodou. Para bancos, fixe o serviço a um nó (`--constraint`) ou use armazenamento compartilhado. Veja [[Drivers de volume]].

## Exercício

Crie um serviço `web` com 3 réplicas, escale para 5, simule a queda de um container (`docker rm -f`) e observe o Swarm recriando a task com `docker service ps web`.

## Veja também

- [[Inicializando um Swarm]]
- [[Atualizações progressivas e rollback]]
- [[Stacks com docker stack deploy]]
- [[MOC - Swarm e Orquestração]]
