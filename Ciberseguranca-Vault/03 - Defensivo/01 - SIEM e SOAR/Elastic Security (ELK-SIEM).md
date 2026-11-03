---
titulo: "Elastic Security (ELK/SIEM)"
tipo: ferramenta
nome: "Elastic Security (ELK/SIEM)"
categoria: "Defensivo/SIEM-SOAR"
subcategoria: "SIEM / Análise de Logs Open Source"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Elastic License / SSPL"
linguagem: "Java"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.elastic.co/security"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/siem
---

# Elastic Security (ELK/SIEM)

> Stack ELK (Elasticsearch, Logstash, Kibana) estendida com regras de detecção para uso como SIEM.

## Como funciona
O Elasticsearch indexa documentos JSON (logs normalizados) em estruturas otimizadas para busca e agregação distribuída; o Logstash/Beats cuidam da ingestão e parsing de diferentes formatos de log na entrada, e a camada 'Security' adiciona regras de detecção pré-construídas (mapeadas ao MITRE ATT&CK), gestão de casos e um mecanismo de resposta básico sobre os mesmos dados indexados.

## Como usar
Logs chegam via Beats/Logstash para um índice no Elasticsearch; no Kibana, a seção Security permite ativar regras de detecção prontas ou escrever consultas KQL/EQL customizadas, com alertas encaminhados a um 'case' para acompanhamento da investigação.

## Casos de uso
- SIEM self-hosted de baixo custo de licenciamento
- Busca forense em grandes volumes de log com agregações complexas

## Alternativas
[[Splunk]] · [[Wazuh]] · [[Graylog]]

## Categoria
[[MOC - SIEM e SOAR]]

## Link oficial
https://www.elastic.co/security
