---
tags: [markdown]
aliases: [Admonitions nativos, Blocos de destaque]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Sintaxe estendida]]", "[[Admonition]]", "[[Snippets CSS]]"]
---

# Callouts

Callouts são citações com tipo, usadas para destacar informações.

````markdown
> [!tip] Título opcional
> Conteúdo do callout.
````

## Tipos comuns
`note`, `abstract`, `info`, `todo`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`.

> [!tip] Dica
> Este é um callout do tipo `tip`.

> [!warning] Atenção
> Use para riscos e armadilhas.

> [!example] Exemplo
> Use para mostrar uso prático.

## Dobráveis
- `> [!faq]-` começa **recolhido**
- `> [!faq]+` começa **expandido**

> [!faq]- Clique para abrir
> Conteúdo oculto até ser expandido.

## Aninhados
````markdown
> [!question] Externo
> > [!note] Interno
> > Texto
````

## Customizar
Crie tipos novos com CSS ([[Snippets CSS]]). O plugin [[Admonition]] oferece outra abordagem.

## Veja também
- [[Sintaxe estendida]]
- [[Cheat sheet Markdown]]

## Exercício
Crie um callout dobrável do tipo `question` com uma pergunta e a resposta dentro.
