---
tags: [plugins-comunidade, automacao, captura]
aliases: [QuickAdd plugin, Captura rápida plugin]
tipo: plugin
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Templater]]", "[[Captura rápida e compartilhamento]]", "[[Notas diárias]]"]
---

# QuickAdd

Cria **escolhas** para capturar e automatizar: templates, capturas e macros.

## Tipos de escolha
| Tipo | Faz |
|---|---|
| **Template** | cria nota a partir de template |
| **Capture** | adiciona texto a uma nota existente |
| **Macro** | encadeia comandos e scripts |
| **Multi** | agrupa escolhas |

## Exemplo: captura para a caixa de entrada
- Tipo: Capture.
- Arquivo: `00 - Caixa de entrada/Inbox.md`.
- Posição: final do arquivo.
- Formato: `- {{DATE:HH:mm}} {{VALUE}}`.

Execute pela paleta (*QuickAdd: Run QuickAdd*) ou crie um atalho ([[Hotkeys]]).

> [!tip] Mobile
> Adicione o comando à barra do celular para captura de uma mão ([[Barra de ações no mobile]]).

> [!question] Verificar na documentação oficial
> Confirme as variáveis de formato (`{{DATE}}`, `{{VALUE}}`...) na documentação do plugin.

## Veja também
- [[Templater]]
- [[Captura, processamento, conexão e saída]]

## Exercício
Crie uma captura que acrescenta uma linha com hora à nota diária.
