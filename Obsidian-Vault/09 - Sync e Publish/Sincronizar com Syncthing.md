---
tags: [sync]
aliases: [Syncthing, Sincronização P2P]
tipo: guia
nivel: avancado
criado: 2026-10-23
relacionados: ["[[Conflitos de sincronização]]", "[[Backup]]", "[[Alternativas de sincronização]]"]
---

# Sincronizar com Syncthing

Sincronização **peer-to-peer**, gratuita e sem nuvem de terceiros.

## Como
1. Instale o Syncthing nos dispositivos (desktop e Android).
2. Compartilhe a pasta do vault entre eles.
3. Configure o `.stignore` para evitar arquivos voláteis.

```text
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.trash
```
4. Ative o **controle de versões** do Syncthing como rede de segurança.

## Pontos de atenção
- Dispositivos precisam estar online ao mesmo tempo (ou usar um servidor sempre ligado).
- iOS não tem cliente oficial; existem apps de terceiros.
- Conflitos geram cópias `.sync-conflict` ([[Conflitos de sincronização]]).

> [!question] Verificar na documentação oficial
> Confirme as opções atuais de clientes Android e iOS na documentação do Syncthing.

## Veja também
- [[Backup]]
- [[Sincronizar com Git]]

## Exercício
Configure dois dispositivos e provoque um conflito de propósito para ver o arquivo gerado.
