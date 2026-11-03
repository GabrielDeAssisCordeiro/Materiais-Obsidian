---
titulo: "Metasploit Framework"
tipo: ferramenta
nome: "Metasploit Framework"
categoria: "Ofensivo/Exploracao"
subcategoria: "Framework de Exploração"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "BSD-3-Clause"
linguagem: "Ruby"
mitre_attack: ["T1203", "T1210"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.metasploit.com/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/exploracao
---

# Metasploit Framework

> Framework modular para desenvolvimento, teste e execução de exploits, payloads e pós-exploração.

## Como funciona
Organiza-se em módulos independentes — exploits, payloads, encoders, auxiliares e módulos de pós-exploração — que podem ser combinados livremente: um exploit entrega um payload (ex.: Meterpreter), que abre um canal de comunicação com um 'handler' na máquina do operador. O Meterpreter, em particular, roda em memória e oferece uma API extensível para comandos pós-exploração sem gravar novos arquivos em disco.

## Como usar
No `msfconsole`, seleciona-se um exploit (`use exploit/...`), define-se o payload (`set payload ...`), os parâmetros do alvo (`set RHOSTS`, `set LHOST`) e executa-se com `run` ou `exploit`. O módulo `multi/handler` é usado para capturar conexões de payloads gerados separadamente (ex.: via `msfvenom`).

## Casos de uso
- Validação de exploração de vulnerabilidades identificadas em scan
- Geração de payloads para testes de engenharia social autorizados

## Alternativas
[[Cobalt Strike]] · [[Sliver]]

## Categoria
[[MOC - Exploração]]

## Link oficial
https://www.metasploit.com/
