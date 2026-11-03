---
tags:
  - referencia
aliases: []
tipo: cheatsheet
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Criar Sandbox com Docker]]"
  - "[[Criar Sandbox com Podman Rootless]]"
---
# Cheat Sheet - Docker e Podman

```bash
# Execução restrita (Docker; Podman aceita as mesmas flags principais)
docker run --rm -it --read-only --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --cap-drop=ALL --security-opt no-new-privileges --network none \
  --memory 256m --cpus 0.5 --pids-limit 100 --user 65534:65534 alpine:3 sh

# Runtime alternativo
docker run --rm --runtime=runsc alpine:3 dmesg

# Inspeção
docker inspect ID --format '{{.HostConfig.Privileged}} {{.HostConfig.CapDrop}}'
docker stats --no-stream
docker events --since 10m

# Limpeza
docker rm -f $(docker ps -aq)
docker system prune -a --volumes       # CUIDADO: remove tudo sem uso

# Podman rootless
podman info --format '{{.Host.Security.Rootless}}'
podman run --rm --network none docker.io/library/alpine:3 echo ok
```

> [!danger] Nunca: `--privileged`, `-v /var/run/docker.sock:...`, `--pid=host`, `--network=host`, `--security-opt seccomp=unconfined`.

## Veja também

- [[Glossário#Sandboxes e isolamento]]
- [[Cheat Sheet - Isolamento no Linux]]
- [[Cheat Sheet - VMs]]
- [[MOC - Referência - Sandbox]]
