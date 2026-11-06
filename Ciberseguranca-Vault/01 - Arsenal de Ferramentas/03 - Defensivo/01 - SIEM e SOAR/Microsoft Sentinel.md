---
titulo: "Microsoft Sentinel"
tipo: ferramenta
nome: "Microsoft Sentinel"
categoria: "Defensivo/SIEM-SOAR"
subcategoria: "SIEM/SOAR em Nuvem"
plataformas: ["Cloud (Azure)"]
licenca: "Comercial (pay-as-you-go)"
linguagem: "N/A"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://azure.microsoft.com/products/microsoft-sentinel"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/siem
  - arsenal-de-ferramentas
---

# Microsoft Sentinel

> SIEM e SOAR nativos em nuvem da Microsoft, integrados ao ecossistema Azure e Microsoft 365.

## Como funciona
Ingere dados via conectores prontos para dezenas de fontes (Azure AD, Microsoft 365, firewalls, outros SIEMs) para um workspace do Log Analytics, aplicando analytics rules (muitas mapeadas ao MITRE ATT&CK) sobre esses dados; playbooks construídos em Azure Logic Apps automatizam respostas (ex.: desabilitar conta, isolar máquina) quando um alerta específico é gerado.

## Como usar
Habilita-se um conector de dados relevante, cria-se uma 'Analytics Rule' (pronta ou customizada em KQL) e, opcionalmente, um Playbook de resposta automática vinculado àquela regra; incidentes gerados aparecem centralizados na página de Incidentes para triagem do analista.

## Casos de uso
- SOC centralizado para ambientes majoritariamente Microsoft/Azure
- Automação de resposta a incidentes via playbooks SOAR

## Alternativas
[[Splunk]] · [[Elastic Security (ELK-SIEM)|Elastic Security (ELK/SIEM)]]

## Categoria
[[MOC - SIEM e SOAR]]

## Link oficial
https://azure.microsoft.com/products/microsoft-sentinel
