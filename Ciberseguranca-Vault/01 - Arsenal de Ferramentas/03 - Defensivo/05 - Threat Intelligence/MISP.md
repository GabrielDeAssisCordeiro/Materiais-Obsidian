---
titulo: "MISP"
tipo: ferramenta
nome: "MISP"
categoria: "Defensivo/Threat-Intelligence"
subcategoria: "Plataforma de Threat Intelligence"
plataformas: ["Linux", "Docker"]
licenca: "AGPL-3.0"
linguagem: "PHP/Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.misp-project.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/threat-intel
  - arsenal-de-ferramentas
---

# MISP

> Plataforma open source para compartilhamento estruturado de indicadores de comprometimento (IOCs) entre organizações.

## Como funciona
Modela ameaças como 'eventos' contendo atributos (IOCs como hashes, IPs, domínios) e os organiza em um grafo de relações e tags de taxonomia (incluindo mapeamento a MITRE ATT&CK); comunidades de confiança compartilham eventos entre instâncias MISP via sincronização automática, permitindo que um IOC identificado em uma organização seja propagado rapidamente a parceiros confiáveis.

## Como usar
Cria-se um 'Event' descrevendo o incidente/campanha e adicionam-se atributos (IOCs) manualmente ou via importação de feeds automatizados; a sincronização com outras instâncias/comunidades é configurada via 'Sync Servers', e os IOCs exportados podem alimentar diretamente regras de SIEM/IDS.

## Casos de uso
- Compartilhamento de IOCs entre organizações/comunidades de confiança
- Enriquecimento de alertas de SIEM com inteligência de ameaça contextual

## Alternativas
[[OpenCTI]] · [[AlienVault OTX]]

## Categoria
[[MOC - Threat Intelligence]]

## Link oficial
https://www.misp-project.org/
