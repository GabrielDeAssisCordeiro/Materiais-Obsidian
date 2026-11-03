---
tags:
  - docker
  - cicd
  - registry
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Pipeline CI-CD com Docker]]"
  - "[[GitLab Container Registry]]"
  - "[[Riscos do --privileged]]"
  - "[[Cache remoto de build]]"
---

# GitLab CI com Docker

`.gitlab-ci.yml` com build, teste e push usando Docker-in-Docker (`dind`).

```yaml
stages:
  - build
  - test
  - release

variables:
  DOCKER_TLS_CERTDIR: "/certs"
  IMAGE: "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA"

default:
  image: docker:27
  services:
    - docker:27-dind
  before_script:
    - echo "$CI_REGISTRY_PASSWORD" | docker login "$CI_REGISTRY" -u "$CI_REGISTRY_USER" --password-stdin

build:
  stage: build
  script:
    - docker pull "$CI_REGISTRY_IMAGE:latest" || true
    - docker build --cache-from "$CI_REGISTRY_IMAGE:latest" -t "$IMAGE" .
    - docker push "$IMAGE"

test:
  stage: test
  script:
    - docker run --rm "$IMAGE" npm test

release:
  stage: release
  rules:
    - if: $CI_COMMIT_TAG
  script:
    - docker pull "$IMAGE"
    - docker tag "$IMAGE" "$CI_REGISTRY_IMAGE:$CI_COMMIT_TAG"
    - docker tag "$IMAGE" "$CI_REGISTRY_IMAGE:latest"
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_TAG"
    - docker push "$CI_REGISTRY_IMAGE:latest"
```

## Observações

| Tema | Detalhe |
|---|---|
| `dind` | O serviço roda em modo privilegiado; o runner precisa permitir (`privileged = true`) |
| Cache | `--cache-from` com a imagem anterior (ou cache de registry do Buildx) |
| Variáveis predefinidas | `CI_REGISTRY*`, `CI_COMMIT_SHORT_SHA`, `CI_COMMIT_TAG` |
| Alternativa ao `dind` | Montar o socket do host (**riscoso**), BuildKit rootless, Buildah |

> [!warning] Kaniko
> O Kaniko foi uma alternativa popular para builds sem daemon, mas o projeto original foi arquivado. Avalie Buildah, BuildKit rootless/remoto ou forks mantidos.

> [!question] Verificar na documentação oficial
> Confirme o status atual das alternativas ao `dind` e a documentação de "Build and push container images" do GitLab.

> [!danger] `latest` no `release` é conveniência
> Para deploy, use sempre a **tag de versão** ou o digest, não `latest`.

## Exercício

Crie o pipeline acima em um projeto de teste, rode-o e confirme as imagens `sha` e `tag` no registry do projeto.

## Veja também

- [[Pipeline CI-CD com Docker]]
- [[GitLab Container Registry]]
- [[Riscos do --privileged]]
- [[Cache remoto de build]]
- [[MOC - CI-CD e DevOps]]
