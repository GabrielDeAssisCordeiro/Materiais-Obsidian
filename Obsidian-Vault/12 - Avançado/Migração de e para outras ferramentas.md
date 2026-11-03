---
tags: [avancado, integracao]
aliases: [Migrar para Obsidian, Sair do Obsidian, Notion Evernote Logseq]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Core - Importer]]", "[[Importar e exportar]]", "[[Local-first e propriedade dos dados]]"]
---

# Migração de e para outras ferramentas

## Para o Obsidian
| Origem | Caminho |
|---|---|
| Notion, Evernote, Apple Notes, OneNote, Google Keep, Bear | plugin [[Core - Importer]] |
| Roam, Logseq | exportar Markdown; ajustar referências de bloco |
| Outros apps Markdown | copiar a pasta e abrir como vault |
| Texto simples/Word | converter com Pandoc |

## Passos
1. Importe para uma **pasta de teste**.
2. Revise links, anexos e formatação.
3. Padronize propriedades ([[Nomenclatura de propriedades]]).
4. Só então integre ao vault principal.

## Para fora do Obsidian
- Arquivos já estão em `.md`; copie a pasta.
- Converta wikilinks para Markdown se necessário ([[Wikilinks e links Markdown]]).
- Exporte com Pandoc ou PDF ([[Importar e exportar]]).

> [!warning] Recursos exclusivos
> Callouts, embeds e `.canvas` / `.base` não funcionam fora do Obsidian ([[Sintaxe estendida]]).

> [!question] Verificar na documentação oficial
> Confirme limitações atuais do Importer para cada origem.

## Veja também
- [[Backup]]
- [[CLI e automação]]

## Exercício
Importe cinco notas de outro app para uma pasta de teste e liste o que precisou ajustar.
