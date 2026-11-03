---
tags:
  - docker
  - containers
  - comandos
  - logs
  - observabilidade
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comando docker inspect]]"
  - "[[Modos interativo e detached]]"
  - "[[Comando docker exec e attach]]"
---

# Comando docker logs

`docker logs` mostra o que o processo principal escreveu em **stdout** e **stderr**.

```bash
docker logs web                 # tudo
docker logs -f web              # acompanha em tempo real (follow)
docker logs --tail 100 web      # últimas 100 linhas
docker logs --since 10m web     # últimos 10 minutos
docker logs --since 2026-10-24T08:00:00 --until 2026-10-24T09:00:00 web
docker logs -t web              # com timestamps
docker logs -f --tail 20 -t web # combinando
```

> [!info] Boa prática: logar em stdout/stderr
> Aplicações em container devem escrever logs no **fluxo padrão** e deixar a plataforma coletar. Gravar em arquivos dentro do container dificulta a coleta e enche a camada gravável. Imagens oficiais costumam redirecionar logs para `/dev/stdout`.

> [!warning] Logs crescem sem limite por padrão
> O driver `json-file` não rotaciona arquivos por padrão. Configure `max-size` e `max-file` (globalmente no [[Arquivo daemon.json]] ou por container):
> ```bash
> docker run -d --log-opt max-size=10m --log-opt max-file=3 nginx:1.27
> ```

> [!bug] `docker logs` vazio
> Pode ser que a aplicação escreva em arquivo, ou que o driver de log não suporte leitura (por exemplo `syslog` ou `none`). Confira com `docker inspect --format '{{.HostConfig.LogConfig.Type}}' NOME`.

## Exercício

Rode `docker run -d --name relogio alpine sh -c 'while true; do date; sleep 1; done'` e use `docker logs -f --tail 5 -t relogio`. Depois remova o container.

## Veja também

- [[Comando docker inspect]]
- [[Modos interativo e detached]]
- [[Comando docker exec e attach]]
- [[MOC - Containers]]
