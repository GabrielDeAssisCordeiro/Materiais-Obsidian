---
titulo: "FTK Imager"
tipo: ferramenta
nome: "FTK Imager"
categoria: "DFIR/Disco-e-Imagem"
subcategoria: "Aquisição Forense de Imagem"
plataformas: ["Windows"]
licenca: "Gratuito (Exterro)"
linguagem: "N/A"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://www.exterro.com/digital-forensics-software/ftk-imager"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/disco
  - arsenal-de-ferramentas
---

# FTK Imager

> Ferramenta gratuita para criação forense de imagens bit-a-bit de discos e visualização rápida de evidências.

## Como funciona
Realiza a cópia bit-a-bit (setor por setor) de uma mídia de origem, calculando hashes criptográficos (MD5/SHA1) antes e depois da aquisição para comprovar a integridade da imagem gerada, condição essencial para a cadeia de custódia em processos forenses; também permite visualizar o conteúdo de uma imagem já existente sem montá-la no sistema operacional.

## Como usar
No menu 'File > Create Disk Image', seleciona-se a mídia de origem (física, lógica ou já uma imagem) e o formato de destino (E01, RAW); ao final, o relatório de verificação confirma se os hashes de origem e destino coincidem, validando a integridade da cópia.

## Casos de uso
- Aquisição forense preservando a cadeia de custódia
- Triagem rápida de uma imagem sem análise aprofundada

## Alternativas
[[Autopsy]] · [[dd - dc3dd|dd / dc3dd]]

## Categoria
[[MOC - Disco e Imagem]]

## Link oficial
https://www.exterro.com/digital-forensics-software/ftk-imager
