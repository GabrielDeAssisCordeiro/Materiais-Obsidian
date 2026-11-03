---
tags:
  - docker
  - containers
  - comandos
  - inspect
  - observabilidade
aliases: []
tipo: comando
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comandos ps e rm]]"
  - "[[Comando docker logs]]"
  - "[[Comandos stats e top]]"
  - "[[Camada gravável do container]]"
---

# Comando docker inspect

`docker inspect` retorna **JSON** com toda a configuração e estado de containers, imagens, redes e volumes. O parâmetro `--format` (templates Go) extrai campos.

```bash
docker inspect web                                   # JSON completo

# Campos úteis
docker inspect --format '{{.State.Status}}' web
docker inspect --format '{{.State.ExitCode}}' web
docker inspect --format '{{.State.OOMKilled}}' web
docker inspect --format '{{.Config.Image}}' web
docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' web

# IP em cada rede
docker inspect --format '{{range $rede, $dados := .NetworkSettings.Networks}}{{$rede}}={{$dados.IPAddress}} {{end}}' web

# Portas publicadas
docker inspect --format '{{json .NetworkSettings.Ports}}' web

# Montagens
docker inspect --format '{{json .Mounts}}' web

# Variáveis de ambiente
docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}' web
```

## Inspecionar outros objetos

```bash
docker image inspect nginx:1.27 --format '{{.Architecture}}/{{.Os}}'
docker network inspect bridge
docker volume inspect pgdata
```

> [!tip] Combine com `jq`
> `docker inspect web | jq '.[0].State'` facilita a leitura quando `jq` está instalado.

> [!danger] Segredos aparecem no inspect
> Variáveis de ambiente passadas com `-e` ficam visíveis em `docker inspect`. Não use `ENV`/`-e` para segredos sensíveis; prefira Docker secrets ou arquivos montados.

## Exercício

Para um container qualquer, extraia com `--format`: status, imagem, IP e política de restart, em uma única linha separada por espaços.

## Veja também

- [[Comandos ps e rm]]
- [[Comando docker logs]]
- [[Comandos stats e top]]
- [[Camada gravável do container]]
- [[MOC - Containers]]
