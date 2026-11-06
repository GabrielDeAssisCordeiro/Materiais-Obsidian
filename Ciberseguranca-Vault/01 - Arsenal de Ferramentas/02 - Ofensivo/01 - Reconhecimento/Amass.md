---
titulo: "Amass"
tipo: ferramenta
nome: "Amass"
categoria: "Ofensivo/Reconhecimento"
subcategoria: "Mapeamento de Superfície de Ataque"
plataformas: ["Linux", "macOS", "Windows"]
licenca: "Apache-2.0"
linguagem: "Go"
mitre_attack: ["T1596"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/owasp-amass/amass"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/recon
  - arsenal-de-ferramentas
---

# Amass

> Enumera subdomínios e mapeia infraestrutura DNS/ASN de um alvo.

## Como funciona
Combina técnicas passivas (consultas a dezenas de fontes OSINT, certificate transparency logs, APIs de inteligência) com técnicas ativas opcionais (brute force de DNS, resolução recursiva, varredura de zonas). Internamente constrói um grafo de relacionamento entre domínios, subdomínios, endereços IP, blocos CIDR e sistemas autônomos (ASN), permitindo visualizar como a infraestrutura de uma organização se conecta.

## Como usar
O modo mais seguro é `amass enum -passive -d alvo.com`, que não toca diretamente o alvo. Para enumeração ativa (mais completa, porém mais barulhenta), remove-se `-passive` e usa-se `-brute` com uma wordlist. O subcomando `amass viz` gera visualizações do grafo coletado e `amass db` consulta resultados já armazenados.

## Casos de uso
- Enumeração de subdomínios em escopo de bug bounty
- Construção de grafo de infraestrutura externa

## Alternativas
[[theHarvester]] · Subfinder · [[SpiderFoot]]

## Categoria
[[MOC - Reconhecimento]]

## Link oficial
https://github.com/owasp-amass/amass
