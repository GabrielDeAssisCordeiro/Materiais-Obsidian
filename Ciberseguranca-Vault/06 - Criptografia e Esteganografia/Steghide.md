---
titulo: "Steghide"
tipo: ferramenta
nome: "Steghide"
categoria: "Cripto-e-Stego"
subcategoria: "Esteganografia em Imagens/Áudio"
plataformas: ["Linux", "Windows"]
licenca: "GPLv2"
linguagem: "C++"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://steghide.sourceforge.net/"
tags:
  - ciberseguranca
  - ferramenta
  - stego
---

# Steghide

> Ferramenta clássica para ocultar e extrair dados embutidos em arquivos de imagem (JPEG/BMP) e áudio (WAV/AU).

## Como funciona
Embute os dados a ocultar diretamente nos bits menos significativos dos pixels/amostras de áudio do arquivo portador, de forma que a alteração seja imperceptível a olho/ouvido nu, opcionalmente criptografando o conteúdo embutido com uma senha antes de incorporá-lo, de modo que mesmo sabendo que há dados ocultos, extraí-los exige a senha correta.

## Como usar
`steghide embed -cf imagem.jpg -ef segredo.txt` embute o arquivo `segredo.txt` dentro de `imagem.jpg` (solicitando uma senha); `steghide extract -sf imagem.jpg` reverte o processo, pedindo a mesma senha para recuperar o conteúdo original.

## Casos de uso
- Testes de CTF envolvendo esteganografia clássica
- Demonstração educacional de técnicas de ocultação de dados

## Alternativas
[[zsteg]]

## Categoria
[[MOC - Criptografia e Esteganografia]]

## Link oficial
https://steghide.sourceforge.net/
