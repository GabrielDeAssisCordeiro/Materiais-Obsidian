---
titulo: "Flashcards - 08 Observabilidade e Detecção"
aliases: ["Flashcards 08"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - revisao
  - flashcards
tipo: revisao
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Logging Estruturado]]"
  - "[[Regras Sigma]]"
  - "[[Detecção como Código]]"
---

# Flashcards - 08 Observabilidade e Detecção

## Resumo

Cartões de revisão do módulo **Observabilidade e Detecção**, no formato `pergunta::resposta` compatível com o plugin Spaced Repetition.

## Conceitos-chave

- Cada linha da seção *Flashcards* é um cartão.
- A tag `#flashcards` marca a nota para o plugin.
- Conteúdo-fonte: [[Logging Estruturado]], [[Regras Sigma]], [[Detecção como Código]], [[Redução de Falsos Positivos]].

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

O que é Sigma?::Formato YAML genérico de regras para logs, convertido para SIEMs por backends.
O que é YARA?::Linguagem para identificar arquivos ou memória por strings e condições.
O que é Suricata?::Motor de IDS, IPS e NSM de rede cuja saída estruturada é o eve.json.
Qual a faixa recomendada de sid para regras locais do Suricata?::1000000 ou superior.
O que é Detection as Code?::Tratar regras como código: versionadas, revisadas, testadas e implantadas por pipeline.
Como testar uma regra de detecção?::Com eventos positivos e negativos, backtesting e emulação em laboratório.
O que é alert fatigue?::Desgaste por excesso de alertas, que leva a ignorá-los.
Como deve ser uma boa allowlist?::Específica, com dono, justificativa e validade.
Quais são os golden signals?::Latência, tráfego, erros e saturação.
Por que evitar rótulos de alta cardinalidade em métricas?::Valores ilimitados explodem memória e custo.
Para que serve o correlation ID?::Ligar todos os logs de uma mesma operação ou requisição.

## Veja também

- [[Logging Estruturado]]
- [[Regras Sigma]]
- [[Detecção como Código]]
- [[Redução de Falsos Positivos]]
- [[MOC - Revisão - Integração]]

#flashcards #seguranca/revisao/flashcards
