---
tags: [configuracoes]
aliases: [Config por dispositivo, Settings por vault, Sincronizar configurações]
tipo: conceito
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Pasta .obsidian]]", "[[Obsidian Sync]]", "[[Sincronizar com Git]]"]
---

# Configurações por dispositivo ou por vault

## Regra geral
As configurações ficam **dentro do vault**, em `.obsidian` ([[Pasta .obsidian]]). Vaults diferentes têm configurações independentes; o mesmo vault copiado carrega suas configurações.

## O que é por vault
Atalhos, plugins instalados, temas, snippets, opções de editor e de links.

## O que é por dispositivo
- Layout aberto (`workspace.json`) e tamanhos de janela.
- Alguns itens do app (conta, idioma da interface, lista de vaults).
- Diferenças entre desktop e mobile: plugins pesados ou atalhos de teclado.

## Sincronizando configurações
- O **Obsidian Sync** permite escolher quais tipos sincronizar (principais, aparência, atalhos, plugins etc.) ([[Obsidian Sync]]).
- Com iCloud, Syncthing ou Git, a pasta `.obsidian` vai junto, o que pode gerar conflitos entre dispositivos ([[Conflitos de sincronização]]).
- Há opção **Override config folder** para usar pastas diferentes por dispositivo (ex.: `.obsidian-mobile`) ([[Configurações de Arquivos e links]]).

> [!question] Verificar na documentação oficial
> Confirme quais itens exatamente o Sync cobre e como funciona a pasta de configuração alternativa.

> [!tip] Mobile mais leve
> Mantenha menos plugins no celular ([[Sincronização no mobile]]).

## Veja também
- [[Conflitos de sincronização]]
- [[Backup]]

## Exercício
Decida quais configurações você quer iguais em todos os dispositivos e quais deveriam diferir.
