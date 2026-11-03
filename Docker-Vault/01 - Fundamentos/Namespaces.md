---
tags:
  - docker
  - fundamentos
  - kernel
  - isolamento
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Cgroups - Docker]]"
  - "[[Containers vs Máquinas Virtuais]]"
  - "[[containerd e runc]]"
  - "[[Union filesystems e OverlayFS]]"
---

# Namespaces

**Namespaces** são um recurso do kernel Linux que dá a cada processo uma **visão isolada** de determinado recurso do sistema. É o que faz o container "achar" que tem seu próprio sistema.

## Tipos de namespace usados por containers

| Namespace | Isola | Efeito no container |
|---|---|---|
| `pid` | IDs de processo | O processo principal é o PID 1; não enxerga processos do host. |
| `net` | Interfaces, rotas, portas, iptables | Interface de rede e IP próprios. |
| `mnt` | Pontos de montagem | Sistema de arquivos raiz próprio. |
| `uts` | Hostname e domínio | Hostname próprio. |
| `ipc` | Memória compartilhada e filas SysV | IPC isolado. |
| `user` | UIDs e GIDs | Root no container pode mapear para usuário comum no host (user namespaces). |
| `cgroup` | Visão da hierarquia de cgroups | Vê apenas seu próprio cgroup. |
| `time` | Relógios monotônicos (kernel 5.6+) | Pouco usado em containers. |

## Demonstração segura em laboratório (Linux)

```bash
# Cria um novo namespace de PID e de montagem para um shell
sudo unshare --pid --fork --mount-proc bash

# Dentro do novo shell: só os processos deste namespace aparecem
ps aux
echo $$      # o shell é PID 1 neste namespace
exit
```

```bash
# Compare o hostname do host com o de um container
hostname
docker run --rm alpine hostname

# Container compartilhando o namespace de rede do host (--network host)
docker run --rm --network host alpine ip addr
```

> [!warning] Compartilhar namespaces reduz o isolamento
> Opções como `--pid=host`, `--network=host` e `--ipc=host` removem parte do isolamento. Use apenas quando necessário e entendendo o risco. Veja [[Princípio do menor privilégio - Docker]].

> [!tip] User namespaces
> Com [[Modo rootless]] ou `userns-remap`, o "root" do container é mapeado para um UID sem privilégios no host, reduzindo o impacto de um escape.

## Exercício

Rode `docker run --rm alpine ps` e, depois, `docker run --rm --pid=host alpine ps`. Explique a diferença e o risco do segundo comando.

## Veja também

- [[Cgroups - Docker]]
- [[Containers vs Máquinas Virtuais]]
- [[containerd e runc]]
- [[Union filesystems e OverlayFS]]
- [[MOC - Fundamentos - Docker]]
