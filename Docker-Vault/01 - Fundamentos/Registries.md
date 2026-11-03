---
tags:
  - docker
  - fundamentos
  - registry
  - imagens
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Docker Hub]]"
  - "[[Padrão OCI]]"
  - "[[Imagens vs Containers]]"
  - "[[Arquitetura do Docker]]"
---

# Registries

Um **registry** é um serviço que **armazena e distribui imagens** de container. Dentro de um registry, imagens ficam em **repositórios**, e cada versão recebe uma **tag**.

## Anatomia do nome de uma imagem

```text
registro.exemplo.com:5000 / equipe / api : 1.4.2
└──── host[:porta] ──────┘   └namespace┘ └repo┘ └tag┘

nginx:1.27                       → docker.io/library/nginx:1.27 (Docker Hub, imagem oficial)
meuusuario/app:2.0               → docker.io/meuusuario/app:2.0
ghcr.io/org/app@sha256:ab12...   → GitHub Container Registry, referência por digest
```

Sem host explícito, o Docker usa o **Docker Hub** (`docker.io`).

## Registries comuns

| Registry | Observação |
|---|---|
| Docker Hub | Padrão; imagens oficiais, verificadas e privadas. |
| GitHub Container Registry (`ghcr.io`) | Integrado ao GitHub Actions. |
| GitLab Container Registry | Integrado ao GitLab CI. |
| AWS ECR, Google Artifact Registry, Azure ACR | Registries gerenciados das nuvens. |
| `registry:2` / Harbor | Auto-hospedados. |

```bash
docker pull nginx:1.27           # baixa do Docker Hub
docker pull ghcr.io/OWNER/IMAGEM:TAG   # de outro registry (substitua OWNER, IMAGEM e TAG)
```

> [!info] Tags vs digests
> Tags são ponteiros **mutáveis**; o digest (`sha256:...`) é **imutável** e identifica exatamente o conteúdo. Veja [[Tags e digests de imagens]].

## Exercício

Escreva o nome completo (com host) para a imagem `redis:7` e para a imagem `ghcr.io/org/app:1.0`, indicando qual é o registry de cada uma.

## Veja também

- [[Docker Hub]]
- [[Padrão OCI]]
- [[Imagens vs Containers]]
- [[Arquitetura do Docker]]
- [[MOC - Fundamentos - Docker]]
