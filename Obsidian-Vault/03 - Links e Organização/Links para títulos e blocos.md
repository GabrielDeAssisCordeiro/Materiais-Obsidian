---
tags: [links, sintaxe]
aliases: [Heading links, Block links, Referência de blocos]
tipo: conceito
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Wikilinks e links Markdown]]", "[[Embeds]]", "[[Backlinks e links de saída]]"]
---

# Links para títulos e blocos

## Títulos
```markdown
[[Nota#Título]]        título em outra nota
[[#Título]]            título na mesma nota
[[Nota#Título#Subtítulo]]
```

## Blocos
Todo parágrafo, item de lista ou citação pode ter um **ID de bloco**:
```markdown
Este parágrafo pode ser referenciado. ^meu-bloco

[[Nota#^meu-bloco]]
![[Nota#^meu-bloco]]
```
- IDs podem conter letras, números e hífen.
- Ao digitar `[[Nota#^`, o Obsidian lista blocos e **gera o ID** automaticamente.
- Busca em todo o vault: `[[##` para títulos e `[[^^` para blocos.

> [!warning] Fragilidade
> Renomear um título quebra links para ele (o Obsidian pode atualizar, conforme configuração). IDs de bloco são mais estáveis.

> [!tip] Citações reaproveitáveis
> Combine com [[Embeds]] para trazer um bloco específico para outra nota.

## Veja também
- [[Notas atômicas]]
- [[Backlinks e links de saída]]

## Exercício
Dê um ID a um parágrafo e incorpore-o em outra nota.
