---
tags:
  - docker
  - dockerfile
  - instrucao
  - healthcheck
aliases: []
tipo: instrucao
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Healthchecks em containers]]"
  - "[[Políticas de restart]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instrução HEALTHCHECK

Embute no Dockerfile a verificação de saúde da aplicação.

```dockerfile
# syntax=docker/dockerfile:1
FROM nginx:1.27-alpine

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget -qO- http://127.0.0.1/ >/dev/null || exit 1
```

| Opção | Padrão | Descrição |
|---|---|---|
| `--interval` | 30s | Intervalo entre checagens |
| `--timeout` | 30s | Tempo máximo de cada checagem |
| `--start-period` | 0s | Carência inicial (falhas não contam) |
| `--start-interval` | 5s | Intervalo durante o período de carência |
| `--retries` | 3 | Falhas consecutivas para `unhealthy` |

Desabilite um healthcheck herdado com `HEALTHCHECK NONE`.

```bash
docker build -t nginx-hc .
docker run -d --name hc nginx-hc
sleep 15 && docker ps --format '{{.Names}}: {{.Status}}'
docker rm -f hc
```

> [!question] Verificar na documentação oficial
> `--start-interval` exige versões recentes do Engine (25.0 ou superior). Confirme no seu ambiente.

> [!tip] Use ferramentas presentes na imagem
> Em imagens Alpine/BusyBox, `wget` existe; `curl` pode não existir. Em distroless, construa um mini-binário de healthcheck ou use o recurso da própria aplicação.

## Exercício

Adicione um HEALTHCHECK a uma imagem sua que consulta `/health` e simule falha parando o endpoint. Observe `starting`, `healthy` e `unhealthy`.

## Veja também

- [[Healthchecks em containers]]
- [[Políticas de restart]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
