---
titulo: "Trivy"
tipo: ferramenta
nome: "Trivy"
categoria: "Cloud-e-Container"
subcategoria: "Scanner de Vulnerabilidades em Containers/IaC"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "Go"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://aquasecurity.github.io/trivy/"
tags:
  - ciberseguranca
  - ferramenta
  - cloud
---

# Trivy

> Scanner all-in-one para vulnerabilidades em imagens de container, dependências de código e configuração IaC.

## Como funciona
Analisa as camadas de uma imagem de container identificando pacotes de sistema e bibliotecas de linguagem instalados, comparando suas versões contra bases de dados de vulnerabilidades conhecidas (CVE), e aplica também regras de boas práticas sobre arquivos de infraestrutura como código (Terraform, Dockerfile, Kubernetes manifests) para detectar más configurações antes mesmo do deploy.

## Como usar
`trivy image nome-da-imagem:tag` varre uma imagem de container já construída listando CVEs por severidade; `trivy config ./terraform/` varre arquivos de infraestrutura como código em busca de más configurações, sendo facilmente integrável a pipelines CI/CD para bloquear builds com vulnerabilidades críticas.

## Casos de uso
- Varredura de vulnerabilidades em imagens Docker antes do deploy
- Checagem de más configurações em arquivos Terraform/Kubernetes

## Alternativas
[[Docker Bench for Security]]

## Categoria
[[MOC - Cloud e Container]]

## Link oficial
https://aquasecurity.github.io/trivy/
