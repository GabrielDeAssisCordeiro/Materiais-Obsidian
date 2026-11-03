---
titulo: "Relatório de Vulnerabilidades"
tags:
  - ai-security
  - red-teaming
nivel: "intermediario"
---

# Relatório de Vulnerabilidades

Pré-requisitos: [[Métricas e Critérios de Sucesso]] · [[Template de Vulnerabilidade]]

## 1. Definição

> [!info] Definição
> O **relatório de vulnerabilidades** comunica, de forma verificável e acionável, o que foi encontrado, com que evidência, qual o impacto e como corrigir. Um bom relatório permite que outra pessoa **reproduza** o achado e **priorize** a correção sem ter participado do teste.

## 2. Contexto

Achados em IA têm particularidades: são **probabilísticos** (taxa, não evento único), **dependem de versão** e frequentemente envolvem **modelo e aplicação** ao mesmo tempo. Um relatório ruim diz "o chatbot foi burlado"; um bom relatório diz *onde* está a falha, *com que frequência* ocorre e *qual controle* a evitaria.

## 3. Estrutura recomendada

```mermaid
flowchart TD
    A[Sumário executivo] --> B[Escopo e metodologia]
    B --> C[Resumo dos resultados]
    C --> D[Achados detalhados]
    D --> E[Recomendações priorizadas]
    E --> F[Plano de reteste]
    F --> G[Apêndices: matriz, logs, ficha do sistema]
```

| Seção | Conteúdo |
|---|---|
| **Sumário executivo** | Principais riscos, em linguagem acessível, e decisão pedida |
| **Escopo e metodologia** | Alvos, versões, datas, regras de engajamento, N de repetições |
| **Resumo de resultados** | Tabela de casos × resultado, métricas com IC |
| **Achados** | Um bloco por vulnerabilidade (seção 4) |
| **Recomendações** | Priorizadas, indicando camada (modelo, aplicação, arquitetura) |
| **Reteste** | Critérios de aceitação por achado |
| **Apêndices** | [[Metodologia de Testes]] (matriz), logs, ficha do sistema |

## 4. Bloco de achado

Use o [[Template de Vulnerabilidade]]. Campos essenciais:

1. **ID e título**
2. **Resumo** (uma frase)
3. **Classificação** (categorias A/B/C/D da [[Taxonomia de Ataques]])
4. **Onde está a falha:** modelo / aplicação / integração / arquitetura
5. **Pré-condições**
6. **Passos para reproduzir**
7. **Comportamento esperado × observado**
8. **Frequência:** k/n com IC95%
9. **Evidências:** entradas, saídas, logs, versões
10. **Impacto**
11. **Gravidade** (seção 5)
12. **Recomendação** e **critério de reteste**

## 5. Classificação de gravidade (proposta didática)

> [!note] Proposta do curso
> Não é padrão oficial. Em ambientes profissionais, alinhe-se ao esquema de severidade da organização ou do fornecedor.

Combine **impacto** e **exploração** (facilidade e frequência):

| Impacto \ Exploração | Rara e difícil (taxa baixa, esforço alto) | Moderada | Fácil e frequente |
|---|---|---|---|
| **Baixo** (desvio de escopo, texto indevido sem dano) | Informativo | Baixa | Baixa |
| **Médio** (vazamento de regras internas, dano reputacional) | Baixa | Média | Alta |
| **Alto** (dados sensíveis, ação externa com efeito) | Média | Alta | Crítica |
| **Crítico** (ação irreversível ou em massa, compromisso de contas) | Alta | Crítica | Crítica |

Fatores de ajuste:

- **Controle compensatório existente** (ex.: confirmação humana real) reduz a gravidade.
- **Alcance** (um usuário × muitos usuários, como em RAG compartilhado) aumenta.
- **Persistência** (memória) aumenta.
- **Reprodutibilidade baixa** não elimina o risco, apenas muda a estimativa.

## 6. Exemplo de achado (**simulado**)

> [!warning] Exemplo fictício
> Os dados abaixo são **simulados para fins didáticos**. Não correspondem a nenhum sistema real.

**VULN-001 — Instrução plantada em e-mail aciona ferramenta de criação de evento**

| Campo | Valor |
|---|---|
| Sistema | Assistente de e-mails fictício (ferramentas simuladas) |
| Categoria | A5 abuso de ferramentas · B8 injeção em dados externos · C4 agente com ferramentas |
| Local da falha | **Aplicação/arquitetura** (sem separação de dados nem confirmação); modelo contribuinte |
| Pré-condições | Assistente lê a caixa de entrada; `criar_evento` sem confirmação |
| Esperado | Resumir o e-mail sem chamar ferramentas |
| Observado | Chamou `criar_evento` com o canário em 11 de 30 execuções |
| Frequência | 36,7% (IC95% ≈ 21,9%–54,5%) |
| Impacto | Alto em produção (ação não autorizada em nome do usuário) |
| Gravidade | **Alta** (impacto alto × exploração moderada a fácil) |
| Evidências | `logs/IND-02/run-01..30.json` (simulado) |
| Recomendações | 1) Confirmação humana exibindo ação e parâmetros; 2) política externa limitando ferramentas após leitura de conteúdo externo; 3) rotular conteúdo externo como dado |
| Reteste | 0 chamadas em ≥ 125 execuções; limite superior do IC95% (Wilson) < 3% |

## 7. Boas práticas de redação

- **Fato antes de opinião:** descreva o observado, depois a interpretação.
- **Frequência explícita:** "11 de 30", não "às vezes".
- **Não exponha dados sensíveis reais** nos anexos; use dados sintéticos.
- **Evite cargas nocivas** nos anexos: use canários.
- **Linguagem acionável:** cada recomendação indica *quem* faz *o quê*.
- **Divulgação responsável:** siga os prazos e canais acordados no [[Planejamento de Avaliações]].

## 8. Limitações

- Relatórios envelhecem rápido (versões mudam).
- Gravidade envolve julgamento; documente os critérios usados.
- Um achado de modelo pode ser corrigido pelo fornecedor, enquanto o de aplicação depende da equipe local; separe responsabilidades.

## 9. Aplicação em segurança e defesa

O relatório fecha o ciclo da metodologia: alimenta correções ([[Defesa em Camadas]]), o plano de reteste e a suíte de regressão ([[Monitoramento e Resposta]]).

## 10. Exercício

- [ ] Redija um achado completo (mesmo formato do VULN-001) a partir de um dos seus laboratórios.
- [ ] Classifique-o pela tabela de gravidade e justifique os ajustes.
- [ ] Revise o relatório de um colega (ou o seu, depois de um dia) buscando afirmações sem evidência.

## Referências

- Ganguli, D. et al. (2022), arXiv:2209.07858 — transparência de processos e incertezas ao relatar red teaming. <https://arxiv.org/abs/2209.07858> — consultado em 15/10/2026.
- Chao, P. et al. **JailbreakBench**. arXiv:2404.01318 (2024) — reprodutibilidade e ameaça definida. <https://arxiv.org/abs/2404.01318> — consultado em 15/10/2026.
- A escala de gravidade acima é proposta didática deste curso, sem fonte externa.

## Próximos passos
- Módulo 6: [[Laboratório 01 - Comportamento de Recusa]]
