---
tags: [rust, template]
aliases: ["Template conceito", "Nova nota de conceito"]
tipo: template
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Home - Rust]]", "[[Template de exercício]]", "[[Template de projeto]]"]
---

# Template de nota de conceito

> [!info] Como usar
> Copie o conteúdo (a partir do bloco de frontmatter abaixo) para uma nota nova, ou use o plugin nativo **Templates**: `Ctrl/Cmd + P` → "Inserir template". As variáveis `{{title}}` e `{{date}}` são preenchidas automaticamente.

```markdown
---
tags: [rust]
aliases: []
tipo: conceito
nivel: iniciante
criado: {{date:YYYY-MM-DD}}
relacionados: []
---

# {{title}}

Uma ou duas frases que definem o conceito.

## Por quê

Que problema isto resolve?

## Exemplo

(bloco de código rust, compilável)

> [!tip] Regra prática
> Resumo em uma linha.

> [!warning] Armadilha
> O erro mais comum.

## Exercício

Um exercício curto para fixar.

## Veja também

- [[nota relacionada]]
```

> [!tip] Antes de salvar
> Confira: o exemplo compila? Há links para notas que existem? O campo `nivel` é `iniciante`, `intermediario` ou `avancado`?

## Veja também

- [[Home - Rust]]
- [[Template de exercício]]
- [[Template de projeto]]
