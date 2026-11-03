---
tags:
  - devops
  - dev
aliases:
  - "Staging"
tipo: devops
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Caso - Homologação e Staging]]"
  - "[[Infraestrutura como Código]]"
---
# Ambientes de Staging e Promoção

Fluxo típico: **dev → CI → staging → produção**.

| Princípio | Prática |
|---|---|
| Paridade | Mesma configuração de produção, em escala menor |
| Promoção, não reconstrução | O **mesmo artefato** (imagem) vai de staging a produção |
| Dados | Sintéticos/anonimizados — ver [[Conformidade e LGPD]] |
| Acesso | Restrito; não é público por padrão |
| Integrações | Contas de teste dos provedores |

> [!warning] Staging exposto e com dados reais é uma fonte comum de vazamentos.

## Veja também

- [[Caso - Homologação e Staging]]
- [[Feature Flags]]
- [[Dados de Teste e Mocks]]
- [[MOC - Dev e DevOps]]
