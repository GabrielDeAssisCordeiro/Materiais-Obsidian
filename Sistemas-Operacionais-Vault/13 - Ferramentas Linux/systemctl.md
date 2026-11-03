---
titulo: "systemctl"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[Init e systemd]]"
  - "[[journalctl]]"
  - "[[cron]]"
  - "[[cgroups - SO]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# systemctl

## Finalidade

Interface de controle do **systemd**: iniciar, parar, habilitar e inspecionar **unidades** (serviços, timers, sockets, montagens, alvos). Conceitos em [[Init e systemd]].

## Sintaxe

```bash
systemctl status nginx                  # estado, PID, cgroup, últimos logs
sudo systemctl start|stop|restart|reload nginx
sudo systemctl enable nginx             # inicia no boot
sudo systemctl enable --now nginx       # habilita e inicia agora
sudo systemctl disable --now nginx
sudo systemctl mask nginx               # impede qualquer início (link para /dev/null)
sudo systemctl unmask nginx
systemctl is-active nginx; systemctl is-enabled nginx; systemctl is-failed nginx
systemctl list-units --type=service --state=running
systemctl list-unit-files --state=enabled
systemctl --failed                      # unidades que falharam
systemctl list-timers                   # timers (alternativa ao cron)
systemctl list-dependencies multi-user.target
systemctl cat nginx                     # arquivo da unidade + drop-ins
sudo systemctl edit nginx               # cria override em /etc/systemd/system/nginx.service.d/
sudo systemctl daemon-reload            # relê arquivos de unidade após editar
systemctl get-default; sudo systemctl set-default multi-user.target
sudo systemctl isolate rescue.target    # modo de recuperação
sudo systemctl reboot | poweroff | suspend
systemctl --user status                 # serviços da sessão do usuário
systemctl show nginx -p MainPID,MemoryCurrent,ActiveState
```

## Saída comentada

```text
$ systemctl status nginx
● nginx.service - A high performance web server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; preset: enabled)
#                    ^ arquivo da unidade               ^ inicia no boot
     Active: active (running) since Mon 2026-10-26 08:00:11 -03; 9h ago
   Main PID: 1304 (nginx)
      Tasks: 5 (limit: 18956)
     Memory: 18.2M
        CPU: 2.1s
     CGroup: /system.slice/nginx.service
             ├─1304 nginx: master process
             └─1305 nginx: worker process
out 26 08:00:11 srv systemd[1]: Started nginx.service.       # últimas linhas do journal
```

| Campo `Active` | Significado |
|---|---|
| `active (running)` | Processo em execução |
| `active (exited)` | Tarefa única concluída (oneshot) |
| `inactive (dead)` | Parado |
| `failed` | Falhou (veja `journalctl -u`) |
| `activating (start)` | Iniciando |

## Receitas

```bash
# Serviço falhou: investigar
systemctl status meuapp -l --no-pager
journalctl -u meuapp -b -n 100 --no-pager
systemctl show meuapp -p ExecMainStatus,Result

# Sobrescrever configuração sem editar o arquivo do pacote
sudo systemctl edit meuapp
#   [Service]
#   Environment=NIVEL_LOG=debug
#   Restart=always
#   MemoryMax=1G

# Limites e consumo em tempo real
systemd-cgtop
systemctl set-property meuapp.service CPUQuota=50%

# Serviços lentos no boot
systemd-analyze blame | head; systemd-analyze critical-chain
```

> [!warning] `restart` x `reload`
> `reload` pede ao serviço que releia a configuração sem interrupção (se suportado); `restart` para e inicia (interrompe conexões). Teste a sintaxe antes (`nginx -t`).

## Pontos-chave

- `status`, `enable --now`, `restart`, `--failed`, `edit` e `daemon-reload` cobrem o dia a dia.
- Sempre cruze com [[journalctl]] para logs.
- `mask` bloqueia totalmente um serviço.

## Veja também

[[Init e systemd]] · [[journalctl]] · [[MOC - Ferramentas Nativas do Linux]]
