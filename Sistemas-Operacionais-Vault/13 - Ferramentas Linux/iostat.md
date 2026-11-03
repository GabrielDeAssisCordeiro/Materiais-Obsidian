---
titulo: "iostat"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[vmstat]]"
  - "[[Escalonadores de Disco]]"
  - "[[Dispositivos de Bloco e de Caractere]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# iostat

## Finalidade

Mostra **estatísticas de CPU e de dispositivos de bloco**: IOPS, vazão, latência, tamanho da fila e saturação. Parte do pacote `sysstat` (`apt install sysstat`). Lê `/proc/diskstats`.

## Sintaxe

```bash
iostat                    # desde o boot
iostat -x 1               # estendido, a cada 1 s (o mais útil)
iostat -xz 1              # omite dispositivos ociosos
iostat -xm 2 5            # em MB/s, 5 amostras
iostat -p sda 1           # inclui partições
iostat -c                 # só CPU;  iostat -d  só disco
iostat -t                 # com hora
```

## Saída comentada (`-x`)

```text
$ iostat -xz 1
avg-cpu: %user %nice %system %iowait %steal %idle
          12.0   0.0     5.0    18.5    0.0  64.5

Device   r/s    w/s   rMB/s  wMB/s  r_await w_await aqu-sz  rareq-sz wareq-sz %util
sda     85.0   40.0    3.4    1.2     11.2    28.4    3.10     41.0     30.7   97.0
nvme0n1 1200   800    75.0   40.0     0.15    0.30    0.40     64.0     51.2   30.0
```

| Coluna | Significado |
|---|---|
| `r/s`, `w/s` | **IOPS** de leitura/escrita |
| `rMB/s`, `wMB/s` | Vazão |
| `r_await`, `w_await` | **Latência média** (fila + serviço) em ms |
| `aqu-sz` (antes `avgqu-sz`) | Tamanho médio da fila |
| `rareq-sz`, `wareq-sz` | Tamanho médio das requisições (KiB) |
| `%util` | Tempo em que o dispositivo teve E/S em andamento |
| `%iowait` (CPU) | CPU ociosa esperando E/S |

## Interpretação

| Sinal | Significado |
|---|---|
| **`%util` ~100% + `await` alto + fila crescente** | HDD/dispositivo **saturado** |
| `%util` 100% em **NVMe/SSD** com `await` baixo | Não significa saturação (paralelismo interno): olhe latência e fila |
| `await` alto com poucas IOPS | Dispositivo lento ou com erro (cheque `dmesg`, SMART) |
| `wareq-sz` pequeno e muitas IOPS | Escritas pequenas e aleatórias (use buffering, melhor FS, SSD) |
| `%iowait` alto | Gargalo de disco/rede-FS |

> [!tip] Rotina
> Compare `r/s + w/s` com a capacidade (HDD ~100-200 IOPS; SSD SATA ~50-100 K; NVMe centenas de milhares) e a latência esperada (HDD ~10 ms, SSD ~0,1 ms).

## Ferramentas complementares

```bash
sudo iotop -o                  # processos que mais fazem E/S (ou: pidstat -d 1)
sudo smartctl -a /dev/sda      # saúde SMART
lsblk -d -o NAME,ROTA,SCHED    # tipo (HDD=1) e escalonador
sudo fio --name=teste --rw=randread --bs=4k --size=1G --runtime=20 --direct=1 --filename=/dev/sdX  # benchmark
dmesg | grep -iE "I/O error|ata[0-9]|nvme"
```

## Pontos-chave

- Use `iostat -xz 1`; observe `await`, `aqu-sz`, `%util` e tamanho de requisição.
- `%util` não indica saturação em dispositivos paralelos (SSD/NVMe).
- Combine com [[vmstat]] (`wa`, `b`) e `iotop`/`pidstat -d` para achar o processo.

## Veja também

[[vmstat]] · [[Escalonadores de Disco]] · [[MOC - Ferramentas Nativas do Linux]]
