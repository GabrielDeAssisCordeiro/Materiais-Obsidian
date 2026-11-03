---
tags:
  - docker
  - compose
  - recursos
  - deploy
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Limites de recursos - Docker]]"
  - "[[Cgroups - Docker]]"
  - "[[Múltiplos arquivos e overrides]]"
---

# deploy.resources e limites

No Compose v2, `deploy.resources` é respeitado mesmo **fora do Swarm**.

```yaml
services:
  api:
    image: traefik/whoami:v1.10
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M
          pids: 200
        reservations:
          cpus: "0.25"
          memory: 128M
    restart: unless-stopped
```

| Chave | Efeito |
|---|---|
| `limits.cpus` | Teto de CPU (como `--cpus`) |
| `limits.memory` | Teto de memória (excedê-lo causa OOM kill) |
| `limits.pids` | Máximo de processos |
| `reservations.*` | Recursos garantidos (mais relevante em orquestradores) |

Equivalentes de nível de serviço (também válidos): `mem_limit`, `cpus`, `pids_limit`.

```bash
docker compose up -d
docker stats --no-stream
docker inspect --format '{{.HostConfig.Memory}} {{.HostConfig.NanoCpus}}' $(docker compose ps -q api)
```

> [!tip] Defina limites desde o início
> Facilita descobrir vazamentos de memória em desenvolvimento e evita surpresas em produção. Veja [[Limites de recursos - Docker]].

## Exercício

Limite um serviço a 64M de memória e rode nele um processo que consome mais que isso para provocar o OOM kill. Confira com `docker inspect`.

## Veja também

- [[Limites de recursos - Docker]]
- [[Cgroups - Docker]]
- [[Múltiplos arquivos e overrides]]
- [[MOC - Docker Compose]]
