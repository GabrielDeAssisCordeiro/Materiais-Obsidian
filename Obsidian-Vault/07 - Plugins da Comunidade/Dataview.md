---
tags: [plugins-comunidade, dataview, consultas]
aliases: [Dataview plugin]
tipo: plugin
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Consultas Dataview]]", "[[DataviewJS]]", "[[Bases]]"]
---

# Dataview

Plugin que trata o vault como banco de dados e executa **consultas** sobre notas, [[Properties]] e tarefas.

## Instalação e configuração
1. Instale e ative ([[Instalando e avaliando segurança]]).
2. Em Settings → Dataview: habilite *Inline queries* e, se for usar, *JavaScript queries* ([[DataviewJS]]).
3. Ajuste o intervalo de atualização.

## Exemplos
````markdown
```dataview
TABLE tipo, nivel
FROM "01 - Fundamentos"
WHERE nivel = "iniciante"
SORT file.name ASC
```
````

Lista de tarefas abertas:
````markdown
```dataview
TASK
WHERE !completed
GROUP BY file.link
```
````

Inline: `` `= this.file.name` ``

## Campos
- Implícitos: `file.name`, `file.link`, `file.tags`, `file.ctime`, `file.mtime`.
- Properties do frontmatter e campos inline `chave:: valor`.

> [!tip] Dataview × Bases
> Para consultas simples, [[Bases]] é nativo e visual. Dataview continua mais flexível para consultas complexas e scripts.

> [!warning] Exige o plugin
> Sem o plugin, os blocos aparecem como código.

## Veja também
- [[Consultas Dataview]]
- [[Cheat sheet Dataview]]
- [[Nomenclatura de propriedades]]

## Exercício
Crie uma tabela das notas com `tipo: plugin`, mostrando `nivel` e a última modificação.
