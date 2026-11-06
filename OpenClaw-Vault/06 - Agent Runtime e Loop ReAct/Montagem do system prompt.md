---
titulo: "Montagem do system prompt"
tags:
  - openclaw
  - conceito
  - agent-runtime
tipo: conceito
aliases: ['System prompt', 'Prompt do sistema']
nivel: avancado
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/concepts/system-prompt"
  - "https://docs.openclaw.ai/concepts/agent"
relacionados:
  - "[[Arquivos do workspace do agente]]"
  - "[[Montagem de contexto e o comando context]]"
  - "[[O agent runtime embutido]]"
  - "[[Anatomia do loop do agente no OpenClaw]]"
---

# Montagem do system prompt

## Objetivo

Entender, em alto nível, como o OpenClaw constrói o system prompt de cada execução e que parte dele você controla.

## Explicação

O system prompt **não é um texto fixo**: o OpenClaw o monta a cada execução a partir de camadas, segundo a página dedicada:

1. `buildAgentSystemPrompt` é um **renderizador puro**: recebe entradas explícitas e não lê a configuração global.
2. `buildConfiguredAgentSystemPrompt` aplica ajustes vindos da configuração para um agente específico antes de renderizar. A página cita, por exemplo, exibição do proprietário, dicas de TTS, apelidos de modelo, modo de citação de memória e modo de delegação a subagentes.
3. **Adaptadores de runtime** (embutido, CLI, prévias de comando e exportação, compactação) reúnem fatos ao vivo (ferramentas, estado do sandbox, capacidades do canal, arquivos de contexto, contribuições do provedor) e chamam a fachada configurada.

Sessões hospedadas em nodes usam o mesmo preparo de prompt e de bootstrap que as sessões locais do Gateway.

**Seções.** A parte lida da página descreve seções como:

| Seção | Ideia |
|---|---|
| Tooling | Lembrete de ferramentas estruturadas e orientação de uso; com `progress_card` ligado (`tools.updatePlan`, padrão ligado) orienta a manter um plano durável |
| Execution Bias | Agir em pedidos acionáveis, verificar antes de finalizar e deixar política de ferramentas, sandbox e aprovações de execução limitarem o risco em tempo de execução |
| Promised Work | Cumprir trabalho prometido ou em segundo plano e nunca tratar progresso como conclusão |
| Project Context | Arquivos de bootstrap do workspace injetados, tema de [[Arquivos do workspace do agente]] |

**Contribuições de provedores.** Plugins de provedor podem substituir as seções `interaction_style`, `tool_call_style` ou `execution_bias`, e adicionar um prefixo estável acima da **fronteira de cache de prompt** ou um sufixo dinâmico abaixo dela. Para rotas da família OpenAI, `plugins.entries.openai.config.personality` aceita `"friendly"` (padrão), `"on"` (apelido de `"friendly"`) ou `"off"`.

> [!warning] Página truncada
> A leitura desta página ficou parcial nesta sessão: partes sobre injeção dos arquivos de bootstrap, limites de tamanho e modos de prompt não foram lidas. Consulte `docs.openclaw.ai/concepts/system-prompt` antes de depender de detalhes.

> [!tip] Política em código, não no prompt
> A seção Execution Bias lembra que o risco é limitado por política, sandbox e aprovações **em tempo de execução**. O prompt orienta; não protege. Veja [[Fronteiras de confiança na arquitetura]].

## Exemplo prático

Para ver o efeito da montagem, rode `/context detail` no chat e observe o tamanho do system prompt e a contribuição de cada arquivo e de cada skill. Depois altere o `SOUL.md` do workspace e rode o comando de novo.

```markdown
/context detail
```

## Armadilhas comuns

- Escrever regras de segurança no `AGENTS.md` e acreditar que bastam.
- Inflar o `AGENTS.md` com texto que o agente raramente usa: custa tokens em toda execução.
- Mexer em seções de provedor sem entender o cache de prompt: alterar o prefixo pode invalidar o cache.

## Resumo

- O system prompt é montado por camadas a cada execução.
- Seções: Tooling, Execution Bias, Promised Work, Project Context e outras.
- Provedores podem contribuir com seções e com prefixo e sufixo em relação ao cache.
- O prompt orienta; os controles de verdade são em código.

## Relacionados

- [[Arquivos do workspace do agente]]
- [[Montagem de contexto e o comando context]]
- [[O agent runtime embutido]]
- [[Anatomia do loop do agente no OpenClaw]]

## Exercícios

1. Que camadas participam da montagem do system prompt?
2. O que é a "fronteira de cache de prompt"?
3. Por que regras de segurança no prompt não bastam?
4. Que comando mostra o tamanho do system prompt e dos arquivos injetados?
