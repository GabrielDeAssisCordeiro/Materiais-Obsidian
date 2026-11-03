---
tags:
  - docker
  - build-avancado
  - buildx
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Buildx e BuildKit]]"
  - "[[Build multiplataforma]]"
  - "[[Cache remoto de build]]"
  - "[[Visão geral do Docker Compose]]"
---

# Docker Buildx Bake

O **Bake** descreve vários builds (alvos) em um arquivo declarativo e os executa em paralelo, com variáveis e herança. Aceita HCL, JSON e até `compose.yaml`.

`docker-bake.hcl`:

```hcl
variable "TAG" {
  default = "dev"
}

group "default" {
  targets = ["api", "web"]
}

target "base" {
  platforms = ["linux/amd64", "linux/arm64"]
}

target "api" {
  inherits   = ["base"]
  context    = "./api"
  dockerfile = "Dockerfile"
  tags       = ["meuusuario/api:${TAG}"]
}

target "web" {
  inherits = ["base"]
  context  = "./web"
  tags     = ["meuusuario/web:${TAG}"]
}
```

```bash
docker buildx bake --print            # mostra a configuração resolvida (não constrói)
docker buildx bake                    # constrói o grupo default
docker buildx bake api                # apenas um alvo
TAG=1.2.0 docker buildx bake --push   # variável de ambiente + publica
docker buildx bake --set api.args.VERSION=1.2.0   # sobrescreve atributos
```

> [!tip] Bake com Compose
> `docker buildx bake -f compose.yaml` constrói os serviços que têm `build:` definidos, aproveitando paralelismo.

> [!info] Por que usar?
> Substitui scripts longos com vários `docker build`, centraliza tags/plataformas/cache e padroniza o build entre desenvolvimento e CI.

## Exercício

Crie um `docker-bake.hcl` com dois alvos de imagens simples, use `--print` para validar e execute o grupo `default`.

## Veja também

- [[Buildx e BuildKit]]
- [[Build multiplataforma]]
- [[Cache remoto de build]]
- [[Visão geral do Docker Compose]]
- [[MOC - Build Avançado]]
