---
tags:
  - docker
  - producao
  - 12-factor
  - boas-praticas
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Variáveis de ambiente em containers]]"
  - "[[Boas práticas de logs em containers]]"
  - "[[Healthchecks em containers]]"
  - "[[Checklist de produção]]"
---

# Aplicações 12-factor em containers

O método **12-factor** descreve como construir aplicações adequadas à nuvem. Containers casam muito bem com ele.

| Fator | Como aplicar com Docker |
|---|---|
| 1. Código-base | Um repositório, uma imagem por serviço |
| 2. Dependências | Declaradas e instaladas no `Dockerfile` (lockfiles) |
| 3. Configuração | **Variáveis de ambiente**/secrets, nunca na imagem |
| 4. Serviços de apoio | Banco, cache e filas como recursos anexados (URLs em env) |
| 5. Build, release, run | `docker build` → tag/registry → `docker run`/deploy |
| 6. Processos | Containers **stateless**; estado em volumes/serviços externos |
| 7. Vínculo de porta | A app escuta em uma porta (`0.0.0.0:$PORT`) |
| 8. Concorrência | Escalar por **mais containers**, não por threads gigantes |
| 9. Descartabilidade | Inicialização rápida e **shutdown gracioso** (SIGTERM) |
| 10. Paridade dev/prod | Mesma imagem; Compose em dev, orquestrador em prod |
| 11. Logs | Fluxo em **stdout/stderr** |
| 12. Processos administrativos | `docker compose run --rm app comando` (migrações, scripts) |

```bash
# Fator 3: a mesma imagem em ambientes diferentes
docker run -d --env-file dev.env  meu-app:1.4.2
docker run -d --env-file prod.env meu-app:1.4.2

# Fator 12: tarefa administrativa pontual
docker compose run --rm app python manage.py migrate
```

> [!tip] Graceful shutdown
> Ao receber SIGTERM, pare de aceitar novas conexões, conclua as requisições em andamento e feche conexões, dentro do `stop_grace_period` (padrão 10 s). Ajuste com `docker stop -t` ou `stop_grace_period: 30s` no Compose.

> [!warning] Estado dentro do container
> Sessões em memória, uploads no disco do container ou caches locais impedem escalar e perdem dados em cada deploy. Mova-os para Redis, banco ou armazenamento de objetos.

## Exercício

Avalie uma aplicação sua contra os 12 fatores e liste três ajustes que a tornariam mais "container-friendly".

## Veja também

- [[Variáveis de ambiente em containers]]
- [[Boas práticas de logs em containers]]
- [[Healthchecks em containers]]
- [[Checklist de produção]]
- [[MOC - Produção]]
