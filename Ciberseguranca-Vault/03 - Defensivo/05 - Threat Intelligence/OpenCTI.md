---
titulo: "OpenCTI"
tipo: ferramenta
nome: "OpenCTI"
categoria: "Defensivo/Threat-Intelligence"
subcategoria: "Plataforma de Threat Intelligence"
plataformas: ["Linux", "Docker"]
licenca: "Apache-2.0"
linguagem: "TypeScript/Python"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://www.opencti.io/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/threat-intel
---

# OpenCTI

> Plataforma de Cyber Threat Intelligence estruturada em grafo, baseada no modelo de dados STIX2.

## Como funciona
Modela todas as entidades (atores de ameaça, malware, campanhas, IOCs, TTPs) e seus relacionamentos como um grafo de conhecimento seguindo o padrão STIX2, permitindo consultas complexas sobre como diferentes ameaças se conectam (ex.: 'quais campanhas usaram esta família de malware e quais TTPs do MITRE ATT&CK foram observadas'), com conectores prontos para importar dados de MISP, feeds comerciais e outras fontes.

## Como usar
Dados chegam via 'conectores' configuráveis (importação de feeds, MISP, relatórios manuais) e são explorados através do grafo de relações na interface web; relatórios de inteligência podem ser criados vinculando entidades existentes e exportados para consumo por outras equipes.

## Casos de uso
- Modelagem estruturada de atores e campanhas de ameaça (STIX2)
- Correlação de TTPs do MITRE ATT&CK com inteligência coletada

## Alternativas
[[MISP]]

## Categoria
[[MOC - Threat Intelligence]]

## Link oficial
https://www.opencti.io/
