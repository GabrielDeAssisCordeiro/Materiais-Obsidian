---
titulo: "dd / dc3dd"
tipo: ferramenta
nome: "dd / dc3dd"
categoria: "DFIR/Disco-e-Imagem"
subcategoria: "Aquisição Forense via Linha de Comando"
plataformas: ["Linux", "macOS"]
licenca: "GPL (dc3dd) / Padrão Unix (dd)"
linguagem: "C"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://sourceforge.net/projects/dc3dd/"
tags:
  - ciberseguranca
  - ferramenta
  - dfir/disco
  - arsenal-de-ferramentas
---

# dd / dc3dd

> Utilitários de cópia de baixo nível usados para aquisição forense de mídias em ambiente Linux.

## Como funciona
Copiam dados bloco a bloco diretamente do dispositivo de origem para um arquivo de destino, sem interpretar o sistema de arquivos; o `dc3dd` (fork forense do `dd` mantido pelo DC3) adiciona cálculo de hash em tempo real durante a cópia e geração de logs de aquisição, atendendo requisitos formais de documentação forense que o `dd` padrão não oferece nativamente.

## Como usar
`dc3dd if=/dev/sdX of=imagem.dd hash=sha256 log=aquisicao.log` copia o disco de origem calculando o hash simultaneamente e registrando o processo em log; o `dd` tradicional usa sintaxe semelhante (`dd if=/dev/sdX of=imagem.dd bs=4M`) mas sem verificação de integridade embutida.

## Casos de uso
- Aquisição forense em ambientes Linux sem ferramentas gráficas
- Clonagem de mídia para análise offline

## Alternativas
[[FTK Imager]]

## Categoria
[[MOC - Disco e Imagem]]

## Link oficial
https://sourceforge.net/projects/dc3dd/
