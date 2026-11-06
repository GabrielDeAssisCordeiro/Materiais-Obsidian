---
titulo: "Nmap"
tipo: ferramenta
nome: "Nmap"
categoria: "Ofensivo/Scanning-Enum"
subcategoria: "Scanner de Portas"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C/Lua (NSE)"
mitre_attack: ["T1046", "T1595"]
nivel: iniciante
situacao: ativo
link_oficial: "https://nmap.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/scanning
  - arsenal-de-ferramentas
---

# Nmap

> Scanner de rede para descoberta de hosts, portas abertas, serviços e versões.

## Como funciona
Envia pacotes TCP/UDP/ICMP cuidadosamente construídos e interpreta as respostas (ou ausência delas) para inferir o estado de cada porta (aberta, fechada, filtrada). Técnicas como SYN scan (`-sS`) completam apenas parte do handshake TCP para serem mais furtivas; o motor NSE (Nmap Scripting Engine) executa scripts Lua para detecção de versão, vulnerabilidades e até exploração leve.

## Como usar
Um scan típico combina detecção de serviço (`-sV`), scripts padrão (`-sC`), todas as portas (`-p-`) e saída em todos os formatos (`-oA`). Timing templates (`-T0` a `-T5`) controlam velocidade versus discrição, e `--script vuln` roda a categoria de scripts voltada à identificação de vulnerabilidades conhecidas.

## Casos de uso
- Enumeração inicial de serviços em pentest de infraestrutura
- Execução de scripts NSE para detecção de vulnerabilidades conhecidas

## Alternativas
[[Masscan]] · RustScan

## Categoria
[[MOC - Scanning e Enumeração]]

## Link oficial
https://nmap.org/
