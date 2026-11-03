---
titulo: "ExifTool (metadados — uso dual OSINT)"
tipo: ferramenta
nome: "ExifTool (metadados — uso dual OSINT)"
categoria: "OSINT"
subcategoria: "Extração de Metadados para OSINT"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Perl Artistic License"
linguagem: "Perl"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://exiftool.org/"
tags:
  - ciberseguranca
  - ferramenta
  - osint
---

# ExifTool (metadados — uso dual OSINT)

> Referenciado aqui pela ótica de investigação OSINT; nota completa (uso em triagem de malware) em [[strings - Exiftool (utilitários de triagem)|strings / Exiftool (utilitários de triagem)]], pasta 4.4-Analise-Estatica.

## Como funciona
Ver nota correspondente na pasta de Análise Estática para detalhes técnicos do parser de metadados.

## Como usar
Em contexto OSINT, a extração de metadados de imagens/documentos publicados publicamente (coordenadas GPS embutidas, software e data de criação, nome de autor no sistema) pode revelar informações não intencionalmente divulgadas pela fonte.

## Casos de uso
- Geolocalização de imagens via metadados GPS não removidos
- Atribuição de autoria/origem de documentos vazados

## Alternativas
[[Sherlock]]

## Categoria
[[MOC - OSINT]]

## Link oficial
https://exiftool.org/
