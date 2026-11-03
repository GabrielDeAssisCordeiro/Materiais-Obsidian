---
tags:
  - casos-de-uso
aliases:
  - "Pipelines isolados"
tipo: caso-de-uso
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Sandbox por Containers]]"
  - "[[Caso - Testes de Software e QA]]"
---
# Caso - CI e CD

Pipelines executam código de commits e *pull requests* — inclusive de contribuidores externos. Cada job deve rodar em **ambiente efêmero**.

- Runners efêmeros (um job, uma VM/container descartável).
- Segredos só em etapas que precisam deles; **nunca** expor a PRs de forks.
- Cache e artefatos tratados como entrada não confiável.

> [!danger] Segredos em pipelines
> Um PR malicioso pode tentar ler variáveis de ambiente. Restrinja permissões do token do pipeline ao mínimo.

## Exercício

Revise um pipeline seu: quais segredos estão disponíveis em jobs disparados por forks?

## Veja também

- [[Sandbox por Containers]]
- [[Caso - Testes de Software e QA]]
- [[Caso - Homologação e Staging]]
- [[MOC - Casos de Uso]]
