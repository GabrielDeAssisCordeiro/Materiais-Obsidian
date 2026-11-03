---
tags:
  - docker
  - fundamentos
  - cli
  - api
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Arquitetura do Docker]]"
  - "[[Docker Daemon dockerd]]"
  - "[[Contextos do Docker]]"
---

# Docker CLI e API

O **Docker CLI** é um cliente da **Engine API**, uma API REST versionada. Tudo que a CLI faz, você pode fazer via HTTP.

## Estrutura de comandos

A CLI moderna agrupa comandos por objeto (`docker <objeto> <ação>`), embora os atalhos antigos continuem funcionando:

| Forma moderna | Atalho clássico |
|---|---|
| `docker container ls` | `docker ps` |
| `docker container run` | `docker run` |
| `docker image ls` | `docker images` |
| `docker image pull` | `docker pull` |
| `docker system prune` | — |

```bash
docker --help                 # lista comandos
docker container --help       # ajuda de um grupo
docker run --help             # ajuda de um comando
```

## Falando direto com a API (apenas em laboratório)

```bash
# Lista containers via API REST pelo socket Unix
curl --unix-socket /var/run/docker.sock http://localhost/containers/json

# Versão da API
curl --unix-socket /var/run/docker.sock http://localhost/version
```

> [!info] Versão da API
> A CLI negocia automaticamente a versão da API com o daemon. Para fixar uma versão (útil em diagnósticos), use `DOCKER_API_VERSION`:
> ```bash
> DOCKER_API_VERSION=1.43 docker version
> ```
> O Engine 29 reduziu a versão mínima de API suportada (v1.40) para ampliar a compatibilidade com clientes antigos.

> [!question] Verificar na documentação oficial
> A versão máxima atual da Engine API depende do release do Engine instalado. Consulte `docker version` e o histórico de versões da API na documentação.

## Variáveis de ambiente úteis

| Variável | Efeito |
|---|---|
| `DOCKER_HOST` | Endereço do daemon (`unix://`, `tcp://`, `ssh://`). |
| `DOCKER_CONTEXT` | Seleciona o [[Contextos do Docker]] ativo. |
| `DOCKER_CONFIG` | Diretório de configuração do cliente (padrão `~/.docker`). |
| `DOCKER_BUILDKIT` | Habilita/desabilita BuildKit no builder clássico. |

## Exercício

Use `curl --unix-socket` para listar imagens (`/images/json`) e compare com a saída de `docker image ls`.

## Veja também

- [[Arquitetura do Docker]]
- [[Docker Daemon dockerd]]
- [[Contextos do Docker]]
- [[MOC - Fundamentos - Docker]]
