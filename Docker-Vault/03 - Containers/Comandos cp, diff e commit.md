---
tags:
  - docker
  - containers
  - comandos
  - arquivos
aliases: []
tipo: comando
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comando docker exec e attach]]"
  - "[[Camada gravável do container]]"
  - "[[Camadas de uma imagem]]"
  - "[[Introdução ao Dockerfile]]"
---

# Comandos cp, diff e commit

## `docker cp`: copiar arquivos entre host e container

```bash
# Container → host
docker cp web:/etc/nginx/nginx.conf ./nginx.conf

# Host → container
docker cp ./index.html web:/usr/share/nginx/html/index.html

# Diretórios inteiros
docker cp web:/var/log/nginx ./logs-nginx
```

## `docker diff`: o que mudou na camada gravável

```bash
docker diff web
# A = adicionado, C = alterado, D = removido
```

## `docker commit`: transformar um container em imagem

```bash
docker run -d --name base alpine:3.20 sleep 600
docker exec base apk add --no-cache curl
docker commit -m "alpine com curl" base meu-alpine:curl
docker run --rm meu-alpine:curl curl --version
docker rm -f base
```

> [!warning] `commit` não é boa prática
> Imagens criadas com `commit` **não são reproduzíveis** (não há registro das etapas) e podem carregar lixo e segredos. Em vez disso, escreva um **Dockerfile** e use `docker build`. Veja [[Introdução ao Dockerfile]].

> [!tip] Usos legítimos de `cp` e `diff`
> Extrair arquivos de configuração padrão para usar como ponto de partida e investigar o que uma aplicação está gravando fora de volumes.

## Exercício

Extraia `/etc/nginx/conf.d/default.conf` de um container Nginx, edite-o localmente e copie de volta. Use `docker diff` para confirmar a alteração.

## Veja também

- [[Comando docker exec e attach]]
- [[Camada gravável do container]]
- [[Camadas de uma imagem]]
- [[Introdução ao Dockerfile]]
- [[MOC - Containers]]
