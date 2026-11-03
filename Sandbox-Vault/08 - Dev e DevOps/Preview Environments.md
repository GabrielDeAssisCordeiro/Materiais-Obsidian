---
tags:
  - devops
  - dev
aliases:
  - "Ambientes de preview"
  - "Review apps"
tipo: devops
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Ambientes Efêmeros]]"
  - "[[Caso - CI e CD]]"
---
# Preview Environments

Um ambiente por *pull request*, com URL própria, para revisar mudanças funcionando.

```yaml
# .github/workflows/preview.yml (esqueleto)
name: preview
on:
  pull_request:
    types: [opened, synchronize, reopened, closed]
permissions:
  contents: read
jobs:
  preview:
    runs-on: ubuntu-latest
    if: github.event.action != 'closed'
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t app:pr-${{ github.event.number }} .
      # implante em um ambiente temporário (por IaC) e comente a URL no PR
  teardown:
    runs-on: ubuntu-latest
    if: github.event.action == 'closed'
    steps:
      - run: echo "destruir ambiente pr-${{ github.event.number }}"
```

> [!danger] Cuidado com `pull_request_target` e segredos
> PRs de forks não devem acessar segredos nem executar código não confiável com privilégios. Prefira `pull_request` e permissões mínimas.

## Exercício

Escreva o job de *teardown* que remove o ambiente quando o PR for fechado.

## Veja também

- [[Ambientes Efêmeros]]
- [[Infraestrutura como Código]]
- [[Runners Efêmeros e Pipelines Seguros]]
- [[MOC - Dev e DevOps]]
