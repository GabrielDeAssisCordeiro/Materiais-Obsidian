---
titulo: "Cheatsheet de Windows Privilege Escalation"
tipo: cheatsheet
nome: "Cheatsheet de Windows Privilege Escalation"
categoria: "Fundamentos/Cheatsheets"
subcategoria: "Referência Rápida"
plataformas: ["Windows"]
licenca: "N/A (referência)"
linguagem: "N/A"
mitre_attack: ["T1068"]
nivel: intermediario
situacao: ativo
link_oficial: "https://lolbas-project.github.io/"
tags:
  - ciberseguranca
  - cheatsheet
  - fundamentos
  - arsenal-de-ferramentas
---

# Cheatsheet de Windows Privilege Escalation

> Referência consolidada de técnicas e comandos manuais para escalonamento de privilégio em sistemas Windows.

## Como funciona
Reúne vetores conhecidos (serviços com permissão insegura, DLL hijacking, tokens de privilégio mal configurados, binários nativos abusáveis — catalogados em projetos como LOLBAS) junto a comandos concretos que exploram cada vetor, complementando ferramentas automatizadas (WinPEAS) quando é necessário entender manualmente a causa raiz de um achado.

## Como usar
Identificado um vetor (ex.: um serviço Windows com permissão de escrita insegura), consulta-se a técnica correspondente para o comando exato de exploração (ex.: substituir o binário do serviço e reiniciá-lo para execução com privilégio elevado).

## Casos de uso
- Confirmação manual de vetores de escalonamento em ambiente Windows/AD
- Referência de estudo para certificações focadas em Windows (CRTP, OSCP)

## Alternativas
[[PEASS-ng]] · [[Cheatsheet de Linux Privilege Escalation]]

## Categoria
[[MOC - Cheatsheets]]

## Link oficial
https://lolbas-project.github.io/
