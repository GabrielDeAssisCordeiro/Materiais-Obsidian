---
titulo: "Flashcards - 07 Automação e Orquestração"
aliases: ["Flashcards 07"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Playbooks e Runbooks]]"
  - "[[SOAR - Shuffle TheHive Cortex e n8n]]"
  - "[[Human-in-the-Loop]]"
---

# Flashcards - 07 Automação e Orquestração

## Resumo

Cartões de revisão do módulo **Automação e Orquestração**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Playbooks e Runbooks]], [[SOAR - Shuffle TheHive Cortex e n8n]], [[Human-in-the-Loop]], [[Métricas - MTTD e MTTR]].

## Como funciona

Instale o plugin Spaced Repetition e use *Review flashcards*. O algoritmo agenda a próxima revisão conforme sua avaliação (fácil, bom, difícil).

## Exemplo prático

Responda mentalmente antes de virar o cartão. Se errar, releia a nota de origem e reformule o cartão com suas palavras.

## Boas práticas

- Revise um pouco todos os dias.
- Crie cartões próprios para pontos que você errou.
- Mantenha respostas curtas.

## Erros comuns

- Decorar sem entender a razão.
- Acumular revisões atrasadas.
- Cartões longos demais.

## Referências para aprofundar

Plugin Spaced Repetition para Obsidian.

## Flashcards

#flashcards

Qual a diferença entre runbook e playbook?::Runbook é um procedimento operacional; playbook é um runbook orientado a um cenário de segurança.
Qual a regra de ouro da automação de resposta?::Automatizar o que é rápido e reversível; exigir aprovação para o arriscado ou irreversível.
O que é blast radius?::O alcance do impacto de uma ação; deve ser limitado.
O que é human-in-the-loop?::Manter uma pessoa na decisão de ações automatizadas relevantes.
O que fazer quando ninguém aprova em tempo hábil?::Não executar a ação destrutiva e escalar a outro aprovador.
O que mede o MTTD?::O tempo médio entre o início do incidente e sua detecção.
Por que definir qual variante de MTTR se usa?::Pode significar respond, resolve, recover ou repair.
Por que preferir a mediana à média nas métricas?::A média é sensível a outliers.
Como se diferenciam Shuffle, TheHive/Cortex e n8n?::Shuffle é um SOAR open source; TheHive gere casos e Cortex executa analyzers; n8n automatiza workflows gerais.
O que é enriquecimento de alertas?::Anexar contexto, como reputação, dono e criticidade, para apoiar a decisão.
Por que a pontuação de prioridade deve ser explicável?::Para que o analista entenda os motivos e confie e ajuste o modelo.

## Veja também

- [[Playbooks e Runbooks]]
- [[SOAR - Shuffle TheHive Cortex e n8n]]
- [[Human-in-the-Loop]]
- [[Métricas - MTTD e MTTR]]
- [[MOC - Revisão - Integração]]

#flashcards #seguranca/revisao/flashcards
