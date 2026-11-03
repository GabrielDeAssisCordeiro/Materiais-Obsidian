---
tags: [fluxos]
aliases: [Estudos, Faculdade, Notas de aula]
tipo: fluxo
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Citations e Zotero Integration]]", "[[Matemática com LaTeX]]", "[[Zettelkasten]]"]
---

# Fluxo de estudos acadêmicos

## Estrutura
```text
Estudos/
├── Disciplinas/
│   └── Cálculo I/
├── Literatura/
├── Conceitos/
└── Revisão/
```

## Passo a passo
1. **Aula:** nota com `disciplina`, `data` e resumo ([[Templates]]).
2. **Leitura:** nota de literatura por fonte ([[Fluxo de leitura]], [[Citations e Zotero Integration]]).
3. **Conceitos:** nota atômica por ideia ([[Notas atômicas]]), com fórmulas em [[Matemática com LaTeX]].
4. **Conexão:** MOC por disciplina ([[MOCs]]).
5. **Revisão:** perguntas e respostas em callouts dobráveis ([[Callouts]]) e flashcards ([[Flashcards]]).
6. **Provas e trabalhos:** consultas por `disciplina` com [[Bases]].

> [!example] Template de aula
> ```markdown
> ---
> tipo: aula
> disciplina:
> data: {{date:YYYY-MM-DD}}
> ---
> ## Resumo
> ## Dúvidas
> ```

## Veja também
- [[Zettelkasten]]
- [[Captura, processamento, conexão e saída]]

## Exercício
Crie o MOC de uma disciplina com 5 conceitos e 2 fontes.
