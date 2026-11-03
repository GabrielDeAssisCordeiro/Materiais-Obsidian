---
titulo: "CrackMapExec"
tipo: ferramenta
nome: "CrackMapExec"
categoria: "Ofensivo/Active-Directory"
subcategoria: "Execução e Enumeração em Massa"
plataformas: ["Linux"]
licenca: "BSD-3-Clause (NetExec é o fork ativo)"
linguagem: "Python"
mitre_attack: ["T1021.002", "T1110"]
nivel: avancado
situacao: legado
link_oficial: "https://github.com/Pennyw0rth/NetExec"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/ad
---

# CrackMapExec

> "Canivete suíço" para redes AD: validação de credenciais, execução de comando e enumeração via SMB/WinRM. Projeto sucessor ativo: NetExec.

## Como funciona
Automatiza a aplicação de um conjunto de credenciais (ou hash, para pass-the-hash) contra múltiplos hosts simultaneamente via protocolos nativos do Windows (SMB, WinRM, LDAP, MSSQL), reportando sucesso/falha de autenticação em massa e, quando autenticado, permitindo execução remota de comandos através dos mesmos mecanismos usados por administradores legítimos.

## Como usar
`crackmapexec smb 10.0.0.0/24 -u usuario -p senha` testa a credencial contra toda a sub-rede; módulos (`-M`) adicionam funcionalidades como dump de SAM, spidering de shares ou execução de comando (`-x`). O projeto sucessor NetExec mantém sintaxe muito semelhante.

## Casos de uso
- Spray de credenciais em múltiplos hosts de domínio
- Execução remota de comandos em pós-exploração de AD

## Alternativas
NetExec · [[Impacket]]

## Categoria
[[MOC - Active Directory]]

## Link oficial
https://github.com/Pennyw0rth/NetExec
