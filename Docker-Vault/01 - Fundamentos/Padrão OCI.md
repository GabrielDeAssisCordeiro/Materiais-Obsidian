---
tags:
  - docker
  - fundamentos
  - padroes
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[containerd e runc]]"
  - "[[Imagens vs Containers]]"
  - "[[Registries]]"
  - "[[História do Docker]]"
---

# Padrão OCI

A **Open Container Initiative (OCI)** é um projeto da Linux Foundation, criado em 2015 por Docker e outras empresas, para padronizar os formatos de containers e evitar dependência de um único fornecedor.

## As três especificações

| Especificação | O que define |
|---|---|
| **Runtime Spec** | Como executar um container a partir de um *bundle* (`config.json` + rootfs). Implementação de referência: `runc`. |
| **Image Spec** | O formato da imagem: *manifest*, *config*, camadas (tar + gzip/zstd) e *index* multiplataforma. |
| **Distribution Spec** | A API HTTP para enviar e baixar imagens e artefatos em registries. |

## Por que importa?

- Uma imagem construída com Docker roda em Podman, containerd, CRI-O e Kubernetes.
- Qualquer registry compatível (Docker Hub, GHCR, ECR, ACR, Harbor) armazena as mesmas imagens.
- Ferramentas de segurança e de build (Trivy, Cosign, Buildah) funcionam entre ecossistemas.

## Estrutura de uma imagem OCI

```text
index (multiplataforma)
 ├── manifest linux/amd64 ─► config + camadas
 └── manifest linux/arm64 ─► config + camadas
```

```bash
# Inspeciona o manifest (inclui o index multiplataforma) sem baixar a imagem
docker buildx imagetools inspect alpine:3.20
```

> [!info] Artefatos OCI
> Registries OCI armazenam também outros artefatos: charts Helm, SBOMs, assinaturas e atestados de *provenance*. Veja [[Registries]].

## Exercício

Execute `docker buildx imagetools inspect alpine:3.20` e liste as plataformas disponíveis para essa imagem.

## Veja também

- [[containerd e runc]]
- [[Imagens vs Containers]]
- [[Registries]]
- [[História do Docker]]
- [[MOC - Fundamentos - Docker]]
