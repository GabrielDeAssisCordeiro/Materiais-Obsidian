---
tags: [links, sintaxe]
aliases: [Wikilinks, Links internos, Links Markdown]
tipo: conceito
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Aliases]]", "[[Links para títulos e blocos]]", "[[Configurações de Arquivos e links]]"]
---

# Wikilinks e links Markdown

O Obsidian aceita dois formatos de link interno.

| Formato | Exemplo |
|---|---|
| **Wikilink** | `[[Nome da nota]]` |
| Wikilink com texto | `[[Nome da nota\|texto exibido]]` (em tabelas, escape o pipe) |
| **Link Markdown** | `[texto](Nome%20da%20nota.md)` ou `[texto](<Nome da nota.md>)` |
| Link externo | `[Obsidian](https://obsidian.md)` |

## Qual usar?
- **Wikilink:** mais rápido de digitar (`[[` abre sugestões) e é o padrão.
- **Markdown:** mais compatível com outros programas.
- Alterne em **Settings → Files and links → Use Wikilinks** ([[Configurações de Arquivos e links]]).
- O formato do caminho (mais curto, relativo ou absoluto) também é configurável.

## Criando links
1. Digite `[[` e escolha a nota.
2. Selecione texto e digite `[[` para transformá-lo em link.
3. Clique num link inexistente para criar a nota ([[Links não resolvidos]]).

> [!tip] Renomeie sem medo
> Com *Automatically update internal links* ativo, renomear ou mover a nota atualiza os links.

> [!warning] Nomes duplicados
> Com o formato "mais curto possível", duas notas com o mesmo nome em pastas diferentes exigem o caminho no link. Prefira títulos únicos.

## Veja também
- [[Aliases]]
- [[Backlinks e links de saída]]
- [[Alternador rápido]]

## Exercício
Crie três notas e ligue-as em triângulo. Depois renomeie uma e confirme que os links continuam funcionando.
