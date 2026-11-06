---
titulo: "Nessus"
tipo: ferramenta
nome: "Nessus"
categoria: "Ofensivo/Scanning-Enum"
subcategoria: "Scanner de Vulnerabilidades"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Comercial (Essentials gratuito limitado)"
linguagem: "N/A"
mitre_attack: ["T1595.002"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.tenable.com/products/nessus"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/scanning
  - arsenal-de-ferramentas
---

# Nessus

> Scanner de vulnerabilidades com base extensa de plugins para identificação de CVEs e más configurações.

## Como funciona
Mantém um feed de 'plugins' (scripts de verificação) atualizado diariamente pela Tenable, cada um correspondendo a uma vulnerabilidade, configuração insegura ou prática de compliance específica. Durante o scan, combina varredura de portas, detecção de serviço/versão e, quando possível, autenticação no host (via SSH/SMB) para checagens mais profundas e precisas, reduzindo falsos positivos.

## Como usar
Via interface web, cria-se uma 'Policy' escolhendo o template (ex.: Basic Network Scan, Advanced), define-se o(s) alvo(s) e, opcionalmente, credenciais para scan autenticado. Após a execução, o relatório classifica achados por severidade (CVSS) e permite exportação em PDF/CSV/Nessus XML.

## Casos de uso
- Avaliação de vulnerabilidades em escopo de compliance
- Varredura periódica de infraestrutura interna

## Alternativas
[[OpenVAS]] · [[Qualys]]

## Categoria
[[MOC - Scanning e Enumeração]]

## Link oficial
https://www.tenable.com/products/nessus
