---
titulo: "CeWL"
tipo: ferramenta
nome: "CeWL"
categoria: "Ofensivo/Password-Cracking"
subcategoria: "Geração de Wordlist"
plataformas: ["Linux", "macOS"]
licenca: "GPLv2"
linguagem: "Ruby"
mitre_attack: ["T1589"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/digininja/CeWL"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/senha
  - arsenal-de-ferramentas
---

# CeWL

> Gera wordlists customizadas a partir do conteúdo textual de um site alvo.

## Como funciona
Faz crawling do site informado até uma profundidade configurável, extrai todas as palavras do conteúdo textual das páginas visitadas e produz uma lista de palavras únicas (respeitando um tamanho mínimo), partindo da premissa de que senhas corporativas frequentemente incorporam termos específicos do negócio, produtos ou nomes presentes no próprio site.

## Como usar
`cewl https://alvo.com -d 2 -m 5 -w wordlist.txt` faz crawling até profundidade 2, mantém apenas palavras com 5+ caracteres e salva o resultado em arquivo; a wordlist gerada é tipicamente combinada com regras de mutação do Hashcat/John para aumentar a cobertura.

## Casos de uso
- Criação de wordlist contextual para ataques de senha direcionados
- Complemento a Hashcat/Hydra com termos específicos da organização

## Alternativas
crunch

## Categoria
[[MOC - Password Cracking]]

## Link oficial
https://github.com/digininja/CeWL
