---
tags:
  - docker
  - compose
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Interpolação e arquivo .env]]"
  - "[[Variáveis de ambiente em containers]]"
  - "[[configs e secrets no Compose]]"
---

# Variáveis de ambiente e env_file

```yaml
services:
  api:
    image: alpine:3.20
    command: sh -c 'env | sort | grep -E "^(APP_|LOG_)"'
    environment:
      APP_ENV: desenvolvimento          # formato mapa
      LOG_LEVEL: debug
      # ou formato lista:
      # - APP_ENV=desenvolvimento
    env_file:
      - ./comum.env                     # lista simples
      - path: ./local.env               # formato longo
        required: false                 # não falha se o arquivo não existir
```

`comum.env`:

```text
APP_NAME=minha-api
LOG_LEVEL=info
```

## Precedência (da maior para a menor)

1. `docker compose run -e VAR=valor`
2. `environment:` no `compose.yaml` (e variáveis do shell referenciadas nele)
3. `env_file:`
4. `ENV` definido na imagem

> [!tip] Variável sem valor
> `environment: - HOME` passa o valor da variável do shell do host para o container (se existir).

> [!warning] `env_file` ≠ interpolação
> O `env_file` fornece variáveis **ao container**; já o `.env` do projeto fornece variáveis para **interpolar o próprio compose.yaml** (`${VAR}`). São mecanismos diferentes. Veja [[Interpolação e arquivo .env]].

> [!danger] Segredos
> Não versione arquivos `.env` com segredos reais (adicione ao `.gitignore`) e prefira [[configs e secrets no Compose]] para senhas.

## Exercício

Defina a mesma variável em `env_file`, `environment` e no shell com `docker compose run -e` para comprovar a ordem de precedência.

## Veja também

- [[Interpolação e arquivo .env]]
- [[Variáveis de ambiente em containers]]
- [[configs e secrets no Compose]]
- [[MOC - Docker Compose]]
