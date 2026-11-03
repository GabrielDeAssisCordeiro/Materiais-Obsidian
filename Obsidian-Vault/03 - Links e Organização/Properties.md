---
tags: [properties]
aliases: [Propriedades, Frontmatter, Metadados]
tipo: conceito
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Tipos de properties]]", "[[Sintaxe YAML do frontmatter]]", "[[Core - Properties view]]"]
---

# Properties

**Properties** são metadados no topo da nota, guardados como YAML ([[Sintaxe YAML do frontmatter]]). O Obsidian oferece uma interface visual para editá-las.

```yaml
---
tags: [estudo]
aliases: [Exemplo]
tipo: conceito
nivel: iniciante
criado: 2026-10-23
---
```

## Para que servem
- Filtrar e agrupar com [[Bases]] e [[Consultas Dataview]].
- Aliases e tags nativos ([[Propriedades padrão]]).
- Estilizar a nota com `cssclasses` ([[cssclasses]]).
- Padronizar notas com [[Templates]].

## Edição
- A interface mostra campos conforme o tipo ([[Tipos de properties]]).
- Alterne entre visual e código em **Settings → Editor → Properties in document**.
- O painel de properties lista todas no vault ([[Core - Properties view]]).

> [!tip] Padronize
> Escolha poucos nomes e use sempre igual ([[Nomenclatura de propriedades]]).

## Veja também
- [[Tipos de properties]]
- [[Propriedades padrão]]
- [[Configurações do Editor]]

## Exercício
Adicione `tipo` e `nivel` a cinco notas e crie uma Base filtrando por `nivel`.
