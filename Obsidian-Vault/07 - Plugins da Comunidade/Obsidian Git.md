---
tags: [plugins-comunidade, plugin]
aliases: [Git plugin, Versionamento com Git]
tipo: plugin
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Sincronizar com Git]]", "[[Backup]]", "[[Conflitos de sincronização]]", "[[MOC - Plugins da Comunidade]]"]
---

# Obsidian Git

## Para que serve
Faz commit, pull e push do vault automaticamente, dando histórico completo e backup remoto.

## Instalação e configuração
Instale em **Settings → Community plugins → Browse** ([[Instalando e avaliando segurança]]).

- Exige Git instalado e um repositório (local ou remoto).
- Configure intervalo de *auto commit-and-sync* e a mensagem de commit.
- Ative *pull on startup*.
- Crie um `.gitignore`.

## Exemplo prático
```text
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.trash/
```
Commit manual: comando *Obsidian Git: Commit all changes*.

> [!warning] Mobile limitado
> O suporte no celular é mais restrito; veja [[Sincronização no mobile]].

## Veja também
- [[Sincronizar com Git]]
- [[Backup]]
- [[Conflitos de sincronização]]
- [[MOC - Plugins da Comunidade]]

## Exercício
Instale em um vault de teste, execute o exemplo e decida se vale manter no vault principal.
