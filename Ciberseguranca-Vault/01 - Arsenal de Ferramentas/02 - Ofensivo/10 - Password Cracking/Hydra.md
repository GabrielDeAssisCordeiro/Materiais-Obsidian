---
titulo: "Hydra"
tipo: ferramenta
nome: "Hydra"
categoria: "Ofensivo/Password-Cracking"
subcategoria: "Força Bruta em Serviços de Rede"
plataformas: ["Linux", "macOS", "Windows"]
licenca: "AGPL-3.0"
linguagem: "C"
mitre_attack: ["T1110.001"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/vanhauser-thc/thc-hydra"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/senha
  - arsenal-de-ferramentas
---

# Hydra

> Ferramenta de força bruta para dezenas de protocolos de rede (SSH, FTP, RDP, HTTP-Form, etc.).

## Como funciona
Para cada protocolo suportado, implementa o cliente mínimo necessário para tentar autenticação (handshake SSH, requisição HTTP com formulário de login, etc.) e itera sobre combinações de usuário/senha fornecidas, usando múltiplas conexões paralelas para acelerar o processo e reportando quais combinações resultaram em autenticação bem-sucedida.

## Como usar
`hydra -l usuario -P wordlist.txt ssh://alvo.ip` testa um usuário fixo contra uma wordlist de senhas via SSH; `-L` permite também uma lista de usuários, e módulos HTTP exigem especificar o formato exato do formulário de login (`http-post-form` com os campos e a string de falha esperada).

## Casos de uso
- Teste de robustez de autenticação em serviços expostos
- Validação de bloqueio de conta após tentativas (lockout policy)

## Alternativas
Medusa · [[CrackMapExec]]

## Categoria
[[MOC - Password Cracking]]

## Link oficial
https://github.com/vanhauser-thc/thc-hydra
