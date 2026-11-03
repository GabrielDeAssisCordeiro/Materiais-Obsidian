---
tags: [avancado, bases]
aliases: [Bases fórmulas, Filtros e fórmulas em Bases]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Bases]]", "[[Core - Bases]]", "[[Consultas Dataview]]"]
---

# Bases avançado

Complementa [[Bases]]. Arquivos `.base` são YAML com `filters`, `formulas`, `properties`, `summaries` e `views`.

## Exemplo completo
```yaml
filters:
  and:
    - file.inFolder("06 - Plugins Core")
    - 'nivel != "avancado"'
formulas:
  rotulo: 'tipo + " / " + nivel'
properties:
  formula.rotulo:
    displayName: "Rótulo"
views:
  - type: table
    name: "Plugins core"
    order:
      - file.name
      - nivel
      - formula.rotulo
    sort:
      - property: file.name
        direction: ASC
```

## Conceitos
- **Filtros** com `and`, `or` e `not`; funções como `file.hasTag("x")` e `file.inFolder("pasta")`.
- **Propriedades**: da nota (`nivel`), do arquivo (`file.name`, `file.mtime`) e de fórmula (`formula.nome`).
- **Fórmulas**: expressões com operadores e funções, entre aspas simples quando contêm aspas duplas.
- **Views** múltiplas sobre os mesmos dados (tabela, lista, cartões; mapa quando aplicável).
- **Summaries**: soma, média, contagem por coluna.

> [!question] Verificar na documentação oficial
> Confirme funções, tipos de view e sintaxe de ordenação em help.obsidian.md/bases/syntax.

## Bases × Dataview
| Aspecto | Bases | Dataview |
|---|---|---|
| Instalação | nativo | plugin |
| Edição | visual + YAML | texto (DQL/JS) |
| Poder | bom e crescente | maior flexibilidade |

## Veja também
- [[Bases]]
- [[Consultas Dataview]]

## Exercício
Crie uma Base com duas views sobre a mesma pasta: uma tabela e uma lista.
