---
titulo: "MOC - Automação e Orquestração"
aliases: ["MOC Automação"]
tags:
  - integracao-seguranca
  - moc
  - automacao
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[Playbooks e Runbooks]]"
  - "[[MOC - DevSecOps e CI-CD]]"
---

# MOC - Automação e Orquestração

## Resumo

Automação e orquestração da resposta: playbooks, plataformas SOAR, enriquecimento, aprovação humana e métricas. Volte à [[Home - Integração]].

## Conceitos-chave

Playbook, orquestração, blast radius, HITL e MTTD/MTTR.

## Como funciona

Documente, execute manualmente, meça e então automatize.

## Notas

- [[Playbooks e Runbooks]] — Runbooks e playbooks versionados.
- [[SOAR - Shuffle TheHive Cortex e n8n]] — Shuffle, TheHive/Cortex e n8n.
- [[Automação de Resposta a Incidentes]] — Contenção automatizada com salvaguardas.
- [[Enriquecimento de Alertas e Escalonamento]] — Contexto, pontuação e escalonamento.
- [[Human-in-the-Loop]] — Níveis de autonomia e aprovação humana.
- [[Métricas - MTTD e MTTR]] — MTTD, MTTA, MTTR e boas práticas de medição.

## Exemplo prático

Um alerta do SIEM aciona um [[Playbooks e Runbooks]], é enriquecido ([[Enriquecimento de Alertas e Escalonamento]]) e depende de aprovação ([[Human-in-the-Loop]]) antes da contenção.

## Boas práticas

Automatize o reversível; aprove o arriscado.

## Erros comuns

Automação sem auditoria nem rollback.

## Referências para aprofundar

- [[Ferramentas de Detecção e Resposta - EDR SIEM SOAR]]

## Veja também

- [[Home - Integração]]
- [[MOC - DevSecOps e CI-CD]]
- [[MOC - Observabilidade e Detecção]]
