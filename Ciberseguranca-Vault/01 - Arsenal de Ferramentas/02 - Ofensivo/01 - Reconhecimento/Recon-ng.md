---
titulo: "Recon-ng"
tipo: ferramenta
nome: "Recon-ng"
categoria: "Ofensivo/Reconhecimento"
subcategoria: "Framework de OSINT"
plataformas: ["Linux", "macOS"]
licenca: "GPLv3"
linguagem: "Python"
mitre_attack: ["T1596", "T1593"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/lanmaster53/recon-ng"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/recon
  - arsenal-de-ferramentas
---

# Recon-ng

> Framework modular estilo Metasploit para automação de reconhecimento web via módulos e APIs.

## Como funciona
Organiza o reconhecimento em 'workspaces' por cliente/engajamento, dentro dos quais módulos independentes (instalados via marketplace interno) consultam APIs de terceiros, bancos de dados de vazamento, WHOIS e mecanismos de busca. Os resultados de um módulo (ex.: domínios encontrados) alimentam automaticamente a entrada de outros módulos, criando um pipeline de coleta encadeado armazenado em um banco SQLite local.

## Como usar
Inicia-se com `recon-ng`, cria-se um workspace (`workspaces create cliente`), instalam-se módulos (`marketplace install all`) e carrega-se um módulo (`modules load recon/domains-hosts/hackertarget`). Após `options set SOURCE alvo.com` e `run`, os resultados ficam disponíveis para os módulos seguintes e podem ser exportados em relatório.

## Casos de uso
- Pipeline de coleta OSINT reutilizável
- Integração com bancos de dados de workspace por cliente

## Alternativas
[[theHarvester]] · [[SpiderFoot]] · [[Maltego]]

## Categoria
[[MOC - Reconhecimento]]

## Link oficial
https://github.com/lanmaster53/recon-ng
