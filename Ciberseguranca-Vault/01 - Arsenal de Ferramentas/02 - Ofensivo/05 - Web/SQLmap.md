---
titulo: "SQLmap"
tipo: ferramenta
nome: "SQLmap"
categoria: "Ofensivo/Web"
subcategoria: "Automação de SQL Injection"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "Python"
mitre_attack: ["T1190"]
nivel: intermediario
situacao: ativo
link_oficial: "https://sqlmap.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/web
  - arsenal-de-ferramentas
---

# SQLmap

> Detecta e explora automaticamente vulnerabilidades de SQL injection, incluindo extração de dados.

## Como funciona
Envia uma série sistemática de payloads (boolean-based, time-based, error-based, UNION-based) ao parâmetro informado e analisa diferenças sutis nas respostas (tempo, conteúdo, erros) para confirmar e classificar o tipo de injeção; a partir daí, reconstrói logicamente a estrutura do banco (bancos, tabelas, colunas) sem necessidade de acesso direto, usando apenas as respostas inferidas.

## Como usar
`sqlmap -u "https://alvo.com/item?id=1" --dbs` identifica a injeção no parâmetro `id` e lista os bancos disponíveis; a partir daí, `--tables -D banco`, `--dump -T tabela` aprofundam a extração. Flags como `--risk` e `--level` controlam a agressividade dos testes e `--tamper` aplica scripts de evasão de WAF.

## Casos de uso
- Validação de SQLi identificada manualmente no Burp
- Extração automatizada de esquema de banco de dados em teste autorizado

## Alternativas
Burp Suite (extensões) · NoSQLMap

## Categoria
[[MOC - Web]]

## Link oficial
https://sqlmap.org/
