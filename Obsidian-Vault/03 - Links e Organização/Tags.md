---
tags: [tags, organizacao]
aliases: [Hashtags, Etiquetas]
tipo: conceito
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Tags aninhadas]]", "[[Core - Tags]]", "[[Pastas, tags ou links]]"]
---

# Tags

Tags classificam notas de forma transversal.

## Onde escrever
```markdown
No texto: #estudo #projeto-x

Em properties:
---
tags: [estudo, projeto-x]
---
```
Em properties **não** se usa `#` ([[Propriedades padrão]]).

## Regras
- Aceitam letras, números, `_`, `-` e `/` (para [[Tags aninhadas]]).
- Não podem conter espaços.
- Precisam ter ao menos um caractere não numérico (`#2026` não é tag).
- Não diferenciam maiúsculas de minúsculas.

## Usar
- Painel de tags ([[Core - Tags]]).
- Busca `tag:#estudo` ([[Busca e operadores]]).
- Filtros em [[Graph view]] e [[Bases]].

> [!tip] Use poucas tags
> Prefira tags para **estado e tipo** (`#rascunho`, `#livro`), e links para **assuntos**. Veja [[Pastas, tags ou links]].

## Veja também
- [[Properties]]
- [[Nomenclatura de propriedades]]

## Exercício
Aplique a tag `#revisar` a três notas e liste-as pela busca.
