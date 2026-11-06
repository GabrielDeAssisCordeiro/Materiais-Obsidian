---
titulo: "OpenVAS"
tipo: ferramenta
nome: "OpenVAS"
categoria: "Ofensivo/Scanning-Enum"
subcategoria: "Scanner de Vulnerabilidades Open Source"
plataformas: ["Linux"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: ["T1595.002"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.openvas.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/scanning
  - arsenal-de-ferramentas
---

# OpenVAS

> Scanner de vulnerabilidades open source mantido pela Greenbone, com feed de testes (NVTs) atualizado.

## Como funciona
Funciona de forma semelhante ao Nessus: executa milhares de 'Network Vulnerability Tests' (NVTs) organizados em famílias, atualizados pelo Greenbone Community Feed. A arquitetura é dividida em componentes (scanner, gerenciador, interface web Greenbone Security Assistant) que se comunicam para orquestrar varreduras, armazenar resultados e gerar relatórios.

## Como usar
Após iniciar os serviços (`gvm-start` ou via container), acessa-se a interface web Greenbone Security Assistant, cria-se uma 'Target' com o(s) IP(s) alvo e uma 'Task' associando o target a uma configuração de scan (ex.: Full and Fast). O progresso e os resultados ficam disponíveis em tempo real na própria interface.

## Casos de uso
- Alternativa gratuita ao Nessus em avaliações internas
- Varredura contínua integrada a pipelines de gestão de vulnerabilidades

## Alternativas
[[Nessus]] · [[Qualys]]

## Categoria
[[MOC - Scanning e Enumeração]]

## Link oficial
https://www.openvas.org/
