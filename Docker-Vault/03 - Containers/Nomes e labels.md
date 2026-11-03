---
tags:
  - docker
  - containers
  - organizacao
  - labels
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comandos ps e rm]]"
  - "[[Comando docker run]]"
  - "[[Comando docker inspect]]"
---

# Nomes e labels

## Nomes

```bash
docker run -d --name api-pedidos nginx:1.27        # nome único por daemon
docker run -d --hostname api01 nginx:1.27          # hostname interno
docker rename api-pedidos api-pedidos-v2
```

Sem `--name`, o Docker gera nomes aleatórios (ex.: `eager_turing`). Em redes definidas pelo usuário, o nome do container é resolvido pelo DNS interno (veja [[Redes bridge]]).

## Labels

Labels são metadados chave=valor para organizar, filtrar e automatizar.

```bash
docker run -d --name web \
  --label app=loja --label ambiente=dev --label equipe=plataforma \
  nginx:1.27

# Filtrar
docker ps --filter "label=app=loja"
docker ps --filter "label=ambiente"

# Ler
docker inspect --format '{{json .Config.Labels}}' web
```

> [!tip] Convenções
> Use prefixos reversos de domínio para evitar colisões (`com.exemplo.equipe`) e as chaves padrão OCI (`org.opencontainers.image.source`, `...version`) em imagens. Proxies como o Traefik leem labels para configurar rotas dinamicamente.

## Exercício

Crie dois containers com a label `app=a` e um com `app=b`. Remova apenas os de `app=a` usando `docker rm -f $(docker ps -aq --filter label=app=a)`.

## Veja também

- [[Comandos ps e rm]]
- [[Comando docker run]]
- [[Comando docker inspect]]
- [[MOC - Containers]]
