---
titulo: "MOC - Observabilidade e Detecção"
aliases: ["MOC Observabilidade"]
tags:
  - integracao-seguranca
  - moc
  - deteccao
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[Logging Estruturado]]"
  - "[[MOC - Automação e Orquestração]]"
---

# MOC - Observabilidade e Detecção

## Resumo

Telemetria e engenharia de detecção: logs, métricas, traces e regras como código. Volte à [[Home - Integração]].

## Conceitos-chave

Observabilidade, regras portáteis, detecção como código e redução de ruído.

## Como funciona

Primeiro a telemetria, depois as regras, depois testes e tuning.

## Notas

- [[Logging Estruturado]] — Logs em JSON, correlation ID e esquema comum.
- [[Métricas e Tracing - Prometheus e OpenTelemetry]] — Prometheus e OpenTelemetry para saúde da integração.
- [[Regras Sigma]] — Regras de detecção portáteis para logs.
- [[YARA - Integração]] — Padrões para identificar arquivos e memória.
- [[Suricata - Integração]] — IDS/IPS de rede e eve.json.
- [[Detecção como Código]] — Ciclo de vida de regras com git e CI/CD.
- [[Testes de Regras de Detecção]] — Unitários, backtesting e emulação.
- [[Redução de Falsos Positivos]] — Tuning sem criar pontos cegos.

## Exemplo prático

Uma regra Sigma ([[Regras Sigma]]) entra por PR, é testada ([[Testes de Regras de Detecção]]) e implantada pelo pipeline ([[Detecção como Código]]).

## Boas práticas

Teste cada regra e meça sua precisão.

## Erros comuns

Regras sem dono e sem testes.

## Referências para aprofundar

- [[MITRE ATT&CK - Integração]]

## Veja também

- [[Home - Integração]]
- [[MOC - Automação e Orquestração]]
- [[MOC - Segurança da Própria Ferramenta]]
