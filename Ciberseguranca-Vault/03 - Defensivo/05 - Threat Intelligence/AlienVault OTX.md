---
titulo: "AlienVault OTX"
tipo: ferramenta
nome: "AlienVault OTX"
categoria: "Defensivo/Threat-Intelligence"
subcategoria: "Feed Comunitário de Threat Intelligence"
plataformas: ["Web", "API"]
licenca: "Gratuito"
linguagem: "N/A"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://otx.alienvault.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/threat-intel
---

# AlienVault OTX

> Plataforma comunitária gratuita de compartilhamento de indicadores de ameaça (Open Threat Exchange).

## Como funciona
Agrega 'pulses' (coleções de IOCs relacionados a uma campanha ou família de malware específica) submetidos pela comunidade de pesquisadores de segurança e por feeds automatizados, disponibilizando-os para consulta e assinatura gratuita via interface web ou API.

## Como usar
Pesquisa-se um indicador diretamente na interface ou assina-se 'pulses' de interesse para receber atualizações; a API permite consumir pulses automaticamente e alimentar outras ferramentas (como MISP) com os IOCs coletados.

## Casos de uso
- Fonte gratuita de IOCs para enriquecer alertas de SIEM
- Acompanhamento de campanhas específicas relatadas pela comunidade

## Alternativas
[[MISP]] · [[VirusTotal]]

## Categoria
[[MOC - Threat Intelligence]]

## Link oficial
https://otx.alienvault.com/
