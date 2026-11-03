---
tags: [configuracoes, avancado]
aliases: [.obsidian, Pasta de configuração, Config folder]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Vault]]", "[[Configurações por dispositivo ou por vault]]", "[[Backup]]"]
---

# Pasta .obsidian

Pasta oculta na raiz do vault onde ficam as **configurações** ([[Vault]]).

## Arquivos comuns
| Arquivo/pasta | Conteúdo |
|---|---|
| `app.json` | configurações gerais (links, anexos, editor) |
| `appearance.json` | tema, fontes, snippets ativos |
| `core-plugins.json` | plugins core ativos ([[Configurações de Plugins core]]) |
| `community-plugins.json` | plugins da comunidade ativos |
| `hotkeys.json` | atalhos |
| `workspace.json` | layout atual |
| `graph.json` | opções do grafo |
| `bookmarks.json` | marcadores |
| `types.json` | tipos de properties ([[Tipos de properties]]) |
| `plugins/` | plugins instalados |
| `themes/` | temas |
| `snippets/` | CSS personalizado ([[Snippets CSS]]) |

```json
{
  "alwaysUpdateLinks": true,
  "attachmentFolderPath": "Anexos"
}
```

> [!warning] Edite com o Obsidian fechado
> Alterações manuais com o app aberto podem ser sobrescritas. Faça cópia antes.

> [!tip] Versionamento
> Em repositório Git, ignore `workspace.json` e `plugins/*/data.json` sensíveis ([[Sincronizar com Git]]).

> [!question] Verificar na documentação oficial
> Os nomes e formatos dos arquivos podem mudar; confirme em help.obsidian.md.

## Veja também
- [[Backup]]
- [[Solução de problemas]]

## Exercício
Abra a pasta `.obsidian` do seu vault e identifique o arquivo que guarda seus atalhos.
