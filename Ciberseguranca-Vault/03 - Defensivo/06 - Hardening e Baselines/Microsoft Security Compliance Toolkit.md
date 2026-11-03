---
titulo: "Microsoft Security Compliance Toolkit"
tipo: ferramenta
nome: "Microsoft Security Compliance Toolkit"
categoria: "Defensivo/Hardening-e-Baselines"
subcategoria: "Baselines de Hardening Windows"
plataformas: ["Windows"]
licenca: "Gratuito (Microsoft)"
linguagem: "N/A"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://learn.microsoft.com/windows/security/threat-protection/security-compliance-toolkit-10"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/hardening
---

# Microsoft Security Compliance Toolkit

> Conjunto de baselines de segurança recomendadas pela Microsoft para Windows e produtos relacionados, em formato de GPO.

## Como funciona
Disponibiliza, para cada versão do Windows/Windows Server, um conjunto de Objetos de Política de Grupo (GPO) pré-configurados implementando as recomendações de hardening da própria Microsoft, junto com uma ferramenta de comparação (Policy Analyzer) que identifica diferenças entre a configuração atual de um ambiente e a baseline recomendada.

## Como usar
Baixa-se o pacote de baseline correspondente à versão do Windows, importam-se os GPOs no Group Policy Management Console (ou localmente via LGPO.exe), e o Policy Analyzer compara a configuração vigente contra a baseline para identificar desvios antes da aplicação.

## Casos de uso
- Hardening padronizado de ambientes Windows corporativos
- Comparação de configuração vigente contra baseline recomendada

## Alternativas
[[CIS-CAT (CIS Benchmarks)]]

## Categoria
[[MOC - Hardening e Baselines]]

## Link oficial
https://learn.microsoft.com/windows/security/threat-protection/security-compliance-toolkit-10
