---
tags:
  - docker
  - observabilidade
  - memoria
  - troubleshooting
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Limites de recursos - Docker]]"
  - "[[Cgroups - Docker]]"
  - "[[Comando docker events]]"
---

# Análise de OOM kill

**OOM kill** ocorre quando um processo excede o limite de memória do cgroup (ou a memória do host) e o kernel o encerra.

## Reproduzindo em laboratório

```bash
docker run --name oom -m 20m alpine:3.20 sh -c 'tail /dev/zero'
echo "exit code: $?"
docker inspect --format 'OOMKilled={{.State.OOMKilled}} exit={{.State.ExitCode}}' oom
docker rm oom
```

## Confirmando

```bash
# Estado do container
docker inspect --format '{{.State.OOMKilled}}' NOME

# Eventos
docker events --filter event=oom --since 1h

# Log do kernel no host
sudo dmesg -T | grep -iE 'out of memory|killed process'
journalctl -k | grep -i oom

# Contador do cgroup v2 (dentro do container)
docker exec NOME cat /sys/fs/cgroup/memory.events
```

## O que fazer

| Ação | Quando |
|---|---|
| Aumentar `--memory` | O limite está abaixo do uso legítimo |
| Corrigir vazamento de memória | O uso cresce sem parar (monitore com [[Métricas com cAdvisor, Prometheus e Grafana]]) |
| Configurar o runtime | JVM (`-XX:MaxRAMPercentage`), Node (`--max-old-space-size`), Python (limitar workers/cache) |
| Reduzir concorrência | Muitas threads/workers para a memória disponível |
| Usar `--memory-reservation` + limite | Margem para picos |
| Ajustar swap | `--memory-swap` igual a `--memory` desabilita swap |

> [!warning] OOM do host vs OOM do container
> Sem limites, o kernel do **host** pode encerrar qualquer processo (inclusive o `dockerd`). Defina limites em todos os containers.

> [!info] Exit code 137
> 137 = 128 + 9 (SIGKILL). Pode ser OOM **ou** `docker kill`/`docker stop` com timeout. Confirme com `OOMKilled`.

## Exercício

Reproduza o OOM com `-m 20m`, confirme com `OOMKilled`, `docker events` e `memory.events`. Depois aumente o limite e verifique a mudança.

## Veja também

- [[Limites de recursos - Docker]]
- [[Cgroups - Docker]]
- [[Comando docker events]]
- [[MOC - Observabilidade e Depuração]]
