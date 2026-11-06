---
titulo: "Cobalt Strike"
tipo: ferramenta
nome: "Cobalt Strike"
categoria: "Ofensivo/Exploracao"
subcategoria: "Plataforma de Simulação de Adversário (C2)"
plataformas: ["Linux (servidor)", "Windows/Linux/macOS (cliente)"]
licenca: "Comercial"
linguagem: "Java"
mitre_attack: ["T1071", "T1105", "T1569"]
nivel: avancado
situacao: ativo
link_oficial: "https://www.cobaltstrike.com/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/exploracao
  - arsenal-de-ferramentas
---

# Cobalt Strike

> Plataforma comercial de red team com C2 (Beacon), engenharia social e movimentação lateral.

## Como funciona
O componente central é o 'Beacon', um implante leve que se comunica com o Teamserver (servidor C2) de forma assíncrona e configurável (HTTP/S, DNS, SMB para movimentação lateral peer-to-peer), com perfis de 'malleable C2' que disfarçam o tráfego para se assemelhar a serviços legítimos e dificultar a detecção por ferramentas de rede.

## Como usar
O operador sobe o Teamserver (`./teamserver <IP> <senha>`) e conecta-se via cliente Aggressor; a partir da interface gráfica, gera-se um 'listener', entrega-se um Beacon ao alvo (ex.: via payload de engenharia social) e, após o callback, utiliza-se o console do Beacon para comandos, pivoteamento e scripts Aggressor Script de automação.

## Casos de uso
- Simulações de adversário (red team) de longa duração
- Exercícios de detecção para equipes blue team (purple team)

## Alternativas
[[Sliver]] · [[Metasploit Framework]] · Brute Ratel

## Categoria
[[MOC - Exploração]]

## Link oficial
https://www.cobaltstrike.com/
