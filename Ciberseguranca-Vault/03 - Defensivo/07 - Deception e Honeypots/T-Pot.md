---
titulo: "T-Pot"
tipo: ferramenta
nome: "T-Pot"
categoria: "Defensivo/Deception-Honeypots"
subcategoria: "Plataforma Multi-Honeypot"
plataformas: ["Linux", "Docker"]
licenca: "GPLv3"
linguagem: "Shell/Docker"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/telekom-security/tpot"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/deception
---

# T-Pot

> Plataforma que orquestra dezenas de honeypots diferentes (incluindo Cowrie) em containers, com dashboard unificado.

## Como funciona
Empacota mais de 20 honeypots especializados em diferentes protocolos/serviços (SSH, Web, ICS, bancos de dados) como containers Docker isolados, todos rodando simultaneamente na mesma máquina e alimentando um pipeline Elastic Stack centralizado que consolida e visualiza os ataques capturados por qualquer um dos honeypots em um único dashboard geográfico.

## Como usar
A instalação é feita via script automatizado que sobe todos os containers configurados; o dashboard Kibana embutido (acessível via porta dedicada) exibe em tempo real a origem geográfica, tipo de ataque e honeypot específico que capturou cada tentativa.

## Casos de uso
- Observatório de ameaças com cobertura de múltiplos protocolos simultaneamente
- Pesquisa de tendências de ataques automatizados na internet

## Alternativas
[[Cowrie]] · [[Honeyd]]

## Categoria
[[MOC - Deception e Honeypots]]

## Link oficial
https://github.com/telekom-security/tpot
