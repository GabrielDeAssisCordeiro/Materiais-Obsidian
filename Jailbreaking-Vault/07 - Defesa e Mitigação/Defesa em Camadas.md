---
titulo: "Defesa em Camadas"
tags:
  - ai-security
  - defesa
  - arquitetura
  - guardrails
nivel: "intermediario"
---

# Defesa em Camadas

Voltar ao [[00 - Índice Jailbreaking]] · Prática: [[Laboratório 04 - Defesa em Camadas]] · Pré-requisitos: [[Taxonomia de Ataques]], [[Conceitos Fundamentais]], [[Alinhamento e Guardrails]]

## 1. Definição

> [!info] Definição
> **Defesa em camadas** (*defense in depth*) é projetar o sistema de modo que **nenhum controle isolado** decida o resultado de segurança: cada camada cobre um tipo de falha, e a falha de uma não derruba as outras. Em sistemas com LLM, a regra se agrava porque as camadas mais visíveis (treinamento, prompt) são **probabilísticas**, e só as camadas feitas de **código e arquitetura** dão garantia.

## 2. Contexto

A literatura converge numa conclusão incômoda: não há, até onde os trabalhos revisados aqui mostram, uma defesa de modelo que elimine o problema.

- Wallace et al. (2024) propõem treinar o modelo para seguir uma **hierarquia de instruções** e relatam ganho de robustez, inclusive contra ataques não vistos no treinamento, mas **com GPT-3.5** e como redução, não eliminação.
- Hines et al. (2024) propõem o *spotlighting* e relatam queda da taxa de sucesso de ataque de mais de 50% para menos de 2% **nos seus experimentos** com modelos da família GPT.
- Chen et al. (2024) propõem separar prompt e dados em dois canais (*structured queries*) com modelo treinado para isso.
- Jain et al. (2023) avaliam defesas-base (detecção por perplexidade, paráfrase, retokenização, treinamento adversarial) e discutem o **trade-off entre robustez e desempenho**.
- Liu et al. (2024) formalizam ataques de prompt injection e fazem um *benchmark* de 5 ataques e 10 defesas em 10 modelos e 7 tarefas.
- Debenedetti et al. (2025), com o CaMeL, mudam a abordagem: criam uma camada de sistema **em volta** do modelo, de modo que dados não confiáveis não alterem o fluxo de controle, e relatam resolver 77% das tarefas do AgentDojo com segurança comprovável, contra 84% do sistema sem defesa. **Segurança tem custo de utilidade, e esse custo foi medido.**

## 3. As camadas

```mermaid
flowchart TB
    U[Usuário / conteúdo externo] --> E[1. Entrada<br/>limites, normalização,<br/>delimitação, sanitização]
    E --> C[2. Contexto<br/>mínimo necessário,<br/>sem segredos, proveniência]
    C --> M[3. Modelo<br/>hierarquia, prompt claro,<br/>treinamento de segurança]
    M --> S[4. Saída<br/>contrato, filtros,<br/>classificadores]
    M --> F[5. Ferramentas<br/>política, autorização,<br/>confirmação, sandbox]
    S --> R[Resposta]
    F --> A[Ação]
    O[6. Operação<br/>logs, alertas, resposta,<br/>reteste] -.observa.-> E & M & S & F
```

| Camada | Exemplo de controle | Natureza | Cobre bem | Não cobre |
|---|---|---|---|---|
| **1. Entrada** | Limite de tamanho, normalização Unicode, remoção de marcas forjadas, delimitação | Determinística (a parte de código) | Entradas malformadas, marcas forjadas | Conteúdo semanticamente malicioso |
| **2. Contexto** | Segredos fora do prompt, dados mínimos, rótulo de proveniência | Determinística (arquitetura) | **Vazamento do que nunca esteve no contexto** | O que o usuário legitimamente pode ver |
| **3. Modelo** | Hierarquia de instruções, prompt reforçado, treinamento | **Probabilística** | Maioria dos casos comuns | Cauda da distribuição; ataques novos |
| **4. Saída** | Contrato validado por código, filtro normalizado, classificador | Determinística (contrato) / probabilística (classificador) | Formato, canais de exfiltração, segredos conhecidos | Sequestro semântico dentro do formato; segredos codificados de formas imprevistas |
| **5. Ferramentas** | Política por código, listas de permissão, confirmação com ação real, isolamento | **Determinística** | Ação indevida, destinatário indevido | O que o usuário aprova sem ler |
| **6. Operação** | Logs, alertas, resposta a incidentes, regressão | Detecção, não prevenção | Aprender e limitar dano | Impedir o primeiro incidente |

## 4. Ordem de prioridade (da maior garantia para a menor)

> [!important] Regra de projeto
> Gaste esforço **de cima para baixo** nesta lista. Cada item só substitui o seguinte se for realmente aplicável.

1. **Remover o que pode vazar.** Segredo que não está no contexto não pode ser emitido por nenhum jailbreak. Dados fora do alcance do modelo não podem ser exfiltrados por ele.
2. **Autorização fora do modelo.** Quem pode ver o quê é decidido por código no backend, com a identidade do usuário, nunca por pedido ao modelo.
3. **Menor privilégio e política de ferramentas** ([[Segurança de Agentes]]).
4. **Contrato de saída** validado por código ([[Validação de Entradas e Saídas]]).
5. **Filtros e classificadores** (probabilísticos, com falsos positivos e negativos).
6. **Reforço do modelo e do prompt** (hierarquia, delimitação, instruções claras).
7. **Monitoramento e resposta** ([[Monitoramento e Resposta]]): não previne, mas limita o dano e alimenta o reteste.

## 5. Evidência do laboratório (backend **simulado**)

> [!danger] Estes números vêm do backend `mock` do kit
> O `mock` é um **modelo simulado**: as probabilidades dentro dele foram escolhidas pelo autor do kit. Os números abaixo servem para **ver o formato de uma análise camada a camada**, e não dizem nada sobre modelos reais. Para medir de verdade, rode o [[Laboratório 04 - Defesa em Camadas]] com o **seu** modelo.

Varredura L0 a L7 (15 casos, n = 30 por caso; ASR agregado sobre 12 casos de ataque × 30 = 360 execuções; utilidade sobre 3 controles × 30 = 90):

| Config | Camada acrescentada | ASR modelo | ASR sistema | Utilidade |
|---|---|---|---|---|
| L0 | linha de base | 40,8% | 40,8% | 98,9% |
| L1 | prompt reforçado | 22,2% | 22,2% | 100% |
| L2 | delimitação | 9,7% | 9,7% | 100% |
| L3 | sanitização de marcas forjadas | 8,1% | 8,1% | 100% |
| L4 | filtro de saída **exato** | 8,1% | 6,7% | 100% |
| L5 | filtro **normalizado** | 8,1% | 4,7% | 100% |
| L6 | política que **nega** ferramentas após conteúdo externo | 8,1% | 3,1% | **66,7%** |
| L7 | confirmação humana simulada (vê a ação real) | 8,1% | 3,1% | 100% |

Leituras corretas:

- **As colunas "modelo" e "sistema" separam o que cada camada faz.** Depois de L3 o ASR do modelo para de cair (8,1%); L4 a L7 reduzem só o do **sistema**. Isso é a distinção entre melhorar o modelo e **cercar** o modelo.
- **L6 compra segurança com utilidade:** a utilidade cai a 66,7%, porque a política nega até ações legítimas pedidas pelo usuário. **L7 recupera** a utilidade (100%) pedindo confirmação. Mas, no kit, o "humano" é simulado e aprova só o que o usuário pediu; humanos reais erram, sobretudo quando aprovam demais ([[Ataques Contra Agentes de IA]]).
- **Sobra risco residual em L7:** 11/360 = 3,1%. Os logs mostram duas fontes: **INJ-02** (sequestro da tarefa do tradutor em saída de texto: 2/30) e **OBF-03** (segredo fragmentado: 9/30). Nenhuma camada acima cobre esses dois casos. Um **contrato de saída** cobriria o primeiro; remover o segredo do contexto cobriria o segundo.

Experimento do filtro de saída (apenas OBF-01 a OBF-03, n = 100 por caso; ASR do sistema):

| Config | OBF-01 | OBF-02 | OBF-03 | Agregado |
|---|---|---|---|---|
| L3 (sem filtro) | 16/100 | 6/100 | 20/100 | 42/300 = 14,0% |
| L4 (filtro **exato**) | 16/100 | 6/100 | 20/100 | 42/300 = 14,0% |
| L5 (filtro **normalizado**) | **0/100** | 6/100 | 20/100 | 26/300 = 8,7% |

O filtro por string exata **não mudou nada** contra segredos com separadores; o normalizado zerou o OBF-01, mas **OBF-02 e OBF-03 continuam passando**. O filtro tem pontos cegos, e cada novo filtro cria novos.

> [!tip] "0/100" não é "abaixo de 3%"
> Com zero falhas em 100 execuções, o limite superior do IC95% de Wilson é 3,7%. Para afirmar "abaixo de 3%" com zero falhas são necessárias **≥ 125** execuções ([[Métricas e Critérios de Sucesso]]). O portão de regressão em `codigo/gate_regressao.py` aplica exatamente essa regra.

## 6. Camadas não são independentes

Somar camadas **não multiplica** a proteção quando as falhas são **correlacionadas**:

| Causa de correlação | Efeito |
|---|---|
| Mesmo modelo no assistente e no classificador | Pontos cegos parecidos |
| Mesma distribuição de treino | Cobertura igualmente ausente em idiomas ou formatos raros |
| Filtro e juiz com a mesma regra | O ponto cego fica invisível na medição |
| Camada que assume que a anterior funcionou | Falha em cascata (ex.: confirmar sem checar origem) |

Por isso se mede **cada camada isoladamente e em conjunto** ([[Laboratório 04 - Defesa em Camadas]]) e se mantém ao menos uma camada **de natureza diferente** (código determinístico) cobrindo o dano mais grave.

## 7. Atacante que conhece a defesa

Defesas avaliadas só contra ataques fixos superestimam a robustez. Jain et al. (2023) discutem que o custo e a fraqueza dos otimizadores discretos de texto tornavam ataques adaptativos mais difíceis em LLMs do que em visão computacional **naquele estado da arte**; é uma observação datada, e não uma garantia. A prática correta é incluir **avaliação adaptativa** ([[Ataques Adaptativos e Transferência]]) e priorizar defesas cujo efeito **não depende** de o modelo resistir.

## 8. Exemplo de arquitetura (alvo de brinquedo)

Assistente de e-mails fictício com ferramentas simuladas:

```mermaid
flowchart LR
    X[E-mail externo] -->|rotulado como<br/>não confiável| P[Preparo<br/>sanitiza e delimita]
    P --> M[Modelo<br/>sem segredos]
    M -->|TOOL_CALL| G[Política por código<br/>Sessao.contaminada?]
    G -->|leitura| OK[Executa]
    G -->|efeito externo| H{{Humano vê<br/>ação real}}
    H -->|aprova| OK
    H -->|nega| N[Bloqueia + log]
    M -->|texto| V[Contrato de saída]
    V -->|cumpre| R[Resposta]
    V -->|não cumpre| N
    N --> L[(Logs e alertas)]
```

Código de referência (testado): `codigo/politica_ferramentas.py`, `codigo/contrato_saida.py` e `codigo/alertas.py`.

## 9. Custos e armadilhas

| Camada | Custo típico | Armadilha |
|---|---|---|
| Classificador de entrada/saída | Latência, custo por chamada, falsos positivos | Tratá-lo como garantia |
| Política de ferramentas | Perda de utilidade (L6) | Políticas tão frouxas que nunca bloqueiam |
| Confirmação humana | Atrito, **fadiga de aprovação** | Mostrar resumo do modelo em vez da ação real |
| Reforço de prompt | Manutenção, regressões entre versões | Achar que "funcionou" por um teste |
| Filtro por string | Falsa sensação de cobertura | Não normalizar |

## 10. Como projetar, em sete passos

1. **Modelo de ameaças:** fontes de texto, dados, ações, usuários ([[Planejamento de Avaliações]]).
2. **Triângulo de risco** de cada fluxo ([[Conceitos Fundamentais]]).
3. **Eliminar** o que pode ser eliminado (segredos, dados, privilégios).
4. **Camadas determinísticas** para o dano mais grave.
5. **Camadas probabilísticas** para reduzir a frequência do restante.
6. **Medir** camada a camada, com controles de utilidade ([[Métricas e Critérios de Sucesso]]).
7. **Monitorar e retestar** a cada mudança ([[Monitoramento e Resposta]]).

## 11. Limitações desta nota

- Os números do laboratório são do `mock`.
- Os resultados dos artigos refletem modelos, tarefas e datas específicos.
- A ordem de prioridade é uma recomendação de projeto do curso, não um padrão oficial.

## Exercício

- [ ] Para o seu alvo de brinquedo, preencha uma tabela "ameaça × camada que cobre × camada que **não** cobre".
- [ ] Rode `python3 -I gate_regressao.py` sobre os logs do seu Lab 04 e explique por que n = 30 não consegue **aprovar** nenhum caso com limite de 3%.
- [ ] Escreva o que você removeria **do contexto** do seu alvo para fechar o OBF-03 sem nenhum filtro novo.

## Referências

- Wallace, E.; Xiao, K.; Leike, R.; Weng, L.; Heidecke, J.; Beutel, A. **The Instruction Hierarchy**. arXiv:2404.13208, 19/04/2024. <https://arxiv.org/abs/2404.13208> — consultado em 15/10/2026.
- Hines, K. et al. **Defending Against Indirect Prompt Injection Attacks With Spotlighting**. arXiv:2403.14720, 20/03/2024. <https://arxiv.org/abs/2403.14720> — consultado em 15/10/2026.
- Chen, S.; Piet, J.; Sitawarin, C.; Wagner, D. **StruQ**. arXiv:2402.06363, 09/02/2024 (v2: 25/09/2024). <https://arxiv.org/abs/2402.06363> — consultado em 15/10/2026.
- Jain, N. et al. **Baseline Defenses for Adversarial Attacks Against Aligned Language Models**. arXiv:2309.00614, 01/09/2023. <https://arxiv.org/abs/2309.00614> — consultado em 15/10/2026.
- Liu, Y.; Jia, Y.; Geng, R.; Jia, J.; Gong, N. Z. **Formalizing and Benchmarking Prompt Injection Attacks and Defenses**. arXiv:2310.12815, 19/10/2023 (v3: 01/06/2024). <https://arxiv.org/abs/2310.12815> — consultado em 17/10/2026.
- Nesta nota, dos artigos foram lidos os **resumos** (*abstracts*); os textos completos não foram lidos, e por isso as afirmações se limitam ao que os resumos dizem.
- Debenedetti, E. et al. **Defeating Prompt Injections by Design**. arXiv:2503.18813, 24/03/2025 (v2: 24/06/2025). <https://arxiv.org/abs/2503.18813> — consultado em 15/10/2026.
- A ideia de defesa em profundidade e a priorização por garantia são princípios clássicos de engenharia de segurança, sem fonte única citada aqui.

## Conceitos relacionados
[[Validação de Entradas e Saídas]] · [[Segurança de Agentes]] · [[Monitoramento e Resposta]] · [[Alinhamento e Guardrails]]

## Próximos passos
- [[Validação de Entradas e Saídas]]
