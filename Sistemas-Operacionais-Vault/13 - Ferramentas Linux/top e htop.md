---
titulo: "top e htop"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[ps]]"
  - "[[vmstat]]"
  - "[[CFS - Completely Fair Scheduler]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# top e htop

## Finalidade

Monitores **interativos** que atualizam periodicamente processos, CPU, memória e carga. O **htop** acrescenta cores, rolagem, árvore, mouse, busca e ações fáceis (matar, renice).

## Sintaxe

```bash
top                       # interativo
top -b -n 1 | head -20    # modo lote: uma amostra (para scripts)
top -H -p 1234            # threads de um processo
top -u ana                # processos de um usuário
htop                      # interface melhorada (instalar: apt/dnf install htop)
htop -t                   # árvore de processos
```

Teclas do `top`: `1` CPUs individuais, `M` ordena por memória, `P` por CPU, `T` por tempo, `k` mata, `r` renice, `H` threads, `c` linha de comando completa, `f` campos, `q` sai. No `htop`: `F5` árvore, `F6` ordenar, `F9` matar, `F7/F8` nice, `F4` filtrar, `F2` configuração.

## Saída comentada

```text
top - 14:05:11 up 3 days,  2:31,  2 users,  load average: 2.40, 1.95, 1.50
#                                          carga média de 1, 5 e 15 min (processos prontos + em D)
Tasks: 312 total,   2 running, 309 sleeping,   0 stopped,   1 zombie
%Cpu(s): 18.2 us,  4.1 sy,  0.0 ni, 75.9 id,  1.6 wa,  0.0 hi,  0.2 si,  0.0 st
#         usuário  sistema  nice   ocioso   E/S-wait   IRQ     softirq   steal (VM)
MiB Mem :  15920.0 total,   812.3 free,  9210.4 used,  5897.3 buff/cache
MiB Swap:   4096.0 total,  2800.0 free,  1296.0 used.  5800.1 avail Mem
#                                                      ^ memória disponível sem swap

  PID USER   PR  NI    VIRT    RES    SHR S  %CPU  %MEM   TIME+ COMMAND
 2210 ana    20   0 3120400 217000  90000 S  85.0   1.3  3:12.4 firefox
#                               ^RES residente   ^S estado   ^%CPU pode passar de 100% (multicore)
```

## Interpretando

| Indicador | Leitura |
|---|---|
| **load average** | Compare com o número de CPUs (`nproc`): carga ≈ nº de CPUs = saturado |
| `us` alto | Aplicações consomem CPU |
| `sy` alto | Muito tempo no kernel (syscalls, interrupções, trocas) |
| `wa` alto | CPU ociosa esperando disco/rede: gargalo de E/S ([[iostat]]) |
| `st` alto | VM sofrendo disputa do hypervisor |
| `si/hi` altos | Interrupções (rede) |
| `avail Mem` baixo e swap crescendo | Pressão de memória ([[free]], [[vmstat]]) |

> [!tip] Carga e E/S
> No Linux, o *load average* conta processos em estado `D` também; carga alta com CPU ociosa aponta para disco/NFS.

## Receitas

```bash
top -b -n1 -o %MEM | head -15                   # maiores consumidores de memória
htop -p $(pgrep -d, postgres)                   # só os processos do PostgreSQL
watch -n1 "ps -eo pid,%cpu,cmd --sort=-%cpu | head -5"
uptime; nproc                                   # carga x núcleos
```

## Alternativas

`btop` (visual completo), `glances`, `atop` (histórico), `nmon`, `bpytop`; para disco `iotop`, rede `iftop`/`nethogs`.

## Pontos-chave

- Olhe carga, `%CPU`, `wa` e memória *available*.
- `htop` facilita ações; `top` está sempre instalado.
- Para histórico use `atop`/`sar`; para análise fina, `perf`/`strace`.

## Veja também

[[ps]] · [[vmstat]] · [[MOC - Ferramentas Nativas do Linux]]
