---
titulo: "Pontos de extensão - plugins, skills e hooks"
tags:
  - openclaw
  - conceito
  - arquitetura
tipo: conceito
aliases: ['Extensibilidade', 'Plugin SDK']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
  - "https://docs.openclaw.ai/concepts/features"
  - "https://docs.openclaw.ai/clawhub/how-it-works"
relacionados:
  - "[[Arquitetura em camadas do OpenClaw]]"
  - "[[ClawHub, plugins e o ecossistema]]"
  - "[[Fronteiras de confiança na arquitetura]]"
  - "[[O agent runtime embutido]]"
---

# Pontos de extensão - plugins, skills e hooks

## Objetivo

Conhecer as quatro formas de estender o OpenClaw e saber quando usar cada uma.

## Explicação

A documentação, na seção de capacidades, separa a extensibilidade em quatro mecanismos:

| Mecanismo | O que é | Quando usar |
|---|---|---|
| **Skills** | Pacotes de texto centrados em `SKILL.md` que ensinam procedimentos que o agente carrega sob demanda | Ensinar um fluxo de trabalho repetível |
| **Plugins** | Extensões de código: canais, provedores de modelo, ferramentas, voz, memória | Adicionar uma capacidade nova ao sistema |
| **Hooks** | Código que reage a eventos (início de sessão, mensagens, chamadas de ferramenta, ciclo de vida do Gateway) | Aplicar política, registrar auditoria, enriquecer prompts |
| **Automação** | Cron, webhooks, gatilhos de e-mail e ordens permanentes | Executar trabalho sem pedido manual |

**Plugins.** Os canais do núcleo são poucos (A2A, Reef, Telegram e WebChat); os demais são plugins oficiais instalados sob demanda. Há ainda plugins de provedores, de ferramentas e de voz, além de um SDK de plugins com manifestos, pontos de entrada e hooks. O catálogo e o fluxo de instalação via ClawHub estão em [[ClawHub, plugins e o ecossistema]].

**Hooks de política.** A documentação lista famílias de hooks: de política de chamada de ferramenta, de prompt e sessão, de mensagem e entrega, e de ciclo de vida do Gateway. Os hooks de política são relevantes para segurança, porque aplicam regras **em código**, como discutido em [[Fronteiras de confiança na arquitetura]].

> [!warning] Extensões ampliam a superfície de ataque
> Um plugin é código que roda com os privilégios do Gateway; uma skill pode trazer scripts. Leia o código, as permissões declaradas e o status de varredura antes de instalar. Veja [[MOC - Skills|Skills]] e [[MOC - Ameaças e Riscos|Ameaças e Riscos]].

## Exemplo prático

Inventário rápido do que está instalado na sua máquina:

```bash
openclaw skills list
openclaw plugins list
```

Anote, para cada item, de onde veio (núcleo, ClawHub, npm, pasta local) e quem o mantém.

## Armadilhas comuns

- Escrever como skill algo que precisa de código (use um plugin) ou o contrário.
- Instalar plugins só porque "estavam na lista".
- Não saber qual extensão introduziu um comportamento novo; mantenha o inventário.

## Resumo

- Quatro mecanismos: skills, plugins, hooks e automação.
- Skills ensinam; plugins adicionam capacidades; hooks aplicam política e reagem a eventos.
- Todo ponto de extensão amplia a superfície de ataque.

## Relacionados

- [[Arquitetura em camadas do OpenClaw]]
- [[ClawHub, plugins e o ecossistema]]
- [[Fronteiras de confiança na arquitetura]]
- [[O agent runtime embutido]]
- [[MOC - Automação e Agendamento|Automação e Agendamento]]

## Exercícios

1. Qual a diferença entre skill e plugin?
2. Para que servem os hooks de política de ferramenta?
3. Quais canais fazem parte do núcleo?
4. Por que manter um inventário de extensões é uma boa prática?
