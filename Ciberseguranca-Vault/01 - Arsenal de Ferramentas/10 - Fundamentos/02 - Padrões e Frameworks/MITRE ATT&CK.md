---
titulo: "MITRE ATT&CK"
tipo: padrao
nome: "MITRE ATT&CK"
categoria: "Fundamentos/Padroes-e-Frameworks"
subcategoria: "Framework de Táticas e Técnicas de Ataque"
plataformas: ["Web"]
licenca: "Gratuito (MITRE)"
linguagem: "N/A"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://attack.mitre.org/"
tags:
  - ciberseguranca
  - padrao
  - fundamentos
  - arsenal-de-ferramentas
---

# MITRE ATT&CK

> Base de conhecimento pública que cataloga táticas, técnicas e procedimentos (TTPs) reais usados por adversários.

## Como funciona
Organiza o conhecimento sobre comportamento adversário em uma matriz de 'táticas' (objetivos do atacante, como Acesso Inicial ou Persistência) e, dentro de cada tática, 'técnicas' específicas (métodos concretos para alcançar aquele objetivo, cada uma com um ID único como T1566 para Phishing), documentadas a partir de observações reais de grupos de ameaça e campanhas, servindo como linguagem comum entre ofensiva, defesa e inteligência de ameaça.

## Como usar
Usado para mapear ferramentas/técnicas usadas em um engajamento de red team a IDs específicos (facilitando comunicação com o blue team), para avaliar cobertura de detecção de um SIEM contra técnicas específicas, e para estruturar relatórios de threat intelligence referenciando os TTPs observados de um grupo de ameaça.

## Casos de uso
- Mapeamento de TTPs observados durante um incidente ou red team
- Avaliação de cobertura de detecção de um SOC contra técnicas conhecidas

## Alternativas
[[Cadeia de Ataque - Cyber Kill Chain|Cadeia de Ataque / Cyber Kill Chain]]

## Veja também
[[MITRE ATLAS]] (matriz equivalente para sistemas de IA)

## Categoria
[[MOC - Padrões e Frameworks]]

## Link oficial
https://attack.mitre.org/
