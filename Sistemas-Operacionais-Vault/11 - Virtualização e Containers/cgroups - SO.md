---
titulo: "cgroups - SO"
tags:
  - sistemas-operacionais
  - conceito
  - virtualizacao
tipo: conceito
nivel: avancado
relacionados:
  - "[[Containers]]"
  - "[[Namespaces do Linux - SO]]"
  - "[[CFS - Completely Fair Scheduler]]"
  - "[[Init e systemd]]"
  - "[[Memória Virtual]]"
---

# cgroups - SO

## Resumo

Os **control groups** (cgroups) organizam processos em uma **hierarquia** e **limitam, contabilizam e priorizam** o uso de recursos (CPU, memória, E/S, PIDs, rede via eBPF). É o mecanismo de **"quanto o contêiner pode usar"** ([[Containers]]) e é usado por todo serviço do [[Init e systemd|systemd]].

## cgroup v2 (hierarquia unificada)

```mermaid
flowchart TB
    R[/sys/fs/cgroup: raiz] --> SYS[system.slice: serviços]
    R --> USR[user.slice: sessões de usuário]
    R --> DK[docker/ ou machine.slice: contêineres]
    SYS --> SSH[sshd.service]
    SYS --> DB[postgresql.service]
    DK --> C1[contêiner 1]
    DK --> C2[contêiner 2]
```

Cada diretório é um cgroup; mover o PID de um processo para `cgroup.procs` o coloca no grupo. **Controladores** são habilitados em `cgroup.subtree_control`.

## Controladores principais

| Controlador | Arquivos importantes | Efeito |
|---|---|---|
| **cpu** | `cpu.weight` (1-10000), `cpu.max` (`quota period`) | Peso relativo ([[CFS - Completely Fair Scheduler]]) e teto absoluto |
| **cpuset** | `cpuset.cpus`, `cpuset.mems` | Restringe CPUs e nós NUMA |
| **memory** | `memory.max`, `memory.high`, `memory.swap.max`, `memory.current`, `memory.events` | Limite rígido (OOM), limite suave (*throttle*), contabilidade |
| **io** | `io.max`, `io.weight`, `io.stat` | Largura de banda/IOPS por dispositivo |
| **pids** | `pids.max` | Limita número de processos (anti *fork bomb*) |
| **hugetlb, rdma, misc** | - | Outros recursos |
| **freezer** | `cgroup.freeze` | Congela todos os processos |

## Uso manual

```bash
mount | grep cgroup2                                   # /sys/fs/cgroup tipo cgroup2
cat /sys/fs/cgroup/cgroup.controllers                  # controladores disponíveis

sudo mkdir /sys/fs/cgroup/teste
echo "+cpu +memory +pids" | sudo tee /sys/fs/cgroup/cgroup.subtree_control
echo "20000 100000"  | sudo tee /sys/fs/cgroup/teste/cpu.max     # 20% de 1 CPU
echo 100M            | sudo tee /sys/fs/cgroup/teste/memory.max
echo 50              | sudo tee /sys/fs/cgroup/teste/pids.max
echo $$              | sudo tee /sys/fs/cgroup/teste/cgroup.procs # coloca o shell no grupo

# Teste: laço infinito consome só ~20% de CPU
sh -c 'while :; do :; done' &
top -b -n1 | head -10

# Memória acima de 100 MiB: o processo é morto pelo OOM do cgroup
cat /sys/fs/cgroup/teste/memory.events                 # contador oom_kill
```

Saída comentada (`memory.events`):

```text
low 0
high 0        # quantas vezes passou de memory.high (foi desacelerado)
max 4         # quantas vezes bateu em memory.max
oom 1         # entradas em OOM
oom_kill 1    # processos mortos pelo OOM dentro do cgroup
```

## Com systemd e Docker

```bash
sudo systemd-run --scope -p MemoryMax=300M -p CPUQuota=50% stress --vm 1 --vm-bytes 500M
systemd-cgtop                                          # top por cgroup
systemd-cgls                                           # árvore de cgroups
systemctl set-property meuapp.service CPUWeight=200 MemoryHigh=400M

docker run --cpus 1.5 --memory 512m --memory-swap 512m --pids-limit 200 --blkio-weight 300 alpine
docker stats                                           # uso por contêiner (lido dos cgroups)
cat /sys/fs/cgroup/system.slice/docker-<ID>.scope/memory.max
```

Kubernetes: `resources.requests` → `cpu.weight`/escalonamento; `resources.limits` → `cpu.max`/`memory.max`.

## cgroup v1 x v2

| Aspecto | v1 | v2 |
|---|---|---|
| Hierarquias | Uma por controlador | **Uma única** unificada |
| Regras | Processos em vários grupos | Processo em um cgroup folha |
| Memória + swap, E/S com buffer | Limitado | Melhor (`memory.swap`, `io` com *writeback*) |
| Delegação (rootless) | Difícil | Suportada |
| PSI e *pressure* | Parcial | `cpu.pressure`, `memory.pressure`, `io.pressure` |

```bash
stat -fc %T /sys/fs/cgroup/                            # cgroup2fs = v2
cat /sys/fs/cgroup/teste/memory.pressure               # some/full avg10: tempo de estagnação por memória
```

## Pontos de atenção

> [!warning] CPU quota x contêineres e latência
> `cpu.max` limita por **período** (ex.: 100 ms): ao esgotar a cota, **todos** os processos do grupo ficam parados até o próximo período (*throttling*), causando picos de latência em aplicações multithread. Prefira `cpu.weight` (justiça) quando não precisa de teto rígido.

> [!tip] Aplicações conscientes de contêiner
> JVM, Go e outros devem ler os limites do cgroup (`GOMAXPROCS`, `-XX:+UseContainerSupport`), ou superdimensionarão threads e heap.

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Limites e contabilidade por grupo de processos | Configuração fina é complexa |
| Evita vizinho barulhento e *fork bombs* | Quotas rígidas causam *throttling* |
| Base de contêineres, systemd, Kubernetes | Apenas Linux (Windows tem Job Objects; FreeBSD, `rctl`) |

## Pontos-chave

- cgroups limitam e medem recursos; [[Namespaces do Linux - SO]] isolam a visão.
- v2: hierarquia unificada, controladores `cpu`, `memory`, `io`, `pids`.
- `systemd-run`, `docker --memory/--cpus` e `systemd-cgtop` são os caminhos práticos.

## Veja também

[[Containers]] · [[Namespaces do Linux - SO]] · [[CFS - Completely Fair Scheduler]] · [[MOC - Virtualização e Containers]]
