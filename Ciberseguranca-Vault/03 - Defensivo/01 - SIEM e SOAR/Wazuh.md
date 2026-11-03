---
titulo: "Wazuh"
tipo: ferramenta
nome: "Wazuh"
categoria: "Defensivo/SIEM-SOAR"
subcategoria: "SIEM/EDR Open Source"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C/Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://wazuh.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/siem
---

# Wazuh

> Plataforma open source unificando SIEM e detecção de endpoint (HIDS), construída sobre o Elastic Stack.

## Como funciona
Um agente leve instalado em cada host coleta logs, monitora integridade de arquivos (FIM), audita configurações e aplica regras de detecção localmente, enviando os achados a um servidor central (manager) que correlaciona eventos de múltiplos agentes, aplica regras de decodificação e disponibiliza os resultados via Elastic Stack/Kibana integrado.

## Como usar
Instala-se o manager central e, em cada endpoint monitorado, o agente Wazuh apontando para ele; via dashboard Kibana embutido, consultam-se alertas por regra, agente ou severidade, e novas regras de detecção customizadas podem ser adicionadas em XML.

## Casos de uso
- SIEM + detecção de endpoint sem custo de licenciamento
- Monitoramento de integridade de arquivos e compliance (PCI-DSS, CIS)

## Alternativas
[[OSSEC]] · [[Elastic Security (ELK-SIEM)|Elastic Security (ELK/SIEM)]]

## Categoria
[[MOC - SIEM e SOAR]]

## Link oficial
https://wazuh.com/
