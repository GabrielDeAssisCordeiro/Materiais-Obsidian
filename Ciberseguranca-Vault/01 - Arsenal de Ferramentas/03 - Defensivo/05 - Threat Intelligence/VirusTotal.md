---
titulo: "VirusTotal"
tipo: ferramenta
nome: "VirusTotal"
categoria: "Defensivo/Threat-Intelligence"
subcategoria: "Análise de Arquivos/URLs e Reputação"
plataformas: ["Web", "API"]
licenca: "Comercial (consulta básica gratuita)"
linguagem: "N/A"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://www.virustotal.com/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/threat-intel
  - arsenal-de-ferramentas
---

# VirusTotal

> Serviço que agrega o veredito de dezenas de motores antivírus e sandboxes sobre arquivos, URLs e domínios.

## Como funciona
Ao receber um arquivo, hash, URL ou domínio, consulta simultaneamente dezenas de motores antivírus comerciais e serviços de sandbox/reputação, consolidando todos os vereditos em um único relatório que também expõe metadados estáticos do arquivo (hashes, comportamento observado em sandbox, relações com outras amostras já vistas).

## Como usar
A consulta mais simples é colar um hash, URL ou fazer upload de um arquivo diretamente na interface web; a API permite automação (ex.: verificar automaticamente hashes extraídos de um log de EDR) e o uso de 'VT Graph' explora visualmente relações entre amostras e infraestrutura.

## Casos de uso
- Triagem rápida de reputação de arquivo/URL suspeito
- Pivotagem entre amostras de malware relacionadas durante investigação

## Alternativas
[[AlienVault OTX]]

## Categoria
[[MOC - Threat Intelligence]]

## Link oficial
https://www.virustotal.com/
