---
titulo: "journalctl"
tags:
  - sistemas-operacionais
  - ferramenta
  - linux
tipo: ferramenta
nivel: intermediario
relacionados:
  - "[[systemctl]]"
  - "[[dmesg]]"
  - "[[Init e systemd]]"
  - "[[MOC - Ferramentas Nativas do Linux]]"
---

# journalctl

## Finalidade

Consulta o **journal do systemd** (`systemd-journald`): log **binário e indexado** que reúne mensagens do kernel, serviços, `syslog`, stdout/stderr das unidades e eventos de boot, com campos estruturados (unidade, PID, prioridade).

## Sintaxe

```bash
journalctl                          # tudo (mais antigo primeiro)
journalctl -e                       # pula para o fim
journalctl -f                       # acompanha (como tail -f)
journalctl -n 50                    # últimas 50 linhas
journalctl -u nginx                 # uma unidade
journalctl -u nginx -u php-fpm -f   # várias
journalctl -b                       # boot atual;  -b -1 boot anterior
journalctl --list-boots
journalctl -k                       # mensagens do kernel (como dmesg)
journalctl -p err                   # prioridade >= erro;  -p warning..err
journalctl --since "2026-10-26 08:00" --until "10 min ago"
journalctl --since yesterday
journalctl _PID=1234                # por campo
journalctl _UID=1000 _COMM=sshd
journalctl -o json-pretty -n1       # saída estruturada
journalctl -o short-precise         # microssegundos
journalctl -r                       # ordem reversa (mais recente primeiro)
journalctl --no-pager | grep erro
journalctl --disk-usage
sudo journalctl --vacuum-size=500M  # limita tamanho; --vacuum-time=2weeks
```

## Prioridades (syslog)

| Nº | Nome | Uso |
|---|---|---|
| 0 | emerg | Sistema inutilizável |
| 1 | alert | Ação imediata |
| 2 | crit | Condição crítica |
| 3 | err | Erro |
| 4 | warning | Aviso |
| 5 | notice | Normal, significativo |
| 6 | info | Informativo |
| 7 | debug | Depuração |

## Saída comentada

```text
$ journalctl -u ssh -n 3 --no-pager
out 26 10:02:11 srv sshd[1822]: Failed password for root from 203.0.113.9 port 51522 ssh2
out 26 10:02:14 srv sshd[1822]: Failed password for root from 203.0.113.9 port 51522 ssh2
out 26 10:02:20 srv sshd[1822]: Disconnected from authenticating user root 203.0.113.9
# data hora  host  unidade[PID]: mensagem  -> tentativas de força bruta no SSH
```

## Receitas

```bash
journalctl -b -p err --no-pager                      # erros do boot atual
journalctl -u meuapp --since "1 hour ago" -p warning # avisos da última hora
journalctl -u meuapp -f -o cat                       # só a mensagem, ao vivo
journalctl /usr/bin/sudo                             # por executável
journalctl _SYSTEMD_UNIT=docker.service + _COMM=containerd
journalctl -b -1 -k | tail -50                       # kernel do boot anterior (depois de travar)
systemd-analyze blame | head                         # ligado ao boot
sudo journalctl --rotate && sudo journalctl --vacuum-time=7d
```

## Persistência

Por padrão pode ser **volátil** (`/run/log/journal`). Para guardar entre boots:

```bash
sudo mkdir -p /var/log/journal
sudo systemctl restart systemd-journald
# ou em /etc/systemd/journald.conf: Storage=persistent  SystemMaxUse=1G
```

> [!tip] Registrar do shell ou de scripts
> `logger -t meu_script -p user.warning "falha ao copiar"` e depois `journalctl -t meu_script`. Em unidades systemd, tudo em stdout/stderr já vai para o journal.

## Vantagens e limites

| Vantagens | Limites |
|---|---|
| Indexado, filtros por campos, rápido | Formato binário (exige `journalctl`) |
| Metadados confiáveis (UID, unidade) | Pode crescer sem limites mal configurado |
| Integra kernel + serviços + boot | Integrar com ferramentas externas exige `rsyslog`/exportação |

## Pontos-chave

- `-u`, `-b`, `-p`, `--since`, `-f` resolvem 90% dos casos.
- `journalctl -b -1` ajuda a investigar travamentos passados.
- Configure persistência e limite de tamanho.

## Veja também

[[systemctl]] · [[dmesg]] · [[MOC - Ferramentas Nativas do Linux]]
