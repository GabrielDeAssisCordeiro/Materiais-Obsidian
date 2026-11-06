---
titulo: "Masscan"
tipo: ferramenta
nome: "Masscan"
categoria: "Ofensivo/Scanning-Enum"
subcategoria: "Scanner de Portas de Alta Velocidade"
plataformas: ["Linux"]
licenca: "AGPL-3.0"
linguagem: "C"
mitre_attack: ["T1046"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/robertdavidgraham/masscan"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/scanning
  - arsenal-de-ferramentas
---

# Masscan

> Scanner assíncrono capaz de varrer toda a internet em minutos; usado para varreduras massivas de portas.

## Como funciona
Usa uma pilha TCP/IP própria, independente do kernel, e envia pacotes SYN de forma assíncrona em taxa configurável (pacotes por segundo), sem esperar resposta antes de enviar o próximo. As respostas são correlacionadas posteriormente, permitindo taxas de varredura ordens de magnitude maiores que ferramentas tradicionais, ao custo de maior chance de perda de pacotes em redes congestionadas.

## Como usar
A sintaxe lembra o Nmap: `masscan -p1-65535 10.0.0.0/8 --rate=10000` define o range de portas, o CIDR alvo e a taxa de envio. É recomendável usar `--rate` moderado em redes de produção e, por ser agressivo, combinar com Nmap para enumeração detalhada apenas das portas que o Masscan identificou como abertas.

## Casos de uso
- Varredura rápida de grandes blocos de IP antes de scan detalhado com Nmap
- Descoberta inicial de ativos em red team de larga escala

## Alternativas
[[Nmap]] · RustScan

## Categoria
[[MOC - Scanning e Enumeração]]

## Link oficial
https://github.com/robertdavidgraham/masscan
