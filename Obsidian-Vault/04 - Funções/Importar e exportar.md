---
tags: [funcoes]
aliases: [Importer, Exportar PDF, Web Clipper]
tipo: funcao
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Core - Importer]]", "[[Migração de e para outras ferramentas]]", "[[Backup]]"]
---

# Importar e exportar

## Importar
- **Importer** (plugin core): traz notas de Evernote, Notion, Apple Notes, OneNote, Google Keep, Bear, Roam, HTML, Markdown e CSV ([[Core - Importer]]).
- **Web Clipper:** extensão oficial de navegador que salva páginas como notas.

> [!question] Verificar na documentação oficial
> A lista de fontes do Importer cresce; confirme as disponíveis e as limitações de cada uma.

## Exportar
- **PDF:** menu da nota → *Export to PDF*.
- **Markdown:** os arquivos já estão em `.md`; copie a pasta.
- **HTML/outros:** via Pandoc ou plugins ([[Migração de e para outras ferramentas]]).
- Para site: [[Obsidian Publish]].

> [!warning] Compatibilidade
> Wikilinks, callouts e embeds não são Markdown universal ([[Sintaxe estendida]]). Antes de exportar para outros sistemas, considere usar links Markdown ([[Wikilinks e links Markdown]]).

## Veja também
- [[Backup]]
- [[Gerenciamento de anexos]]

## Exercício
Exporte uma nota com callout e tabela para PDF e confira a renderização.
