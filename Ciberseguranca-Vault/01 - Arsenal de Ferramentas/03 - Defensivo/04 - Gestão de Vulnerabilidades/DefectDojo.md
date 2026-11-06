---
titulo: "DefectDojo"
tipo: ferramenta
nome: "DefectDojo"
categoria: "Defensivo/Gestao-de-Vulnerabilidades"
subcategoria: "Gestão de Vulnerabilidades / ASPM"
plataformas: ["Linux", "Docker"]
licenca: "BSD-3-Clause"
linguagem: "Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.defectdojo.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/vuln-mgmt
  - arsenal-de-ferramentas
---

# DefectDojo

> Plataforma open source para centralizar, deduplicar e gerenciar achados de múltiplas ferramentas de varredura.

## Como funciona
Importa resultados de dezenas de scanners diferentes (Nessus, Nuclei, OWASP ZAP, Trivy, etc.) através de parsers específicos para cada formato, normalizando tudo em um modelo de dados único; aplica regras de deduplicação para evitar que o mesmo achado apareça repetido vindo de ferramentas distintas, e organiza o ciclo de vida da remediação por produto e engajamento.

## Como usar
Cria-se um 'Product' e um 'Engagement' (ex.: um pentest ou pipeline de CI específico) e importa-se o relatório bruto do scanner (upload de arquivo XML/JSON); o DefectDojo deduplica automaticamente contra achados já existentes e disponibiliza dashboards de tendência de risco ao longo do tempo.

## Casos de uso
- Consolidação de achados de múltiplos scanners em um único painel
- Rastreamento do ciclo de vida de remediação de vulnerabilidades

## Alternativas
[[Faraday]]

## Categoria
[[MOC - Gestão de Vulnerabilidades]]

## Link oficial
https://www.defectdojo.org/
