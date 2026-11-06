---
titulo: "searchsploit"
tipo: ferramenta
nome: "searchsploit"
categoria: "Ofensivo/Exploracao"
subcategoria: "Busca de Exploits"
plataformas: ["Linux", "macOS"]
licenca: "GPLv2"
linguagem: "Bash/Perl"
mitre_attack: ["T1588.005"]
nivel: iniciante
situacao: ativo
link_oficial: "https://www.exploit-db.com/searchsploit"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/exploracao
  - arsenal-de-ferramentas
---

# searchsploit

> Interface de linha de comando offline para a base de dados do Exploit-DB.

## Como funciona
Mantém um espelho local (clonado via git) de todo o repositório Exploit-DB, incluindo os códigos-fonte dos exploits, e indexa os títulos/metadados em um arquivo CSV para buscas rápidas por palavra-chave, sem depender de conexão à internet.

## Como usar
`searchsploit apache 2.4.49` busca por termos no título; `-m` copia o exploit encontrado para o diretório atual para uso/edição e `searchsploit -u` atualiza a base local. A flag `-x` exibe o conteúdo do exploit diretamente no terminal antes de copiá-lo.

## Casos de uso
- Identificação rápida de exploits públicos para versão de serviço detectada
- Trabalho offline em ambientes isolados (labs, CTFs)

## Alternativas
[[ExploitDB]] · [[Metasploit Framework]]

## Categoria
[[MOC - Exploração]]

## Link oficial
https://www.exploit-db.com/searchsploit
