---
titulo: "OWASP ZAP"
tipo: ferramenta
nome: "OWASP ZAP"
categoria: "Ofensivo/Web"
subcategoria: "Scanner Web Open Source"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "Java"
mitre_attack: ["T1190"]
nivel: iniciante
situacao: ativo
link_oficial: "https://www.zaproxy.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/web
  - arsenal-de-ferramentas
---

# OWASP ZAP

> Alternativa open source ao Burp Suite, com scanner automatizado e proxy de interceptação.

## Como funciona
Combina um proxy de interceptação (igual em conceito ao Burp) com um 'spider' que mapeia automaticamente a estrutura da aplicação navegando por links e formulários, e um motor de varredura ativa que injeta payloads conhecidos (XSS, SQLi, path traversal) nos pontos de entrada identificados, classificando achados por risco.

## Como usar
O modo mais rápido é via CLI headless: `zap.sh -cmd -quickurl https://alvo.com -quickout relatorio.html` executa spider + varredura ativa e gera relatório automaticamente. A interface gráfica também permite configurar contexto de autenticação para varrer áreas logadas da aplicação.

## Casos de uso
- Varredura automatizada de aplicações web sem custo de licença
- Integração em pipelines CI/CD para DevSecOps

## Alternativas
[[Burp Suite]] · [[Nikto]]

## Categoria
[[MOC - Web]]

## Link oficial
https://www.zaproxy.org/
