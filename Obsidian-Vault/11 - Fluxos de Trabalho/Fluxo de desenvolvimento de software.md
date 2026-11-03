---
tags: [fluxos]
aliases: [Dev, Notas de programação, Documentação técnica]
tipo: fluxo
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Blocos de código]]", "[[Obsidian Git]]", "[[Diagramas Mermaid]]"]
---

# Fluxo de desenvolvimento de software

## Uso típico
- Snippets e comandos em [[Blocos de código]].
- Diagramas de arquitetura em [[Diagramas Mermaid]].
- Decisões de arquitetura (ADR) em notas curtas.
- Logs de depuração e aprendizados.
- Versionamento do vault com [[Obsidian Git]].

## Estrutura
```text
Dev/
├── Snippets/
├── Decisões/
├── Projetos/
└── Estudos/
```

## Dicas
- Uma nota por problema resolvido, com causa e solução.
- Tags de linguagem: `#lang/python`, `#lang/js` ([[Tags aninhadas]]).
- Não guarde segredos nas notas ([[Sincronizar com Git]]).

> [!warning] Segredos
> Chaves, senhas e tokens não devem ficar em Markdown versionado.

## Veja também
- [[Fluxo de gestão de projetos]]
- [[Sincronizar com Git]]

## Exercício
Documente um bug que resolveu esta semana com causa, solução e um diagrama.
