---
titulo: "Cheatsheet de Linux Privilege Escalation"
tipo: cheatsheet
nome: "Cheatsheet de Linux Privilege Escalation"
categoria: "Fundamentos/Cheatsheets"
subcategoria: "Referência Rápida"
plataformas: ["Linux"]
licenca: "N/A (referência)"
linguagem: "N/A"
mitre_attack: ["T1068"]
nivel: intermediario
situacao: ativo
link_oficial: "https://gtfobins.github.io/"
tags:
  - ciberseguranca
  - cheatsheet
  - fundamentos
---

# Cheatsheet de Linux Privilege Escalation

> Referência consolidada de técnicas e comandos manuais para escalonamento de privilégio em sistemas Linux.

## Como funciona
Reúne vetores conhecidos de escalonamento (binários SUID mal configurados, entradas de sudoers permissivas, cron jobs graváveis, kernels vulneráveis) junto a exemplos concretos de comandos que exploram cada vetor, servindo como complemento manual às ferramentas automatizadas (como o PEASS-ng) quando é preciso entender ou confirmar manualmente um achado específico.

## Como usar
Após identificar um vetor (ex.: um binário com SUID não padrão), consulta-se a entrada correspondente na cheatsheet/GTFOBins para o comando exato que abusa daquele binário especificamente para obter privilégio elevado.

## Casos de uso
- Confirmação manual de um vetor de escalonamento identificado por ferramenta automatizada
- Referência de estudo para certificações práticas (OSCP)

## Alternativas
[[PEASS-ng]] · [[Cheatsheet de Windows Privilege Escalation]]

## Categoria
[[MOC - Cheatsheets]]

## Link oficial
https://gtfobins.github.io/
