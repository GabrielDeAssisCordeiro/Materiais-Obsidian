---
titulo: "Telegram - configurar o bot passo a passo"
tags:
  - openclaw
  - conceito
  - canais
tipo: conceito
aliases: ['Telegram', 'BotFather']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/channels/telegram"
  - "https://docs.openclaw.ai/channels/telegram/setup"
  - "https://docs.openclaw.ai/channels/telegram/access-control"
relacionados:
  - "[[Pareamento e política de DM]]"
  - "[[Grupos - menção obrigatória e groupPolicy]]"
  - "[[Visão geral dos canais e instalação sob demanda]]"
  - "[[Configuração do Gateway em openclaw.json]]"
---

# Telegram - configurar o bot passo a passo

## Objetivo

Conectar um bot do Telegram ao OpenClaw, aprovar o primeiro DM e, se quiser, colocá-lo em um grupo.

## Explicação

O Telegram usa a biblioteca grammY, com DMs e grupos. O **long polling é o padrão** (webhook é opcional) e a política de DM padrão é **pareamento**.

**1. Criar o token.** No Telegram, converse com **@BotFather** (confira que o nome é exatamente esse), envie `/newbot`, siga as perguntas e guarde o token. Também há o fluxo web em `t.me/BotFather?startapp`.

**2. Dar o token ao OpenClaw.** Três formas, com esta precedência: `tokenFile` > `botToken` > variável de ambiente `TELEGRAM_BOT_TOKEN` (esta vale só para a conta padrão).

```bash
openclaw channels add --channel telegram --token <token-do-bot>
```

Ou, em `~/.openclaw/openclaw.json`:

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing",
      groups: { "*": { requireMention: true } },
    },
  },
}
```

O Telegram **não** usa `openclaw channels login`: defina o token e inicie o Gateway.

**3. Verificar.** A recarga a quente aplica a configuração ao Gateway em execução:

```bash
openclaw channels status --probe
```

Se o Gateway estiver parado: `openclaw gateway start` (serviço) ou `openclaw gateway` (terminal atual). Depois de mudar o ambiente do serviço, reinicie.

**4. Aprovar o primeiro DM.** Envie qualquer mensagem ao bot (isso cria um pedido de pareamento) e aprove:

```bash
openclaw pairing list telegram
openclaw pairing approve telegram <CODIGO>
```

**5. Grupo.** Adicione o bot ao grupo e anote seu ID de usuário (para `allowFrom` e `groupAllowFrom`) e o ID do chat do grupo (chave em `channels.telegram.groups`). O ID vem de `openclaw logs --follow`, de um bot de ID ou do método `getUpdates` da Bot API. Depois de liberado o grupo, `/whoami@<usuario_do_bot>` confirma os IDs. IDs de supergrupo que começam com `-100` vão em `channels.telegram.groups`, não em `groupAllowFrom`.

**6. Modo de privacidade.** Bots têm Privacy Mode por padrão e recebem menos mensagens de grupo. Para receber todas, desative com `/setprivacy` no BotFather ou torne o bot administrador.

> [!info] Cache de identidade
> Após iniciar com sucesso, o OpenClaw guarda a identidade do bot por até 24 horas; trocar ou remover o token limpa esse cache.

## Exemplo prático

Fluxo completo de teste: crie o bot, rode `openclaw channels add --channel telegram --token ...`, confirme com `openclaw channels status --probe`, mande "oi" ao bot, rode `openclaw pairing list telegram`, aprove o código e mande "oi" de novo para ver a resposta do agente.

## Armadilhas comuns

- Comitar o token em um repositório: guarde-o em variável de ambiente ou arquivo protegido.
- Esquecer que o código de pareamento expira em 1 hora.
- Esperar respostas em grupo sem desativar o modo de privacidade ou sem mencionar o bot.

## Resumo

- Token via BotFather; fornecido por `channels add`, `botToken`, `tokenFile` ou `TELEGRAM_BOT_TOKEN`.
- Verifique com `channels status --probe`; aprove DMs com `pairing approve`.
- Grupos exigem IDs corretos e atenção ao modo de privacidade.

## Relacionados

- [[Pareamento e política de DM]]
- [[Grupos - menção obrigatória e groupPolicy]]
- [[Allowlists e política de ferramentas por chat]]
- [[Visão geral dos canais e instalação sob demanda]]

## Exercícios

1. Qual é a precedência entre `tokenFile`, `botToken` e `TELEGRAM_BOT_TOKEN`?
2. Qual é a política de DM padrão do Telegram?
3. Por que o bot pode não ver mensagens de um grupo e como resolver?
4. Em que chave entram os IDs de supergrupos que começam com `-100`?
5. Quanto tempo vale um código de pareamento?
