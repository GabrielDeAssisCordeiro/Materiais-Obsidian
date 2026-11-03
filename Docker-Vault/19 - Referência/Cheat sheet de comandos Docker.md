---
tags:
  - docker
  - referencia
  - cheat-sheet
  - comandos
aliases:
  - Cheat sheet Docker
  - Comandos Docker
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Cheat sheet de Dockerfile]]"
  - "[[Cheat sheet de Docker Compose]]"
  - "[[Cheat sheet de redes Docker]]"
  - "[[Cheat sheet de volumes Docker]]"
  - "[[Cheat sheet de limpeza Docker]]"
  - "[[Comando docker run]]"
---

# Cheat sheet de comandos Docker

## Containers

```bash
docker run -d --name web -p 8080:80 nginx:1.27       # cria e inicia em segundo plano
docker run --rm -it alpine:3.20 sh                   # shell descartável
docker ps [-a]                                       # lista (todos com -a)
docker logs -f --tail 100 web                        # logs
docker exec -it web sh                               # shell no container em execução
docker stop web && docker start web                  # parar/iniciar
docker restart web                                   # reiniciar
docker kill web                                      # SIGKILL
docker rm [-f] web                                   # remover
docker inspect web                                   # JSON completo
docker inspect -f '{{.State.Status}}' web            # campo específico
docker stats --no-stream                             # consumo de recursos
docker top web                                       # processos
docker cp web:/etc/nginx/nginx.conf .                # copiar do container
docker diff web                                      # mudanças na camada gravável
docker port web                                      # portas publicadas
docker rename web web-v1
docker update --restart unless-stopped --memory 256m web
docker wait web                                      # espera terminar e mostra o código
docker pause web && docker unpause web
```

## Imagens

```bash
docker pull nginx:1.27
docker build -t meu-app:1.0 .
docker build --no-cache --target prod -f Dockerfile.prod -t meu-app:prod .
docker images [--digests]
docker history meu-app:1.0
docker image inspect meu-app:1.0
docker tag meu-app:1.0 usuario/meu-app:1.0
docker push usuario/meu-app:1.0
docker save -o app.tar meu-app:1.0 && docker load -i app.tar
docker rmi meu-app:1.0
docker search nginx --filter is-official=true
```

## Buildx

```bash
docker buildx ls
docker buildx create --name multi --driver docker-container --use
docker buildx build --platform linux/amd64,linux/arm64 -t usuario/app:1.0 --push .
docker buildx bake --print
docker buildx imagetools inspect usuario/app:1.0
docker buildx du && docker buildx prune
```

## Sistema e diagnóstico

```bash
docker version                 # cliente e servidor
docker info                    # configuração do daemon
docker system df               # uso de disco
docker events --since 10m      # eventos
docker context ls              # contextos
docker login / docker logout
docker network ls / docker volume ls
```

## Execução: opções mais usadas

| Opção | Efeito |
|---|---|
| `-d` / `-it` / `--rm` | Segundo plano / interativo / remove ao sair |
| `-p H:C` / `-P` | Publica porta |
| `-e K=V` / `--env-file f` | Variáveis |
| `-v nome:/dest` / `--mount` | Volumes e montagens |
| `--network` / `--network-alias` | Rede |
| `--restart` | Política de restart |
| `-m` / `--cpus` / `--pids-limit` | Limites |
| `-u` / `--read-only` / `--cap-drop` | Segurança |
| `--init` / `--entrypoint` / `-w` | PID 1 / entrypoint / diretório |

## Exercício

Sem consultar, escreva os comandos para: subir um Redis em segundo plano com volume, ver os logs, entrar no container e removê-lo preservando o volume.

## Veja também

- [[Cheat sheet de Dockerfile]]
- [[Cheat sheet de Docker Compose]]
- [[Cheat sheet de redes Docker]]
- [[Cheat sheet de volumes Docker]]
- [[Cheat sheet de limpeza Docker]]
- [[Comando docker run]]
- [[MOC - Referência - Docker]]
