---
tags:
  - docker
  - containers
  - comandos
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Ciclo de vida do container]]"
  - "[[Comando docker inspect]]"
  - "[[Nomes e labels]]"
  - "[[Limpeza com prune]]"
---

# Comandos ps e rm

## Listar containers

```bash
docker ps                      # somente em execução
docker ps -a                   # todos, inclusive parados
docker ps -q                   # apenas IDs
docker ps -s                   # inclui tamanho
docker ps -a --filter "status=exited"
docker ps --filter "name=web" --filter "label=app=loja"

# Formato personalizado (Go template)
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
```

## Remover containers

```bash
docker rm app                  # container parado
docker rm -f app               # força (envia SIGKILL e remove)
docker rm -v app               # remove também volumes anônimos associados
docker rm $(docker ps -aq --filter status=exited)

# Remove todos os containers parados de uma vez
docker container prune
```

> [!danger] Cuidado com `docker rm -f $(docker ps -aq)`
> Remove **todos** os containers, inclusive de bancos de dados em execução. Dados em volumes persistem, mas os containers e suas camadas graváveis somem. Use filtros.

> [!tip] IDs curtos
> Você pode usar os primeiros caracteres do ID (`docker rm 3f2a`) desde que sejam únicos.

## Exercício

Crie 3 containers `alpine` com labels diferentes e liste apenas os que possuem a label `grupo=a` usando `--filter`.

## Veja também

- [[Ciclo de vida do container]]
- [[Comando docker inspect]]
- [[Nomes e labels]]
- [[Limpeza com prune]]
- [[MOC - Containers]]
