---
titulo: "Falco"
tipo: ferramenta
nome: "Falco"
categoria: "Cloud-e-Container"
subcategoria: "Detecção de Comportamento em Runtime (Containers)"
plataformas: ["Linux"]
licenca: "Apache-2.0"
linguagem: "C++"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://falco.org/"
tags:
  - ciberseguranca
  - ferramenta
  - cloud
---

# Falco

> Motor de detecção de comportamento anômalo em tempo real para containers e hosts Linux, projeto da CNCF.

## Como funciona
Monitora chamadas de sistema (syscalls) em tempo real diretamente no kernel (via eBPF ou módulo de kernel) e as compara contra um conjunto de regras declarativas que descrevem comportamento esperado versus suspeito (ex.: um shell sendo aberto dentro de um container que nunca deveria ter um shell interativo), gerando alertas imediatos quando uma regra é violada — funcionando como um EDR especializado em ambientes de container.

## Como usar
Após a instalação (como daemonset em Kubernetes ou serviço no host), regras são definidas em YAML descrevendo condições de syscall suspeitas; alertas gerados podem ser encaminhados a um SIEM ou sistema de resposta automatizada via integrações (Falcosidekick).

## Casos de uso
- Detecção de comportamento anômalo em tempo real dentro de containers
- Resposta automatizada a atividade suspeita em ambientes Kubernetes

## Alternativas
[[kube-hunter]]

## Categoria
[[MOC - Cloud e Container]]

## Link oficial
https://falco.org/
