---
titulo: "Impacket"
tipo: ferramenta
nome: "Impacket"
categoria: "Ofensivo/Active-Directory"
subcategoria: "Biblioteca de Protocolos Windows"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0 modificada"
linguagem: "Python"
mitre_attack: ["T1558", "T1021.002"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/fortra/impacket"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/ad
---

# Impacket

> Coleção de classes Python para construir e manipular protocolos de rede Windows (SMB, MSRPC, Kerberos).

## Como funciona
Implementa em Python puro os protocolos binários nativos do Windows (SMB/SMB2, MSRPC, Kerberos, LDAP) desde a camada de parsing, permitindo construir ferramentas que interagem diretamente com esses protocolos sem depender de bibliotecas do sistema operacional Windows — por isso os scripts rodam a partir de Linux contra alvos Windows.

## Como usar
A biblioteca vem com dezenas de scripts prontos: `secretsdump.py dominio/usuario:senha@alvo.ip` extrai hashes remotamente via replicação de domínio ou registro local; `psexec.py` e `wmiexec.py` executam comandos remotamente usando credenciais válidas; `GetUserSPNs.py` realiza Kerberoasting.

## Casos de uso
- Extração remota de hashes via secretsdump
- Movimentação lateral com psexec.py / wmiexec.py

## Alternativas
[[CrackMapExec]] · NetExec

## Categoria
[[MOC - Active Directory]]

## Link oficial
https://github.com/fortra/impacket
