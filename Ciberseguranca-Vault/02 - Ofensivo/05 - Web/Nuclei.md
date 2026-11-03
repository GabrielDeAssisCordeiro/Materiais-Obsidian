---
titulo: "Nuclei"
tipo: ferramenta
nome: "Nuclei"
categoria: "Ofensivo/Web"
subcategoria: "Scanner Baseado em Templates"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "Go"
mitre_attack: ["T1190", "T1595.002"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/projectdiscovery/nuclei"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/web
---

# Nuclei

> Scanner de vulnerabilidades rápido, dirigido por templates YAML comunitários (CVEs, CVEs, misconfig).

## Como funciona
Cada verificação é descrita declarativamente em um template YAML (requisição a enviar, padrão esperado na resposta para confirmar o achado), mantidos em um repositório comunitário atualizado constantemente com novos CVEs; o motor executa milhares desses templates em paralelo contra um ou mais alvos, sem precisar de código customizado por vulnerabilidade.

## Como usar
`nuclei -u https://alvo.com -t cves/` roda apenas templates da categoria CVEs contra um alvo; `-l` aceita lista de alvos para varredura em massa, e `-severity critical,high` filtra por gravidade. Também é possível escrever templates próprios para vulnerabilidades específicas de uma aplicação interna.

## Casos de uso
- Varredura em massa de CVEs conhecidos em bug bounty
- Integração em pipelines de varredura contínua

## Alternativas
[[Nikto]] · [[OWASP ZAP]]

## Categoria
[[MOC - Web]]

## Link oficial
https://github.com/projectdiscovery/nuclei
