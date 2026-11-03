---
titulo: "strace"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[System Calls]]"
  - "[[lsof]]"
  - "[[Sinais]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# strace

## Finalidade

**Rastreia as [[System Calls|chamadas de sistema]]** e sinais de um processo, mostrando argumentos, retorno e erros. Usa `ptrace`. Excelente para descobrir **por que um programa falha** (arquivo não encontrado, permissão, rede) sem ter o código-fonte.

## Sintaxe

```bash
strace [opções] comando [args]       # inicia e rastreia
strace -p PID                        # anexa a um processo em execução
strace -f ...                        # segue filhos (fork/threads)
strace -e trace=openat,read,write ...# filtra chamadas
strace -e trace=file|network|process|memory|signal ...   # classes
strace -c ...                        # resumo estatístico por syscall
strace -T ...                        # tempo gasto em cada chamada
strace -tt ...                       # carimbo de tempo com microssegundos
strace -s 200 ...                    # tamanho de strings exibidas
strace -o saida.txt ...              # grava em arquivo
strace -y ...                        # mostra caminho dos descritores
```

## Exemplo 1: por que não abre o arquivo?

```bash
$ strace -e trace=openat ./meuprograma
openat(AT_FDCWD, "/etc/meuapp.conf", O_RDONLY) = -1 ENOENT (No such file or directory)
#                                                  ^ falhou: arquivo não existe
openat(AT_FDCWD, "/home/ana/.meuapp", O_RDONLY) = 3     # usou o fallback, fd 3
```

## Exemplo 2: resumo e gargalos

```bash
$ strace -c -f ls -R /usr > /dev/null
% time     seconds  usecs/call     calls    errors syscall
 52.10    0.021     12           1730         getdents64    # listar diretórios
 30.40    0.012      3           3900         newfstatat    # stat em cada arquivo
  8.20    0.003      2           1500         openat
# mostra onde o tempo vai e quantas chamadas falham (errors)
```

## Exemplo 3: processo travado

```bash
sudo strace -p 4321 -T
read(5, <unfinished ...>        # bloqueado lendo o descritor 5 (possível socket/pipe sem dados)
ls -l /proc/4321/fd/5           # descobre o que é
```

```bash
# Rastrear conexões de rede de um comando
strace -f -e trace=network curl -s https://exemplo.com > /dev/null
# connect(3, {sa_family=AF_INET, sin_port=htons(443), sin_addr=inet_addr("93.184.216.34")}, 16) = 0
```

## Leitura de uma linha

```text
openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC) = 3
│       │                        │                    └ retorno (fd 3; -1 = erro + errno)
│       │                        └ flags
│       └ argumentos
└ nome da syscall
```

## Quando não usar / cuidados

> [!warning] Sobrecarga e privacidade
> O `ptrace` deixa o processo **10x a 100x mais lento**; evite em produção sob carga (use `perf trace`, `bpftrace`, `BCC`/`eBPF`). O rastreio pode expor senhas e dados (strings lidas/escritas): proteja o arquivo de saída.

## Alternativas

`ltrace` (chamadas de biblioteca), `perf trace`, `bpftrace`, `ftrace`, `sysdig`, `gdb`; no macOS `dtruss`/`fs_usage`; no Windows, Process Monitor.

## Pontos-chave

- `strace -f -e trace=... -o arq` é o padrão de investigação.
- `ENOENT`, `EACCES`, `ECONNREFUSED` explicam a maioria das falhas.
- `-c` e `-T` revelam onde o tempo é gasto.

## Veja também

[[System Calls]] · [[lsof]] · [[MOC - Ferramentas Nativas do Linux]]
