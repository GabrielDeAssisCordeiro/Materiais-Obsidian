---
titulo: "DVWA"
tipo: ferramenta
nome: "DVWA"
categoria: "Plataforma"
subcategoria: "Aplicação Web Vulnerável para Treino"
plataformas: ["Linux", "Docker"]
licenca: "GPLv3"
linguagem: "PHP"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/digininja/DVWA"
tags:
  - ciberseguranca
  - ferramenta
  - plataforma
  - arsenal-de-ferramentas
---

# DVWA

> Damn Vulnerable Web Application: aplicação PHP propositalmente vulnerável para prática de segurança web.

## Como funciona
Implementa deliberadamente as vulnerabilidades mais comuns do OWASP Top 10 (SQLi, XSS, CSRF, upload inseguro de arquivos) em um ambiente controlado, com três níveis de dificuldade de proteção configuráveis (low/medium/high) que permitem praticar a mesma classe de vulnerabilidade sob diferentes graus de mitigação implementada.

## Como usar
Sobe-se a aplicação localmente (via Docker ou LAMP manual), ajusta-se o nível de segurança desejado no painel administrativo e pratica-se cada categoria de vulnerabilidade disponível no menu lateral (ex.: SQL Injection, XSS Reflected) usando ferramentas como Burp Suite/SQLmap contra o próprio ambiente.

## Casos de uso
- Prática isolada de vulnerabilidades web do OWASP Top 10
- Ambiente de ensino para demonstrar diferentes níveis de mitigação

## Alternativas
[[Metasploitable]]

## Categoria
[[MOC - Plataformas, Distros e Labs]]

## Link oficial
https://github.com/digininja/DVWA
