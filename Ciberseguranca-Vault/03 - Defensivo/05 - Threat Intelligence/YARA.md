---
titulo: "YARA"
tipo: ferramenta
nome: "YARA"
categoria: "Defensivo/Threat-Intelligence"
subcategoria: "Regras de Detecção/Caça a Ameaças"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "BSD-3-Clause"
linguagem: "C"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://virustotal.github.io/yara/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/threat-intel
---

# YARA

> Linguagem e motor de criação de regras para identificação e classificação de malware por padrões.

## Como funciona
Permite descrever um padrão de detecção ('regra') combinando strings (textos, bytes hexadecimais, expressões regulares) e condições lógicas sobre a presença, contagem e posição dessas strings dentro de um arquivo ou processo em memória; o motor varre arquivos/memória comparando-os contra o conjunto de regras carregado e reporta quais regras deram match.

## Como usar
Escreve-se uma regra em um arquivo `.yar` definindo `strings` e uma seção `condition`; a varredura é feita com `yara regra.yar arquivo_ou_diretorio` (ou em memória de um processo com `-p PID`), e o mesmo conjunto de regras é amplamente reutilizado por EDRs, sandboxes e no próprio VirusTotal.

## Casos de uso
- Caça a ameaças (threat hunting) por padrões específicos de malware
- Classificação automatizada de amostras por família de malware

## Alternativas
[[VirusTotal]]

## Categoria
[[MOC - Threat Intelligence]]

## Link oficial
https://virustotal.github.io/yara/
