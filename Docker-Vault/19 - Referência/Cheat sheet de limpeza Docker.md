---
tags:
  - docker
  - referencia
  - cheat-sheet
  - prune
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Limpeza com prune]]"
  - "[[Comandos ps e rm]]"
  - "[[Erros comuns e soluções]]"
---

# Cheat sheet de limpeza Docker

```bash
docker system df                               # quanto cada tipo ocupa
docker system df -v                            # detalhado

docker container prune                         # containers parados
docker image prune                             # imagens dangling
docker image prune -a                          # imagens sem container
docker image prune -a --filter "until=168h"    # mais antigas que 7 dias
docker network prune                           # redes sem uso
docker volume prune                            # volumes anônimos sem uso
docker builder prune                           # cache de build
docker builder prune --keep-storage 10GB
docker system prune                            # containers, redes, dangling e cache
docker system prune -a --volumes               # AGRESSIVO

docker rm -f $(docker ps -aq --filter status=exited)
docker rmi $(docker images -q --filter dangling=true)
```

| Comando | Risco |
|---|---|
| `container prune`, `network prune` | Baixo |
| `image prune` | Baixo |
| `image prune -a` | Médio: precisará baixar de novo |
| `builder prune` | Médio: builds ficam mais lentos |
| `volume prune`, `--volumes` | **Alto: pode apagar dados** |

> [!danger] Antes de qualquer `--volumes`
> Liste e confira os volumes (`docker volume ls`) e faça backup do que importa.

> [!tip] Para servidores
> Agende `docker image prune -af --filter "until=720h"` e `docker builder prune -f --keep-storage 10GB`, além de rotação de logs.

## Veja também

- [[Limpeza com prune]]
- [[Comandos ps e rm]]
- [[Erros comuns e soluções]]
- [[MOC - Referência - Docker]]
