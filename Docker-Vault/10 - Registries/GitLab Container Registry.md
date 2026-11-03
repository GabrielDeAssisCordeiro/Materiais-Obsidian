---
tags:
  - docker
  - registries
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Login e tokens de acesso]]"
  - "[[Registries]]"
  - "[[Automação de publicação de imagens]]"
---

# GitLab Container Registry

Cada projeto GitLab pode ter um **registry de containers** integrado: `registry.gitlab.com/GRUPO/PROJETO[/IMAGEM]:TAG` (ou o domínio do seu GitLab auto-hospedado).

## Manual

```bash
# Token de acesso pessoal ou de implantação (deploy token) com read_registry/write_registry
echo "$GITLAB_TOKEN" | docker login registry.gitlab.com -u SEU_USUARIO --password-stdin

docker build -t registry.gitlab.com/grupo/projeto/api:1.0 .
docker push registry.gitlab.com/grupo/projeto/api:1.0
```

## No GitLab CI

Variáveis predefinidas: `CI_REGISTRY`, `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD`, `CI_REGISTRY_IMAGE`.

```yaml
build:
  image: docker:27
  services:
    - docker:27-dind
  script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login "$CI_REGISTRY" -u "$CI_REGISTRY_USER" --password-stdin
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA" .
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"
```

> [!tip] Política de limpeza
> Habilite as **políticas de limpeza de tags** do projeto (Settings → Packages and registries) para remover tags antigas automaticamente.

> [!warning] Docker-in-Docker exige privilégios
> O serviço `dind` roda `--privileged`. Avalie alternativas (Kaniko, BuildKit rootless, Buildah) em runners compartilhados. Veja a pasta de CI/CD.

## Exercício

Em um projeto GitLab, crie um pipeline mínimo que constrói e publica uma imagem com a tag do commit.

## Veja também

- [[Login e tokens de acesso]]
- [[Registries]]
- [[Automação de publicação de imagens]]
- [[MOC - Registries]]
