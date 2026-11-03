---
tags:
  - docker
  - imagens
  - versionamento
  - semver
  - producao
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Tags e digests de imagens]]"
  - "[[Comando docker tag e push]]"
  - "[[Docker Hub]]"
  - "[[Escolha da imagem base]]"
---

# Versionamento e tags imutáveis

Uma boa estratégia de tags torna deploys **previsíveis** e **reversíveis**.

## Esquema recomendado (SemVer)

Publique a mesma imagem com várias tags:

```text
meuapp:1.4.2      ← exata (nunca mais muda)
meuapp:1.4        ← última correção da 1.4
meuapp:1         ← último minor da 1.x
meuapp:sha-a1b2c3d ← commit de origem (rastreabilidade)
```

```bash
VERSAO=1.4.2
docker build -t meuapp:$VERSAO .
docker tag meuapp:$VERSAO meuapp:1.4
docker tag meuapp:$VERSAO meuapp:1
docker tag meuapp:$VERSAO meuapp:sha-$(git rev-parse --short HEAD)
```

## Regras práticas

| Regra | Motivo |
|---|---|
| Produção usa **tag exata** ou **digest** | Reprodutibilidade e rollback |
| `latest` só para conveniência de testes | Pode mudar a qualquer momento |
| Nunca sobrescrever uma tag de versão publicada | Quebra a confiança de quem já a usa |
| Registrar commit e data em *labels* OCI | Auditoria |

```dockerfile
LABEL org.opencontainers.image.version="1.4.2" \
      org.opencontainers.image.source="https://exemplo.com/repo" \
      org.opencontainers.image.revision="a1b2c3d"
```

> [!tip] Tags imutáveis no registry
> Muitos registries (ECR, ACR, GAR, Docker Hub em planos pagos) permitem tornar tags **imutáveis**, impedindo `push` sobre tags existentes. Habilite para repositórios de produção.

> [!info] Rollback
> Se cada deploy usa uma tag exata ou digest, voltar é apenas reimplantar a versão anterior.

## Exercício

Defina o script de tags para uma versão `2.0.1` do seu projeto gerando as tags `2.0.1`, `2.0`, `2` e `sha-<commit>`, e explique qual delas você usaria em produção.

## Veja também

- [[Tags e digests de imagens]]
- [[Comando docker tag e push]]
- [[Docker Hub]]
- [[Escolha da imagem base]]
- [[MOC - Imagens]]
