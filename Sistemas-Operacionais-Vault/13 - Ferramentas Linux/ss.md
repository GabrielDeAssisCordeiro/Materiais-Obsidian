---
titulo: "ss"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[ip]]"
  - "[[Sockets]]"
  - "[[lsof]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# ss

## Finalidade

**Socket Statistics**: lista e filtra **sockets** ([[Sockets]]) lendo diretamente do kernel (netlink); sucessor mais rápido do `netstat`.

## Sintaxe

```bash
ss -tulpn                 # TCP+UDP, escutando, com processo, numérico  (o mais usado)
ss -tlnp                  # só TCP em escuta
ss -ulnp                  # só UDP
ss -tn                    # TCP estabelecidos (sem nomes)
ss -s                     # resumo estatístico
ss -a                     # todos os estados
ss -xlp                   # sockets UNIX
ss -ti                    # informações internas TCP (rtt, cwnd, retransmissões)
ss -o                     # temporizadores
ss -m                     # uso de memória por socket
ss -tn state established  # por estado
ss -tn state time-wait | wc -l
ss -tn dst 203.0.113.9    # por destino
ss -tn '( sport = :443 or dport = :443 )'
ss -tnp sport = :8080     # por porta de origem (local)
ss -4 / -6                # só IPv4 / IPv6
```

Flags: `-t` TCP, `-u` UDP, `-l` listening, `-p` processo (requer root para outros), `-n` numérico, `-a` todos, `-e` detalhes, `-r` resolve nomes.

## Saída comentada

```text
$ sudo ss -tlnp
State   Recv-Q  Send-Q   Local Address:Port   Peer Address:Port  Process
LISTEN  0       511            0.0.0.0:80          0.0.0.0:*     users:(("nginx",pid=1304,fd=6))
LISTEN  0       128               [::]:22             [::]:*     users:(("sshd",pid=822,fd=4))
LISTEN  0       4096         127.0.0.1:5432          0.0.0.0:*     users:(("postgres",pid=912,fd=5))
# 0.0.0.0 = todas as interfaces (exposto); 127.0.0.1 = só local
# Em LISTEN: Recv-Q = conexões na fila de accept; Send-Q = tamanho máximo do backlog
```

| Estado TCP | Significado |
|---|---|
| `LISTEN` | Aguardando conexões |
| `ESTAB` | Conexão estabelecida |
| `SYN-SENT`/`SYN-RECV` | Handshake em andamento |
| `TIME-WAIT` | Fechada; aguardando 2×MSL |
| `CLOSE-WAIT` | Peer fechou; a **aplicação local ainda não fechou** (vazamento de sockets) |
| `FIN-WAIT-1/2`, `LAST-ACK` | Encerramento |

## Diagnósticos

```bash
# Quem usa a porta 8080?
sudo ss -tlnp 'sport = :8080'

# Conexões por estado
ss -tan | awk 'NR>1 {c[$1]++} END {for (s in c) print s, c[s]}'

# Muitos CLOSE-WAIT → app não fecha conexões
ss -tanp state close-wait | head

# Top de IPs conectados à porta 443
ss -tn '( sport = :443 )' | awk 'NR>1 {split($5,a,":"); print a[1]}' | sort | uniq -c | sort -rn | head

# Qualidade da conexão (retransmissões, RTT)
ss -ti dst 203.0.113.9 | head -4

# Fila de accept cheia (Recv-Q alto em LISTEN) → aplicação lenta ou backlog pequeno
ss -ltn 'sport = :80'
sysctl net.core.somaxconn
```

```bash
# Equivalências com ferramentas antigas
netstat -tulpn     →  ss -tulpn
netstat -s         →  ss -s  (ou nstat)
```

> [!tip] Limites de descritores
> Muitos sockets exigem `ulimit -n` alto e ajustes (`net.ipv4.ip_local_port_range`, `tcp_tw_reuse`). Veja `/proc/net/sockstat`.

## Pontos-chave

- `ss -tulpn` mostra serviços em escuta e processos.
- Filtros por estado e porta evitam `grep` desnecessário.
- `CLOSE-WAIT` acumulado indica bug na aplicação.

## Veja também

[[ip]] · [[Sockets]] · [[lsof]] · [[MOC - Ferramentas Nativas do Linux]]
