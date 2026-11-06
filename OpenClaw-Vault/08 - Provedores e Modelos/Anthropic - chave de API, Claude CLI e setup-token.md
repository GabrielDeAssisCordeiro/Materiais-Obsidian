---
titulo: "Anthropic - chave de API, Claude CLI e setup-token"
tags:
  - openclaw
  - conceito
  - provedores
tipo: conceito
aliases: ['Anthropic', 'Claude CLI', 'setup-token']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/zh-CN/providers/anthropic"
  - "https://docs.openclaw.ai/cli/models"
relacionados:
  - "[[Provedores, referências de modelo e a CLI models]]"
  - "[[Thinking e cache de prompt]]"
  - "[[Custo e escolha de modelo]]"
  - "[[Failover de modelos e fallbacks]]"
---

# Anthropic - chave de API, Claude CLI e setup-token

## Objetivo

Configurar o provedor Anthropic pelos três caminhos de autenticação documentados e entender o aviso de cobrança.

## Explicação

A documentação (versão lida em inglês via a página em chinês simplificado, que espelha a oficial) lista três formas:

| Caminho | Como funciona | Quando usar |
|---|---|---|
| **Chave de API** | Acesso pago por uso à API da Anthropic, referências `anthropic/*` | Automação compartilhada e gasto previsível |
| **Claude CLI** | Reaproveita um login existente do Claude Code **no mesmo host** | Uso pessoal em máquina que já tem o Claude Code |
| **Setup-token** | Token de longa duração gerado por `claude setup-token` | Quando o login precisa viver em outro host |

**1. Chave de API.** Crie a chave no Console da Anthropic e rode:

```bash
openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
openclaw models list --provider anthropic
```

Ou escolha "Anthropic API key" dentro de `openclaw onboard`. Configuração equivalente:

```json5
{
  env: { ANTHROPIC_API_KEY: "chave-de-exemplo-nao-real" },
  agents: { defaults: { model: { primary: "anthropic/claude-opus-5" } } },
}
```

**2. Claude CLI.** Confirme que a CLI existe e está logada (`claude --version`), rode `openclaw onboard` e escolha "Claude CLI"; o OpenClaw detecta e reutiliza as credenciais. O OpenClaw precisa rodar **no mesmo host** do login. Docker pode funcionar se o diretório home do container for persistido; outras configurações, como Podman, não montam o `~/.claude` do host. Para direcionar a execução pelo runtime da CLI:

```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-opus-5" },
      models: {
        "anthropic/claude-opus-5": { agentRuntime: { id: "claude-cli" } },
      },
    },
  },
}
```

A referência antiga `claude-cli/claude-opus-4-7` ainda funciona, mas novas configurações devem usar `anthropic/*` com a sobrescrita de runtime.

**3. Setup-token.** Em qualquer máquina com o Claude Code:

```bash
claude setup-token
openclaw models auth login --provider anthropic --method setup-token
```

O token começa com `sk-ant-oat01-`. No app do macOS, escolha "Anthropic setup-token" durante o onboarding.

> [!warning] Aviso de cobrança da própria documentação
> O backend da Claude CLI executa `claude -p`, que a Anthropic trata como uso programático (Agent SDK). Ele **conta contra os limites da assinatura**, e a política da Anthropic pode mudar. Para automação compartilhada em produção e gasto previsível, use **chave de API**. Confira as condições vigentes diretamente com a Anthropic.

> [!danger] Segredo é segredo
> Chave de API e setup-token dão acesso à sua conta. Nunca os cole em chats, repositórios ou na memória do agente. Veja [[MOC - Segurança e Hardening|Segurança e Hardening]].

## Exemplo prático

```bash
export ANTHROPIC_API_KEY="..."   # defina na sessão; não grave em arquivos versionados
openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
openclaw models list --provider anthropic
openclaw models set anthropic/claude-opus-5
```

Se `models list` não mostrar o nome do exemplo, use um dos que aparecerem.

## Armadilhas comuns

- Rodar o OpenClaw em um host diferente do login do Claude CLI.
- Usar assinatura em automação pesada e estourar limites.
- Deixar a chave dentro do `openclaw.json` versionado.

## Resumo

- Três caminhos: chave de API, Claude CLI, setup-token.
- Claude CLI exige o mesmo host; conta nos limites da assinatura.
- Produção compartilhada: chave de API.
- Guarde segredos fora de arquivos versionados.

## Relacionados

- [[Provedores, referências de modelo e a CLI models]]
- [[Thinking e cache de prompt]]
- [[Custo e escolha de modelo]]
- [[Failover de modelos e fallbacks]]

## Exercícios

1. Quais são os três caminhos de autenticação da Anthropic?
2. Por que o Claude CLI exige o mesmo host?
3. Qual é o aviso de cobrança sobre o backend da Claude CLI?
4. Que comando gera o setup-token e qual o prefixo dele?
