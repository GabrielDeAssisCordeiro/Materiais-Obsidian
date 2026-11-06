---
titulo: "Modelos locais - Ollama e llama.cpp"
tags:
  - openclaw
  - conceito
  - provedores
tipo: conceito
aliases: ['Modelos locais', 'Ollama', 'llama.cpp']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/providers/ollama"
  - "https://docs.openclaw.ai/gateway/local-models"
  - "https://docs.openclaw.ai/concepts/features"
relacionados:
  - "[[Diretório de provedores e como ler a lista]]"
  - "[[Custo e escolha de modelo]]"
  - "[[Confiança, permissões e riscos de agentes]]"
  - "[[Provedores, referências de modelo e a CLI models]]"
---

# Modelos locais - Ollama e llama.cpp

## Objetivo

Rodar o OpenClaw com modelo local, conhecendo as armadilhas de URL, contexto e segurança.

## Explicação

**Recomendação da documentação.** O caminho recomendado é instalar o plugin llama.cpp, rodar `openclaw onboard` e escolher **Managed local server**. O assistente mostra o host do Gateway, o modelo, o tamanho do download e o backend antes de baixar, e **verifica uma chamada real de ferramenta** antes de mudar o modelo padrão. LM Studio e Ollama são alternativas para gerenciar o modelo à parte; há ainda "Local model services" para servidores que só sobem quando um modelo selecionado precisa deles.

**Ollama.** Há três modos: Cloud + Local (host Ollama com modelos locais e, se logado, modelos `:cloud`), só local e **Ollama Cloud** direto em `https://ollama.com` pelo provedor `ollama-cloud` (referências `ollama-cloud/<modelo>`).

> [!warning] Não use /v1 com Ollama
> O OpenClaw usa a **API nativa** do Ollama (`/api/chat`), não o endpoint compatível com OpenAI. Usar `http://host:11434/v1` **quebra a chamada de ferramentas** e pode fazer o modelo escrever JSON de ferramenta como texto. Use a URL nativa, sem `/v1`:

```json5
{
  models: {
    providers: {
      ollama: { baseUrl: "http://host:11434" },
    },
  },
}
```

A chave atual é `baseUrl` (`baseURL` é aceita por compatibilidade com exemplos de SDK OpenAI). O formato exato do bloco do provedor (descoberta implícita, lista explícita de modelos) está nas páginas de configuração e receitas do Ollama; o trecho acima mostra só a ideia da URL e deve ser confirmado lá.

**Hardware e tamanho.** A memória depende dos pesos, do contexto, do runtime e de outras cargas. Receitas curadas do llama.cpp usam **contexto de 64K**; a menor tem piso de 8 GiB de memória do host, e as maiores exigem mais; esses pisos não garantem encaixe nem velocidade. Deixe espaço para o prompt completo do OpenClaw, ferramentas, histórico e saída: **um modelo que responde a um prompt curto ainda pode falhar em um turno de agente**. Teste tarefas reais antes de torná-lo padrão.

**Segurança.** "Modelos locais não têm os filtros de segurança dos provedores hospedados": mantenha permissões de ferramenta e defesas contra injeção de prompt adequadas ao modelo e à tarefa.

## Exemplo prático

1. Em uma VM com memória suficiente, rode `openclaw onboard` e escolha **Managed local server**.
2. Confirme a chamada de ferramenta verificada pelo assistente.
3. Teste três tarefas reais (resumir um arquivo, listar uma pasta, buscar algo) com `exec` e escrita **desligados**.
4. Só então decida se o modelo local serve como padrão ou como fallback.

## Armadilhas comuns

- Apontar o `baseUrl` do Ollama para `/v1`.
- Escolher um modelo pequeno demais e esperar o mesmo comportamento de um modelo de ponta.
- Conceder ferramentas poderosas a um modelo local pouco robusto.

## Resumo

- Caminho recomendado: llama.cpp com "Managed local server"; Ollama e LM Studio como alternativas.
- Ollama: `baseUrl` sem `/v1`.
- Modelos locais exigem testes com tarefas reais e ferramentas restritas.

## Relacionados

- [[Diretório de provedores e como ler a lista]]
- [[Custo e escolha de modelo]]
- [[Confiança, permissões e riscos de agentes]]
- [[Provedores, referências de modelo e a CLI models]]

## Exercícios

1. Qual é o caminho recomendado para modelos locais pela documentação?
2. Por que não usar `/v1` na URL do Ollama?
3. Por que um modelo que responde a prompts curtos pode falhar em um turno de agente?
4. Que cuidado de segurança vale para modelos locais?
