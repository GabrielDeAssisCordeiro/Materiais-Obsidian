---
titulo: "Sherlock"
tipo: ferramenta
nome: "Sherlock"
categoria: "OSINT"
subcategoria: "Busca de Usernames em Redes Sociais"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "Python"
mitre_attack: ["T1593"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/sherlock-project/sherlock"
tags:
  - ciberseguranca
  - ferramenta
  - osint
  - arsenal-de-ferramentas
---

# Sherlock

> Ferramenta que verifica a existência de um nome de usuário específico em centenas de plataformas sociais.

## Como funciona
Para cada plataforma em seu banco de dados interno, constrói a URL de perfil correspondente ao username informado e verifica se a página existe (via código de status HTTP ou presença de padrões específicos que indicam perfil inexistente), consolidando em segundos uma lista de todas as plataformas onde aquele exato username está registrado.

## Como usar
`sherlock usuario123` testa o username contra centenas de sites simultaneamente e lista todos onde uma conta com aquele nome foi encontrada, com o link direto para cada perfil confirmado.

## Casos de uso
- Mapeamento de presença digital de um indivíduo por username
- Investigação inicial em casos de fraude ou engenharia social

## Alternativas
[[Maltego]]

## Categoria
[[MOC - OSINT]]

## Link oficial
https://github.com/sherlock-project/sherlock
