---
titulo: "Shodan"
tipo: ferramenta
nome: "Shodan"
categoria: "Ofensivo/Reconhecimento"
subcategoria: "Busca de Dispositivos Expostos"
plataformas: ["Web", "CLI"]
licenca: "Comercial (busca básica gratuita)"
linguagem: "N/A"
mitre_attack: ["T1596.005"]
nivel: iniciante
situacao: ativo
link_oficial: "https://www.shodan.io/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/recon
---

# Shodan

> Motor de busca indexando banners de serviços expostos na internet (IoT, ICS, servidores).

## Como funciona
Varre continuamente toda a internet em diversas portas, capturando o banner de resposta de cada serviço (versão de software, certificados TLS, cabeçalhos HTTP) e indexando esse conteúdo de forma pesquisável, como um 'Google para dispositivos'. Os resultados incluem geolocalização aproximada, organização responsável pelo IP e histórico de exposição.

## Como usar
A busca básica usa filtros como `country:`, `port:`, `org:` e `product:` diretamente na caixa de pesquisa ou via CLI (shodan search 'apache' country:BR). A API permite automação de consultas e o módulo `shodan host <ip>` detalha um IP específico; filtros avançados exigem conta paga.

## Casos de uso
- Identificação de ativos expostos de um cliente antes de pentest externo
- Pesquisa de dispositivos ICS/SCADA vulneráveis para avaliação de risco

## Alternativas
Censys · ZoomEye

## Categoria
[[MOC - Reconhecimento]]

## Link oficial
https://www.shodan.io/
