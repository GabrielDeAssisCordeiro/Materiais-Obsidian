---
titulo: "Graylog"
tipo: ferramenta
nome: "Graylog"
categoria: "Defensivo/SIEM-SOAR"
subcategoria: "Gestão de Logs / SIEM"
plataformas: ["Linux", "Docker"]
licenca: "SSPL / Comercial (Enterprise)"
linguagem: "Java"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.graylog.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/siem
  - arsenal-de-ferramentas
---

# Graylog

> Plataforma de gestão centralizada de logs com recursos de correlação voltados a segurança.

## Como funciona
Recebe logs via diversos protocolos de entrada (Syslog, GELF, Beats) e os armazena em um backend Elasticsearch/OpenSearch, oferecendo uma camada de regras de 'pipeline' para normalizar, enriquecer e extrair campos dos eventos antes de indexá-los, além de alertas configuráveis baseados em consultas salvas.

## Como usar
Configura-se um 'Input' para o protocolo de origem (ex.: Syslog UDP), cria-se 'Streams' para rotear categorias específicas de log e 'Pipelines' para enriquecer os dados; alertas são definidos sobre consultas salvas e notificam via e-mail, Slack ou webhook.

## Casos de uso
- Centralização de logs de infraestrutura heterogênea
- Alternativa mais leve a SIEMs comerciais para times menores

## Alternativas
[[Splunk]] · [[Elastic Security (ELK-SIEM)|Elastic Security (ELK/SIEM)]]

## Categoria
[[MOC - SIEM e SOAR]]

## Link oficial
https://www.graylog.org/
