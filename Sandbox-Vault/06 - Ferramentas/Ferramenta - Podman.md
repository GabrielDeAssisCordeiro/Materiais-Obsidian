---
tags:
  - ferramentas
aliases:
  - "Podman rootless"
tipo: ferramenta
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Containers]]"
  - "[[Criar Sandbox com Podman Rootless]]"
---
# Ferramenta - Podman

Engine de containers **sem daemon** e *rootless* por padrão; CLI compatível com o Docker (`alias docker=podman`). Suporta *pods* e geração de unidades systemd (Quadlet).

```bash
podman run --rm docker.io/library/alpine:3 echo ola
podman ps -a
```

## Veja também

- [[Criar Sandbox com Podman Rootless]]
- [[Sandbox por Containers]]
- [[Comparativo de Ferramentas]]
- [[MOC - Ferramentas]]
