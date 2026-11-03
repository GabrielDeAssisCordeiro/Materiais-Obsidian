---
titulo: "Cowrie"
tipo: ferramenta
nome: "Cowrie"
categoria: "Defensivo/Deception-Honeypots"
subcategoria: "Honeypot SSH/Telnet"
plataformas: ["Linux"]
licenca: "BSD-3-Clause (modificada)"
linguagem: "Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/cowrie/cowrie"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/deception
---

# Cowrie

> Honeypot de média interação que simula um shell SSH/Telnet para capturar tentativas de invasão.

## Como funciona
Emula um ambiente de shell Unix completo (sistema de arquivos falso navegável, comandos respondendo de forma plausível) sem ser um sistema real, registrando toda sessão do atacante — credenciais tentadas, comandos digitados, arquivos que tentou baixar — como se fosse uma gravação de terminal, sem expor um sistema de produção real a risco.

## Como usar
Após a instalação, configura-se a porta de escuta (tipicamente redirecionando a porta 22 real para a porta do Cowrie) e credenciais falsas aceitas; todas as sessões capturadas ficam disponíveis como logs estruturados (JSON) e gravações reproduzíveis dos comandos digitados pelo atacante.

## Casos de uso
- Captura de credenciais e TTPs de ataques automatizados de força bruta SSH
- Alerta antecipado de reconhecimento ativo contra a rede

## Alternativas
[[T-Pot]] · [[Honeyd]]

## Categoria
[[MOC - Deception e Honeypots]]

## Link oficial
https://github.com/cowrie/cowrie
