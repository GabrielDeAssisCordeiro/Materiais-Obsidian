---
tags: [configuracoes, anexos]
aliases: [Anexos, Attachments]
tipo: guia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Configurações de Arquivos e links]]", "[[Embeds]]", "[[Estrutura de pastas]]"]
---

# Gerenciamento de anexos

Anexos são imagens, PDFs, áudios e outros arquivos ligados às notas ([[Embeds]]).

## Onde salvar
Em **Settings → Files and links → Default location for new attachments**:
| Opção | Resultado |
|---|---|
| Raiz do vault | tudo misturado |
| **Pasta específica** | `Anexos/` (usada neste vault) |
| Mesma pasta da nota | anexos junto da nota |
| Subpasta da pasta atual | ex.: `Anexos` dentro de cada pasta |

Esta escolha fica em `attachmentFolderPath` no `app.json` ([[Pasta .obsidian]]).

## Boas práticas
- Use nomes descritivos ao renomear arquivos coletados.
- Evite arquivos gigantes; considere comprimir imagens.
- Anexos entram no backup e na sincronização ([[Backup]]).
- Se mover anexos fora do app, links de imagem podem quebrar ([[Links não resolvidos]]).

> [!tip] Limpar o que sobrou
> Para achar anexos órfãos, use o filtro de anexos do [[Graph view]] ou revise a pasta periodicamente.

## Veja também
- [[Gravação de áudio]]
- [[Configurações de Arquivos e links]]

## Exercício
Cole uma imagem em uma nota e confira em que pasta o arquivo foi salvo.
