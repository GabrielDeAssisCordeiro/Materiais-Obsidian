---
tags:
  - docker
  - volumes
  - armazenamento
  - sintaxe
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Volumes nomeados]]"
  - "[[Bind mounts]]"
  - "[[tmpfs mounts]]"
---

# Sintaxe -v vs --mount

Duas formas de montar armazenamento. `--mount` é **explícita** e mais clara; `-v` é compacta.

| Tarefa | `-v` / `--volume` | `--mount` |
|---|---|---|
| Volume nomeado | `-v dados:/dados` | `--mount type=volume,src=dados,dst=/dados` |
| Bind mount | `-v "$PWD":/app` | `--mount type=bind,src="$PWD",dst=/app` |
| Somente leitura | `-v dados:/dados:ro` | `--mount type=volume,src=dados,dst=/dados,readonly` |
| tmpfs | `--tmpfs /tmp` | `--mount type=tmpfs,dst=/tmp` |

```bash
docker run --rm \
  --mount type=volume,src=dados,dst=/dados \
  --mount type=bind,src="$PWD",dst=/app,readonly \
  alpine:3.20 ls /dados /app
```

## Diferença de comportamento importante

| Situação | `-v` | `--mount` |
|---|---|---|
| Diretório do host inexistente (bind) | **Cria** o diretório (como root) | **Erro** |

> [!tip] Prefira `--mount` em scripts
> A criação silenciosa de diretórios com `-v` esconde erros de digitação. Em Compose, a sintaxe longa de `volumes:` equivale ao `--mount`.

```yaml
# compose.yaml — sintaxe longa
services:
  app:
    image: alpine:3.20
    command: sleep 300
    volumes:
      - type: volume
        source: dados
        target: /dados
      - type: bind
        source: ./config
        target: /config
        read_only: true
volumes:
  dados:
```

## Exercício

Reescreva três comandos `docker run -v ...` seus usando `--mount` e compare o comportamento ao apontar para um caminho inexistente.

## Veja também

- [[Volumes nomeados]]
- [[Bind mounts]]
- [[tmpfs mounts]]
- [[MOC - Volumes e Armazenamento]]
