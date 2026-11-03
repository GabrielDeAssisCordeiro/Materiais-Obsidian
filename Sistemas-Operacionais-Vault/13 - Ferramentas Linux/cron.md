---
titulo: "cron"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: iniciante
relacionados:
  - "[[systemctl]]"
  - "[[Init e systemd]]"
  - "[[SO em Lote (Batch)]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# cron

## Finalidade

O **cron** é o serviço de **agendamento periódico** de comandos. Descendente direto da ideia de [[SO em Lote (Batch)|jobs em lote]]. O `crontab` edita a tabela de cada usuário; `at` agenda **uma execução única**; os **timers do systemd** são a alternativa moderna ([[systemctl]]).

## Formato do crontab

```text
┌───────── minuto (0-59)
│ ┌─────── hora (0-23)
│ │ ┌───── dia do mês (1-31)
│ │ │ ┌─── mês (1-12 ou jan-dez)
│ │ │ │ ┌─ dia da semana (0-7; 0 e 7 = domingo, ou dom-sab)
│ │ │ │ │
* * * * *  comando
```

| Símbolo | Significado | Exemplo |
|---|---|---|
| `*` | Qualquer valor | `* * * * *` = todo minuto |
| `,` | Lista | `0 8,12,18 * * *` |
| `-` | Intervalo | `0 9-17 * * 1-5` (seg-sex, 9 às 17) |
| `/` | Passo | `*/15 * * * *` (a cada 15 min) |
| `@reboot`, `@hourly`, `@daily`, `@weekly`, `@monthly`, `@yearly` | Atalhos | `@reboot /opt/app/start.sh` |

## Comandos

```bash
crontab -e                  # edita o crontab do usuário
crontab -l                  # lista
crontab -r                  # remove TUDO (cuidado: sem confirmação)
sudo crontab -u ana -l      # de outro usuário
ls /etc/cron.d /etc/cron.daily /etc/cron.hourly /etc/cron.weekly /etc/cron.monthly
cat /etc/crontab            # tabela do sistema (tem coluna extra de usuário)
```

## Exemplos

```cron
# /var/spool/cron/crontabs/ana  (crontab -e)
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=ana@exemplo.com

# Backup todo dia às 02:30, com log
30 2 * * *   /home/ana/bin/backup.sh >> /home/ana/backup.log 2>&1

# A cada 5 minutos, de segunda a sexta, em horário comercial
*/5 9-18 * * 1-5   /opt/monitor/check.sh

# Primeiro dia do mês às 06:00
0 6 1 * *   /opt/relatorios/mensal.sh

# Na inicialização
@reboot   /opt/app/start.sh

# Evita execuções sobrepostas com flock
*/10 * * * *   flock -n /tmp/sync.lock /opt/sync.sh

# Limpeza de arquivos com mais de 7 dias
15 3 * * *   find /var/tmp/cache -type f -mtime +7 -delete
```

Execução única com `at`:

```bash
echo "/opt/scripts/relatorio.sh" | at 23:30
at now + 2 hours <<< "reboot"
atq; atrm 3
```

## Armadilhas

> [!warning] Por que "funciona no terminal mas não no cron"
> - **Ambiente mínimo**: `PATH` curto e sem variáveis do seu perfil. Use caminhos absolutos e defina `PATH`.
> - **`%` precisa de escape** (`\%`) em comandos: `date +\%F`.
> - Diretório de trabalho é `$HOME`.
> - Sem terminal: nada de `read`/interação; **redirecione saída** (`>> log 2>&1`) ou o cron tenta enviar e-mail.
> - Fuso horário e horário de verão podem pular ou duplicar execuções.
> - O cron **não** executa tarefas perdidas com a máquina desligada (use `anacron` ou `Persistent=true` em timers).

```bash
grep CRON /var/log/syslog | tail          # Debian/Ubuntu
journalctl -u cron -u crond --since today # systemd
sudo systemctl status cron
```

## cron x systemd timers

| Aspecto | cron | systemd timer |
|---|---|---|
| Configuração | Uma linha | Dois arquivos (`.timer` + `.service`) |
| Logs | Syslog/e-mail | `journalctl -u unidade` |
| Execuções perdidas | Não (use anacron) | `Persistent=true` |
| Dependências e limites (cgroups) | Não | Sim |
| Atraso aleatório | Manual | `RandomizedDelaySec=` |
| Precisão e calendário | Minuto | Segundos, expressões ricas |

```ini
# /etc/systemd/system/backup.timer
[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
RandomizedDelaySec=300
[Install]
WantedBy=timers.target
```

## Pontos-chave

- Cinco campos + comando; `crontab -e/-l`.
- Use caminhos absolutos, redirecione saída e evite sobreposição (`flock`).
- Para tarefas modernas e rastreáveis, considere timers do systemd.

## Veja também

[[systemctl]] · [[SO em Lote (Batch)]] · [[MOC - Ferramentas Nativas do Linux]]
