---
titulo: "dtrace"
tags:
  - sistemas-operacionais
  - ferramenta
  - macos
tipo: ferramenta
nivel: avancado
relacionados:
  - "[[strace]]"
  - "[[fs_usage]]"
  - "[[System Calls]]"
  - "[[MOC - Ferramentas Nativas do macOS]]"
---

# dtrace

## Finalidade

Framework de **rastreamento dinâmico** (originário do Solaris) para observar kernel e aplicações em produção com baixo custo, sem recompilar. Equivale (e vai além) ao [[strace]] e se aproxima do eBPF/`perf` do Linux. Observa [[System Calls|syscalls]], funções, I/O, escalonamento.

## Modelo

Programa em **D**: `provedor:módulo:função:nome /predicado/ { ação }`.

```mermaid
flowchart LR
    A[Probes: syscall, proc, io, fbt, pid, profile] --> B[Predicado / filtro]
    B --> C[Ações: printf, count, quantize, ustack]
    C --> D[Agregações em buffers do kernel]
```

| Provedor | Uso |
|---|---|
| `syscall` | Entrada/saída de chamadas de sistema |
| `proc` | Criação e saída de processos |
| `io` | Operações de E/S de bloco |
| `profile` | Amostragem periódica (profiling) |
| `fbt` | Funções do kernel (*function boundary tracing*) |
| `pid` | Funções em processos de usuário |

## Exemplos

```bash
sudo dtrace -l | head                                         # lista probes
sudo dtrace -n 'syscall:::entry { @[execname] = count(); }'   # syscalls por programa (Ctrl+C mostra)
sudo dtrace -n 'syscall::open*:entry { printf("%s %s", execname, copyinstr(arg0)); }'
sudo dtrace -n 'proc:::exec-success { printf("%s", curpsinfo->pr_psargs); }'     # novos processos
sudo dtrace -n 'profile-997 /pid == $target/ { @[ustack()] = count(); }' -p 1234 # profiling por pilha
sudo dtrace -n 'syscall::read:entry { self->t = timestamp; }
                syscall::read:return /self->t/ { @["ns"] = quantize(timestamp - self->t); self->t = 0; }'
sudo dtruss -f -p 1234                                         # estilo strace (script D)
sudo dtruss -c ls                                              # contagem de syscalls
```

Saída de `quantize` (histograma):

```text
           value  ------------- Distribution ------------- count
            1024 |                                         0
            2048 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@            71
            4096 |@@@@@@@@@@@                             28
            8192 |@                                       3
```

## Restrições do macOS (SIP)

> [!warning] SIP
> Com o **System Integrity Protection** ativo, `dtrace` não rastreia processos protegidos da Apple nem o kernel completamente. Para depuração avançada, desative apenas as restrições de DTrace no modo de recuperação (`csrutil enable --without dtrace`), ciente do risco de segurança. Em Apple Silicon, também é preciso permitir *boot-args*/política reduzida.

Alternativas modernas: **Instruments** (Xcode), `sample`, `spindump`, `fs_usage`, `powermetrics`.

## Vantagens e desvantagens

| Vantagens | Desvantagens |
|---|---|
| Baixo overhead em produção, seguro (verificado) | Curva de aprendizado (linguagem D) |
| Rastreia kernel e usuário no mesmo script | Limitado pelo SIP no macOS |
| Agregações eficientes | Menos moderno que eBPF no Linux |

## Pontos-chave

- `sudo dtrace -n 'provedor:módulo:função:nome /pred/ { ação }'`.
- `dtruss` é o atalho estilo strace.
- SIP restringe o uso em processos da Apple.

## Veja também

[[strace]] · [[fs_usage]] · [[MOC - Ferramentas Nativas do macOS]]
