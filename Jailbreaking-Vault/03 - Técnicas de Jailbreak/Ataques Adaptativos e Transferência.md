---
titulo: "Ataques Adaptativos e Transferência"
tags:
  - ai-security
  - jailbreak
  - tecnica
nivel: "avancado"
---

# Ataques Adaptativos e Transferência

Pré-requisitos: [[Ataques Diretos]] · [[Obfuscação e Codificação]] · [[Jailbreak Multiturno]]

> [!warning] Nível de detalhe
> Esta nota explica **o princípio, os resultados publicados e como se defender e avaliar**. Não traz sufixos adversariais prontos nem código de otimização para uso contra modelos reais.

## 1. Definição

> [!info] Definições
> - **Ataque adaptativo:** o atacante **ajusta a entrada com base nas respostas** do alvo, de forma iterativa (manual ou automática), em vez de usar um texto fixo.
> - **Transferência** (*transferability*): propriedade de uma entrada otimizada contra um modelo continuar eficaz contra **outros** modelos.
> - **Avaliação adaptativa:** em segurança, defesas devem ser testadas contra atacantes que **conhecem a defesa** e se adaptam a ela; testar só contra ataques fixos superestima a robustez.

## 2. Fundamento técnico

Duas linhas de pesquisa:

**Otimização por gradiente/busca.** Zou et al. (2023) propuseram encontrar automaticamente um sufixo que, anexado a pedidos, maximiza a probabilidade de o modelo começar com uma resposta afirmativa em vez de recusar, usando busca gulosa e baseada em gradiente. Relataram que sufixos treinados em modelos abertos transferiram-se, em seus experimentos, para modelos fechados e abertos.

**Refinamento iterativo por LLM atacante.** Chao et al. (2023) propuseram o PAIR: um LLM atacante consulta o alvo, observa as respostas e refina candidatos de jailbreak, com apenas acesso de caixa-preta; segundo o artigo, frequentemente menos de vinte consultas bastaram nos seus testes, e as entradas geradas são semânticas (legíveis), inspiradas em engenharia social.

## 3. Mecanismo de funcionamento

```mermaid
flowchart LR
    A[Atacante<br/>humano ou LLM] -->|candidato| T[Alvo]
    T -->|resposta| J[Juiz / métrica de sucesso]
    J -->|feedback| A
    J -->|sucesso| R[Entrada eficaz]
    R -.testada em outros modelos.-> X[Transferência?]
```

Componentes de qualquer ataque adaptativo: **gerador de candidatos**, **acesso ao alvo** (pesos, probabilidades ou só respostas), **função de sucesso** e **orçamento** (nº de consultas, custo).

| Cenário | Acesso do atacante | Exemplo |
|---|---|---|
| Caixa-branca | Pesos e gradientes | Otimização de sufixos |
| Caixa-cinza | Probabilidades de tokens | Variações de busca |
| Caixa-preta | Só entradas e saídas | PAIR |

## 4. Pré-requisitos

Compreensão de ML e de avaliação; para laboratório, um alvo local ou autorizado e um orçamento definido. **Aqui se pratica o lado de avaliação**: construir o juiz, o orçamento e a medição.

## 5. Exemplo (alvo de brinquedo, lado avaliador)

> [!example] Experimento de adaptação com limite de orçamento
> Alvo: assistente da biblioteca com canário `ABACAXI-42` ([[Ataques Diretos]]).
>
> | ID | Estratégia | Medição |
> |---|---|---|
> | ADP-01 | 50 variações fixas escritas à mão | Taxa de sucesso e consultas até o 1º sucesso |
> | ADP-02 | Refinamento manual guiado pelas respostas anteriores | Consultas até o 1º sucesso |
> | ADP-03 | Mesmo experimento com **defesa ativa** (filtro de saída + reforço no prompt) | Redução da taxa; consultas até o 1º sucesso |
> | ADP-04 | Reaplicar as melhores entradas de ADP-02 em **outro modelo** | Taxa de transferência |

A função de sucesso é objetiva: o canário aparece na saída (verificação por código, não por opinião).

## 6. Análise do resultado esperado

- Entradas fixas costumam ter taxa baixa; adaptação aumenta a taxa **dentro do orçamento**.
- Defesas fracas "caem" quando o atacante se adapta; defesas estruturais (o segredo não está no contexto, autorização externa) **não** dependem de o modelo resistir.
- Transferência é **parcial e variável**; reporte como taxa, não como fato.

## 7. Motivos pelos quais a técnica pode falhar

- Entradas otimizadas contra um modelo específico perdem eficácia em outro (**sobreajuste**).
- Entradas com aparência anômala (texto de alta perplexidade) são detectáveis por filtros: Jain et al. (2023) avaliam detecção por perplexidade, pré-processamento (paráfrase, retokenização) e treinamento adversarial, e discutem que o custo e a fraqueza dos otimizadores discretos de texto tornam ataques adaptativos mais difíceis em LLMs do que em visão computacional, uma conclusão sobre aquele estado da arte.
- Defesa por perturbação: SmoothLLM (Robey et al.) perturba cópias da entrada e agrega as respostas, com base na observação de que prompts adversariais gerados são frágeis a mudanças de caracteres, e reporta robustez inclusive contra GCG adaptativo, com pequeno custo de desempenho.
- Orçamento de consultas limitado por *rate limit* ou monitoramento.

## 8. Limitações e variáveis

Qualidade do juiz (falsos positivos), orçamento, acesso ao alvo, diferença entre modelos, aleatoriedade, atualização do alvo durante o experimento. **Resultados de artigos refletem versões e datas específicas.**

## 9. Riscos associados

Escalabilidade: automação reduz o custo de achar falhas, para pesquisadores e para atacantes. Entradas que transferem podem afetar muitos sistemas simultaneamente.

## 10. Métodos de detecção

- Monitorar **volume e padrão de consultas** por conta (muitas variações semelhantes).
- Detectores de entrada anômala (perplexidade, estrutura).
- Alertas em sequências de tentativas com refinamento progressivo.

## 11. Estratégias de mitigação

- **Defesa em camadas** com controles determinísticos ([[Defesa em Camadas]]).
- *Rate limiting*, detecção de abuso e bloqueio de contas.
- Pré-processamento e perturbação de entrada, avaliados quanto ao custo em utilidade.
- Red teaming adaptativo contínuo e reteste após cada mudança ([[Metodologia de Testes]]).
- Treinamento adversarial pelo desenvolvedor do modelo.

## 12. Exercícios práticos

- [ ] Implemente o juiz automático por canário e execute ADP-01 a ADP-04 com orçamento fixo.
- [ ] Compare a taxa de sucesso com e sem defesa e discuta se um atacante que conhece a defesa mudaria o resultado.
- [ ] Mapeie o experimento para o [[Laboratório 05 - Avaliação Comparativa]].

## 13. Referências

- Zou, A.; Wang, Z.; Carlini, N.; Nasr, M.; Kolter, J. Z.; Fredrikson, M. **Universal and Transferable Adversarial Attacks on Aligned Language Models**. arXiv:2307.15043, 27/07/2023 (v2: 20/12/2023). <https://arxiv.org/abs/2307.15043> — consultado em 15/10/2026.
- Chao, P.; Robey, A.; Dobriban, E.; Hassani, H.; Pappas, G. J.; Wong, E. **Jailbreaking Black Box Large Language Models in Twenty Queries**. arXiv:2310.08419, 12/10/2023 (v4: 18/07/2024). <https://arxiv.org/abs/2310.08419> — consultado em 15/10/2026.
- Jain, N. et al. **Baseline Defenses for Adversarial Attacks Against Aligned Language Models**. arXiv:2309.00614, 01/09/2023. <https://arxiv.org/abs/2309.00614> — consultado em 15/10/2026.
- Robey, A.; Wong, E.; Hassani, H.; Pappas, G. J. **SmoothLLM**. arXiv:2310.03684, 05/10/2023 (v4: 11/06/2024). <https://arxiv.org/abs/2310.03684> — consultado em 15/10/2026.

> [!note] Status do conhecimento
> **Documentado em pesquisa (2023–2024)**; corrida contínua entre ataques e defesas. Trate qualquer número como retrato de uma data.

## Próximos passos
- Módulo 4: [[Conceitos Fundamentais]]
