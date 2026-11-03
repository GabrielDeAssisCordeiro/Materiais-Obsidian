---
tags:
  - seguranca
aliases:
  - "Observabilidade"
tipo: cuidado
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Fuga de Sandbox]]"
  - "[[Evasão de Sandbox por Malware]]"
---
# Logs e Monitoramento

Sem observação, não há como saber se a contenção funcionou.

| O que registrar | Por quê |
|---|---|
| Início/fim, comando e usuário de cada execução | Rastreabilidade |
| Consumo de CPU/memória/E-S | Detectar abuso |
| Tentativas de conexão bloqueadas | Detectar exfiltração |
| Negações de seccomp/AppArmor/SELinux | Detectar tentativas de escape |
| Tráfego de rede do laboratório | Análise de comportamento |

```bash
docker stats --no-stream
docker events --since 10m
sudo journalctl -k | grep -i -E 'apparmor|seccomp|audit'
```

> [!tip] Envie logs para fora da sandbox
> O código hostil pode apagar logs locais. Use coleta externa e somente-anexo (*append-only*).

## Exercício

Configure um container com `--log-driver` externo ou `journald` e confirme que os logs persistem após `docker rm`.

## Veja também

- [[Fuga de Sandbox]]
- [[Evasão de Sandbox por Malware]]
- [[Limites de Recursos]]
- [[MOC - Cuidados e Segurança]]
