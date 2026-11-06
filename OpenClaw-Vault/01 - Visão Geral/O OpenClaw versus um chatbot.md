---
titulo: "O OpenClaw versus um chatbot"
tags:
  - openclaw
  - conceito
  - visao-geral
tipo: conceito
aliases: ['Agente vs chatbot']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
  - "https://docs.openclaw.ai/concepts/features"
relacionados:
  - "[[O que é o OpenClaw]]"
  - "[[Principais capacidades do OpenClaw]]"
  - "[[O que é um agente de IA]]"
  - "[[Uso de ferramentas e tool calling]]"
---

# O OpenClaw versus um chatbot

## Objetivo

Entender, com critérios claros, por que o OpenClaw não deve ser tratado como "mais um chatbot".

## Explicação

Um chatbot típico vive dentro de um aplicativo ou site de um provedor: você escreve, ele responde com texto, e o histórico fica no serviço do provedor. O OpenClaw inverte vários desses pontos.

| Critério | Chatbot hospedado | OpenClaw |
|---|---|---|
| Onde roda | Nos servidores do provedor | No seu hardware (laptop, servidor, VPS) |
| Onde você conversa | No app do provedor | Nos apps de chat que você já usa, mais CLI e painel web |
| O que faz | Principalmente responde texto | Pode executar ferramentas: comandos, navegador, arquivos, busca na web |
| Continuidade | Histórico no serviço | Sessões e memória mantidas pelo Gateway no seu disco |
| Iniciativa | Só responde quando chamado | Pode agir por agendamento, hooks e webhooks |
| Modelo | O do provedor | Qualquer provedor suportado, ou modelo local |

A diferença central é a palavra **agente**: o OpenClaw recebe um objetivo, decide quais ferramentas usar, observa o resultado e continua até concluir. Esse ciclo é detalhado em [[O padrão ReAct]].

> [!warning] Poder implica risco
> Capacidade de agir é também superfície de ataque. A documentação afirma que o isolamento por sandbox vem desligado por padrão, então vale conhecer os controles de [[MOC - Segurança e Hardening|Segurança e Hardening]] antes de dar acesso a contas e arquivos reais.

## Exemplo prático

Compare duas mensagens enviadas pelo celular:

```markdown
Chatbot:   "Como faço para listar arquivos grandes no Linux?"
OpenClaw:  "Liste os 10 maiores arquivos da pasta de downloads e me mande o resultado."
```

O chatbot explica o comando. O OpenClaw, se tiver a ferramenta de execução habilitada e permissão para isso, roda a tarefa na máquina onde o Gateway está e devolve o resultado na conversa. O segundo caso exige decisões de permissão que o primeiro não exige.

## Armadilhas comuns

- Esperar comportamento "mágico" sem configurar um modelo e credenciais.
- Dar a um bot de grupo as mesmas permissões que você tem. Em grupos, a ativação por menção e as listas de remetentes autorizados existem exatamente para evitar isso; veja [[MOC - Canais e Mensageria|Canais e Mensageria]].
- Assumir que o histórico some ao fechar o app: ele permanece no host do Gateway, o que é bom para continuidade e ruim se o host for comprometido.

## Resumo

- Chatbot responde; agente decide e age.
- O OpenClaw roda no seu hardware e fala pelos seus apps de chat.
- Ferramentas, memória e agendamento tornam-no mais útil e mais arriscado.
- Controle de acesso deixa de ser opcional.

## Relacionados

- [[O que é o OpenClaw]]
- [[Principais capacidades do OpenClaw]]
- [[O que é um agente de IA]]
- [[Uso de ferramentas e tool calling]]
- [[MOC - Comparações|Comparações]]

## Exercícios

1. Cite três diferenças entre um chatbot hospedado e o OpenClaw.
2. Por que dar permissão de execução a um agente exige mais cuidado que usar um chatbot?
3. Onde ficam as sessões e a memória no OpenClaw?
4. Dê um exemplo de tarefa que só um agente com ferramentas consegue cumprir.
