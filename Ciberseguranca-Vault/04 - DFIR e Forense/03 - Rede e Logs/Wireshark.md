---
titulo: "Wireshark"
tipo: ferramenta
nome: "Wireshark"
categoria: "DFIR/Rede-e-Logs"
subcategoria: "Análise de Tráfego de Rede"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://www.wireshark.org/"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/rede
---

# Wireshark

> Analisador de protocolos de rede gráfico, padrão de facto para inspeção detalhada de pacotes.

## Como funciona
Captura pacotes diretamente de uma interface de rede (ou lê capturas salvas em PCAP) e decodifica cada camada do protocolo (Ethernet, IP, TCP/UDP, aplicação) em uma árvore navegável, permitindo inspecionar byte a byte o conteúdo de qualquer pacote e reconstruir fluxos completos de conversação (ex.: reconstituir um arquivo transferido via HTTP).

## Como usar
A captura ao vivo inicia selecionando a interface de rede desejada; filtros de exibição (ex.: `http.request` ou `ip.addr==10.0.0.5`) isolam o tráfego relevante, e a opção 'Follow TCP Stream' reconstrói uma conversa completa de forma legível a partir dos pacotes individuais.

## Casos de uso
- Análise forense detalhada de uma captura de rede de um incidente
- Depuração de protocolos de rede em nível de pacote

## Alternativas
[[tcpdump]] · [[NetworkMiner]]

## Categoria
[[MOC - Rede e Logs]]

## Link oficial
https://www.wireshark.org/
