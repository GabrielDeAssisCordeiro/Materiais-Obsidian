---
tags:
  - docker
  - cicd
  - github-actions
  - buildx
  - ghcr
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Pipeline CI-CD com Docker]]"
  - "[[Cache remoto de build]]"
  - "[[Build multiplataforma]]"
  - "[[GitHub Container Registry]]"
  - "[[Tagging e versionamento semântico em CI]]"
---

# GitHub Actions para build e push

Workflow completo: build multiplataforma, tags automáticas, cache, SBOM/provenance e push ao **GHCR**.

`.github/workflows/docker.yml`:

```yaml
name: docker

on:
  push:
    branches: [main]
    tags: ["v*.*.*"]
  pull_request:

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: QEMU (multiplataforma)
        uses: docker/setup-qemu-action@v3

      - name: Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login no GHCR
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Metadados (tags e labels)
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha

      - name: Build e push
        uses: docker/build-push-action@v6
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          sbom: true
          provenance: mode=max
```

## O que cada parte faz

| Passo | Função |
|---|---|
| `setup-qemu` / `setup-buildx` | Habilita multiplataforma e o builder `docker-container` |
| `login-action` | Autentica com o `GITHUB_TOKEN` (sem segredos pessoais) |
| `metadata-action` | Gera tags (`main`, `1.2.3`, `1.2`, `sha-abc123`) e labels OCI |
| `build-push-action` | Constrói e publica; em PRs apenas constrói (sem push) |
| `cache-*` | Cache do GitHub Actions entre execuções |

> [!tip] Release por tag
> Ao criar uma tag `v1.2.3` no Git, o workflow publica `1.2.3`, `1.2` e `sha-...` automaticamente.

> [!warning] Fixe versões e permissões
> Em projetos sensíveis, fixe as actions por **SHA de commit** e mantenha `permissions` mínimas. Para publicar em registries externos use **OIDC** em vez de segredos de longa duração.

> [!question] Verificar na documentação oficial
> As versões maiores das actions (`@v3`, `@v4`, `@v5`, `@v6`) evoluem. Confirme as atuais no GitHub Marketplace e na documentação do Docker sobre GitHub Actions; a configuração do backend `type=gha` também pode ter mudado.

## Exercício

Adapte o workflow ao seu repositório, abra um PR (só build) e depois crie uma tag `v0.1.0` para ver a publicação no GHCR com as tags geradas.

## Veja também

- [[Pipeline CI-CD com Docker]]
- [[Cache remoto de build]]
- [[Build multiplataforma]]
- [[GitHub Container Registry]]
- [[Tagging e versionamento semântico em CI]]
- [[MOC - CI-CD e DevOps]]
