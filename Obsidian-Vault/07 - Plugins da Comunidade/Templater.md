---
tags: [plugins-comunidade, templates, automacao]
aliases: [Templater plugin, Templates avançados]
tipo: plugin
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Templates]]", "[[Notas diárias]]", "[[QuickAdd]]"]
---

# Templater

Sistema de templates com **variáveis, funções e JavaScript**, muito além do [[Core - Templates]].

## Configuração essencial
- **Template folder location:** `Templates`.
- *Trigger Templater on new file creation*: aplica templates automaticamente.
- *Folder templates*: template por pasta.
- Funções definidas pelo usuário exigem habilitar execução de scripts (atenção à segurança, [[Instalando e avaliando segurança]]).

## Sintaxe
```markdown
---
criado: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>

Amanhã: <% tp.date.tomorrow("YYYY-MM-DD") %>
<% tp.file.cursor() %>
```

| Função | Faz |
|---|---|
| `tp.date.now(formato)` | data atual |
| `tp.file.title` | título da nota |
| `tp.file.cursor()` | posiciona o cursor |
| `tp.system.prompt("Pergunta")` | pede texto |

> [!example] Nota diária com Templater
> Use um template com `tp.date.now` e aponte-o nas [[Notas diárias]] ou no [[Periodic Notes]].

> [!question] Verificar na documentação oficial
> Confirme a lista atual de módulos (`tp.date`, `tp.file`, `tp.system`, `tp.web`...) na documentação do plugin.

## Veja também
- [[Templates]]
- [[QuickAdd]]
- [[Linter]]

## Exercício
Crie um template de reunião que pergunte o título e preencha data e hora automaticamente.
