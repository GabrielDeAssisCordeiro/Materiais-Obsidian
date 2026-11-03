---
tags:
  - docker
  - instalacao
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Instalação no Linux]]"
  - "[[Instalação no Windows com WSL2]]"
  - "[[Instalação no macOS]]"
  - "[[Arquitetura do Docker]]"
  - "[[Comando docker run]]"
---

# Verificando com hello-world

A imagem `hello-world` é o teste mais simples para confirmar que cliente, daemon, rede e registry estão funcionando.

```bash
docker run --rm hello-world
```

## O que a mensagem de saída explica

1. O **cliente** contatou o **daemon**.
2. O daemon fez **pull** da imagem `hello-world` do Docker Hub.
3. O daemon **criou um container** a partir da imagem e executou o programa que imprime a mensagem.
4. O daemon enviou a saída ao cliente, que a exibiu no terminal.

## Verificações complementares

```bash
docker version                 # cliente e servidor respondem?
docker info                    # driver, cgroup, runtime, registry
docker compose version         # plugin Compose instalado?
docker buildx version          # plugin Buildx instalado?
docker run --rm alpine:3.20 echo "ola, docker"
```

## Diagnóstico rápido

| Sintoma | Provável causa | Ação |
|---|---|---|
| `Cannot connect to the Docker daemon` | Daemon parado ou `DOCKER_HOST` errado | `systemctl status docker`, `docker context ls` |
| `permission denied ... docker.sock` | Usuário fora do grupo `docker` | Veja [[Pós-instalação no Linux]] |
| `Unable to find image ... TLS handshake timeout` | Rede, proxy ou DNS | Testar `curl https://registry-1.docker.io/v2/` e configurar proxy |
| `exec format error` | Imagem de outra arquitetura | Usar `--platform` ou imagem multiplataforma |

## Exercício

Execute `hello-world` e, em seguida, `docker image ls` e `docker container ls -a`. Por que o container não aparece mais na lista quando usamos `--rm`?

## Veja também

- [[Instalação no Linux]]
- [[Instalação no Windows com WSL2]]
- [[Instalação no macOS]]
- [[Arquitetura do Docker]]
- [[Comando docker run]]
- [[MOC - Instalação e Configuração]]
