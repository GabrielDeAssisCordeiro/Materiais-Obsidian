---
titulo: "zsteg"
tipo: ferramenta
nome: "zsteg"
categoria: "Cripto-e-Stego"
subcategoria: "Detecção de Esteganografia em PNG/BMP"
plataformas: ["Linux", "macOS"]
licenca: "MIT"
linguagem: "Ruby"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/zed-0xff/zsteg"
tags:
  - ciberseguranca
  - ferramenta
  - stego
  - arsenal-de-ferramentas
---

# zsteg

> Ferramenta especializada em detectar dados ocultos em imagens PNG/BMP via técnicas de LSB (bit menos significativo).

## Como funciona
Testa sistematicamente diversas combinações conhecidas de ocultação LSB (diferentes canais de cor, ordens de bit, padrões de varredura) contra a imagem fornecida, reportando quais combinações produzem dados que parecem estruturados (texto legível, cabeçalhos de arquivo reconhecíveis), automatizando o que seria uma busca manual exaustiva por esteganografia simples.

## Como usar
`zsteg imagem.png` roda automaticamente todas as combinações testáveis e lista os resultados mais promissores; `-a` força testar todas as combinações possíveis mesmo as menos prováveis, útil quando o resultado padrão não revela nada óbvio.

## Casos de uso
- Resolução de desafios de CTF envolvendo esteganografia em PNG
- Triagem automatizada de imagens suspeitas de conter dados ocultos

## Alternativas
[[Steghide]]

## Categoria
[[MOC - Criptografia e Esteganografia]]

## Link oficial
https://github.com/zed-0xff/zsteg
