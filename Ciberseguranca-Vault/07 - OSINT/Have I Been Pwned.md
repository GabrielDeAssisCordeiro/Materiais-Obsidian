---
titulo: "Have I Been Pwned"
tipo: ferramenta
nome: "Have I Been Pwned"
categoria: "OSINT"
subcategoria: "Consulta de Vazamentos de Dados"
plataformas: ["Web", "API"]
licenca: "Gratuito (consulta) / Comercial (API em massa)"
linguagem: "N/A"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://haveibeenpwned.com/"
tags:
  - ciberseguranca
  - ferramenta
  - osint
---

# Have I Been Pwned

> Serviço que permite verificar se um e-mail ou senha apareceu em vazamentos de dados conhecidos publicamente.

## Como funciona
Mantém um banco agregado de bilhões de registros provenientes de vazamentos de dados publicamente divulgados, indexados por e-mail (e, para senhas, por hash SHA-1 via um mecanismo de k-anonimato que evita enviar a senha completa ao serviço), permitindo verificar rapidamente se uma credencial específica já foi exposta sem comprometer a privacidade da consulta.

## Como usar
A consulta básica é feita digitando o e-mail no site, que lista em quais vazamentos conhecidos aquele e-mail apareceu; a verificação de senha usa o endpoint de k-anonimato, enviando apenas os primeiros caracteres do hash SHA-1 da senha e recebendo de volta todos os sufixos correspondentes para comparação local.

## Casos de uso
- Verificação de exposição de credenciais corporativas em vazamentos públicos
- Validação de política de senha contra bases de senhas comprometidas

## Alternativas
[[MISP]]

## Categoria
[[MOC - OSINT]]

## Link oficial
https://haveibeenpwned.com/
