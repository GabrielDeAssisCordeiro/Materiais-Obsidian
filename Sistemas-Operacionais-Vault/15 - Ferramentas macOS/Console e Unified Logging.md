---
titulo: "Console e Unified Logging"
tags:
  - sistemas-operacionais
  - ferramenta
  - macos
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[journalctl]]"
  - "[[Event Viewer (Visualizador de Eventos)]]"
  - "[[dmesg]]"
  - "[[MOC - Ferramentas Nativas do macOS]]"
---

# Console e Unified Logging

## Finalidade

O **Console** é o visualizador gráfico do **Unified Logging System** (desde o macOS Sierra): um repositório binário, estruturado e eficiente que unifica logs do kernel, daemons e apps. Equivale ao [[journalctl]] e ao [[Event Viewer (Visualizador de Eventos)]]. A CLI é o comando `log`.

## Características

| Aspecto | Descrição |
|---|---|
| Armazenamento | Binário (`/var/db/diagnostics`, `tracev3`), não texto |
| Níveis | `default`, `info`, `debug`, `error`, `fault` |
| Metadados | processo, subsystem (`com.apple.xxx`), category, PID, thread |
| Privacidade | Valores dinâmicos aparecem como `<private>` (salvo configuração) |
| Desempenho | Compressão, entrada em memória e persistência seletiva (info/debug só em memória por padrão) |

## Uso do Console

Barra lateral: **Mensagens de Log**, **Relatórios de Falhas** (`.crash`/`.ips`), **Relatórios de Diagnóstico**, **Arquivos de log** (`/var/log`). Filtros por processo, subsystem, categoria e mensagem; salvar buscas.

## Comando `log`

```bash
log show --last 1h --predicate 'eventMessage CONTAINS "error"' | tail
log show --last 30m --predicate 'process == "Safari"' --info
log show --last 5m --predicate 'subsystem == "com.apple.bluetooth"' --debug
log stream --predicate 'process == "sshd"'                 # tempo real (tail -f)
log stream --level debug --predicate 'subsystem == "com.exemplo.app"'
log show --last 1d --predicate 'eventMessage CONTAINS "Kernel panic" OR messageType == fault'
sudo log collect --last 1h --output ~/Desktop/logs.logarchive   # exporta
log show --archive ~/Desktop/logs.logarchive
log config --status
```

Predicados NSPredicate: `process`, `processID`, `subsystem`, `category`, `messageType`, `eventMessage`, `sender`.

Gerando logs em scripts:

```bash
logger -p user.notice "Backup concluído"       # syslog clássico → Unified Logging
log show --last 1m --predicate 'eventMessage CONTAINS "Backup"'
```

## Outros diagnósticos

```bash
dmesg | tail                                    # buffer do kernel
ls ~/Library/Logs/DiagnosticReports             # relatórios de falha
sudo sysdiagnose -f ~/Desktop                   # coleta completa para suporte
```

> [!tip] Falhas de aplicativos
> Em *Relatórios de Falhas* veja `Exception Type` (ex.: `EXC_BAD_ACCESS`/SIGSEGV), `Crashed Thread` e a pilha de chamadas para identificar a causa.

## Pontos-chave

- Logs unificados em formato binário; consulte com `log show/stream` e predicados.
- `fault` e `error` são os mais úteis para diagnóstico.
- `sysdiagnose` e `log collect` para suporte.

## Veja também

[[journalctl]] · [[Event Viewer (Visualizador de Eventos)]] · [[MOC - Ferramentas Nativas do macOS]]
