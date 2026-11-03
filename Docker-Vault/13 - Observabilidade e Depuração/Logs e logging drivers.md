---
tags:
  - docker
  - observabilidade
  - logs
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comando docker logs]]"
  - "[[Boas práticas de logs em containers]]"
  - "[[Logs centralizados com Loki]]"
  - "[[Arquivo daemon.json]]"
---

# Logs e logging drivers

O Docker captura **stdout** e **stderr** do processo principal e os entrega a um **logging driver**.

| Driver | Característica |
|---|---|
| `json-file` | Padrão histórico; arquivo JSON por container; **sem rotação por padrão** |
| `local` | Formato otimizado, **com rotação por padrão**; recomendado para uso local |
| `journald` | Envia ao journal do systemd |
| `syslog` | Para um servidor syslog |
| `fluentd`, `gelf`, `splunk` | Coletores externos |
| `awslogs`, `gcplogs` | CloudWatch Logs, Cloud Logging |
| `none` | Descarta os logs |

```bash
# Driver padrão do daemon
docker info --format '{{.LoggingDriver}}'

# Por container, com rotação
docker run -d --name app \
  --log-driver local \
  --log-opt max-size=10m --log-opt max-file=3 \
  nginx:1.27

docker inspect --format '{{json .HostConfig.LogConfig}}' app
docker rm -f app
```

## Padrão global (daemon.json)

```json
{
  "log-driver": "local",
  "log-opts": { "max-size": "10m", "max-file": "5" }
}
```

## Em Compose

```yaml
services:
  app:
    image: nginx:1.27
    logging:
      driver: local
      options:
        max-size: "10m"
        max-file: "3"
```

> [!info] `docker logs` e drivers remotos
> O comando `docker logs` funciona com `json-file`, `local` e `journald`. Para outros drivers, o Docker mantém um **cache local** (*dual logging*) para que `docker logs` continue funcionando em versões modernas.

> [!warning] Mudar o driver não afeta containers existentes
> A configuração é lida na **criação** do container. Recrie-os após alterar o `daemon.json`.

> [!bug] Disco cheio por logs
> Sem rotação, o `json-file` cresce indefinidamente. Configure `max-size`/`max-file` ou use o driver `local`.

## Exercício

Crie dois containers com drivers diferentes (`json-file` e `local`), gere bastante saída e compare o comportamento de rotação.

## Veja também

- [[Comando docker logs]]
- [[Boas práticas de logs em containers]]
- [[Logs centralizados com Loki]]
- [[Arquivo daemon.json]]
- [[MOC - Observabilidade e Depuração]]
