---
tags: [avancado, manutencao]
aliases: [Troubleshooting, Problemas comuns]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Desempenho]]", "[[Backup]]", "[[Pasta .obsidian]]"]
---

# Solução de problemas

## Método geral
1. **Reproduzir** com o mínimo possível.
2. Ativar o **Restricted Mode** ([[Plugins da comunidade e Restricted Mode]]).
3. Se resolveu, reative plugins **pela metade** até achar o culpado.
4. Teste em um **vault limpo** (*sandbox*).
5. Comando de recarregar o app sem salvar, se disponível.

## Problemas e causas
| Sintoma | Causa provável | Ver |
|---|---|---|
| Links quebrados | arquivos movidos fora do app | [[Links não resolvidos]] |
| Properties não aparecem | YAML inválido | [[Sintaxe YAML do frontmatter]] |
| Lentidão | plugins e vault grande | [[Desempenho]] |
| Notas duplicadas | conflitos de sincronização | [[Conflitos de sincronização]] |
| Interface estranha | snippet/tema | [[Snippets CSS]], [[Temas]] |
| Consulta vazia | plugin desativado ou sintaxe | [[Consultas Dataview]] |
| Perdi texto | sem backup | [[Histórico de arquivos e recuperação]] |

## Ferramentas
- Console do desenvolvedor (`Ctrl/Cmd + Shift + I`) no desktop.
- Informações de depuração em *About* (se disponível).
- Fórum e Discord oficiais.

> [!warning] Antes de mexer em `.obsidian`
> Copie a pasta e feche o app ([[Pasta .obsidian]]).

> [!question] Verificar na documentação oficial
> Confirme comandos e menus de depuração na versão atual.

## Veja também
- [[Backup]]
- [[Erros comuns]]

## Exercício
Simule um problema (ative um snippet que quebra o layout) e resolva-o com o método acima.
