---
titulo: "Sliver"
tipo: ferramenta
nome: "Sliver"
categoria: "Ofensivo/Exploracao"
subcategoria: "Framework C2 Open Source"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv3"
linguagem: "Go"
mitre_attack: ["T1071", "T1105"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/BishopFox/sliver"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/exploracao
---

# Sliver

> Framework C2 multiplataforma, open source, mantido pela Bishop Fox, alternativa ao Cobalt Strike.

## Como funciona
Gera implantes ('sliver') compilados em Go para múltiplas plataformas e arquiteturas, suportando múltiplos protocolos de C2 simultaneamente (mTLS, HTTP/S, DNS, WireGuard) com criptografia ponta a ponta entre implante e servidor. A arquitetura cliente-servidor permite múltiplos operadores conectados ao mesmo servidor C2 de forma colaborativa.

## Como usar
No console (`sliver-server` seguido de `sliver-client` ou modo interativo único), gera-se um implante com `generate --mtls alvo.ip -o implante`, entrega-se o binário ao alvo e, após o callback, interage-se com a sessão via comandos (`use`, `shell`, `execute-assembly` para payloads .NET em memória).

## Casos de uso
- Red team sem custo de licença comercial
- Treinamento de detecção de C2 para blue teams

## Alternativas
[[Cobalt Strike]] · [[Metasploit Framework]] · Havoc

## Categoria
[[MOC - Exploração]]

## Link oficial
https://github.com/BishopFox/sliver
