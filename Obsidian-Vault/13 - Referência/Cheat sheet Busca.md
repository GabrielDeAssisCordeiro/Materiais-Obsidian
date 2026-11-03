---
tags: [referencia, busca, cheat-sheet]
aliases: [Resumo busca, Colinha de busca]
tipo: cheat-sheet
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Busca e operadores]]", "[[Core - Busca]]", "[[Tags]]"]
---

# Cheat sheet Busca

| Operador | Exemplo |
|---|---|
| Frase | `"nota atômica"` |
| OU | `plugin OR tema` |
| Excluir | `-rascunho` |
| Grupo | `(a OR b) c` |
| Regex | `/\d{4}-\d{2}/` |
| Arquivo | `file:Home` |
| Pasta | `path:"06 - Plugins Core"` |
| Conteúdo | `content:vault` |
| Tag | `tag:#estudo` |
| Mesma linha | `line:(a b)` |
| Mesma seção | `section:(a b)` |
| Tarefa pendente | `task-todo:revisar` |
| Property | `[nivel:avancado]` |
| Maiúsculas | `match-case:Vault` |

> [!example] Combinações
> `path:"07 - Plugins da Comunidade" [nivel:iniciante]`

Detalhes em [[Busca e operadores]].

## Veja também
- [[Core - Busca]]
- [[Omnisearch]]

## Exercício
Monte uma busca que encontre notas de pasta específica, com tag e sem outra tag.
