---
tags:
  - docker
  - fundamentos
  - kernel
  - recursos
  - cgroups
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Namespaces]]"
  - "[[Containers vs Máquinas Virtuais]]"
  - "[[Union filesystems e OverlayFS]]"
  - "[[Comando docker run]]"
---

# Cgroups - Docker

**Control groups (cgroups)** limitam, contabilizam e priorizam o uso de recursos (CPU, memória, I/O, número de processos) por grupos de processos. Se os namespaces definem o que o container *vê*, os cgroups definem o quanto ele *pode usar*.

## cgroup v1 vs v2

| Aspecto | v1 | v2 |
|---|---|---|
| Hierarquia | Várias (uma por controlador) | Única e unificada |
| Disponibilidade | Legado | Padrão nas distribuições atuais |
| Verificação | — | `stat -fc %T /sys/fs/cgroup` retorna `cgroup2fs` |

```bash
# Descobre a versão do cgroup usada pelo daemon
docker info --format '{{.CgroupVersion}}'
```

## Limites via Docker

```bash
# Limita memória a 256 MiB e CPU a meio núcleo
docker run -d --name limitado --memory 256m --cpus 0.5 alpine sleep 600

# Confirma o limite dentro do container (cgroup v2): 268435456 bytes
docker exec limitado cat /sys/fs/cgroup/memory.max

# Consumo atual
docker stats --no-stream limitado

docker rm -f limitado
```

| Flag | Efeito |
|---|---|
| `--memory` / `-m` | Limite de memória; excedê-lo pode causar **OOM kill**. |
| `--memory-swap` | Memória + swap. |
| `--cpus` | Fração de CPUs (ex.: `1.5`). |
| `--cpu-shares` | Peso relativo em caso de disputa. |
| `--pids-limit` | Máximo de processos (proteção contra *fork bomb*). |

> [!bug] Container morto sem aviso (exit 137)
> Código de saída **137** (128 + SIGKILL) com `OOMKilled: true` em `docker inspect` indica que o container excedeu o limite de memória.
> ```bash
> docker inspect --format '{{.State.OOMKilled}} {{.State.ExitCode}}' NOME
> ```

> [!tip] Sempre defina limites em produção
> Sem limites, um container pode consumir toda a memória do host e derrubar outros serviços. Veja [[Comando docker run]].

## Exercício

Execute um container com `--memory 64m` rodando `sleep` e confirme o valor de `memory.max` dentro dele. Converta o número para MiB.

## Veja também

- [[Namespaces]]
- [[Containers vs Máquinas Virtuais]]
- [[Union filesystems e OverlayFS]]
- [[Comando docker run]]
- [[MOC - Fundamentos - Docker]]
