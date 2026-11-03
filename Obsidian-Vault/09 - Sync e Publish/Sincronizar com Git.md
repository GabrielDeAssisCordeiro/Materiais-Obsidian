---
tags: [sync]
aliases: [Git, Versionar vault]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Obsidian Git]]", "[[Backup]]", "[[Conflitos de sincronização]]"]
---

# Sincronizar com Git

Git dá **histórico completo** e backup remoto (GitHub, GitLab, servidor próprio).

## Básico
```bash
cd MeuVault
git init
git add .
git commit -m "primeiro commit"
git remote add origin <url-do-repositorio>
git push -u origin main
```

## Com plugin
O plugin [[Obsidian Git]] automatiza commit, pull e push.

## Boas práticas
- Repositório **privado** para notas pessoais.
- `.gitignore` com `workspace.json` e lixeira ([[Pasta .obsidian]]).
- Não versione segredos (chaves, senhas).
- No mobile o suporte é limitado ([[Sincronização no mobile]]).

> [!warning] Arquivos grandes
> Git lida mal com binários grandes (vídeos, áudios). Use Git LFS ou mantenha-os fora.

## Veja também
- [[Backup]]
- [[Conflitos de sincronização]]

## Exercício
Inicialize um repositório no vault de teste e faça três commits.
