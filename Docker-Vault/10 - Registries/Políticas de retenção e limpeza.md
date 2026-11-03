---
tags:
  - docker
  - registries
  - manutencao
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Versionamento e tags imutáveis]]"
  - "[[AWS ECR]]"
  - "[[Google Artifact Registry]]"
  - "[[Azure Container Registry]]"
  - "[[Registry privado local com registry 2]]"
---

# Políticas de retenção e limpeza

Registries acumulam imagens (cada commit gera uma). Sem limpeza, custos e riscos crescem. Defina uma **política de retenção**.

| Registry | Mecanismo |
|---|---|
| AWS ECR | **Lifecycle policies** (JSON) |
| Google Artifact Registry | **Cleanup policies** (por idade, contagem, prefixo de tag) |
| Azure ACR | Retenção de manifests sem tag e `az acr run` com `acr purge` |
| GitLab | Cleanup policies do projeto |
| GHCR | Ações como `actions/delete-package-versions` |
| `registry:2` | `garbage-collect` após excluir manifests |

## Exemplo: lifecycle policy do ECR

```json
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Remove imagens sem tag após 7 dias",
      "selection": {
        "tagStatus": "untagged",
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 7
      },
      "action": { "type": "expire" }
    },
    {
      "rulePriority": 2,
      "description": "Mantém as 30 imagens mais recentes com tag de versão",
      "selection": {
        "tagStatus": "tagged",
        "tagPrefixList": ["v"],
        "countType": "imageCountMoreThan",
        "countNumber": 30
      },
      "action": { "type": "expire" }
    }
  ]
}
```

```bash
aws ecr put-lifecycle-policy --repository-name meu-app --lifecycle-policy-text file://lifecycle.json
```

## Limpeza em `registry:2`

```bash
# 1) Habilite a exclusão no registry (REGISTRY_STORAGE_DELETE_ENABLED=true) e remova o manifest via API
# 2) Libere o espaço
docker exec registry registry garbage-collect /etc/docker/registry/config.yml
```

> [!warning] Nunca remova a imagem que está em produção
> Mantenha sempre as tags **em uso** e algumas anteriores para *rollback*. Remova primeiro imagens sem tag e as de branches efêmeros (por exemplo, `pr-123`).

> [!tip] Estratégia recomendada
> Mantenha as últimas N versões de release, tudo que está em produção, e descarte imagens de PRs após alguns dias.

## Exercício

Escreva uma política de retenção (em prosa ou JSON) para seu projeto: o que manter, por quanto tempo e como proteger a versão em produção.

## Veja também

- [[Versionamento e tags imutáveis]]
- [[AWS ECR]]
- [[Google Artifact Registry]]
- [[Azure Container Registry]]
- [[Registry privado local com registry 2]]
- [[MOC - Registries]]
