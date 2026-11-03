---
tags: [referencia, dataview, cheat-sheet]
aliases: [Resumo Dataview, Colinha Dataview]
tipo: cheat-sheet
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Dataview]]", "[[Consultas Dataview]]", "[[DataviewJS]]"]
---

# Cheat sheet Dataview

## Comandos
| Comando | Uso |
|---|---|
| `TABLE a, b` | tabela com colunas |
| `LIST` | lista de notas |
| `TASK` | tarefas |
| `CALENDAR campo` | calendário |
| `FROM "pasta"` / `FROM #tag` | origem |
| `WHERE cond` | filtro |
| `SORT campo DESC` | ordem |
| `GROUP BY campo` | agrupar |
| `FLATTEN lista AS x` | expandir listas |
| `LIMIT n` | limite |

## Campos e funções
- Campos: `file.name`, `file.link`, `file.tags`, `file.ctime`, `file.mtime`, `file.folder`.
- Funções: `contains()`, `length()`, `date()`, `dur()`, `default()`.
- Campo inline: `chave:: valor`.

## Exemplo
````markdown
```dataview
TABLE nivel
FROM "01 - Fundamentos"
SORT file.name ASC
```
````

> [!warning] Exige o plugin
> Veja [[Dataview]]; nativo equivalente: [[Bases]].

## Veja também
- [[Consultas Dataview]]
- [[DataviewJS]]

## Exercício
Escreva três consultas diferentes sobre este vault.
