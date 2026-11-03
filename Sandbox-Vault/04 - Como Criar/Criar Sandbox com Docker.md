---
tags:
  - como-criar
aliases:
  - "Docker Compose restrito"
  - "docker run seguro"
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Containers]]"
  - "[[Seccomp]]"
  - "[[Capabilities do Linux]]"
  - "[[Cgroups]]"
---
# Criar Sandbox com Docker

## `docker run` endurecido

```bash
docker run --rm -it \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --cap-drop=ALL \
  --security-opt no-new-privileges \
  --network none \
  --memory 256m --memory-swap 256m \
  --cpus 0.5 \
  --pids-limit 100 \
  --user 65534:65534 \
  alpine:3 sh
```

| Flag | Função |
|---|---|
| `--read-only` | Raiz do container somente leitura |
| `--tmpfs` | Área temporária em memória, sem execução |
| `--cap-drop=ALL` | Remove todas as capabilities |
| `--security-opt no-new-privileges` | Bloqueia ganho de privilégio |
| `--network none` | Sem rede |
| `--memory`, `--cpus`, `--pids-limit` | Limites de recursos |
| `--user` | Usuário sem privilégios |

## Docker Compose equivalente

```yaml
services:
  sandbox:
    image: alpine:3
    command: ["sleep", "3600"]
    read_only: true
    tmpfs:
      - /tmp:rw,noexec,nosuid,size=64m
    cap_drop: [ALL]
    security_opt:
      - no-new-privileges:true
    network_mode: none
    mem_limit: 256m
    cpus: 0.5
    pids_limit: 100
    user: "65534:65534"
```

## Verificação

```bash
docker inspect --format '{{.HostConfig.ReadonlyRootfs}} {{.HostConfig.CapDrop}} {{.HostConfig.NetworkMode}}' <container>
```

> [!danger] Nunca em sandbox: `--privileged`, `-v /var/run/docker.sock`, `--pid=host`, `--network=host`, montagem de `/` ou `$HOME`
> Qualquer um desses derruba a contenção.

> [!tip] Fixe versões por *digest* (`image@sha256:...`) para reprodutibilidade e atualize imagens regularmente.

## Exercício

Rode o container acima e tente: `touch /x`, `ping 8.8.8.8`, `apk add curl`. Explique por que cada um falha.

## Veja também

- [[Sandbox por Containers]]
- [[Seccomp]]
- [[Criar Sandbox com Podman Rootless]]
- [[Criar Sandbox para Código de IA]]
- [[MOC - Como Criar]]
