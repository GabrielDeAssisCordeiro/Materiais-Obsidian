---
tags:
  - seguranca
aliases:
  - "Resource limits"
  - "Quotas"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Cgroups]]"
  - "[[Criar Sandbox com Docker]]"
---
# Limites de Recursos

Limites protegem contra negação de serviço (acidental ou intencional).

| Recurso | Docker | Observação |
|---|---|---|
| Memória | `--memory 256m --memory-swap 256m` | Sem swap extra |
| CPU | `--cpus 0.5` | Fração de núcleo |
| Processos | `--pids-limit 100` | Contra *fork bombs* |
| Disco | `--tmpfs ...:size=64m`, quotas do storage driver | Evita encher o disco |
| Tempo | Timeout no orquestrador + `docker kill` | O Docker não tem timeout nativo |
| Arquivos abertos | `--ulimit nofile=1024:1024` | |
| Saída/logs | `--log-opt max-size=10m` | |

> [!danger] Sem limite de tempo, uma sandbox pode rodar para sempre
> Sempre imponha *timeout* externo.

## Exercício

Rode um laço que consome memória em um container com `--memory 128m` e observe o OOM kill com `docker inspect`.

## Veja também

- [[Cgroups]]
- [[Criar Sandbox com Docker]]
- [[Logs e Monitoramento]]
- [[MOC - Cuidados e Segurança]]
