---
tags:
  - fundamentos
  - linux
  - kernel
  - recursos
aliases:
  - "Control groups"
  - "cgroup v2"
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Namespaces do Linux]]"
  - "[[Capabilities do Linux]]"
  - "[[Isolamento e Contenção]]"
  - "[[Sandbox por Containers]]"
---
# Cgroups

**Cgroups** (*control groups*) limitam, contabilizam e priorizam o uso de recursos por grupos de processos: CPU, memória, E/S de disco, número de processos. Enquanto [[Namespaces do Linux]] controlam o que o processo **vê**, cgroups controlam quanto ele **consome**.

## cgroup v2 (unificado)

Principais arquivos em `/sys/fs/cgroup/<grupo>/`:

| Arquivo | Função |
|---|---|
| `memory.max` | Limite rígido de memória (excedeu → OOM kill no grupo) |
| `memory.high` | Limite brando (aplica pressão/redução) |
| `cpu.max` | Cota de CPU no formato `<quota> <periodo>` (µs) |
| `pids.max` | Máximo de processos (defesa contra *fork bomb*) |
| `io.max` | Limites de E/S por dispositivo |

```bash
# Verificar a versão em uso
stat -fc %T /sys/fs/cgroup     # cgroup2fs => v2

# Rodar um comando com limites via systemd (laboratório)
systemd-run --user --scope -p MemoryMax=200M -p CPUQuota=50% -p TasksMax=64 \
  python3 -c "print('ok')"
```

> [!question] Verificar na documentação oficial
> O uso de `systemd-run --user` com controladores de recursos exige delegação de cgroups ao usuário (comum em distribuições recentes com cgroup v2). Se falhar, rode como root ou consulte `man systemd.resource-control`.

## Equivalentes em containers

```bash
docker run --rm --memory=256m --memory-swap=256m --cpus=0.5 --pids-limit=100 alpine:3 sh -c 'echo limitado'
```

> [!danger] Sem limites, a sandbox vira vetor de negação de serviço
> Código não confiável sem `--memory`, `--cpus` e `--pids-limit` pode derrubar o host inteiro.

## Exercício

Rode um container com `--pids-limit=20` e tente criar muitos processos com `sh -c 'for i in $(seq 1 100); do sleep 30 & done'`. O que acontece?

## Veja também

- [[Namespaces do Linux]]
- [[Capabilities do Linux]]
- [[Sandbox por Containers]]
- [[Isolamento e Contenção]]
- [[Sandbox vs VM vs Container vs Jail vs chroot]]
