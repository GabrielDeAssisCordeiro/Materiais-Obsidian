---
tags:
  - docker
  - cicd
  - versionamento
  - semver
  - tags
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Versionamento e tags imutáveis]]"
  - "[[GitHub Actions para build e push]]"
  - "[[Tags e digests de imagens]]"
---

# Tagging e versionamento semântico em CI

Padronize como as tags nascem a partir do Git.

| Origem no Git | Tags da imagem |
|---|---|
| Commit em `main` | `main`, `sha-a1b2c3d` |
| Pull request | `pr-123` (efêmera) |
| Tag `v1.4.2` | `1.4.2`, `1.4`, `1`, `sha-...` |
| Release candidate `v1.5.0-rc.1` | `1.5.0-rc.1` |

## Gerando a versão

```bash
# Versão derivada do Git
VERSAO=$(git describe --tags --always --dirty)
SHA=$(git rev-parse --short HEAD)

docker build \
  --build-arg VERSION="$VERSAO" \
  --label "org.opencontainers.image.version=$VERSAO" \
  --label "org.opencontainers.image.revision=$(git rev-parse HEAD)" \
  -t meu-app:"$VERSAO" -t meu-app:sha-"$SHA" .
```

## Versionamento semântico automático

Ferramentas como **semantic-release** e **release-please** leem *Conventional Commits* (`feat:`, `fix:`, `feat!:`) e calculam a próxima versão (major/minor/patch), criam a tag e o *changelog*, disparando o pipeline de publicação.

| Prefixo | Efeito |
|---|---|
| `fix:` | patch (1.4.2 → 1.4.3) |
| `feat:` | minor (1.4.2 → 1.5.0) |
| `feat!:` ou `BREAKING CHANGE` | major (1.4.2 → 2.0.0) |

> [!tip] Deploy por digest
> O pipeline pode registrar o **digest** da imagem publicada e o deploy usar `imagem@sha256:...`, garantindo que o que foi testado é o que roda. Veja [[Tags e digests de imagens]].

> [!warning] Nunca reutilize uma tag de versão
> Republicar `1.4.2` com conteúdo diferente quebra rollback e auditoria. Torne as tags imutáveis no registry.

## Exercício

Escreva a regra de tagging do seu projeto (tabela Git → tags) e implemente com `docker/metadata-action` ou um script.

## Veja também

- [[Versionamento e tags imutáveis]]
- [[GitHub Actions para build e push]]
- [[Tags e digests de imagens]]
- [[MOC - CI-CD e DevOps]]
