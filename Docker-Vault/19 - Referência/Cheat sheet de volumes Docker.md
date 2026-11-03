---
tags:
  - docker
  - referencia
  - cheat-sheet
  - volumes
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Volumes nomeados]]"
  - "[[Bind mounts]]"
  - "[[Volume vs bind mount vs tmpfs]]"
  - "[[Backup e restauração de volumes]]"
---

# Cheat sheet de volumes Docker

```bash
docker volume create dados
docker volume ls
docker volume inspect dados
docker volume rm dados
docker volume prune                              # volumes anônimos sem uso

# Usar
docker run -v dados:/dados alpine:3.20                    # volume nomeado
docker run -v "$PWD":/app alpine:3.20                     # bind mount
docker run -v "$PWD/cfg":/cfg:ro alpine:3.20              # somente leitura
docker run --tmpfs /tmp:size=64m alpine:3.20              # em memória
docker run --mount type=volume,src=dados,dst=/dados alpine:3.20
docker run --user "$(id -u):$(id -g)" -v "$PWD":/app alpine:3.20   # dono dos arquivos

# Backup / restauração
docker run --rm -v dados:/d:ro -v "$PWD":/b alpine:3.20 tar czf /b/dados.tar.gz -C /d .
docker run --rm -v dados:/d -v "$PWD":/b:ro alpine:3.20 sh -c 'cd /d && tar xzf /b/dados.tar.gz'
```

| Tipo | Use para |
|---|---|
| **Volume** | Dados de produção (bancos, uploads) |
| **Bind mount** | Código em desenvolvimento, configs |
| **tmpfs** | Temporários e sensíveis |

## Lembretes

- Volume **novo** é populado com o conteúdo da imagem no ponto de montagem; bind mount **sobrepõe**.
- `docker compose down -v` e `docker volume prune` **apagam dados**.
- Bancos de dados: prefira **dump lógico** ao copiar arquivos em execução.
- Erros de permissão: ajuste **UID/GID** (`--user`, `chown`), SELinux (`:z`/`:Z`).

## Veja também

- [[Volumes nomeados]]
- [[Bind mounts]]
- [[Volume vs bind mount vs tmpfs]]
- [[Backup e restauração de volumes]]
- [[MOC - Referência - Docker]]
