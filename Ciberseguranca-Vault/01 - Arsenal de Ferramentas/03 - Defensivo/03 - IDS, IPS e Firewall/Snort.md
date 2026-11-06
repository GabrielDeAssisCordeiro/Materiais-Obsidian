---
titulo: "Snort"
tipo: ferramenta
nome: "Snort"
categoria: "Defensivo/IDS-IPS-Firewall"
subcategoria: "IDS/IPS de Rede"
plataformas: ["Linux", "Windows"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.snort.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/ids-ips
  - arsenal-de-ferramentas
---

# Snort

> Sistema de detecção/prevenção de intrusão de rede baseado em assinaturas, um dos mais tradicionais do mercado.

## Como funciona
Inspeciona o tráfego de rede em tempo real comparando pacotes contra um conjunto de 'regras' (assinaturas) que descrevem padrões de tráfego malicioso conhecido (exploits específicos, varreduras, malware); quando configurado em modo inline (IPS), pode descartar ativamente pacotes que correspondam a uma regra, além de apenas registrar e alertar (modo IDS passivo).

## Como usar
Após configurar as interfaces de rede e o conjunto de regras (próprias, da comunidade ou de assinatura paga via Talos), inicia-se o Snort em modo de detecção (`snort -A console -c snort.conf -i eth0`) ou inline/IPS via integração com DAQ/netfilter; alertas e logs ficam disponíveis para análise ou encaminhamento a um SIEM.

## Casos de uso
- Detecção de assinaturas conhecidas de ataque na borda da rede
- Bloqueio ativo (IPS) de tráfego malicioso identificado

## Alternativas
[[Suricata]]

## Categoria
[[MOC - IDS, IPS e Firewall]]

## Link oficial
https://www.snort.org/
