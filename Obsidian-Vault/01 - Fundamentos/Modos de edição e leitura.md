---
tags: [fundamentos, editor]
aliases: [Live Preview, Modo fonte, Reading view]
tipo: conceito
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Configurações do Editor]]", "[[Sintaxe básica]]", "[[Interface]]"]
---

# Modos de edição e leitura

Cada nota pode estar em três visualizações:

| Modo | Descrição |
|---|---|
| **Live Preview** | Edita e vê a formatação quase renderizada; a sintaxe aparece perto do cursor |
| **Source mode** | Mostra o Markdown puro, sem renderizar |
| **Reading view** | Somente leitura, totalmente renderizado |

## Alternar
- `Ctrl/Cmd + E` alterna entre edição e leitura.
- O modo de edição (Live Preview ou Source) é escolhido em **Configurações → Editor** ([[Configurações do Editor]]).
- O modo padrão de abertura das notas também é configurável.

> [!tip] Quando usar cada um
> Use **Live Preview** no dia a dia, **Source** para depurar sintaxe (ex.: [[Sintaxe YAML do frontmatter]]) e **Reading** para revisar o resultado.

> [!warning] Comentários e HTML
> Alguns elementos (como `%%comentários%%`) só ficam ocultos na leitura; veja [[Comentários e notas de rodapé]].

## Veja também
- [[Sintaxe básica]]
- [[Interface]]

## Exercício
Escreva uma tabela ([[Tabelas]]) em Source mode e veja o resultado em Reading view.
