---
titulo: "Modelo OSI/TCP-IP"
tipo: conceito
nome: "Modelo OSI/TCP-IP"
categoria: "Fundamentos/Conceitos"
subcategoria: "Conceito de Redes"
plataformas: ["N/A"]
licenca: "N/A"
linguagem: "N/A"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://www.iso.org/standard/20269.html"
tags:
  - ciberseguranca
  - conceito
  - fundamentos
---

# Modelo OSI/TCP-IP

> Modelos conceituais em camadas que descrevem como a comunicação de rede é estruturada, base para entender onde cada ferramenta de segurança atua.

## Como funciona
O modelo OSI divide a comunicação em 7 camadas (física até aplicação) e o TCP/IP em 4 camadas práticas (acesso à rede, internet, transporte, aplicação); cada ferramenta de segurança de rede opera predominantemente em uma camada específica — por exemplo, um scanner de porta atua na camada de transporte, enquanto um WAF atua na camada de aplicação.

## Como usar
Compreender em qual camada um ataque ou ferramenta de defesa opera ajuda a diagnosticar corretamente um problema (ex.: um firewall de camada 3/4 não bloqueará um ataque de injeção SQL, que ocorre na camada 7/aplicação) e a posicionar controles de segurança na camada correta.

## Casos de uso
- Diagnóstico de em qual camada de rede um problema de segurança ocorre
- Base conceitual para entender o escopo de atuação de cada ferramenta

## Alternativas
[[Cadeia de Ataque - Cyber Kill Chain|Cadeia de Ataque / Cyber Kill Chain]]

## Categoria
[[MOC - Conceitos]]

## Link oficial
https://www.iso.org/standard/20269.html
