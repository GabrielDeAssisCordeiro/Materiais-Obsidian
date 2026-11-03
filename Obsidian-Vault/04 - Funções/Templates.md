---
tags: [funcoes, templates]
aliases: [Modelos, Template de nota]
tipo: funcao
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Core - Templates]]", "[[Templater]]", "[[Notas diárias]]"]
---

# Templates

Templates inserem texto padrão em novas notas ([[Core - Templates]]).

## Configurar
1. Ative o plugin Templates.
2. Defina a **pasta de templates** (neste vault: `Templates/`).
3. Use *Insert template* pela paleta ([[Paleta de comandos]]).

## Variáveis do plugin core
| Variável | Resultado |
|---|---|
| `{{title}}` | título da nota |
| `{{date}}` | data atual |
| `{{time}}` | hora atual |
| `{{date:YYYY-MM-DD}}` | data com formato |

```markdown
---
tags: []
aliases: []
tipo: 
nivel: iniciante
criado: {{date:YYYY-MM-DD}}
relacionados: []
---
# {{title}}

## Veja também
```

## Limites e alternativas
O plugin core faz substituições simples. Para lógica, datas relativas e scripts, use [[Templater]]; para formulários rápidos, [[QuickAdd]].

> [!tip] Padrão de vault
> Um template com o frontmatter padrão evita notas incompletas ([[Nomenclatura de propriedades]]).

## Veja também
- [[Properties]]
- [[Notas diárias]]

## Exercício
Crie um template de nota de reunião com data e participantes.
