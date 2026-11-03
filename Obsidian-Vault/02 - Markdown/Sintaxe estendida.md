---
tags: [markdown, sintaxe]
aliases: [Obsidian Flavored Markdown, Extensões do Obsidian]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Sintaxe básica]]", "[[Callouts]]", "[[Embeds]]"]
---

# Sintaxe estendida

Além do Markdown padrão, o Obsidian adiciona recursos próprios.

| Recurso | Sintaxe | Nota |
|---|---|---|
| Wikilink | `[[Nota]]` | [[Wikilinks e links Markdown]] |
| Link para título | `[[Nota#Título]]` | [[Links para títulos e blocos]] |
| Link para bloco | `[[Nota#^id]]` | [[Links para títulos e blocos]] |
| Embed | `![[Nota]]` | [[Embeds]] |
| Destaque | `==texto==` | |
| Comentário | `%%oculto%%` | [[Comentários e notas de rodapé]] |
| Tag | `#tag` | [[Tags]] |
| Callout | `> [!tip]` | [[Callouts]] |
| Math | `$x^2$` | [[Matemática com LaTeX]] |
| Mermaid | bloco `mermaid` | [[Diagramas Mermaid]] |
| Nota de rodapé | `[^1]` | [[Comentários e notas de rodapé]] |

## Propriedades
Bloco YAML no início da nota:
```yaml
---
tags: [exemplo]
aliases: [Exemplo]
---
```
Veja [[Properties]] e [[Sintaxe YAML do frontmatter]].

> [!warning] Compatibilidade
> Essas extensões não funcionam em todos os leitores de Markdown. Se for exportar, veja [[Importar e exportar]].

## Veja também
- [[Sintaxe básica]]
- [[Cheat sheet Markdown]]

## Exercício
Escreva uma nota que use ao menos 5 recursos da tabela acima.
