---
tags:
  - docker
  - containers
  - resiliencia
  - restart
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comando docker run]]"
  - "[[Healthchecks em containers]]"
  - "[[Ciclo de vida do container]]"
---

# Políticas de restart

A política de restart define o que o daemon faz quando o processo principal do container termina.

| Política | Comportamento |
|---|---|
| `no` | Nunca reinicia (padrão). |
| `on-failure[:N]` | Reinicia apenas se o código de saída for diferente de 0, no máximo N vezes. |
| `always` | Sempre reinicia; também sobe com o daemon. Se parado manualmente, volta quando o daemon reinicia. |
| `unless-stopped` | Como `always`, mas **não** reinicia se foi parado manualmente antes do reboot. |

```bash
docker run -d --name api --restart unless-stopped nginx:1.27
docker run -d --name job --restart on-failure:3 alpine:3.20 sh -c 'exit 1'

# Altera em container existente
docker update --restart unless-stopped api

# Quantas vezes reiniciou
docker inspect --format '{{.RestartCount}}' job
```

> [!tip] Recomendação para serviços
> `unless-stopped` é a escolha usual para serviços de longa duração em servidores únicos. Em orquestradores (Swarm, Kubernetes) a política é definida no serviço.

> [!bug] Container em loop de reinício
> `STATUS` aparecendo como `Restarting (1)` indica falha no startup. Veja os logs (`docker logs`) e o código de saída. Uma política de restart **não conserta** uma aplicação quebrada; ela só mascara o problema.

> [!info] Backoff
> O Docker aumenta o intervalo entre tentativas (começando em 100 ms e dobrando até um teto) e redefine após o container ficar estável por um período.

## Exercício

Crie um container que sempre falha com `--restart on-failure:3` e acompanhe `RestartCount`. Em seguida, troque para `always` e observe o comportamento (e remova o container depois!).

## Veja também

- [[Comando docker run]]
- [[Healthchecks em containers]]
- [[Ciclo de vida do container]]
- [[MOC - Containers]]
