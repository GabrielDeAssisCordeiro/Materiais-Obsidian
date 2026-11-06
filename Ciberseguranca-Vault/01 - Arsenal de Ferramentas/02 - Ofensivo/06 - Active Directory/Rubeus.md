---
titulo: "Rubeus"
tipo: ferramenta
nome: "Rubeus"
categoria: "Ofensivo/Active-Directory"
subcategoria: "Abuso de Kerberos"
plataformas: ["Windows"]
licenca: "BSD-3-Clause"
linguagem: "C#"
mitre_attack: ["T1558.003", "T1550.003"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/GhostPack/Rubeus"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/ad
  - arsenal-de-ferramentas
---

# Rubeus

> Ferramenta para abuso de Kerberos: Kerberoasting, AS-REP Roasting, geração e injeção de tickets.

## Como funciona
Interage diretamente com a API Kerberos do Windows para solicitar, extrair e manipular tickets (TGT/TGS): no Kerberoasting, solicita tickets de serviço para contas com SPN configurado e extrai a porção criptografada (quebrável offline); em ataques de Golden/Silver Ticket, forja tickets válidos a partir de material de chave previamente obtido (ex.: via Mimikatz).

## Como usar
`Rubeus.exe kerberoast /outfile:hashes.txt` coleta e salva hashes de contas de serviço para quebra offline com Hashcat; outros comandos como `asreproast`, `golden` e `ptt` (pass-the-ticket) cobrem os demais cenários de abuso Kerberos.

## Casos de uso
- Extração de hashes de contas de serviço para quebra offline
- Validação de exposição a ataques Golden/Silver Ticket

## Alternativas
Impacket (GetUserSPNs.py) · [[Mimikatz]]

## Categoria
[[MOC - Active Directory]]

## Link oficial
https://github.com/GhostPack/Rubeus
