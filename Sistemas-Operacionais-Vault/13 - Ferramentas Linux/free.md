---
titulo: "free"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[vmstat]]"
  - "[[Swap e Thrashing]]"
  - "[[Buffering, Cache e Spooling]]"
  - "[[Memória Virtual]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# free

## Finalidade

Mostra o **uso de memória física e de swap**. Lê `/proc/meminfo`.

## Sintaxe

```bash
free                # em KiB
free -h             # legível (Gi, Mi)
free -m             # em MiB
free -s 2           # atualiza a cada 2 s
free -h -w          # separa buffers e cache
free -t             # linha de total (RAM+swap)
```

## Saída comentada

```text
$ free -h
               total   used   free  shared  buff/cache  available
Mem:            15Gi   9.0Gi  812Mi   310Mi      5.8Gi      5.7Gi
Swap:          4.0Gi   1.3Gi  2.7Gi
```

| Coluna | Significado |
|---|---|
| `total` | RAM instalada (visível ao SO) |
| `used` | `total - free - buff/cache` (memória de processos e kernel) |
| `free` | Totalmente não usada (**baixo é normal**) |
| `shared` | `tmpfs` e memória compartilhada |
| `buff/cache` | Cache de páginas e buffers do kernel; **recuperável** ([[Buffering, Cache e Spooling]]) |
| **`available`** | Estimativa do que dá para usar **sem recorrer ao swap**: a métrica correta |

> [!tip] "Minha memória está acabando!"
> O Linux usa a RAM ociosa como cache. Preocupe-se quando **`available`** é pequeno, o **swap** cresce, `vmstat` mostra `si/so` > 0 ou aparece `Out of memory` em `dmesg`.

## Diagnósticos

```bash
free -h; grep -E "MemAvailable|SwapCached|Dirty|Slab|Shmem" /proc/meminfo
ps -eo pid,rss,cmd --sort=-rss | head -5          # maiores consumidores
vmstat 1 5                                        # si/so: troca ativa
sudo dmesg | grep -i "out of memory"
cat /proc/pressure/memory                         # PSI
smem -tk | tail                                   # PSS: soma justa de memória compartilhada
```

Regra: `used` crescendo continuamente + `available` caindo = **vazamento** ou carga maior; swap alto com `si/so` ativos = **pressão** real.

## Limpeza de cache (só testes)

```bash
sync; echo 3 | sudo tee /proc/sys/vm/drop_caches   # não "libera memória" útil; só piora o desempenho
```

## Pontos-chave

- Olhe `available`, não `free`.
- Swap em uso ≠ problema; troca contínua (`si/so`) = problema.
- Combine com [[vmstat]] e `ps --sort=-rss`.

## Veja também

[[vmstat]] · [[Swap e Thrashing]] · [[MOC - Ferramentas Nativas do Linux]]
