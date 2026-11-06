---
titulo: "SpiderFoot"
tipo: ferramenta
nome: "SpiderFoot"
categoria: "Ofensivo/Reconhecimento"
subcategoria: "Automação de OSINT"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "Python"
mitre_attack: ["T1596", "T1593"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/smicallef/spiderfoot"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/recon
  - arsenal-de-ferramentas
---

# SpiderFoot

> Automatiza consultas a mais de 200 fontes OSINT e correlaciona os dados em um único relatório.

## Como funciona
Opera por meio de 'módulos' encadeados: o resultado de um módulo (ex.: um IP resolvido) é automaticamente repassado como entrada para outros módulos relevantes (ex.: geolocalização, histórico de abuso, blocklists), formando uma varredura recursiva e correlacionada sem intervenção manual entre etapas.

## Como usar
A interface web (`spiderfoot -l 127.0.0.1:5001`) permite criar uma nova varredura informando o alvo e selecionando o conjunto de módulos (ou usando o preset 'all'). Via CLI, `spiderfoot -s alvo.com -u all` roda tudo de uma vez; os resultados ficam navegáveis por tipo de dado e por correlação de risco.

## Casos de uso
- Varredura OSINT ampla e automatizada em etapa inicial de engajamento
- Monitoramento contínuo de exposição de marca

## Alternativas
[[Recon-ng]] · [[Amass]] · [[theHarvester]]

## Categoria
[[MOC - Reconhecimento]]

## Link oficial
https://github.com/smicallef/spiderfoot
