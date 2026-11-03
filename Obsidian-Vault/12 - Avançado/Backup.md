---
tags: [avancado, seguranca]
aliases: [Cópia de segurança, Backups]
tipo: guia
nivel: iniciante
criado: 2026-10-23
relacionados: ["[[Histórico de arquivos e recuperação]]", "[[Sincronizar com Git]]", "[[Local-first e propriedade dos dados]]"]
---

# Backup

Sincronização **não é** backup: apagar uma nota remove-a em todos os dispositivos.

## Regra 3-2-1
- **3** cópias dos dados.
- **2** mídias diferentes.
- **1** cópia fora do local principal.

## Opções
| Opção | Observação |
|---|---|
| Cópia da pasta do vault | simples; agende com script |
| Time Machine / Histórico de Arquivos | automático no sistema |
| [[Sincronizar com Git]] | histórico completo |
| [[Obsidian Sync]] | versões na nuvem |
| Snapshots locais | [[Histórico de arquivos e recuperação]] |
| Cópia em nuvem | Drive, Dropbox, etc. |

## Boas práticas
- Inclua a pasta `.obsidian` ([[Pasta .obsidian]]) e os anexos.
- **Teste a restauração** pelo menos uma vez.
- Faça backup antes de atualizações grandes e de scripts em lote ([[CLI e automação]]).

> [!warning] Sem teste, não é backup
> Um backup que nunca foi restaurado pode estar incompleto.

## Veja também
- [[Conflitos de sincronização]]
- [[Solução de problemas]]

## Exercício
Faça uma cópia do vault, abra-a como outro vault e confira que as notas abrem.
