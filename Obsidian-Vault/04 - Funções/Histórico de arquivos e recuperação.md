---
tags: [funcoes, seguranca]
aliases: [File recovery, Versões, Snapshots]
tipo: funcao
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Core - Recuperação de arquivos]]", "[[Backup]]", "[[Obsidian Sync]]"]
---

# Histórico de arquivos e recuperação

O plugin **File recovery** guarda **instantâneos** locais das notas ([[Core - Recuperação de arquivos]]).

- Intervalo entre snapshots e tempo de retenção são configuráveis (padrões em minutos e dias).
- Comando *File recovery: Open snapshots* permite comparar e restaurar versões.
- O **Obsidian Sync** tem seu próprio histórico de versões ([[Obsidian Sync]]).
- Com [[Sincronizar com Git]] você tem versionamento completo.

> [!warning] Não substitui backup
> Snapshots ficam no mesmo dispositivo. Faça [[Backup]] regularmente.

> [!tip] Apaguei sem querer
> Verifique snapshots, a lixeira do sistema e o histórico do Sync ou do Git.

## Veja também
- [[Backup]]
- [[Solução de problemas]]

## Exercício
Edite uma nota, espere um snapshot e restaure a versão anterior.
