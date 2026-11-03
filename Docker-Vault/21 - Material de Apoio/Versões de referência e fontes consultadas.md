---
tags:
  - docker
  - anexos
  - fontes
aliases: []
tipo: anexo
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Comunidades e fontes oficiais]]"
  - "[[Como usar este vault - Docker]]"
  - "[[Docker Model Runner]]"
---

# Versões de referência e fontes consultadas

Este material foi elaborado com consulta a fontes oficiais em **24/10/2026**. As versões abaixo são **referências** do momento da elaboração.

| Componente | Referência | Observação |
|---|---|---|
| Docker Engine | Série **29.x** | Instalações novas usam o **containerd image store** por padrão; versão mínima de API reduzida (v1.40) em releases recentes da série |
| Docker Compose | **v2** (plugin `docker compose`) | Compose Specification; **sem** campo `version` |
| Buildx / BuildKit | Plugin atual; BuildKit padrão desde o Engine 23.0 | `docker buildx version` mostra a versão instalada |
| Docker Model Runner | Comandos `docker model ...` | Recurso em evolução; confirme na documentação |
| Docker Hardened Images | Catálogo em `dhi.io` | Anunciadas como gratuitas e abertas (Apache 2.0) |
| Imagens dos exemplos | Tags fixadas (ex.: `nginx:1.27`, `postgres:16`, `python:3.12-slim`, `node:22-alpine`) | Atualize para versões suportadas ao usar |

> [!warning] Tudo envelhece
> Versões de imagens, actions, ferramentas e preços mudam. Antes de usar um exemplo em produção, **verifique as versões atuais** e leia as notas de versão.

> [!question] Verificar na documentação oficial
> Itens marcados com este callout ao longo do vault indicam detalhes que podem ter mudado ou que não foram confirmados em fonte primária no momento da elaboração.

## Fontes primárias consultadas

- Documentação do Docker (Engine, Desktop, Compose, Buildx/BuildKit, Dockerfile reference, Docker Hub, Docker Scout, Swarm, Model Runner, Hardened Images).
- Notas de versão do Docker Engine (série 29).
- Especificações OCI, projetos containerd e runc.
- OWASP Docker Security Cheat Sheet e CIS Docker Benchmark (referência conceitual).

## Veja também

- [[Comunidades e fontes oficiais]]
- [[Como usar este vault - Docker]]
- [[Docker Model Runner]]
