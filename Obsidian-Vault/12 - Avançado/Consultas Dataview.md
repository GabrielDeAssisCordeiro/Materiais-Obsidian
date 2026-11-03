---
tags: [avancado, dataview, consultas]
aliases: [DQL, Dataview Query Language, Consultas]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Dataview]]", "[[DataviewJS]]", "[[Cheat sheet Dataview]]"]
---

# Consultas Dataview

Requer o plugin [[Dataview]]. Consultas usam a linguagem **DQL**.

## Estrutura
```text
TIPO campos
FROM origem
WHERE condição
SORT campo ASC|DESC
LIMIT n
```
Tipos: `TABLE`, `LIST`, `TASK`, `CALENDAR`.

## Exemplos funcionais
Lista de MOCs:
````markdown
```dataview
LIST
FROM #moc
SORT file.name ASC
```
````
Notas avançadas de uma pasta:
````markdown
```dataview
TABLE tipo, nivel
FROM "06 - Plugins Core"
WHERE nivel = "avancado"
SORT file.name ASC
```
````
Notas editadas nos últimos 7 dias:
````markdown
```dataview
TABLE file.mtime AS "Modificado"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 10
```
````
Agrupar por nível:
````markdown
```dataview
TABLE rows.file.link AS "Notas"
FROM "03 - Links e Organização"
GROUP BY nivel
```
````

## Dicas
- `FROM` aceita pastas (`"pasta"`), tags (`#tag`) e links (`[[nota]]`).
- Funções úteis: `contains()`, `length()`, `default()`, `date()`, `dur()`.
- Nomes de propriedades consistentes ([[Nomenclatura de propriedades]]).

> [!warning] Performance
> Consultas em vaults grandes devem usar `FROM` para limitar o escopo ([[Desempenho]]).

> [!tip] Alternativa nativa
> Para tabelas e listas simples, considere [[Bases avançado]].

## Veja também
- [[Cheat sheet Dataview]]
- [[DataviewJS]]

## Exercício
Escreva uma consulta que liste todas as notas com `tipo: plugin` e `nivel: iniciante`.
