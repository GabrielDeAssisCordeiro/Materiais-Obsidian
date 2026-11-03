---
tags:
  - fundamentos
  - linux
  - kernel
aliases:
  - "Linux namespaces"
  - "ns"
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Cgroups]]"
  - "[[Capabilities do Linux]]"
  - "[[Sandbox por Containers]]"
  - "[[Isolamento e Contenção]]"
---
# Namespaces do Linux

**Namespaces** são um recurso do kernel Linux que particiona recursos globais de modo que cada grupo de processos veja **sua própria visão** deles. São o primeiro pilar dos containers (o segundo são os [[Cgroups]]).

## Tipos principais

| Namespace | Isola | Flag de `unshare` |
|---|---|---|
| `mnt` | Pontos de montagem | `--mount` |
| `pid` | Árvore de processos (PIDs) | `--pid` |
| `net` | Interfaces, rotas, firewall, portas | `--net` |
| `ipc` | Filas de mensagens, memória compartilhada | `--ipc` |
| `uts` | Hostname e domínio | `--uts` |
| `user` | Mapeamento de UIDs/GIDs | `--user` |
| `cgroup` | Visão da hierarquia de cgroups | `--cgroup` |
| `time` | Relógios monotônico/boot | `--time` |

## Experimentando (laboratório Linux)

```bash
# Novo namespace de PID, mount e usuário (sem precisar de root, se o sistema permitir)
unshare --user --map-root-user --pid --fork --mount-proc bash
ps aux        # só enxerga os próprios processos
hostname      # ainda é o do host (não isolamos uts)
exit

# Sem rede: apenas a interface loopback (e desativada)
unshare --user --map-root-user --net bash -c 'ip addr'

# Listar namespaces existentes
lsns
```

> [!info] Rootless depende de user namespaces
> Containers *rootless* (Podman, Docker rootless) usam user namespaces para mapear o "root" interno a um UID comum no host. Algumas distribuições restringem esse recurso por política — verifique `sysctl kernel.unprivileged_userns_clone` (Debian/Ubuntu) ou configurações do AppArmor.

> [!warning] Namespaces isolam *visão*, não *privilégio*
> Um processo com capabilities perigosas dentro do namespace ainda pode causar danos. Combine com [[Capabilities do Linux]], [[Seccomp]] e limites de [[Cgroups]].

## Exercício

Rode `unshare --user --map-root-user --pid --fork --mount-proc bash` e execute `echo $$` e `ps aux`. Por que o PID do shell é 1?

## Veja também

- [[Cgroups]]
- [[Capabilities do Linux]]
- [[Seccomp]]
- [[Sandbox por Containers]]
- [[Isolamento e Contenção]]
