---
titulo: "lsof"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[ss]]"
  - "[[strace]]"
  - "[[Inodes]]"
  - "[[Sistemas de Arquivos - Conceitos]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# lsof

## Finalidade

**LiSt Open Files**: lista **arquivos abertos** por processos. Como em UNIX "tudo é arquivo", inclui arquivos comuns, diretórios, **sockets**, pipes, dispositivos e bibliotecas mapeadas.

## Sintaxe

```bash
lsof                          # tudo (muito grande)
lsof -p 1234                  # arquivos de um processo
lsof -u ana                   # de um usuário
lsof /var/log/syslog          # quem tem esse arquivo aberto?
lsof +D /mnt/dados            # tudo aberto dentro de um diretório (recursivo, lento)
lsof -i                       # conexões de rede
lsof -i :80                   # porta 80
lsof -i tcp -sTCP:LISTEN -P -n  # portas em escuta (-P sem nomes de porta, -n sem DNS)
lsof -c nginx                 # por nome do comando
lsof +L1                      # arquivos apagados (links = 0) ainda abertos
lsof -t arquivo               # só PIDs (útil em scripts)
```

Combinar filtros: por padrão são **OU**; `-a` faz **E**: `lsof -a -u ana -i`.

## Saída comentada

```text
$ sudo lsof -i :8080
COMMAND  PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
java    2210 app    45u  IPv6  31822      0t0  TCP *:8080 (LISTEN)
# FD: descritor (45) + modo (u = leitura/escrita, r, w)   TYPE: IPv6/REG/DIR/FIFO/unix
```

| Coluna FD | Significado |
|---|---|
| `cwd`, `rtd` | Diretório corrente e raiz |
| `txt` | Executável |
| `mem` | Bibliotecas e arquivos mapeados (`mmap`) |
| `0u 1u 2u` | stdin, stdout, stderr |
| número + `r/w/u` | Descritor aberto |

## Casos de uso

```bash
# 1. "Device or resource busy" ao desmontar
sudo lsof +f -- /mnt/usb          # quem usa?
sudo fuser -vm /mnt/usb           # alternativa

# 2. Disco cheio mas `du` não encontra o espaço (arquivo apagado ainda aberto)
sudo lsof +L1 | head
#   COMMAND PID USER FD TYPE SIZE NLINK NODE NAME
#   app    933 root 4w  REG  8.2G 0 /var/log/app.log (deleted)   <- libera ao reiniciar o app
#   Solução rápida: truncar via descritor
: > /proc/933/fd/4

# 3. Quem está usando a porta?
sudo lsof -iTCP:5432 -sTCP:LISTEN -n -P

# 4. Vazamento de descritores
lsof -p $(pgrep myapp) | wc -l
cat /proc/$(pgrep myapp)/limits | grep "open files"
ulimit -n

# 5. Conexões estabelecidas de um processo
lsof -a -p 2210 -i tcp -sTCP:ESTABLISHED
```

> [!tip] Sem lsof?
> `ls -l /proc/PID/fd` mostra os descritores abertos; `ss -tlnp` mostra sockets com processo.

## Pontos-chave

- Responde "quem está usando este arquivo/porta?".
- `lsof +L1` resolve o mistério do disco cheio.
- Execute como root para ver processos de outros usuários.

## Veja também

[[ss]] · [[strace]] · [[MOC - Ferramentas Nativas do Linux]]
