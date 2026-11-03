---
tags:
  - ferramentas
aliases:
  - "Docker Engine"
  - "Docker Desktop"
tipo: ferramenta
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Containers]]"
  - "[[Criar Sandbox com Docker]]"
---
# Ferramenta - Docker

Plataforma de containers com daemon (`dockerd`), CLI, imagens (Docker Hub) e Compose.

| Item | Detalhe |
|---|---|
| Isolamento | namespaces + cgroups + seccomp/AppArmor padrão |
| Versão de referência | Engine 29.x em 2026 (consulte as *release notes* oficiais) |
| Rootless | Disponível (`dockerd-rootless-setuptool.sh`) |
| Pontos de atenção | Socket do Docker equivale a root; Docker Desktop tem termos de licença por porte |

```bash
docker version
docker info --format '{{.SecurityOptions}}'
```

## Veja também

- [[Sandbox por Containers]]
- [[Criar Sandbox com Docker]]
- [[Comparativo de Ferramentas]]
- [[MOC - Ferramentas]]
