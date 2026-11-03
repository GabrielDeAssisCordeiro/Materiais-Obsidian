---
titulo: "ps"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[top e htop]]"
  - "[[Estados de Processo]]"
  - "[[Processos]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# ps

## Finalidade

Mostra uma **foto instantânea** dos processos (diferente do [[top e htop|top]], que atualiza). Lê dados do `/proc` ([[PCB - Process Control Block]]).

## Sintaxe

```bash
ps [opções]
ps aux                  # estilo BSD: todos os processos, formato de usuário
ps -ef                  # estilo UNIX: todos, formato completo (mostra PPID)
ps -eo pid,ppid,stat,%cpu,%mem,etime,cmd --sort=-%cpu | head
ps -fp 1234             # processo específico
ps -eLf                 # inclui threads (LWP)
ps --forest -e          # árvore de processos
ps -u ana               # processos de um usuário
```

## Colunas úteis

| Coluna | Significado |
|---|---|
| `PID`, `PPID` | Identificador e pai |
| `USER` | Dono |
| `%CPU`, `%MEM` | Uso (CPU = tempo de CPU / tempo decorrido) |
| `VSZ`, `RSS` | Memória virtual e **residente** (KiB) |
| `STAT` | Estado: `R`, `S`, `D`, `T`, `Z`; sufixos `s` líder de sessão, `+` primeiro plano, `l` multithread, `<` alta prioridade, `N` baixa |
| `START`, `TIME` | Início e CPU acumulada |
| `NI`, `PRI` | Nice e prioridade |
| `WCHAN` | Função do kernel em que dorme |

## Exemplo com saída comentada

```bash
$ ps aux --sort=-%mem | head -4
USER     PID %CPU %MEM    VSZ   RSS TTY   STAT START   TIME COMMAND
postgres 912  1.2 12.4 982340 504120 ?    Ss   09:01   0:41 postgres: main
ana     2210  8.5  5.3 3120400 217000 ?   Sl   09:30   3:12 firefox
root       1  0.0  0.1 168000 11500 ?     Ss   08:58   0:03 /sbin/init
# STAT Ss: dormindo (S) e líder de sessão (s)   Sl: dormindo e multithread (l)
```

## Receitas

```bash
ps -eo stat,pid,ppid,cmd | awk '$1 ~ /^Z/'            # zumbis
ps -eo stat,pid,cmd | awk '$1 ~ /^D/'                 # em espera ininterruptível (E/S)
ps -p $(pgrep -d, nginx) -o pid,etime,rss,cmd         # processos por nome
ps -o pid,ni,cls,pri,cmd -p $$                        # escalonamento do shell
ps -eo pid,comm,wchan:20 | head                       # onde dormem no kernel
```

## Vantagens e limites

| Vantagens | Limites |
|---|---|
| Disponível em todo UNIX; ótima para *scripts* | Não é dinâmico |
| Formato personalizável (`-o`) | `%CPU` do `ps` é média de vida do processo, não instantânea |
| Mostra hierarquia e threads | RSS soma páginas compartilhadas (use `smem`/PSS para precisão) |

## Pontos-chave

- `ps aux` e `ps -ef` são os dois idiomas; `-o` personaliza.
- Estado `D` e `Z` indicam problemas.
- Use com `grep`/`awk`; prefira `pgrep` para buscar por nome.

## Veja também

[[top e htop]] · [[Estados de Processo]] · [[MOC - Ferramentas Nativas do Linux]]
