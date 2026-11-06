---
titulo: "Rekall"
tipo: ferramenta
nome: "Rekall"
categoria: "DFIR/Memoria"
subcategoria: "Análise Forense de Memória"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "Python"
mitre_attack: []
nivel: avancado
situacao: legado
link_oficial: "https://github.com/google/rekall"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/memoria
  - arsenal-de-ferramentas
---

# Rekall

> Framework de análise de memória originado como fork do Volatility, com foco em performance e live forensics.

## Como funciona
Compartilha conceitualmente a mesma abordagem do Volatility (reconstrução de estruturas de kernel a partir de um dump bruto), mas foi otimizado para analisar sistemas ao vivo (live forensics) além de dumps estáticos, com uma arquitetura de plugins e um console interativo próprio para investigação exploratória.

## Como usar
O console interativo (`rekall -f dump.mem`) permite executar plugins de forma semelhante ao Volatility (ex.: `pslist`, `netscan`) e encadear comandos Python diretamente sobre os objetos de memória reconstruídos para análises customizadas.

## Casos de uso
- Análise de memória ao vivo em sistemas ainda em execução
- Investigação exploratória interativa via console Python

## Alternativas
[[Volatility 3]]

## Categoria
[[MOC - Memória]]

## Link oficial
https://github.com/google/rekall
