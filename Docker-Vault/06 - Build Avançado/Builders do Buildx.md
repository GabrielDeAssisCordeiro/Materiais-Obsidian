---
tags:
  - docker
  - build-avancado
  - buildx
  - drivers
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Buildx e BuildKit]]"
  - "[[Build multiplataforma]]"
  - "[[Cache remoto de build]]"
---

# Builders do Buildx

Um **builder** é uma instância do BuildKit com um **driver** específico.

| Driver | Características |
|---|---|
| `docker` | Usa o BuildKit embutido no daemon; recursos limitados (cache avançado e multiplataforma dependem do image store) |
| `docker-container` | BuildKit em um container dedicado; suporta cache remoto, multiplataforma, attestations |
| `kubernetes` | Builds em pods de um cluster |
| `remote` | Conecta a um BuildKit já em execução |

```bash
# Cria e seleciona um builder com driver docker-container
docker buildx create --name meu-builder --driver docker-container --use

# Inicializa e inspeciona
docker buildx inspect --bootstrap

# Alterna e remove
docker buildx use default
docker buildx rm meu-builder
```

> [!info] Containerd image store
> Com o **containerd image store** (padrão em instalações novas do Engine 29 e no Docker Desktop recente), o driver `docker` ganha suporte a multiplataforma e a imagens com attestations sem precisar de um builder separado.

> [!question] Verificar na documentação oficial
> Os recursos exatos do driver `docker` com containerd image store variam por versão. Consulte "Buildx drivers" e "containerd image store" na documentação.

> [!tip] Em CI
> Use `docker/setup-buildx-action` (GitHub Actions) para criar um builder com `docker-container` automaticamente.

## Exercício

Crie um builder `docker-container`, execute `docker buildx inspect --bootstrap` e compare a lista de plataformas com a do builder `default`.

## Veja também

- [[Buildx e BuildKit]]
- [[Build multiplataforma]]
- [[Cache remoto de build]]
- [[MOC - Build Avançado]]
