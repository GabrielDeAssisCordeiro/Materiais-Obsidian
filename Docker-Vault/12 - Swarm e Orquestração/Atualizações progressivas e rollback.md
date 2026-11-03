---
tags:
  - docker
  - swarm
  - rolling-update
  - rollback
  - deploy
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comando docker service]]"
  - "[[Stacks com docker stack deploy]]"
  - "[[Estratégias de rollout]]"
---

# Atualizações progressivas e rollback

Um **rolling update** substitui as réplicas gradualmente, mantendo o serviço disponível.

```bash
docker service create --name web --replicas 4 \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-order start-first \
  --update-failure-action rollback \
  --health-cmd "wget -qO- http://127.0.0.1/ || exit 1" \
  nginx:1.26

# Atualizar a imagem
docker service update --image nginx:1.27 web

# Acompanhar
docker service ps web
docker service inspect --pretty web | grep -A5 -i update

# Reverter manualmente
docker service rollback web
```

| Parâmetro | Significado |
|---|---|
| `--update-parallelism` | Quantas tasks atualizar por vez |
| `--update-delay` | Intervalo entre lotes |
| `--update-order` | `stop-first` (padrão) ou `start-first` (sobe a nova antes de parar a antiga, **sem queda**) |
| `--update-failure-action` | `pause`, `continue` ou `rollback` |
| `--update-monitor` | Janela para detectar falhas após cada lote |
| `--rollback-*` | Mesmos parâmetros para a reversão |

> [!tip] Healthchecks são essenciais
> Sem healthcheck, o Swarm considera a task "saudável" assim que o processo inicia. Com healthcheck, ele só avança quando a nova versão está realmente pronta e faz rollback se falhar.

> [!info] Compatibilidade de versões
> Durante o update coexistem versões antigas e novas. Mudanças de esquema de banco de dados devem ser **retrocompatíveis** (expandir, migrar, contrair).

## Exercício

Faça um update de `nginx:1.26` para uma tag inexistente com `--update-failure-action rollback` e observe a reversão automática.

## Veja também

- [[Comando docker service]]
- [[Stacks com docker stack deploy]]
- [[Estratégias de rollout]]
- [[MOC - Swarm e Orquestração]]
