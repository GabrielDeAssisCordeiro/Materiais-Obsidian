---
tags: [sync]
aliases: [Conflitos, Cópias duplicadas, Conflict files]
tipo: guia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Obsidian Sync]]", "[[Backup]]", "[[Solução de problemas]]"]
---

# Conflitos de sincronização

Conflito ocorre quando a mesma nota muda em dois lugares antes de sincronizar.

## Causas comuns
- Editar no celular e no computador ao mesmo tempo.
- Dispositivo ficou offline e voltou com versão antiga.
- Dois serviços sincronizando o mesmo vault.
- Arquivos de layout (`workspace.json`) sincronizados entre dispositivos.

## Como o Sync lida
O [[Obsidian Sync]] tenta **mesclar texto** e mantém histórico; em outros serviços aparecem **cópias de conflito**.

## Prevenção
- Aguarde a sincronização terminar antes de trocar de dispositivo.
- Ignore `workspace.json` ([[Pasta .obsidian]]).
- Use **uma** ferramenta por vault.
- Tenha [[Backup]] independente.

## Resolver
1. Abra as duas versões lado a lado ([[Painéis, abas e janelas]]).
2. Copie o que falta para uma versão.
3. Apague a cópia de conflito.
4. Se preciso, restaure do histórico ([[Histórico de arquivos e recuperação]]).

> [!warning] Cuidado ao apagar
> Confirme que a versão mantida contém tudo antes de remover a outra.

## Veja também
- [[Solução de problemas]]
- [[Configurações por dispositivo ou por vault]]

## Exercício
Provoque um conflito em um vault de teste e resolva-o sem perder texto.
