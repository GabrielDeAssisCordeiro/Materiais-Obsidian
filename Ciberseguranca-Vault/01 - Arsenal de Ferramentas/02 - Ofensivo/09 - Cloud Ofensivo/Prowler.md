---
titulo: "Prowler"
tipo: ferramenta
nome: "Prowler"
categoria: "Ofensivo/Cloud"
subcategoria: "Auditoria de Compliance AWS"
plataformas: ["Linux", "macOS"]
licenca: "Apache-2.0"
linguagem: "Python"
mitre_attack: ["T1526"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/prowler-cloud/prowler"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/cloud
  - arsenal-de-ferramentas
---

# Prowler

> Ferramenta de auditoria de segurança e compliance (CIS, PCI-DSS, GDPR) para AWS, Azure e GCP.

## Como funciona
Mapeia cada verificação diretamente a controles de frameworks de compliance reconhecidos (CIS Benchmarks, PCI-DSS, GDPR, NIST), coletando a configuração via API do provedor cloud e produzindo não apenas um achado técnico, mas também a referência exata do controle de compliance violado — útil tanto para times de segurança quanto de auditoria.

## Como usar
`prowler aws` executa a bateria completa de checagens contra a conta configurada no profile padrão da AWS CLI; é possível rodar apenas um framework específico (`-g cis_2.0`) ou exportar o resultado em múltiplos formatos (CSV, JSON, HTML) para relatórios de auditoria.

## Casos de uso
- Auditoria de compliance recorrente em múltiplas contas cloud
- Geração de relatório para auditorias regulatórias

## Alternativas
[[ScoutSuite]] · [[CloudSploit]]

## Categoria
[[MOC - Cloud Ofensivo]]

## Link oficial
https://github.com/prowler-cloud/prowler
