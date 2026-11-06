---
titulo: "OPNsense"
tipo: ferramenta
nome: "OPNsense"
categoria: "Defensivo/IDS-IPS-Firewall"
subcategoria: "Firewall/Roteador Open Source"
plataformas: ["FreeBSD (appliance)"]
licenca: "BSD-2-Clause/Apache"
linguagem: "PHP/C"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://opnsense.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/ids-ips
  - arsenal-de-ferramentas
---

# OPNsense

> Fork do pfSense com foco em atualizações mais frequentes, interface modernizada e plugins adicionais.

## Como funciona
Compartilha a mesma base FreeBSD/`pf` do pfSense, mas com um modelo de releases mais frequente e uma arquitetura de plugins (incluindo IDS/IPS via Suricata integrado nativamente) desenvolvida com foco declarado em transparência e auditabilidade do código.

## Como usar
A gestão também é majoritariamente via interface web; o módulo de Intrusion Detection integra o Suricata diretamente na interface, permitindo habilitar conjuntos de regras e modo de bloqueio (IPS) sem configuração manual externa.

## Casos de uso
- Alternativa ao pfSense com ciclo de releases mais ágil
- Firewall com IDS/IPS integrado nativamente na interface

## Alternativas
[[pfSense]]

## Categoria
[[MOC - IDS, IPS e Firewall]]

## Link oficial
https://opnsense.org/
