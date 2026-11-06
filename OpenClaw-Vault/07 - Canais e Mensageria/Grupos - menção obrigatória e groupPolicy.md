---
titulo: "Grupos - menção obrigatória e groupPolicy"
tags:
  - openclaw
  - conceito
  - canais
tipo: conceito
aliases: ['Grupos', 'requireMention', 'groupPolicy']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/channels/groups"
  - "https://docs.openclaw.ai/channels/telegram"
relacionados:
  - "[[Allowlists e política de ferramentas por chat]]"
  - "[[Sessões e chaves de sessão]]"
  - "[[Telegram - configurar o bot passo a passo]]"
  - "[[Pareamento e política de DM]]"
---

# Grupos - menção obrigatória e groupPolicy

## Objetivo

Colocar o agente em grupos sem que ele reaja a toda mensagem nem obedeça a qualquer participante.

## Explicação

Segundo a página de grupos:

- **`requireMention`**: por padrão, o agente só responde quando é **mencionado**. Dá para desligar por grupo. Mensagens sem menção são guardadas **só como contexto**. Uma menção, uma resposta ao bot, um comando ou uma DM disparam resposta; `/activation` também controla o gatilho.
- **`requireMentionInBotThreads`**: com `false`, aceita acompanhamentos sem menção em threads criadas pelo bot; com `true`, exige menção ali. Se omitido, vale o comportamento do canal.
- **`groupPolicy`**: `"disabled"` descarta todas as mensagens de grupo; `"allowlist"` (padrão) bloqueia remetentes de grupo até estarem na lista.
- **Listas**: `*.groups` e `*.groupAllowFrom` controlam quais grupos e remetentes entram. **O acesso a DM é separado** e definido por `*.allowFrom`.
- **Respostas**: o texto final é publicado na sala automaticamente (`visibleReplies: "automatic"`).

Exemplos de chaves por canal: `channels.discord.guilds.<id>.requireMention` e `channels.slack.requireMention`.

```json5
{
  channels: {
    telegram: {
      groups: { "*": { requireMention: true } },
    },
  },
}
```

**Sessão.** Cada grupo tem sua própria sessão por padrão (`session.groupScope`: `per-group`), como explicado em [[Sessões e chaves de sessão]]; o histórico de um grupo não se mistura com suas DMs.

> [!warning] Grupo é entrada de terceiros
> Qualquer participante autorizado pode escrever algo que o agente leia. Em grupos, mantenha menção obrigatória, allowlist e ferramentas restritas: um colega mal-intencionado (ou uma conta comprometida) pode tentar induzir o agente a agir.

## Exemplo prático

Para um grupo de família com um bot só de consulta: `groupPolicy: "allowlist"`, o grupo na lista, `requireMention: true`, e uma política que negue `exec`, `write` e `edit` (nomes das ferramentas conforme a sua versão). Teste enviando uma mensagem sem menção (não deve haver resposta) e outra mencionando o bot.

## Armadilhas comuns

- Desligar `requireMention` em grupos grandes: o agente passa a responder a tudo e gasta tokens.
- Achar que liberar o grupo libera as DMs, ou o contrário.
- Usar `groupPolicy` aberta com ferramentas de execução ativas.

## Resumo

- Menção obrigatória por padrão; mensagens sem menção viram contexto.
- `groupPolicy: "allowlist"` é o padrão; `"disabled"` descarta grupos.
- Acesso a grupos e a DMs são configurados separadamente.

## Relacionados

- [[Allowlists e política de ferramentas por chat]]
- [[Sessões e chaves de sessão]]
- [[Telegram - configurar o bot passo a passo]]
- [[Pareamento e política de DM]]

## Exercícios

1. O que acontece com mensagens de grupo que não mencionam o bot?
2. Qual é o valor padrão de `groupPolicy`?
3. Por que o acesso a DMs e a grupos é configurado separadamente?
4. Cite dois riscos de desligar `requireMention`.
