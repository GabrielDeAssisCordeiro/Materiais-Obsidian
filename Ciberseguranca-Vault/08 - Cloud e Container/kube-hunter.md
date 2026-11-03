---
titulo: "kube-hunter"
tipo: ferramenta
nome: "kube-hunter"
categoria: "Cloud-e-Container"
subcategoria: "Varredura de Segurança Kubernetes"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "Python"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/aquasecurity/kube-hunter"
tags:
  - ciberseguranca
  - ferramenta
  - cloud
---

# kube-hunter

> Ferramenta de varredura ofensiva para identificar vulnerabilidades e más configurações em clusters Kubernetes.

## Como funciona
Executa uma série de testes de reconhecimento e exploração leve contra componentes do cluster (API server, kubelet, dashboards) a partir de um ponto de vista externo, interno ou dentro de um pod, identificando configurações que permitiriam acesso não autorizado à API do cluster ou execução de código em nós, à semelhança de um scanner de vulnerabilidades especializado para Kubernetes.

## Como usar
O modo remoto (`kube-hunter --remote IP`) testa a exposição do cluster a partir de fora; o modo `--pod`, executado dentro de um container do próprio cluster, simula a perspectiva de um atacante que já comprometeu um workload interno.

## Casos de uso
- Avaliação de exposição de componentes do Kubernetes antes de produção
- Simulação de movimentação lateral dentro de um cluster comprometido

## Alternativas
[[Trivy]]

## Categoria
[[MOC - Cloud e Container]]

## Link oficial
https://github.com/aquasecurity/kube-hunter
