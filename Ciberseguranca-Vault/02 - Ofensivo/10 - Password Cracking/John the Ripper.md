---
titulo: "John the Ripper"
tipo: ferramenta
nome: "John the Ripper"
categoria: "Ofensivo/Password-Cracking"
subcategoria: "Quebra de Senhas"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: ["T1110.002"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.openwall.com/john/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/senha
---

# John the Ripper

> Ferramenta clássica de quebra de senhas com suporte a múltiplos formatos de hash e modo "jumbo" comunitário.

## Como funciona
Detecta automaticamente o formato do hash informado (ou aceita indicação manual) e aplica, em sequência, diferentes modos de ataque (wordlist com regras, incremental/força bruta, modo single baseado em dados do próprio usuário) otimizados primariamente para CPU, com a versão comunitária 'jumbo' adicionando suporte a formatos extras (arquivos ZIP, PDF, documentos protegidos).

## Como usar
`john --wordlist=wordlist.txt hashes.txt` roda ataque de dicionário contra o arquivo de hashes; ferramentas auxiliares como `zip2john`/`pdf2john` convertem arquivos protegidos em um formato de hash que o John consegue processar antes da quebra propriamente dita.

## Casos de uso
- Quebra de hashes de arquivos (zip, PDF, documentos protegidos)
- Complemento ao Hashcat em ambientes sem GPU

## Alternativas
[[Hashcat]]

## Categoria
[[MOC - Password Cracking]]

## Link oficial
https://www.openwall.com/john/
