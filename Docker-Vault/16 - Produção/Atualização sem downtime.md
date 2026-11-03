---
tags:
  - docker
  - producao
  - deploy
  - introducao
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Estratégias de rollout]]"
  - "[[Atualizações progressivas e rollback]]"
  - "[[Resiliência em produção]]"
  - "[[Proxy reverso com Traefik]]"
---

# Atualização sem downtime

Com **um único container** por serviço, `docker compose up -d` recria o container e há uma breve interrupção. Para evitá-la, é preciso **redundância** e um **ponto de entrada** que direcione tráfego apenas a instâncias saudáveis.

## Ingredientes

| Ingrediente | Função |
|---|---|
| ≥ 2 instâncias | Uma atende enquanto a outra é atualizada |
| Proxy/load balancer | Encaminha só para instâncias saudáveis |
| Healthchecks | Definem o que é "pronto" |
| Graceful shutdown | Conclui requisições em andamento |
| Migrações compatíveis | Versões antiga e nova convivem durante o deploy |

## Opção A: orquestrador (recomendado)

```bash
# Swarm: sobe a nova task antes de parar a antiga
docker service update --image meu-app:1.5.0 --update-order start-first --update-failure-action rollback api
```

Kubernetes e serviços gerenciados (ECS, Cloud Run, Container Apps) fazem isso nativamente.

## Opção B: Compose de um host com proxy (artesanal, ilustrativo)

```bash
# Serviço "app" sem container_name e sem porta publicada no host; o proxy roteia por rede/labels
docker compose pull app

# Sobe uma segunda instância com a nova imagem, mantendo a antiga
docker compose up -d --no-deps --scale app=2 --no-recreate app

# Aguarde ficar saudável; identifique e remova a instância antiga
docker ps --filter "label=com.docker.compose.service=app" --format '{{.ID}} {{.Image}} {{.Status}}'
docker stop ID_ANTIGO && docker rm ID_ANTIGO

# Volta a escala ao normal
docker compose up -d --no-deps --scale app=1 --no-recreate app
```

> [!question] Verificar na documentação oficial
> O comportamento de `--scale` com `--no-recreate` e a seleção de qual réplica é removida ao reduzir a escala devem ser validados no seu ambiente; trate o procedimento como ponto de partida e teste exaustivamente.

> [!tip] Quando não vale a pena
> Para sistemas internos ou blogs, uma interrupção de poucos segundos pode ser aceitável. Escolha a complexidade proporcional ao custo do downtime.

## Exercício

Monte um laboratório com Traefik e duas réplicas de `traefik/whoami`, e faça uma "atualização" medindo com um loop de `curl` se alguma requisição falha.

## Veja também

- [[Estratégias de rollout]]
- [[Atualizações progressivas e rollback]]
- [[Resiliência em produção]]
- [[Proxy reverso com Traefik]]
- [[MOC - Produção]]
