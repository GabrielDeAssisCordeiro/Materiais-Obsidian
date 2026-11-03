---
tags:
  - docker
  - compose
  - desenvolvimento
  - hot-reload
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Comandos do Docker Compose]]"
  - "[[Bind mounts]]"
  - "[[Serviços com image e build]]"
---

# Compose Watch

O **Compose Watch** monitora arquivos do projeto e **sincroniza ou reconstrói** serviços automaticamente durante o desenvolvimento, sem depender de bind mounts (útil no macOS/Windows e para evitar problemas de permissão).

```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    develop:
      watch:
        - action: sync              # copia arquivos alterados para o container
          path: ./src
          target: /app/src
          ignore:
            - "**/*.test.js"
        - action: sync+restart      # copia e reinicia o serviço
          path: ./config
          target: /app/config
        - action: rebuild           # reconstrói a imagem e recria o container
          path: package.json
```

```bash
docker compose watch            # inicia o modo watch
# ou
docker compose up --watch       # sobe e observa
```

| `action` | Quando usar |
|---|---|
| `sync` | Código com hot reload no runtime (Node com nodemon, Vite, Flask debug) |
| `sync+restart` | Arquivos de configuração que exigem reinício |
| `rebuild` | Mudanças em dependências (`package.json`, `requirements.txt`) ou Dockerfile |
| `sync+exec` | Copia e executa um comando no container |

> [!question] Verificar na documentação oficial
> As ações disponíveis (`sync+exec`) e opções (`initial_sync`) dependem da versão do Compose. Consulte "Use Compose Watch".

> [!tip] Watch vs bind mount
> O bind mount reflete tudo instantaneamente, porém pode ser lento fora do Linux e traz problemas de UID/GID. O Watch copia só o necessário e permite `rebuild` automático.

## Exercício

Configure `develop.watch` em um app Node ou Python com hot reload e edite um arquivo em `src/` para ver a sincronização acontecer.

## Veja também

- [[Comandos do Docker Compose]]
- [[Bind mounts]]
- [[Serviços com image e build]]
- [[MOC - Docker Compose]]
