---
titulo: "ScoutSuite"
tipo: ferramenta
nome: "ScoutSuite"
categoria: "Ofensivo/Cloud"
subcategoria: "Auditoria Multi-Cloud"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "Python"
mitre_attack: ["T1526"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/nccgroup/ScoutSuite"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/cloud
---

# ScoutSuite

> Audita configurações de segurança em AWS, Azure, GCP e outras clouds, gerando relatório HTML navegável.

## Como funciona
Usa as APIs oficiais somente-leitura de cada provedor cloud para coletar o inventário completo de configurações (redes, armazenamento, IAM, bancos de dados) e avalia esse inventário contra um conjunto de regras de boas práticas conhecidas, classificando cada achado por nível de risco em um relatório visual interativo, sem necessidade de credenciais de escrita.

## Como usar
`scout aws --profile perfil` usa um profile de credenciais AWS já configurado localmente para coletar e analisar o ambiente; equivalentes existem para `azure` e `gcp`. O relatório HTML gerado é navegável por serviço e por nível de severidade.

## Casos de uso
- Varredura inicial de postura de segurança cloud multi-provedor
- Identificação de buckets/storage expostos publicamente

## Alternativas
[[Prowler]] · [[CloudSploit]]

## Categoria
[[MOC - Cloud Ofensivo]]

## Link oficial
https://github.com/nccgroup/ScoutSuite
