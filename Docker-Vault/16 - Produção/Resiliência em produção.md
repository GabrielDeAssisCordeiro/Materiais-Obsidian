---
tags:
  - docker
  - producao
  - resiliencia
  - healthcheck
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Healthchecks em containers]]"
  - "[[Políticas de restart]]"
  - "[[Limites de recursos - Docker]]"
  - "[[Aplicações 12-factor em containers]]"
---

# Resiliência em produção

Quatro pilares para containers de produção estáveis:

```yaml
services:
  api:
    image: ghcr.io/org/api:1.4.2           # tag fixa
    restart: unless-stopped                # 1) reinício automático
    healthcheck:                           # 2) saúde da aplicação
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:8080/health || exit 1"]
      interval: 15s
      timeout: 3s
      retries: 3
      start_period: 20s
    deploy:
      resources:                           # 3) limites
        limits:
          cpus: "1.0"
          memory: 512M
    stop_grace_period: 30s                 # 4) encerramento gracioso
    logging:
      driver: local
      options:
        max-size: "10m"
        max-file: "5"
    init: true                             # PID 1 correto (sinais e zumbis)
    read_only: true
    tmpfs:
      - /tmp
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
```

| Pilar | Efeito |
|---|---|
| Restart policy | Recupera de falhas do processo e de reboot do host |
| Healthcheck | Detecta aplicação travada (processo vivo, serviço morto) |
| Limites | Impede que uma falha derrube outros serviços |
| Graceful stop | Evita perda de requisições e dados no deploy |

> [!warning] Restart não substitui correção
> Reinício automático mascara bugs. Monitore `RestartCount` e alerte quando ele aumentar; veja [[Containers em loop de reinício]].

> [!info] Quem age sobre `unhealthy`?
> No Docker simples, ninguém reinicia automaticamente. Em Swarm/Kubernetes, o orquestrador substitui. Em Compose, combine com monitoramento ou ferramentas auxiliares, ou migre para um orquestrador quando essa garantia for necessária.

## Exercício

Aplique o bloco acima a um serviço seu, ajuste o que falhar (por exemplo, caminhos de escrita) e meça o tempo de `docker compose stop`.

## Veja também

- [[Healthchecks em containers]]
- [[Políticas de restart]]
- [[Limites de recursos - Docker]]
- [[Aplicações 12-factor em containers]]
- [[MOC - Produção]]
