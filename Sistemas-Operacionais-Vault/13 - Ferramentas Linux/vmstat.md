---
titulo: "vmstat"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[free]]"
  - "[[iostat]]"
  - "[[Context Switch (Troca de Contexto)]]"
  - "[[Swap e Thrashing]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# vmstat

## Finalidade

Resumo **compacto e contínuo** de processos, memória, swap, E/S, interrupções, trocas de contexto e CPU. Ótimo primeiro olhar para classificar o gargalo.

## Sintaxe

```bash
vmstat                     # média desde o boot (linha única, pouco útil)
vmstat 1                   # uma linha por segundo (a primeira é a média desde o boot!)
vmstat 2 10                # 10 amostras a cada 2 s
vmstat -S M 1              # unidades em MiB
vmstat -a 1                # memória ativa/inativa
vmstat -d                  # estatísticas de disco
vmstat -s                  # contadores de memória e eventos
vmstat -w 1                # saída larga
```

## Saída comentada

```text
$ vmstat 1 3
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 3  1 131072 812340  90112 2012300    0    0   120   450  2100 4800 22  6 70  2  0
```

| Grupo | Coluna | Significado |
|---|---|---|
| procs | `r` | Processos **prontos/executando**; `r` > nº de CPUs = CPU saturada |
| procs | `b` | Processos bloqueados em E/S (`D`) |
| memory | `swpd`, `free`, `buff`, `cache` | KiB de swap usado, livre, buffers e cache |
| swap | `si` / `so` | KiB/s lidos/escritos do swap: **> 0 constante = pressão de memória** |
| io | `bi` / `bo` | Blocos/s lidos/escritos em dispositivos de bloco |
| system | `in` | Interrupções/s |
| system | `cs` | **Trocas de contexto/s** ([[Context Switch (Troca de Contexto)]]) |
| cpu | `us`, `sy`, `id`, `wa`, `st` | Usuário, sistema, ocioso, **espera por E/S**, *steal* |

## Padrões típicos

| Padrão | Diagnóstico |
|---|---|
| `r` alto, `us` alto, `id` baixo | **CPU saturada**; achar o processo com `top` |
| `wa` alto, `b` > 0, `bi/bo` altos | **Gargalo de disco**: [[iostat]] |
| `si/so` > 0 continuamente, `free` baixo | **Falta de memória**: [[Swap e Thrashing|thrashing]] |
| `cs` e `in` muito altos, `sy` alto | Muitas threads/travas ou tempestade de interrupções |
| `st` alto | VM disputando CPU com outras VMs |

## Exemplos

```bash
vmstat 1 | awk 'NR>2 {print strftime("%T"), $1, $2, $7, $8, $15, $16}'    # r b si so id wa com hora
vmstat -d | head                                                         # discos
stress --cpu 4 --timeout 10 & vmstat 1 10                                # veja r e us subirem
```

## Pontos-chave

- Ignore a primeira linha (média desde o boot).
- `r`, `b`, `si/so`, `wa` e `cs` revelam o tipo de gargalo.
- Aprofunde com [[iostat]], [[top e htop|top]], `pidstat`, `perf`.

## Veja também

[[free]] · [[iostat]] · [[MOC - Ferramentas Nativas do Linux]]
