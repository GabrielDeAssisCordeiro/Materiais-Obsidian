---
titulo: "CIS-CAT (CIS Benchmarks)"
tipo: ferramenta
nome: "CIS-CAT (CIS Benchmarks)"
categoria: "Defensivo/Hardening-e-Baselines"
subcategoria: "Avaliação de Baseline de Segurança"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Gratuito (uso não-comercial) / Comercial"
linguagem: "Java"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.cisecurity.org/cis-benchmarks"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/hardening
---

# CIS-CAT (CIS Benchmarks)

> Ferramenta de avaliação automatizada de conformidade com os CIS Benchmarks (baselines de hardening).

## Como funciona
Compara a configuração atual de um sistema (serviços habilitados, políticas de senha, permissões de arquivo) ponto a ponto contra as recomendações detalhadas publicadas nos CIS Benchmarks para aquela plataforma específica, atribuindo um score percentual de conformidade e listando exatamente quais controles falharam.

## Como usar
Executa-se o CIS-CAT Assessor localmente no sistema a avaliar, selecionando o benchmark correspondente ao SO/aplicação instalado; o relatório gerado (HTML/texto) lista cada controle avaliado, o resultado (pass/fail) e a recomendação de remediação associada.

## Casos de uso
- Auditoria de conformidade de hardening antes de certificações/compliance
- Baseline de configuração segura para novos servidores

## Alternativas
[[Lynis]] · [[Microsoft Security Compliance Toolkit]]

## Categoria
[[MOC - Hardening e Baselines]]

## Link oficial
https://www.cisecurity.org/cis-benchmarks
