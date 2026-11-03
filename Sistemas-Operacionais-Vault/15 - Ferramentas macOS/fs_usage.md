---
titulo: "fs_usage"
tags:
  - sistemas-operacionais
  - ferramenta
  - macos
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[dtrace]]"
  - "[[strace]]"
  - "[[lsof]]"
  - "[[MOC - Ferramentas Nativas do macOS]]"
---

# fs_usage

## Finalidade

Exibe em tempo real **chamadas de sistema e operações do sistema de arquivos, rede, page faults e eventos de memória virtual** de processos. Responde "quem está acessando este arquivo/disco agora?". Equivale ao [[strace]] filtrado por E/S e ao Process Monitor do Windows. Requer `sudo`.

## Sintaxe

```bash
sudo fs_usage                        # tudo (muito verboso)
sudo fs_usage -w -f filesys          # só sistema de arquivos, linha larga
sudo fs_usage -w -f network          # operações de rede
sudo fs_usage -w -f pathname         # operações com caminhos
sudo fs_usage -w -f diskio           # E/S de disco
sudo fs_usage -w -f cachehit         # inclui acertos de cache
sudo fs_usage -w Safari              # filtra por nome de processo
sudo fs_usage -w -f filesys 1234     # por PID
sudo fs_usage -w -f filesys | grep -i "\.log"
```

Filtros (`-f`): `filesys`, `network`, `pathname`, `exec`, `diskio`, `cachehit`.

## Saída comentada

```text
12:01:03.211  open     F=5   (R_____)  /Users/ana/doc.txt    0.000042  Safari.1234
12:01:03.212  read     F=5   B=0x1000                        0.000015  Safari.1234
12:01:03.220  WrData[A]       D=0x0123  B=0x2000  /dev/disk3s5   0.002100  mds_stores.512
12:01:03.221  PgIn[...]       ...                                        0.000900  Slack.8801
```

| Campo | Significado |
|---|---|
| Hora | Timestamp |
| Chamada | `open`, `read`, `write`, `stat64`, `getattrlist`, `WrData` (escrita em disco), `RdData`, `PgIn` (page-in), `recvfrom`... |
| `F=` | Descritor de arquivo |
| `B=` | Bytes |
| `D=` | Bloco de disco |
| Tempo | Duração da operação em segundos (valores altos = lentidão) |
| Processo.TID | Nome e thread |

`[A]` = escrita assíncrona; `[S]` = síncrona.

## Casos de uso

1. **Disco ocupado sem causa aparente**: `sudo fs_usage -w -f diskio` revela `mds_stores` (Spotlight), `backupd` (Time Machine) ou `photoanalysisd`.
2. **App lento ao abrir**: veja operações lentas (tempos altos) e acessos repetidos a muitos arquivos.
3. **Arquivo de configuração lido**: filtre por processo e pelo nome do arquivo.
4. **Malware/exfiltração**: operações de rede inesperadas de processos desconhecidos.

## Relacionados

```bash
sudo lsof -p 1234            # arquivos abertos
lsof -i :8080                # quem usa a porta
sudo opensnoop               # (dtrace) aberturas de arquivos
iostat -d 1 5                # taxa de disco
sudo dtruss -t open -p 1234  # syscalls específicas
```

> [!warning] SIP
> Com SIP, alguns processos protegidos têm detalhes omitidos. A saída é volumosa: filtre por processo ou grep.

## Pontos-chave

- `sudo fs_usage -w -f filesys <processo>`: ferramenta rápida de "quem toca em quê".
- Coluna final de tempo mostra operações lentas.
- Para análises programáveis, use [[dtrace]].

## Veja também

[[dtrace]] · [[lsof]] · [[MOC - Ferramentas Nativas do macOS]]
