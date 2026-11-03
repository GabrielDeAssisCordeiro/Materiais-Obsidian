---
titulo: "Splunk"
tipo: ferramenta
nome: "Splunk"
categoria: "Defensivo/SIEM-SOAR"
subcategoria: "SIEM / Análise de Logs"
plataformas: ["Linux", "Windows", "macOS", "Cloud"]
licenca: "Comercial (Free tier limitado)"
linguagem: "C++/Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.splunk.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/siem
---

# Splunk

> Plataforma de ingestão, indexação e correlação de logs para monitoramento e investigação de segurança.

## Como funciona
Ingere dados de praticamente qualquer fonte (logs de sistema, firewall, EDR, aplicações) através de 'forwarders' e os indexa em um formato otimizado para busca full-text em grande escala; sobre esses dados indexados, a linguagem de busca própria (SPL) permite correlacionar eventos de múltiplas fontes, criar dashboards e disparar alertas automatizados (via Splunk ES/SOAR) quando padrões suspeitos são detectados.

## Como usar
Configura-se um 'index' para receber os dados e instala-se um Universal Forwarder nas origens de log; consultas são escritas em SPL (ex.: `index=firewall action=blocked | stats count by src_ip`) e podem virar alertas programados ou painéis persistentes compartilhados com a equipe de SOC.

## Casos de uso
- Monitoramento centralizado de eventos de segurança (SOC)
- Investigação forense de incidentes correlacionando múltiplas fontes de log

## Alternativas
[[Elastic Security (ELK-SIEM)|Elastic Security (ELK/SIEM)]] · [[Microsoft Sentinel]] · [[Graylog]]

## Categoria
[[MOC - SIEM e SOAR]]

## Link oficial
https://www.splunk.com/
