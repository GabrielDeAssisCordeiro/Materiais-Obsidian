---
titulo: "Faraday"
tipo: ferramenta
nome: "Faraday"
categoria: "Defensivo/Gestao-de-Vulnerabilidades"
subcategoria: "Plataforma Colaborativa de Pentest/VM"
plataformas: ["Linux", "Docker"]
licenca: "GPLv3 (Community)"
linguagem: "Python"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://faradaysec.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/vuln-mgmt
  - arsenal-de-ferramentas
---

# Faraday

> Plataforma colaborativa que centraliza resultados de ferramentas de pentest e scanners em um workspace único.

## Como funciona
Funciona como um repositório central (workspace) para o qual diversas ferramentas de segurança (Nmap, Nessus, Burp, etc.) enviam seus resultados via plugins/integrações, permitindo que múltiplos pentesters trabalhando no mesmo engajamento vejam e colaborem sobre os mesmos achados em tempo real, com métricas e relatórios gerados automaticamente a partir dos dados agregados.

## Como usar
Importa-se a saída de uma ferramenta (ex.: XML do Nmap) para um workspace via interface web ou CLI (`faraday-cli`); achados importados podem ser editados, comentados e exportados em relatório final consolidado do engajamento.

## Casos de uso
- Colaboração em tempo real durante um pentest em equipe
- Consolidação de evidências de múltiplas ferramentas em relatório único

## Alternativas
[[DefectDojo]]

## Categoria
[[MOC - Gestão de Vulnerabilidades]]

## Link oficial
https://faradaysec.com/
