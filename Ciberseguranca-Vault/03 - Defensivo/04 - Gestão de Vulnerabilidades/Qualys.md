---
titulo: "Qualys"
tipo: ferramenta
nome: "Qualys"
categoria: "Defensivo/Gestao-de-Vulnerabilidades"
subcategoria: "Gestão de Vulnerabilidades em Nuvem"
plataformas: ["Cloud", "Agentes multiplataforma"]
licenca: "Comercial"
linguagem: "N/A"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.qualys.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/vuln-mgmt
---

# Qualys

> Plataforma comercial em nuvem de gestão contínua de vulnerabilidades e compliance.

## Como funciona
Combina varredura de rede sem agente (appliances virtuais/físicos) com agentes leves instalados em endpoints para visibilidade contínua, mantendo um inventário de ativos e vulnerabilidades sempre atualizado na nuvem da Qualys, com priorização de risco baseada em contexto (exploração ativa conhecida, exposição do ativo) além do CVSS puro.

## Como usar
Configura-se um 'Asset Group' e associa-se a um 'Scan' agendado ou contínuo (via agente); o módulo VMDR consolida vulnerabilidades por prioridade de risco e permite acompanhar o ciclo completo até a remediação confirmada por novo scan.

## Casos de uso
- Gestão contínua de vulnerabilidades em larga escala
- Priorização de remediação baseada em risco real, não apenas CVSS

## Alternativas
[[Nessus]] · [[OpenVAS]]

## Categoria
[[MOC - Gestão de Vulnerabilidades]]

## Link oficial
https://www.qualys.com/
