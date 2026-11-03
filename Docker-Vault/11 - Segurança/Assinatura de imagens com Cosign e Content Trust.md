---
tags:
  - docker
  - seguranca
  - supply-chain
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[SBOM e provenance]]"
  - "[[Docker Hub]]"
  - "[[Tags e digests de imagens]]"
---

# Assinatura de imagens com Cosign e Content Trust

Assinar imagens permite verificar **autenticidade** (quem publicou) e **integridade** (não foi alterada). Sem isso, qualquer um com acesso ao registry poderia substituir uma tag.

## Cosign (Sigstore) — abordagem atual mais difundida

```bash
# Par de chaves (laboratório)
cosign generate-key-pair

# Assina por DIGEST (nunca apenas pela tag)
DIGEST=$(docker buildx imagetools inspect meuusuario/app:1.0 --format '{{json .Manifest.Digest}}' | tr -d '"')
cosign sign --key cosign.key meuusuario/app@$DIGEST

# Verifica
cosign verify --key cosign.pub meuusuario/app:1.0
```

### Assinatura *keyless* (CI com identidade OIDC)

```bash
cosign sign meuusuario/app@$DIGEST
cosign verify meuusuario/app:1.0 \
  --certificate-identity-regexp 'https://github.com/ORG/REPO/.*' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

## Docker Content Trust (DCT)

```bash
export DOCKER_CONTENT_TRUST=1     # exige imagens assinadas em pull/run/push
docker pull nginx:1.27            # falha se a tag não estiver assinada
```

| | Cosign | Docker Content Trust |
|---|---|---|
| Base | Sigstore | Notary v1 |
| Chaves | Próprias ou *keyless* (OIDC) | Hierarquia TUF |
| Armazenamento | No próprio registry (OCI) | Servidor Notary |
| Adoção atual | **Alta** | Legado; uso decrescente |

> [!question] Verificar na documentação oficial
> O estado atual do Docker Content Trust/Notary v1 e de alternativas (Notation, Docker Official Images attestations) deve ser confirmado na documentação do Docker.

> [!tip] Faça valer
> Assinar só adianta se alguém **verifica**. Imponha a verificação no deploy (políticas do Kubernetes como Kyverno/Gatekeeper, ou etapa de CI).

## Exercício

Em um registry local, assine uma imagem com Cosign (par de chaves) e verifique a assinatura. Depois altere a imagem e mostre que a verificação falha.

## Veja também

- [[SBOM e provenance]]
- [[Docker Hub]]
- [[Tags e digests de imagens]]
- [[MOC - Segurança]]
