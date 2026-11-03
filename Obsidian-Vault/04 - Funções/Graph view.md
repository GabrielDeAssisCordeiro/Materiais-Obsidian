---
tags: [funcoes]
aliases: [Grafo, Visão de grafo, Graph]
tipo: funcao
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Core - Graph view]]", "[[Backlinks e links de saída]]", "[[MOCs]]"]
---

# Graph view

Mostra notas como **nós** e links como **linhas** ([[Core - Graph view]]). Abrir: `Ctrl/Cmd + G`.

## Dois grafos
- **Global:** todo o vault.
- **Local:** vizinhança da nota atual, com profundidade ajustável.

## Painel de opções
| Seção | O que faz |
|---|---|
| **Filtros** | busca, tags, anexos, notas inexistentes, órfãs |
| **Grupos** | colore nós por busca (ex.: `path:"06 - Plugins Core"`) |
| **Exibição** | setas, desbotar texto, tamanho dos nós, espessura |
| **Forças** | centro, repulsão, atração de links, distância |

> [!example] Grupos úteis
> - `tag:#moc` em dourado
> - `[nivel:avancado]` em vermelho
> - `path:"Templates"` em cinza

## Uso real
- Descobrir ilhas isoladas (notas órfãs).
- Ver notas centrais ([[MOCs]]).
- Explorar conexões inesperadas ([[Zettelkasten]]).

> [!warning] Grafos enormes
> Com milhares de notas, use o grafo local e filtros para manter o desempenho ([[Desempenho]]).

## Veja também
- [[Links não resolvidos]]
- [[Backlinks e links de saída]]

## Exercício
Crie um grupo que colore todas as notas da pasta `06 - Plugins Core` e outro para MOCs.
