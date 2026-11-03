---
tags: [rust, template, flashcards]
aliases: ["Template flashcards", "Novos flashcards"]
tipo: template
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Home - Rust]]", "[[Template de revisão semanal]]", "[[Template de nota de conceito]]"]
---

# Template de flashcards

Formato de uma linha por cartão: `pergunta::resposta` (compatível com plugins de repetição espaçada, mas legível sem eles).

```markdown
---
tags: [rust, flashcards]
aliases: []
tipo: flashcards
nivel: iniciante
criado: {{date:YYYY-MM-DD}}
relacionados: []
---

# {{title}}

O que é ownership?::Cada valor tem um único dono; ao sair de escopo, é liberado.
O que faz o operador ?::Propaga o erro ao chamador ou extrai o valor de Ok/Some.

## Veja também

- [[nota relacionada]]
```

> [!tip] Bons cartões
> Uma ideia por cartão, perguntas específicas e respostas curtas. Evite usar `::` dentro do texto da pergunta ou da resposta.

## Veja também

- [[Home - Rust]]
- [[Template de revisão semanal]]
- [[Template de nota de conceito]]
