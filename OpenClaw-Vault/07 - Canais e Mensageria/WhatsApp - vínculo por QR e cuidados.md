---
titulo: "WhatsApp - vínculo por QR e cuidados"
tags:
  - openclaw
  - conceito
  - canais
tipo: conceito
aliases: ['WhatsApp', 'Baileys']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/channels/whatsapp"
  - "https://docs.openclaw.ai/channels"
relacionados:
  - "[[Pareamento e política de DM]]"
  - "[[Visão geral dos canais e instalação sob demanda]]"
  - "[[Gateway, clientes e nodes]]"
  - "[[Grupos - menção obrigatória e groupPolicy]]"
---

# WhatsApp - vínculo por QR e cuidados

## Objetivo

Vincular uma conta de WhatsApp ao Gateway, entendendo que o vínculo é uma sessão do WhatsApp Web e que o acesso é controlado em separado.

## Explicação

O canal usa **WhatsApp Web (Baileys)**. O Gateway é dono da(s) sessão(ões) vinculada(s), e **não existe canal separado via Twilio**. Por isso, só um Gateway deve controlar a conta (ver [[Gateway, clientes e nodes]]).

**Requisitos:**

1. O plugin: `openclaw plugins install @openclaw/whatsapp` (o onboarding e `openclaw channels add` também oferecem; `npm:@openclaw/whatsapp` instala direto do npm, e vale fixar uma versão exata para instalações reproduzíveis).
2. Um celular capaz de ler o QR de login.
3. Um Gateway em execução (`openclaw gateway`).

**Vincular:**

```bash
openclaw channels login --channel whatsapp
openclaw channels login --channel whatsapp --account work
openclaw channels add --channel whatsapp --account work --auth-dir /caminho/wa-auth
```

A segunda linha vincula uma conta nomeada; a terceira usa um diretório de autenticação existente e deve rodar **antes** do login.

**Chaves de acesso** (em `channels.whatsapp`): `dmPolicy` (`"pairing"` por padrão para remetentes desconhecidos), `allowFrom` (números aprovados), `groupPolicy` (o exemplo usa `"allowlist"`) e `groupAllowFrom`.

```json5
{
  channels: {
    whatsapp: {
      dmPolicy: "pairing",
      allowFrom: ["+15551234567"],
      groupPolicy: "allowlist",
      groupAllowFrom: ["+15551234567"],
    },
  },
}
```

Para aprovar pedidos de pareamento:

```bash
openclaw pairing list whatsapp
openclaw pairing approve whatsapp <CODIGO>
```

> [!warning] Cuidados da documentação
> - O login é **só por QR**. Em hosts remotos ou sem tela, garanta que o QR chegue ao celular antes de expirar (QR em terminal, captura de tela e anexos de chat podem expirar no caminho).
> - Aprovar um pedido de DM é diferente de vincular a conta por QR.
> - Pedidos de DM expiram em 1 hora, com no máximo 3 pendentes por conta.

## Exemplo prático

Use **um número secundário** (chip dedicado), não o pessoal. Vincule, defina `allowFrom` só com o seu número, envie uma mensagem de teste e confirme a resposta. Guarde o diretório de autenticação com permissões restritas, pois ele equivale a uma sessão logada.

## Armadilhas comuns

- Vincular a conta pessoal principal e deixar `dmPolicy` aberta.
- Copiar o diretório de autenticação para outro lugar sem proteção.
- Esquecer que o QR expira e achar que o canal está quebrado.

## Resumo

- WhatsApp Web via Baileys, plugin `@openclaw/whatsapp`, login por QR.
- Vínculo da conta e aprovação de DMs são etapas distintas.
- Prefira número dedicado e `allowFrom` restrito.

## Relacionados

- [[Pareamento e política de DM]]
- [[Visão geral dos canais e instalação sob demanda]]
- [[Grupos - menção obrigatória e groupPolicy]]
- [[Gateway, clientes e nodes]]

## Exercícios

1. Qual tecnologia o canal de WhatsApp usa?
2. Qual comando vincula uma conta por QR e como se vincula uma conta nomeada?
3. Por que o QR deve alcançar o celular rapidamente em hosts remotos?
4. Qual a diferença entre vincular a conta e aprovar um pedido de DM?
