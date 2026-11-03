---
tags: [markdown]
aliases: [Code blocks, Código inline]
tipo: referencia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Sintaxe básica]]", "[[Consultas Dataview]]", "[[Diagramas Mermaid]]"]
---

# Blocos de código

## Código inline
Use crases: `` `código` ``. Para exibir crases dentro, use duas.

## Bloco com linguagem
````markdown
```python
def ola():
    print("Olá, Obsidian")
```
````

A linguagem após as três crases ativa o realce de sintaxe. Linguagens especiais interpretadas pelo Obsidian ou por plugins:
- `mermaid` → [[Diagramas Mermaid]]
- `dataview`, `dataviewjs` → [[Consultas Dataview]], [[DataviewJS]]
- `base` → [[Bases]]

## Mostrar blocos dentro de blocos
Use mais crases na cerca externa (quatro ou mais) quando o conteúdo tem três.

## Indentação
Quatro espaços também criam bloco de código, mas a cerca com crases é mais clara.

> [!tip] Copiar
> Em Reading view há botão para copiar o conteúdo do bloco.

## Veja também
- [[Sintaxe estendida]]
- [[Cheat sheet Markdown]]

## Exercício
Escreva um bloco `yaml` com um frontmatter completo e outro `bash` com um comando qualquer.
