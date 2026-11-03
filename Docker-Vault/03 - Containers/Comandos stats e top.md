---
tags:
  - docker
  - containers
  - comandos
  - monitoramento
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Limites de recursos - Docker]]"
  - "[[Cgroups - Docker]]"
  - "[[Comando docker inspect]]"
  - "[[Comando docker logs]]"
---

# Comandos stats e top

## `docker stats`: consumo em tempo real

```bash
docker stats                         # todos os containers em execução (atualiza continuamente)
docker stats --no-stream             # uma leitura e sai
docker stats web db                  # containers específicos
docker stats --no-stream --format 'table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.PIDs}}'
```

| Coluna | Significado |
|---|---|
| `CPU %` | Uso de CPU (100% = um núcleo; pode passar de 100% em multi-core) |
| `MEM USAGE / LIMIT` | Memória usada e limite do cgroup |
| `NET I/O` | Tráfego de rede acumulado |
| `BLOCK I/O` | Leitura/escrita em disco acumuladas |
| `PIDS` | Número de processos |

## `docker top`: processos dentro do container

```bash
docker top web
docker top web -o pid,user,args      # opções do ps
```

> [!info] Sem limite, o "LIMIT" é a memória do host
> Se `MEM USAGE / LIMIT` mostra a memória total da máquina, o container não tem limite configurado. Veja [[Limites de recursos - Docker]].

> [!tip] Para métricas históricas
> `docker stats` é instantâneo. Para histórico e alertas, use cAdvisor + Prometheus + Grafana (veja a pasta de Observabilidade).

## Exercício

Suba um container que consome CPU (`docker run -d --name cpu alpine sh -c 'while :; do :; done'`), observe com `docker stats` e depois limite com `docker update --cpus 0.5 cpu`.

## Veja também

- [[Limites de recursos - Docker]]
- [[Cgroups - Docker]]
- [[Comando docker inspect]]
- [[Comando docker logs]]
- [[MOC - Containers]]
