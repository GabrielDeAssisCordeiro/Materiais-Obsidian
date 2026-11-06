---
titulo: "Nikto"
tipo: ferramenta
nome: "Nikto"
categoria: "Ofensivo/Scanning-Enum"
subcategoria: "Scanner Web Básico"
plataformas: ["Linux", "macOS", "Windows"]
licenca: "GPLv2"
linguagem: "Perl"
mitre_attack: ["T1595.002"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/sullo/nikto"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/scanning
  - arsenal-de-ferramentas
---

# Nikto

> Scanner web que identifica arquivos perigosos, versões desatualizadas e más configurações de servidor.

## Como funciona
Mantém um banco de assinaturas de milhares de arquivos/caminhos conhecidos por serem problemáticos (scripts de administração esquecidos, arquivos de backup, painéis expostos) e testa a presença de cada um via requisições HTTP diretas, além de inspecionar cabeçalhos de resposta para identificar versão de servidor desatualizada e cabeçalhos de segurança ausentes.

## Como usar
O uso básico é `nikto -h https://alvo.com`; parâmetros como `-ssl` forçam HTTPS, `-Tuning` restringe categorias de teste (ex.: apenas XSS) e `-Format` define o formato do relatório (txt, html, csv). Por ser bastante ruidoso (gera muitas requisições identificáveis em logs), costuma ser usado em fases onde discrição não é prioridade.

## Casos de uso
- Varredura rápida de más configurações em servidores web
- Complemento ao Burp Suite em fase de reconhecimento web

## Alternativas
[[Burp Suite]] · [[Nuclei]]

## Categoria
[[MOC - Scanning e Enumeração]]

## Link oficial
https://github.com/sullo/nikto
