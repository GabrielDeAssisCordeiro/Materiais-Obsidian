---
titulo: "Principais capacidades do OpenClaw"
tags:
  - openclaw
  - conceito
  - visao-geral
tipo: conceito
aliases: ['Recursos do OpenClaw']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/concepts/features"
  - "https://docs.openclaw.ai/"
relacionados:
  - "[[O que é o OpenClaw]]"
  - "[[O OpenClaw versus um chatbot]]"
  - "[[Para quem é o OpenClaw e o que ele exige]]"
  - "[[Linha do tempo Clawdbot, Moltbot e OpenClaw]]"
---

# Principais capacidades do OpenClaw

## Objetivo

Ter um mapa das capacidades do OpenClaw para saber o que procurar em cada pasta do vault.

## Explicação

A página oficial de recursos organiza as capacidades em grupos. A tabela abaixo resume cada um e aponta onde o vault aprofunda o tema.

| Grupo | O que a documentação lista | Onde estudar |
|---|---|---|
| Canais | Núcleo: A2A, Reef, Telegram e WebChat. Plugins oficiais: Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, WhatsApp e outros | [[MOC - Canais e Mensageria\|Canais]] |
| Roteamento e sessões | Roteamento multiagente; mensagens diretas compartilham a sessão principal e grupos são isolados | [[MOC - Agent Runtime e Loop ReAct\|Runtime]] |
| Modelos e autenticação | Muitos provedores (Anthropic, OpenAI, Google), login por assinatura via OAuth e backends locais como vLLM, SGLang, Ollama, llama.cpp e LM Studio | [[MOC - Provedores e Modelos\|Provedores]] |
| Mídia | Imagens, áudio, vídeo e documentos; transcrição de notas de voz e text-to-speech | [[MOC - Ferramentas e MCP\|Ferramentas]] |
| Apps e interfaces | WebChat, Control UI, app de menu no macOS, nodes iOS e Android | [[MOC - Gateway\|Gateway]] |
| Ferramentas | Automação de navegador, execução de comandos, sandbox, busca na web por vários provedores | [[MOC - Ferramentas e MCP\|Ferramentas]] |
| Automação | Cron, heartbeat, hooks, webhooks, skills, plugins e pipelines Lobster | [[MOC - Automação e Agendamento\|Automação]] |

Dois detalhes ajudam a evitar mal-entendidos. Primeiro, a lista de provedores muda: o diretório de provedores na documentação é a referência mantida. Segundo, grupos são ativados por menção, e mensagens diretas passam por lista de permissão e pareamento, o que reduz o risco de qualquer pessoa falar com o agente.

> [!info] Núcleo versus plugins
> Só alguns canais vêm no núcleo; os demais são plugins oficiais que "instalam sob demanda". Isso explica por que a lista de canais aparece em duas camadas na documentação.

## Exemplo prático

Para listar as skills disponíveis e conferir as elegíveis na sua máquina, a documentação usa:

```bash
openclaw skills list
openclaw skills list --eligible
```

Isso mostra, na prática, a capacidade de skills que o seu agente enxerga neste momento.

## Armadilhas comuns

- Presumir que todo canal vem pré-instalado.
- Tratar uma lista de recursos como garantia de segurança. A própria documentação argumenta que lista de recursos não diz onde fica a fronteira de confiança.
- Habilitar muitas ferramentas de uma vez sem necessidade.

## Resumo

- Capacidades em sete grupos: canais, roteamento, modelos, mídia, apps, ferramentas e automação.
- Canais do núcleo e plugins oficiais convivem.
- Verifique listas de provedores e canais na doc, pois mudam.

## Relacionados

- [[O que é o OpenClaw]]
- [[O OpenClaw versus um chatbot]]
- [[Para quem é o OpenClaw e o que ele exige]]
- [[Tour rápido de instalação e primeira conversa]]

## Exercícios

1. Quais canais fazem parte do núcleo e quais são plugins oficiais?
2. Como mensagens diretas e grupos são tratados quanto às sessões?
3. Cite dois backends de modelo local suportados.
4. Por que uma lista de recursos não prova que o sistema é seguro?
5. Que comando lista as skills elegíveis?
