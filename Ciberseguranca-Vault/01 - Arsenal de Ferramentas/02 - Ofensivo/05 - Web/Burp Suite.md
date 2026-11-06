---
titulo: "Burp Suite"
tipo: ferramenta
nome: "Burp Suite"
categoria: "Ofensivo/Web"
subcategoria: "Proxy de Interceptação Web"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Comercial (Community gratuita)"
linguagem: "Java"
mitre_attack: ["T1190"]
nivel: intermediario
situacao: ativo
link_oficial: "https://portswigger.net/burp"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/web
  - arsenal-de-ferramentas
---

# Burp Suite

> Proxy de interceptação para análise e manipulação de tráfego HTTP/S em testes de aplicações web.

## Como funciona
Posiciona-se como proxy entre o navegador e a aplicação alvo, interceptando e permitindo a edição manual de cada requisição/resposta antes do envio. Módulos complementares (Repeater para reenvio manual, Intruder para automação de ataques parametrizados, Scanner — versão Pro — para varredura automatizada) compartilham o mesmo histórico de tráfego capturado.

## Como usar
Configura-se o proxy do navegador (ou usa-se o Chromium embutido) para apontar para 127.0.0.1:8080, instala-se o certificado CA do Burp para interceptar HTTPS, e navega-se normalmente pela aplicação; requisições interessantes são enviadas ao Repeater (edição manual) ou Intruder (fuzzing automatizado com listas de payloads).

## Casos de uso
- Teste manual de lógica de negócio e vulnerabilidades web (OWASP Top 10)
- Automação de ataques de força bruta e fuzzing via Intruder

## Alternativas
[[OWASP ZAP]]

## Categoria
[[MOC - Web]]

## Link oficial
https://portswigger.net/burp
