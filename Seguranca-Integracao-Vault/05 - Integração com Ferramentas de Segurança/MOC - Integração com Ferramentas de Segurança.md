---
titulo: "MOC - Integração com Ferramentas de Segurança"
aliases: ["MOC Integrações"]
tags:
  - integracao-seguranca
  - moc
  - integracoes
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[Integração com SIEM - Splunk Elastic e Wazuh]]"
  - "[[MOC - Desenvolvimento de Ferramentas]]"
---

# MOC - Integração com Ferramentas de Segurança

## Resumo

Integrações práticas com as principais ferramentas de segurança, cada uma com caso de uso, fluxo, código e armadilhas. Volte à [[Home - Integração]].

## Conceitos-chave

Ingestão, extração, normalização, deduplicação e enriquecimento.

## Como funciona

Cada nota segue o mesmo roteiro: caso de uso, fluxo de integração, exemplo e erros comuns.

## Notas

- [[Integração com SIEM - Splunk Elastic e Wazuh]] — Splunk, Elastic e Wazuh: ingestão e extração.
- [[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]] — Nessus, OpenVAS, Trivy e Nuclei.
- [[Integração com SAST e SCA - Semgrep SonarQube Dependabot e Snyk]] — Semgrep, SonarQube, Dependabot e Snyk.
- [[Integração com Gestão de Segredos - Vault e gitleaks]] — Vault para entregar e gitleaks para detectar segredos.
- [[Integração com Ticketing - Jira e GitHub Issues]] — Jira e GitHub Issues sem duplicatas.
- [[Integração com Mensageria - Slack e Teams]] — Slack e Teams: notificação e aprovação.
- [[Integração com Threat Intelligence - MISP OpenCTI e VirusTotal]] — MISP, OpenCTI e VirusTotal para enriquecimento.

## Exemplo prático

Um scanner ([[Integração com Scanners - Nessus OpenVAS Trivy e Nuclei]]) gera achados que viram tickets ([[Integração com Ticketing - Jira e GitHub Issues]]) e notificações ([[Integração com Mensageria - Slack e Teams]]).

## Boas práticas

Credenciais mínimas, idempotência e respeito a cotas.

## Erros comuns

Ignorar paginação, duplicar tickets e vazar segredos em logs.

## Referências para aprofundar

- [[Panorama de Ferramentas de Segurança]]

## Veja também

- [[Home - Integração]]
- [[MOC - Desenvolvimento de Ferramentas]]
- [[MOC - DevSecOps e CI-CD]]
