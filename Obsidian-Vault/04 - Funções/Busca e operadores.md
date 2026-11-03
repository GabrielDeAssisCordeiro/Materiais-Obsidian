---
tags: [funcoes, busca]
aliases: [Search, Pesquisa, Operadores de busca]
tipo: funcao
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Core - Busca]]", "[[Cheat sheet Busca]]", "[[Tags]]"]
---

# Busca e operadores

Abra com `Ctrl/Cmd + Shift + F` ([[Core - Busca]]).

## Sintaxe básica
- Palavras separadas: todas devem aparecer (E).
- `"frase exata"`, `OR`, `-excluir`, `(grupo)`.
- `/regex/` para expressões regulares.

## Operadores
| Operador | Exemplo | Faz |
|---|---|---|
| `file:` | `file:plano` | busca no nome do arquivo |
| `path:` | `path:"01 - Fundamentos"` | busca no caminho |
| `content:` | `content:vault` | só no conteúdo |
| `tag:` | `tag:#estudo` | notas com a tag |
| `line:()` | `line:(obsidian vault)` | termos na mesma linha |
| `section:()` | `section:(a b)` | na mesma seção |
| `block:()` | `block:(a b)` | no mesmo bloco |
| `task:` | `task-todo:revisar` | tarefas (`task-done:` também) |
| `match-case:` | `match-case:Vault` | diferencia maiúsculas |
| `[propriedade:valor]` | `[nivel:iniciante]` | filtra properties |

> [!example] Exemplos
> - `tag:#estudo -tag:#concluido`
> - `path:"Projetos" task-todo:`
> - `[tipo:plugin] [nivel:avancado]`

## Recursos extras
- Ordenar resultados, mostrar contexto e copiar resultados.
- **Embeds de busca:** bloco ` ```query ` mostra resultados dentro da nota.

> [!question] Verificar na documentação oficial
> Confirme detalhes de `query` embutido e operadores novos na versão atual.

## Veja também
- [[Cheat sheet Busca]]
- [[Consultas Dataview]]
- [[Omnisearch]]

## Exercício
Encontre todas as notas desta pasta com a propriedade `nivel: avancado` usando um filtro de propriedade.
