---
titulo: "ffuf"
tipo: ferramenta
nome: "ffuf"
categoria: "Ofensivo/Web"
subcategoria: "Fuzzer Web"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "Go"
mitre_attack: ["T1595.003"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/ffuf/ffuf"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/web
---

# ffuf

> Fuzzer rápido para descoberta de diretórios, arquivos, subdomínios e parâmetros ocultos.

## Como funciona
Substitui um marcador (`FUZZ`) na URL, cabeçalho ou corpo da requisição por cada entrada de uma wordlist, enviando requisições concorrentes (multithread) e analisando código de status, tamanho de resposta e timing para distinguir recursos reais de páginas de erro padrão (ex.: 'soft 404').

## Como usar
`ffuf -u https://alvo.com/FUZZ -w wordlist.txt -mc 200,301,403` testa cada palavra da wordlist no lugar de `FUZZ` e filtra por códigos de status relevantes; `-fs` filtra por tamanho de resposta para eliminar falsos positivos, e múltiplos pontos `FUZZ` permitem fuzzing combinado (ex.: diretório + extensão).

## Casos de uso
- Descoberta de endpoints ocultos em aplicações web
- Fuzzing de parâmetros para identificar comportamento anômalo

## Alternativas
Gobuster · dirsearch

## Categoria
[[MOC - Web]]

## Link oficial
https://github.com/ffuf/ffuf
