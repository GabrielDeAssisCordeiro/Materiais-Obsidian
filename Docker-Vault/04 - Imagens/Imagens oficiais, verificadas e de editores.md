---
tags:
  - docker
  - imagens
  - docker-hub
  - seguranca
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Docker Hub]]"
  - "[[Escolha da imagem base]]"
  - "[[Docker Scout]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Imagens oficiais, verificadas e de editores

Nem toda imagem do Docker Hub tem o mesmo nível de confiança. Procure os selos:

| Selo | Significado |
|---|---|
| **Docker Official Image** | Curada pela Docker e mantenedores upstream; Dockerfiles públicos, atualizados e revisados (ex.: `nginx`, `postgres`, `python`). |
| **Verified Publisher** | Publicada por empresa verificada (ex.: fornecedores de software). |
| **Docker-Sponsored Open Source** | Projeto open source patrocinado pela Docker. |
| Sem selo | Qualquer usuário pode publicar; confie com cautela. |

## Como avaliar uma imagem

1. Selo oficial/verificado e **página do repositório** (README, tags, Dockerfile de origem).
2. Frequência de atualização e suporte a sua arquitetura.
3. **Tamanho** e conteúdo (base, usuário não-root).
4. Resultado de varredura de vulnerabilidades (Docker Scout, Trivy).
5. Preferir imagens cujo *build* é reproduzível e que publicam SBOM e *provenance*.

```bash
docker search nginx --filter is-official=true --limit 5
docker scout quickview nginx:1.27      # resumo de vulnerabilidades (requer Docker Scout)
```

> [!danger] Imagens de terceiros são código que roda na sua máquina
> Imagens maliciosas já foram publicadas (mineradores de criptomoeda, backdoors). Nunca execute imagens desconhecidas em produção nem com `--privileged`.

> [!tip] Espelhe o que é crítico
> Copie imagens de base para o **seu** registry e construa a partir delas. Isso protege contra remoção de tags, limites de pull e troca de conteúdo.

## Exercício

Pesquise no Docker Hub as imagens `redis`, `bitnami/redis` e uma de usuário desconhecido. Compare selos, frequência de atualização e instruções de uso.

## Veja também

- [[Docker Hub]]
- [[Escolha da imagem base]]
- [[Docker Scout]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Imagens]]
