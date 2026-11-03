---
tags:
  - casos-de-uso
aliases:
  - "Ambiente de homologação"
tipo: caso-de-uso
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Caso - CI e CD]]"
  - "[[Sandbox de Dados]]"
---
# Caso - Homologação e Staging

Homologação é um ambiente **parecido com produção**, mas separado dela, para validar mudanças antes do lançamento.

| Aspecto | Boa prática |
|---|---|
| Dados | Sintéticos ou anonimizados (LGPD) |
| Integrações | Contas/sandbox dos provedores, nunca chaves de produção |
| Rede | Isolada da produção |
| Ciclo de vida | Recriado por IaC, descartável |

## Exercício

Compare as diferenças que seu staging tem em relação à produção e liste riscos de cada diferença.

## Veja também

- [[Caso - CI e CD]]
- [[Sandbox de Dados]]
- [[Caso - Sandbox de APIs e Pagamentos]]
- [[MOC - Casos de Uso]]
