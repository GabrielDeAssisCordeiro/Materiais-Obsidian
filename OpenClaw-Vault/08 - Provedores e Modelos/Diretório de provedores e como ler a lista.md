---
titulo: "Diretório de provedores e como ler a lista"
tags:
  - openclaw
  - conceito
  - provedores
tipo: conceito
aliases: ['Provider directory', 'Provedores suportados']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
  - "https://docs.openclaw.ai/concepts/features"
relacionados:
  - "[[Provedores, referências de modelo e a CLI models]]"
  - "[[Modelos locais - Ollama e llama.cpp]]"
  - "[[Custo e escolha de modelo]]"
  - "[[Pontos de extensão - plugins, skills e hooks]]"
---

# Diretório de provedores e como ler a lista

## Objetivo

Saber onde está a lista oficial de provedores, como ela é organizada e quais famílias existem.

## Explicação

A página de recursos diz que o **diretório de provedores** na documentação é a lista mantida; qualquer lista em livro ou blog envelhece. A navegação da documentação (lida em 27/10/2026) agrupa os provedores assim:

| Grupo | Exemplos listados |
|---|---|
| Modelos de chat e código | Anthropic, OpenAI, Google (Gemini), Mistral, DeepSeek, Groq, xAI, Amazon Bedrock, GitHub Copilot, Hugging Face, Together AI, Venice AI, Z.AI, Moonshot AI, Qwen, MiniMax e muitos outros |
| Gateways e roteadores | OpenRouter, LiteLLM, Cloudflare AI Gateway, Vercel AI Gateway, Kilo Gateway, Bifrost, ClawRouter e outros |
| Runtimes locais | Ollama, LM Studio, vLLM, SGLang, llama.cpp (plugin), oMLX e outros |
| Voz e áudio | Deepgram, ElevenLabs, Azure Speech e outros |
| Imagem, vídeo e música | ComfyUI, Fal, Runway e outros |

Além das chaves de API, a documentação de recursos cita **login por assinatura via OAuth** (por exemplo, OpenAI Codex) e **backends personalizados ou autohospedados**, incluindo endpoints compatíveis com OpenAI e com Anthropic. A página de provedores da Anthropic também descreve o reaproveitamento de um login do Claude Code (veja [[Anthropic - chave de API, Claude CLI e setup-token]]).

**Provedores via plugin.** Muitos provedores são plugins oficiais. A seção de SDK de plugins inclui um guia para construir plugins de provedor, com catálogos de modelos e ganchos de runtime, o que explica a lista longa.

> [!tip] Como avaliar um provedor
> Pergunte: (1) o provedor retém ou treina com meus dados? (2) qual a política de preço e limites? (3) o modelo suporta chamada de ferramentas de forma confiável? (4) onde ficam as credenciais? Nenhuma dessas respostas vem do OpenClaw: vêm do provedor.

## Exemplo prático

Para descobrir o que a **sua** instalação enxerga, use a CLI em vez da memória:

```bash
openclaw models list
openclaw plugins list
```

Anote os provedores disponíveis e remova da configuração os que você não usa.

## Armadilhas comuns

- Confiar em uma lista de provedores de terceiros.
- Escolher um agregador (roteador) sem entender que ele vira mais um intermediário dos seus dados.
- Usar um provedor sem verificar o que ele faz com os prompts e arquivos enviados.

## Resumo

- A lista oficial está no diretório de provedores da documentação.
- Famílias: chat e código, gateways e roteadores, locais, voz e mídia.
- Há chaves de API, OAuth por assinatura e backends compatíveis.

## Relacionados

- [[Provedores, referências de modelo e a CLI models]]
- [[Modelos locais - Ollama e llama.cpp]]
- [[Custo e escolha de modelo]]
- [[Pontos de extensão - plugins, skills e hooks]]

## Exercícios

1. Onde está a lista oficial de provedores e por que não confiar em listas de terceiros?
2. Cite três famílias de provedores.
3. O que é um gateway ou roteador de modelos e que risco adicional ele traz?
4. Que comando mostra os modelos que a sua instalação enxerga?
