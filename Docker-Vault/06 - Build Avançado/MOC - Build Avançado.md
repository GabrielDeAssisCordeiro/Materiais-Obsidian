---
tags:
  - docker
  - moc
aliases:
  - Build Avançado
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Build Avançado

BuildKit e Buildx em profundidade: builders, cache mounts, secret e SSH mounts, builds multiplataforma, Bake, cache remoto, SBOM/provenance, reprodutibilidade e otimização.

> [!tip] Pré-requisito
> Domine primeiro [[Introdução ao Dockerfile]] e [[Multi-stage builds]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Buildx e BuildKit]] — Motor de build e plugin da CLI
- [[Builders do Buildx]] — Drivers docker, docker-container, kubernetes e remote
- [[Cache mounts]] — Diretórios de cache persistentes entre builds
- [[Secret mounts]] — Segredos de build sem vazar nas camadas
- [[SSH mounts]] — Encaminhar o ssh-agent ao build
- [[Build multiplataforma]] — amd64/arm64, QEMU e cross-compilation
- [[Docker Buildx Bake]] — Builds declarativos em HCL
- [[Cache remoto de build]] — registry, local, gha e modos de cache
- [[SBOM e provenance]] — Attestations de cadeia de suprimentos
- [[Builds reproduzíveis]] — Determinismo, digests e timestamps
- [[Otimização de tamanho e tempo de build]] — Técnicas práticas para imagens menores e builds rápidos

## Veja também

- [[Home - Docker]]
