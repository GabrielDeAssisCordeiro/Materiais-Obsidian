---
tags:
  - devops
  - dev
aliases:
  - "CI seguro"
tipo: devops
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Caso - CI e CD]]"
  - "[[Gerenciamento de Segredos e Credenciais]]"
---
# Runners Efêmeros e Pipelines Seguros

- **Runner efêmero:** uma VM/container novo por job, destruído ao final.
- **Permissões mínimas** para o token do pipeline.
- **Segredos** somente em jobs que realmente precisam; nunca para PRs de forks.
- **Ações/dependências fixadas** por versão ou *commit SHA*.
- **Sem cache confiável** de fontes externas sem verificação.
- **Isolamento de rede** do runner quando possível.

```yaml
permissions:
  contents: read
```

> [!danger] Runners persistentes e compartilhados acumulam estado e segredos; evite para código não confiável.

## Exercício

Audite as permissões padrão do token do seu pipeline e reduza-as.

## Veja também

- [[Caso - CI e CD]]
- [[Gerenciamento de Segredos e Credenciais]]
- [[Cadeia de Suprimentos de Software]]
- [[MOC - Dev e DevOps]]
