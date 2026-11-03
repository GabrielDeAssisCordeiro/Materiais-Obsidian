---
titulo: "Suricata"
tipo: ferramenta
nome: "Suricata"
categoria: "Defensivo/IDS-IPS-Firewall"
subcategoria: "IDS/IPS de Rede Multithread"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://suricata.io/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/ids-ips
---

# Suricata

> Motor de IDS/IPS/NSM de código aberto com suporte nativo a múltiplas threads e extração de arquivos.

## Como funciona
Processa o tráfego de forma multithread (aproveitando múltiplos núcleos de CPU, diferente da arquitetura tradicionalmente single-thread do Snort), aplicando o mesmo formato de regras compatível com Snort, além de capacidades nativas de extração de arquivos transferidos na rede e geração de logs estruturados (EVE JSON) prontos para ingestão em um SIEM.

## Como usar
A configuração principal fica em `suricata.yaml`, onde se definem interfaces monitoradas e conjuntos de regras (gerenciáveis via `suricata-update`); a execução (`suricata -c suricata.yaml -i eth0`) gera logs em formato EVE JSON, facilmente integráveis a pipelines de SIEM para correlação.

## Casos de uso
- NSM (Network Security Monitoring) de alta performance
- Extração e análise de arquivos transferidos em rede suspeita

## Alternativas
[[Snort]] · [[Zeek (Bro)]]

## Categoria
[[MOC - IDS, IPS e Firewall]]

## Link oficial
https://suricata.io/
