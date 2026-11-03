---
titulo: "Artigos Científicos"
tags:
  - ai-security
  - referencia
  - pesquisa
nivel: "intermediario"
---

# Artigos Científicos

Consolidação das referências citadas nos módulos 1–7, agrupadas por tema. Cada referência foi conferida na página do arXiv (resumo) e consultada em 15/10/2026, salvo indicação. A coluna *Nota* lista as notas do curso que a citam.

> [!warning] Limites da verificação
> - Para vários artigos li **apenas o resumo**; as notas dos módulos só afirmam o que o resumo sustenta.
> - Números de sucesso de ataque são **retratos do modelo e da data do artigo**; não valem para modelos atuais.
> - Do artigo de *Design Patterns* o texto completo não pôde ser lido; confira os nomes dos padrões antes de citá-los.
> - *Many-shot jailbreaking* e *Constitutional Classifiers* (Anthropic) **não foram verificados**; não estão citados.

## Fundamentos e alinhamento

| Artigo | Ref. | Nota |
|---|---|---|
| Vaswani et al. **Attention Is All You Need** (2017) | arXiv:1706.03762 | [[Como funcionam os LLMs]] |
| Sennrich, Haddow, Birch. **Neural Machine Translation of Rare Words with Subword Units** (2015) | arXiv:1508.07909 | [[Tokens e Contexto]] |
| Ouyang et al. **Training language models to follow instructions with human feedback** (2022) | arXiv:2203.02155 | [[Alinhamento e Guardrails]] |
| Bai et al. **Constitutional AI: Harmlessness from AI Feedback** (2022) | arXiv:2212.08073 | [[Alinhamento e Guardrails]] |
| Wallace et al. **The Instruction Hierarchy** (2024) | arXiv:2404.13208 | [[System Prompt e Hierarquia de Instruções]] · [[Defesa em Camadas]] |

## Jailbreak

| Artigo | Ref. | Nota |
|---|---|---|
| Wei, Haghtalab, Steinhardt. **Jailbroken: How Does LLM Safety Training Fail?** (2023) | arXiv:2307.02483 | [[Taxonomia de Ataques]] · [[Obfuscação e Codificação]] |
| Shen et al. **"Do Anything Now"** (2023) | arXiv:2308.03825 | [[Roleplay e Personificação]] |
| Zou et al. **Universal and Transferable Adversarial Attacks on Aligned Language Models** (2023) | arXiv:2307.15043 | [[Ataques Adaptativos e Transferência]] · [[O que é AI Jailbreaking]] |
| Chao et al. **Jailbreaking Black Box LLMs in Twenty Queries** (2023) | arXiv:2310.08419 | [[Ataques Adaptativos e Transferência]] |
| Russinovich, Salem, Eldan. **Crescendo** (2024) | arXiv:2404.01833 | [[Jailbreak Multiturno]] |
| Yong, Menghini, Bach. **Low-Resource Languages Jailbreak GPT-4** (2023) | arXiv:2310.02446 | [[Ataques Multilíngues]] |
| Deng et al. **Multilingual Jailbreak Challenges in LLMs** (2023) | arXiv:2310.06474 | [[Ataques Multilíngues]] |
| Qi et al. **Visual Adversarial Examples Jailbreak Aligned LLMs** (2023) | arXiv:2306.13213 | [[Jailbreak Multimodal]] |

## Prompt injection e agentes

| Artigo | Ref. | Nota |
|---|---|---|
| Perez, Ribeiro. **Ignore Previous Prompt** (2022) | arXiv:2211.09527 | [[Injeção Direta]] · [[Ataques Diretos]] |
| Greshake et al. **Not what you've signed up for** (2023) | arXiv:2302.12173 | [[Injeção Indireta]] |
| Liu et al. **Formalizing and Benchmarking Prompt Injection Attacks and Defenses** (2023) | arXiv:2310.12815 (consultado em 17/10/2026) | [[Defesa em Camadas]] |
| Zhan et al. **InjecAgent** (2024) | arXiv:2403.02691 | [[Ataques Contra Agentes de IA]] |
| Debenedetti et al. **AgentDojo** (2024) | arXiv:2406.13352 | [[Ataques Contra Agentes de IA]] |

## Defesa

| Artigo | Ref. | Nota |
|---|---|---|
| Jain et al. **Baseline Defenses for Adversarial Attacks Against Aligned LLMs** (2023) | arXiv:2309.00614 | [[Obfuscação e Codificação]] |
| Robey et al. **SmoothLLM** (2023) | arXiv:2310.03684 | [[Obfuscação e Codificação]] |
| Chen et al. **StruQ** (2024) | arXiv:2402.06363 | [[Conceitos Fundamentais]] |
| Hines et al. **Spotlighting** (2024) | arXiv:2403.14720 | [[Conceitos Fundamentais]] |
| Debenedetti et al. **Defeating Prompt Injections by Design (CaMeL)** (2025) | arXiv:2503.18813 | [[Segurança de Agentes]] |
| Beurer-Kellner et al. **Design Patterns for Securing LLM Agents against Prompt Injections** (2025) | arXiv:2506.08837 | [[Segurança de Agentes]] |
| Inan et al. **Llama Guard** (2023) | arXiv:2312.06674 | [[Validação de Entradas e Saídas]] |
| Rebedea et al. **NeMo Guardrails** (2023) | arXiv:2310.10501 | [[Validação de Entradas e Saídas]] |

## Avaliação e red teaming

| Artigo | Ref. | Nota |
|---|---|---|
| Perez et al. **Red Teaming Language Models with Language Models** (2022) | arXiv:2202.03286 | [[Metodologia de Testes]] |
| Ganguli et al. **Red Teaming Language Models to Reduce Harms** (2022) | arXiv:2209.07858 | [[Metodologia de Testes]] · [[Planejamento de Avaliações]] |
| Mazeika et al. **HarmBench** (2024) | arXiv:2402.04249 | [[Métricas e Critérios de Sucesso]] · [[Laboratório 05 - Avaliação Comparativa]] |
| Chao et al. **JailbreakBench** (2024) | arXiv:2404.01318 | [[Métricas e Critérios de Sucesso]] · [[Laboratório 05 - Avaliação Comparativa]] |
| Souly et al. **A StrongREJECT for Empty Jailbreaks** (2024) | arXiv:2402.10260 | [[Métricas e Critérios de Sucesso]] · [[Laboratório 05 - Avaliação Comparativa]] |

Links: `https://arxiv.org/abs/<número>`.

## Como ler um artigo de segurança de LLM

1. **Ameaça:** que acesso o atacante tem (caixa-preta, pesos, só o prompt)?
2. **Alvo:** que modelos e **versões**, em que data?
3. **Métrica:** como o "sucesso" foi julgado (humano, regra, outro modelo)? Veja [[Métricas e Critérios de Sucesso]].
4. **Repetições e intervalos:** há incerteza reportada?
5. **Generalização:** o resultado vale contra modelo atual ou defesa adaptativa?

## Exercício

- [ ] Escolha dois artigos, preencha as cinco perguntas e anote o que o resumo **não** responde.

> [!note] Status do conhecimento
> Lista **verificada na data indicada**; o campo muda rápido, atualize periodicamente.

## Próximos passos
- [[Glossário#Segurança de IA (jailbreaking e prompt injection)]]
