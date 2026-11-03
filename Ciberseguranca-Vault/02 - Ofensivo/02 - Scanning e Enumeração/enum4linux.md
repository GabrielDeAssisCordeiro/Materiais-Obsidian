---
titulo: "enum4linux"
tipo: ferramenta
nome: "enum4linux"
categoria: "Ofensivo/Scanning-Enum"
subcategoria: "Enumeração SMB/NetBIOS"
plataformas: ["Linux"]
licenca: "GPLv3"
linguagem: "Perl/Python (reescrita enum4linux-ng)"
mitre_attack: ["T1135", "T1046"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/CiscoCXSecurity/enum4linux"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/scanning
---

# enum4linux

> Enumera compartilhamentos, usuários, grupos e políticas de senha via SMB em hosts Windows/Samba.

## Como funciona
Encapsula chamadas às ferramentas clássicas do Samba (`rpcclient`, `smbclient`, `net`, `nmblookup`) contra o protocolo SMB/RPC, automatizando consultas que, isoladamente, exigiriam vários comandos manuais: listagem de sessões nulas, enumeração de SIDs de usuários via RID cycling, políticas de bloqueio de conta e shares disponíveis.

## Como usar
Basta `enum4linux -a alvo.ip` para rodar o conjunto completo de testes; flags individuais (`-U` para usuários, `-S` para shares, `-P` para políticas de senha) permitem testes direcionados. A versão reescrita `enum4linux-ng` adiciona saída estruturada em YAML/JSON.

## Casos de uso
- Enumeração de usuários de domínio em fase inicial de pentest AD
- Levantamento de shares abertos para acesso não autenticado

## Alternativas
smbclient · [[CrackMapExec]]

## Categoria
[[MOC - Scanning e Enumeração]]

## Link oficial
https://github.com/CiscoCXSecurity/enum4linux
