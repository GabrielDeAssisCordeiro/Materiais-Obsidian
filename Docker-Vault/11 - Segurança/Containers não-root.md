---
tags:
  - docker
  - seguranca
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Instruções WORKDIR e USER]]"
  - "[[Modo rootless]]"
  - "[[User namespaces e userns-remap]]"
---

# Containers não-root

Por padrão, o processo do container roda como **root (UID 0)** dentro dele. Embora isolado por namespaces, o root do container ainda é perigoso se houver escape, volume mal configurado ou capabilities excessivas.

## Como executar sem root

```dockerfile
# No Dockerfile
FROM python:3.12-slim
RUN useradd --system --uid 10001 --no-create-home app
WORKDIR /app
COPY --chown=10001:10001 . .
USER 10001
CMD ["python", "app.py"]
```

```bash
# Na execução (sobrescreve a imagem)
docker run --rm --user 10001:10001 alpine:3.20 id
```

## Imagens que já vêm prontas

| Imagem | Observação |
|---|---|
| `nginxinc/nginx-unprivileged` | Nginx em porta 8080, sem root |
| `gcr.io/distroless/*:nonroot` | Usuário `nonroot` (UID 65532) |
| `node` | Usuário `node` (UID 1000) |
| `postgres`, `redis` | Iniciam como root e rebaixam privilégio internamente |

## Cuidados

- Portas abaixo de **1024** exigem `NET_BIND_SERVICE` ou uso de porta alta (8080) com mapeamento `-p 80:8080`.
- Diretórios de escrita precisam pertencer ao usuário (veja [[Permissões e UID GID em volumes]]).
- Verifique: `docker run --rm IMAGEM id`.

```bash
# Auditoria: containers em execução como root
docker ps -q | xargs -r docker inspect --format '{{.Name}} user="{{.Config.User}}"'
```

> [!info] Não-root dentro ≠ rootless no host
> Executar como não-root **no container** é independente do [[Modo rootless]], em que o **daemon** também roda sem root. Combine os dois para maior proteção.

## Exercício

Modifique um Dockerfile seu para usar UID 10001 e resolva os problemas de permissão que surgirem, documentando cada correção.

## Veja também

- [[Princípio do menor privilégio - Docker]]
- [[Instruções WORKDIR e USER]]
- [[Modo rootless]]
- [[User namespaces e userns-remap]]
- [[MOC - Segurança]]
