---
tags: [avancado, manutencao]
aliases: [Lentidão]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Solução de problemas]]", "[[Configurações de Plugins core]]", "[[Graph view]]"]
---

# Desempenho

Obsidian costuma ser rápido, mas vaults grandes e muitos plugins podem pesar.

## Checklist
- **Plugins:** desative os que não usa ([[Configurações de Plugins core]], [[Instalando e avaliando segurança]]).
- **Excluir pastas** da indexação (*Excluded files*, [[Configurações de Arquivos e links]]).
- **Grafo:** use o local e filtros ([[Graph view]]).
- **Consultas:** limite com `FROM` ([[Consultas Dataview]]).
- **Anexos grandes:** mantenha fora do vault ou comprima ([[Gerenciamento de anexos]]).
- **Mobile:** menos plugins e menos arquivos ([[iOS e Android]]).

## Diagnóstico
1. Ative o *Restricted Mode* e veja se melhora ([[Plugins da comunidade e Restricted Mode]]).
2. Reative plugins aos poucos.
3. Verifique o tempo de carregamento dos plugins, se o app exibir essa informação.

> [!question] Verificar na documentação oficial
> Confirme onde ver o tempo de carregamento de plugins na versão atual.

## Veja também
- [[Solução de problemas]]

## Exercício
Meça quanto tempo o app leva para abrir com e sem plugins.
