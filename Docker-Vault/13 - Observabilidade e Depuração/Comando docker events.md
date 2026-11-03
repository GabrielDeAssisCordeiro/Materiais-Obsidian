---
tags:
  - docker
  - observabilidade
  - comandos
aliases: []
tipo: comando
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comando docker inspect]]"
  - "[[Análise de OOM kill]]"
  - "[[Containers em loop de reinício]]"
---

# Comando docker events

`docker events` transmite em tempo real os **eventos do daemon** (criação, início, parada, morte, OOM, mudança de saúde, etc.).

```bash
# Em um terminal: observa eventos
docker events

# Filtrando
docker events --filter type=container --filter event=die
docker events --filter event=oom
docker events --filter container=web --since 30m --until 1m
docker events --filter 'type=container' --format '{{.Time}} {{.Actor.Attributes.name}} {{.Action}}'

# Em outro terminal: gera eventos
docker run --rm alpine:3.20 sh -c 'exit 3'
```

| Tipo | Eventos comuns |
|---|---|
| `container` | `create`, `start`, `die`, `kill`, `stop`, `oom`, `health_status`, `destroy` |
| `image` | `pull`, `push`, `tag`, `delete` |
| `network` | `create`, `connect`, `disconnect`, `destroy` |
| `volume` | `create`, `mount`, `unmount`, `destroy` |

> [!tip] Para investigar o passado
> `--since` e `--until` permitem consultar um intervalo recente (o daemon retém os eventos por tempo limitado). Para histórico longo, envie eventos a um sistema de logs/alertas.

> [!info] Evento `die` mostra o exitCode
> Use `--format '{{json .Actor.Attributes}}'` e procure `exitCode` para entender por que o container terminou.

## Exercício

Deixe `docker events --filter event=die` rodando e dispare containers que terminam com códigos diferentes. Anote os `exitCode`.

## Veja também

- [[Comando docker inspect]]
- [[Análise de OOM kill]]
- [[Containers em loop de reinício]]
- [[MOC - Observabilidade e Depuração]]
