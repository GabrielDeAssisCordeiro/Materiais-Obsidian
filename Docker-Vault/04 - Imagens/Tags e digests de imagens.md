---
tags:
  - docker
  - imagens
  - tags
  - versionamento
aliases:
  - Tags e digests
  - latest
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Versionamento e tags imutáveis]]"
  - "[[Comando docker pull]]"
  - "[[Registries]]"
  - "[[Comando docker tag e push]]"
---

# Tags e digests de imagens

## Tag

Rótulo legível apontando para uma versão da imagem (`nginx:1.27`, `postgres:16`). **Tags são mutáveis**: o mantenedor pode publicar outro conteúdo sob a mesma tag (por exemplo, `1.27` recebe correções de segurança; `latest` muda a cada release).

## Digest

Hash SHA-256 do **manifest** da imagem (`sha256:3a1b...`). É **imutável**: o mesmo digest sempre significa exatamente o mesmo conteúdo.

```bash
# Ver digests locais
docker images --digests nginx

# Descobrir o digest de uma imagem no registry (sem baixar)
docker buildx imagetools inspect nginx:1.27 | head -n 5

# Usar por digest (mantendo a tag como comentário legível)
docker pull nginx:1.27@sha256:<digest>
```

## Qual usar?

| Cenário | Recomendação |
|---|---|
| Estudo e laboratório | Tag específica (`nginx:1.27`) |
| Desenvolvimento | Tag de versão menor (`python:3.12-slim`) |
| **Produção e builds auditáveis** | Tag de versão **+ digest** (`image:1.27@sha256:...`) |
| Nunca em produção | `latest` ou tags flutuantes sem controle |

> [!warning] `latest` não significa "mais recente estável"
> É só uma tag padrão. Pode apontar para uma versão antiga, ou mudar sem aviso e quebrar seu deploy.

> [!tip] Atualização controlada
> Ferramentas como Renovate e Dependabot abrem *pull requests* ao detectar novos digests/tags, mantendo a imutabilidade e a atualização contínua.

## Exercício

Obtenha o digest de `alpine:3.20` e execute o container usando `alpine@sha256:<digest>`. Por que isso é mais seguro que usar só a tag?

## Veja também

- [[Versionamento e tags imutáveis]]
- [[Comando docker pull]]
- [[Registries]]
- [[Comando docker tag e push]]
- [[MOC - Imagens]]
