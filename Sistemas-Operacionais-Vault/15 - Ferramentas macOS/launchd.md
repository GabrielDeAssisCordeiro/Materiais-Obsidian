---
titulo: "launchd"
tags:
  - sistemas-operacionais
  - ferramenta
  - macos
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[Init e systemd]]"
  - "[[systemctl]]"
  - "[[cron]]"
  - "[[Task Scheduler (Agendador de Tarefas)]]"
  - "[[MOC - Ferramentas Nativas do macOS]]"
---

# launchd

## Finalidade

`launchd` é o **PID 1** do macOS: inicializa o sistema, inicia e supervisiona **daemons** (serviços do sistema) e **agents** (por usuário) e substitui `init`, `cron`, `inetd` e `xinetd`. Equivalente ao [[Init e systemd|systemd]]. Cada serviço é descrito por um arquivo **plist** (XML).

## Locais dos plists

| Diretório | Tipo | Roda como |
|---|---|---|
| `/System/Library/LaunchDaemons` | Daemons da Apple | root |
| `/Library/LaunchDaemons` | Daemons de terceiros | root, no boot |
| `/Library/LaunchAgents` | Agents globais | cada usuário, no login |
| `~/Library/LaunchAgents` | Agents do usuário | usuário, no login |

## Exemplo de plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.exemplo.backup</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/local/bin/backup.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>2</integer><key>Minute</key><integer>30</integer></dict>
  <key>StandardOutPath</key><string>/tmp/backup.out</string>
  <key>StandardErrorPath</key><string>/tmp/backup.err</string>
  <key>RunAtLoad</key><false/>
</dict>
</plist>
```

Chaves úteis: `KeepAlive` (reinicia se cair), `StartInterval` (segundos), `WatchPaths`, `RunAtLoad`, `UserName`, `EnvironmentVariables`.

## launchctl

```bash
launchctl list | grep exemplo                 # serviços carregados (PID, status, label)
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.exemplo.backup.plist   # carregar (moderno)
launchctl bootout   gui/$(id -u)/com.exemplo.backup                                # descarregar
launchctl kickstart -k gui/$(id -u)/com.exemplo.backup                             # executar agora
launchctl print gui/$(id -u)/com.exemplo.backup                                    # detalhes
sudo launchctl bootstrap system /Library/LaunchDaemons/com.exemplo.daemon.plist
launchctl disable gui/$(id -u)/com.exemplo.backup
plutil -lint arquivo.plist                    # valida sintaxe
# legado (ainda funciona): launchctl load -w arquivo.plist / unload
```

Saída comentada de `launchctl list`:

```text
PID   Status  Label
412   0       com.apple.Finder      # rodando (PID 412), status 0
-     0       com.exemplo.backup    # carregado, não ativo agora
-     78      com.exemplo.falha     # último código de saída 78 (erro)
```

Domínios: `system` (boot), `user/UID`, `gui/UID` (sessão gráfica).

## launchd x systemd x cron

| Aspecto | launchd | systemd | cron |
|---|---|---|---|
| Configuração | plist XML | unit INI | crontab |
| Agendamento | `StartCalendarInterval` | timers | sim |
| Supervisão | `KeepAlive` | `Restart=` | não |
| Ativação sob demanda | sockets/`Sockets` | socket units | não |
| Dependências | simples (implícitas) | ricas | não |

## Segurança

> [!warning] Persistência
> Plists em LaunchAgents/Daemons são vetor comum de **persistência** de malware. Monitore (*Itens de Login e Extensões* nas Configurações, `BlockBlock`) e use `launchctl print`.

## Pontos-chave

- PID 1; daemons (root) e agents (usuário) descritos em plists.
- Use `bootstrap/bootout` (moderno); `plutil -lint` valida.
- Substitui init, cron e inetd.

## Veja também

[[Init e systemd]] · [[cron]] · [[MOC - Ferramentas Nativas do macOS]]
