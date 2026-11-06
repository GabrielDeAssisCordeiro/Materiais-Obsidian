---
titulo: "CyberChef"
tipo: ferramenta
nome: "CyberChef"
categoria: "Cripto-e-Stego"
subcategoria: "Canivete Suíço de Codificação/Criptografia"
plataformas: ["Web (self-hosted ou online)"]
licenca: "Apache-2.0"
linguagem: "JavaScript"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://gchq.github.io/CyberChef/"
tags:
  - ciberseguranca
  - ferramenta
  - cripto
  - arsenal-de-ferramentas
---

# CyberChef

> Ferramenta web (desenvolvida pelo GCHQ) para encadear operações de codificação, criptografia e análise de dados.

## Como funciona
Permite montar visualmente um 'pipeline' arrastando e encadeando operações pré-construídas (Base64, XOR, hashing, regex, descompressão) para transformar uma entrada de dados passo a passo, visualizando o resultado intermediário de cada etapa — útil para desofuscar dados sem precisar escrever código para cada transformação.

## Como usar
Cola-se o dado bruto na área de entrada e arrastam-se operações da lista lateral para a área de 'Recipe' (ex.: 'From Base64' seguido de 'XOR' com uma chave); a saída é atualizada em tempo real a cada operação adicionada ou ajustada.

## Casos de uso
- Desofuscação manual de payloads/dados codificados em múltiplas camadas
- Conversão rápida entre formatos de codificação durante análise

## Alternativas
[[OpenSSL]]

## Categoria
[[MOC - Criptografia e Esteganografia]]

## Link oficial
https://gchq.github.io/CyberChef/
