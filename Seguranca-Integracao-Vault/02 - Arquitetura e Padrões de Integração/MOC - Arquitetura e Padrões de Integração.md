---
titulo: "MOC - Arquitetura e Padrões de Integração"
aliases: []
tags:
  - integracao-seguranca
  - moc
  - arquitetura-de-integracao
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]]"
  - "[[MOC - Fundamentos - Integração]]"
---

# MOC - Arquitetura e Padrões de Integração

## Resumo

Padrões de arquitetura e confiabilidade para integrar ferramentas de segurança. Volte à [[Home - Integração]].

## Conceitos-chave

Acoplamento, assincronia, normalização, idempotência e resiliência.

## Como funciona

Leia na ordem; cada nota aponta para a próxima.

## Notas

- [[Padrões de Integração - Point-to-Point Hub-and-Spoke e Event-Driven]] — Estilos: point-to-point, hub-and-spoke e event-driven.
- [[Webhooks e Polling]] — Push vs. pull, assinatura e anti-replay.
- [[Filas e Streaming - Kafka e RabbitMQ]] — Brokers e logs distribuídos para desacoplar sistemas.
- [[Padrão Adapter e Connector]] — Interface estável e conectores por ferramenta.
- [[Normalização de Dados - OCSF ECS CEF STIX e TAXII]] — OCSF, ECS, CEF, STIX e TAXII.
- [[Idempotência]] — Projetar para duplicatas e reentregas.
- [[Retries com Backoff e Tratamento de Falhas]] — Backoff, jitter, circuit breaker e DLQ.
- [[Rate Limiting]] — Controle de taxa como cliente e provedor.

## Exemplo prático

Um webhook ([[Webhooks e Polling]]) alimenta uma fila ([[Filas e Streaming - Kafka e RabbitMQ]]) com consumidores idempotentes ([[Idempotência]]).

## Boas práticas

Projete para falhas desde o início.

## Erros comuns

Assumir entrega exatamente-uma-vez.

## Referências para aprofundar

- [[Panorama de Ferramentas de Segurança]]

## Veja também

- [[Home - Integração]]
- [[MOC - Fundamentos - Integração]]
- [[MOC - APIs e Autenticação]]
