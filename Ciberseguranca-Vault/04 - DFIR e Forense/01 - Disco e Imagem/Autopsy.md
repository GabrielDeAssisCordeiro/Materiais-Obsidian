---
titulo: "Autopsy"
tipo: ferramenta
nome: "Autopsy"
categoria: "DFIR/Disco-e-Imagem"
subcategoria: "Plataforma de Análise Forense de Disco"
plataformas: ["Windows", "Linux"]
licenca: "Apache-2.0"
linguagem: "Java"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.autopsy.com/"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/disco
---

# Autopsy

> Interface gráfica forense construída sobre o The Sleuth Kit, para análise completa de imagens de disco.

## Como funciona
Monta a imagem forense em modo somente leitura e aplica módulos de análise (timeline, recuperação de arquivos deletados, análise de hash contra bases conhecidas, extração de artefatos de navegador/e-mail) sobre o sistema de arquivos reconstruído, preservando a cadeia de custódia ao nunca escrever na evidência original.

## Como usar
Cria-se um novo 'Case', adiciona-se a imagem de disco (E01/RAW) como fonte de dados e seleciona-se os módulos de ingestão desejados (Hash Lookup, Keyword Search, Timeline); os resultados ficam navegáveis por árvore de diretórios, timeline unificada ou busca por palavra-chave.

## Casos de uso
- Investigação forense completa de uma imagem de disco apreendida
- Recuperação de arquivos deletados e artefatos de navegação

## Alternativas
[[FTK Imager]] · [[EnCase]]

## Categoria
[[MOC - Disco e Imagem]]

## Link oficial
https://www.autopsy.com/
