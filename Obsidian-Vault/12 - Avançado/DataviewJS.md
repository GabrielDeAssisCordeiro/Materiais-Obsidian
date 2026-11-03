---
tags: [avancado, dataview]
aliases: [dv API, Dataview JS]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Consultas Dataview]]", "[[Dataview]]", "[[Instalando e avaliando segurança]]"]
---

# DataviewJS

Consultas escritas em **JavaScript** com a API `dv`. Exige habilitar *JavaScript queries* nas configurações do [[Dataview]].

## Exemplos
Tabela de notas de uma pasta:
````markdown
```dataviewjs
const paginas = dv.pages('"01 - Fundamentos"');
dv.table(
  ["Nota", "Nível"],
  paginas.map(p => [p.file.link, p.nivel])
);
```
````
Lista filtrada:
````markdown
```dataviewjs
dv.header(3, "Notas iniciantes");
dv.list(
  dv.pages('"06 - Plugins Core"')
    .where(p => p.nivel == "iniciante")
    .map(p => p.file.link)
);
```
````
Contagem por tipo:
````markdown
```dataviewjs
const grupos = dv.pages().groupBy(p => p.tipo);
dv.table(["Tipo", "Qtd"], grupos.map(g => [g.key, g.rows.length]));
```
````

## Principais métodos
`dv.pages()`, `dv.table()`, `dv.list()`, `dv.taskList()`, `dv.header()`, `dv.paragraph()`, `dv.current()`.

> [!warning] Segurança
> O código roda com acesso ao vault. Não cole scripts desconhecidos ([[Instalando e avaliando segurança]]).

> [!question] Verificar na documentação oficial
> Confirme a assinatura atual da API em blacksmithgu.github.io/obsidian-dataview.

## Veja também
- [[Consultas Dataview]]
- [[API de plugins]]

## Exercício
Monte uma tabela com as 5 notas modificadas mais recentemente usando `sort`.
