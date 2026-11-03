---
tags:
  - docker
  - build-avancado
  - seguranca
  - supply-chain
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Docker Scout]]"
  - "[[Padrão OCI]]"
  - "[[Builds reproduzíveis]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# SBOM e provenance

**Attestations** são metadados assinados/anexados à imagem que descrevem *do que ela é feita* e *como foi construída*.

| Attestation | Conteúdo |
|---|---|
| **SBOM** (Software Bill of Materials) | Lista de pacotes e bibliotecas na imagem (SPDX/CycloneDX) |
| **Provenance** (SLSA) | Origem do build: repositório, commit, builder, parâmetros |

```bash
# Gera SBOM e provenance no build (e publica no registry)
docker buildx build \
  --sbom=true \
  --provenance=mode=max \
  -t meuusuario/app:1.0 --push .

# Inspeciona
docker buildx imagetools inspect meuusuario/app:1.0 --format '{{ json .SBOM }}'
docker buildx imagetools inspect meuusuario/app:1.0 --format '{{ json .Provenance }}'
```

> [!info] Para que servem
> Auditoria, resposta rápida a vulnerabilidades novas (você sabe onde cada biblioteca está) e verificação de que a imagem veio do pipeline esperado. Ferramentas como Docker Scout, Trivy e Grype consomem SBOMs.

> [!question] Verificar na documentação oficial
> O comportamento padrão de provenance (por exemplo, `mode=min` automático em alguns cenários) e o suporte com o driver `docker` dependem da versão do Buildx e do image store.

> [!tip] Assine também
> Attestations ganham valor quando combinadas com assinatura de imagem (Cosign, Notation). Veja a pasta de segurança.

## Exercício

Construa uma imagem com `--sbom=true` e `--provenance=mode=max` para um registry local (`registry:2`) e inspecione os resultados.

## Veja também

- [[Docker Scout]]
- [[Padrão OCI]]
- [[Builds reproduzíveis]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Build Avançado]]
