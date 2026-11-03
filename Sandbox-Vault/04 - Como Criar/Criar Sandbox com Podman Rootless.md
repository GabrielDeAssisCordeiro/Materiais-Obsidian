---
tags:
  - como-criar
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Containers]]"
  - "[[Namespaces do Linux]]"
  - "[[Criar Sandbox com Docker]]"
---
# Criar Sandbox com Podman Rootless

O **Podman** executa containers **sem daemon** e, por padrão, **sem root** (*rootless*), mapeando o root interno para o seu UID via user namespaces.

## Pré-requisitos

```bash
sudo apt install podman uidmap          # Debian/Ubuntu
grep "$USER" /etc/subuid /etc/subgid     # faixas de UIDs subordinados
podman info --format '{{.Host.Security.Rootless}}'   # true
```

## Execução restrita

```bash
podman run --rm -it \
  --network none --read-only \
  --cap-drop=all --security-opt no-new-privileges \
  --memory 256m --pids-limit 100 \
  docker.io/library/alpine:3 sh
```

> [!info] Por que rootless ajuda
> Se o processo escapar do container, ele encontra apenas um usuário comum no host, não o root.

> [!question] Verificar na documentação oficial
> Limites de recursos em modo rootless dependem de cgroup v2 e da delegação de controladores ao usuário.

## Exercício

Rode `id` dentro do container e `ps -u $USER` no host. Qual UID real o processo tem no host?

## Veja também

- [[Sandbox por Containers]]
- [[Criar Sandbox com Docker]]
- [[Namespaces do Linux]]
- [[MOC - Como Criar]]
