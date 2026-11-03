---
tags: [tags, organizacao]
aliases: [Nested tags, Hierarquia de tags]
tipo: conceito
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Tags]]", "[[Core - Tags]]", "[[Busca e operadores]]"]
---

# Tags aninhadas

Use `/` para criar hierarquia:

```markdown
#area/saude
#area/trabalho/reuniao
#status/ativo
```

## Comportamento
- Buscar `tag:#area` encontra também `#area/saude` e `#area/trabalho/reuniao`.
- O painel de tags mostra a árvore e permite expandir ([[Core - Tags]]).
- Facilita filtros em [[Graph view]] e [[Bases]].

> [!warning] Evite hierarquias profundas
> Mais de dois níveis tende a virar uma segunda estrutura de pastas ([[Pastas, tags ou links]]).

> [!example] Exemplo
> `#status/ativo`, `#status/pausado`, `#status/concluido` descrevem o estado de um projeto.

## Veja também
- [[Tags]]
- [[Nomenclatura de propriedades]]

## Exercício
Defina uma hierarquia com três valores de `#status/...` e aplique em notas de projeto.
