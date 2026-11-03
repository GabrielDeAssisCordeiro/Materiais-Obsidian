---
tags: [avancado, automacao]
aliases: [Obsidian URI, obsidian://]
tipo: referencia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Captura rápida e compartilhamento]]", "[[CLI e automação]]", "[[QuickAdd]]"]
---

# URI scheme

Links `obsidian://` controlam o app a partir de outros programas, atalhos e navegadores.

## Exemplos
```text
obsidian://open?vault=Meu%20Vault&file=Nota
obsidian://new?vault=Meu%20Vault&name=Ideia&content=Texto
obsidian://search?vault=Meu%20Vault&query=tag%3A%23estudo
```
- Nomes e conteúdo precisam de **codificação de URL** (`%20`, `%3A`).
- Útil em atalhos do sistema, widgets e botões em notas ([[Captura rápida e compartilhamento]]).

> [!example] Link em nota
> ```markdown
> [Abrir Home](obsidian://open?vault=Obsidian-Material-de-Estudos&file=%F0%9F%8F%A0%20Home)
> ```

> [!question] Verificar na documentação oficial
> Confirme ações disponíveis (`open`, `new`, `search`, opções de anexar ou sobrescrever, nota diária) em help.obsidian.md.

## Veja também
- [[CLI e automação]]
- [[QuickAdd]]

## Exercício
Crie um link `obsidian://` que abra uma nota específica do seu vault.
