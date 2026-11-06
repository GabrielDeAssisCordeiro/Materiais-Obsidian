---
titulo: "GoPhish"
tipo: ferramenta
nome: "GoPhish"
categoria: "Ofensivo/Social-Engineering"
subcategoria: "Simulação de Phishing"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "Go"
mitre_attack: ["T1566.002"]
nivel: iniciante
situacao: ativo
link_oficial: "https://getgophish.com/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/social-engineering
  - arsenal-de-ferramentas
---

# GoPhish

> Plataforma de campanhas de phishing com templates, rastreamento de cliques e relatórios para programas de conscientização.

## Como funciona
Gerencia o ciclo completo de uma campanha de phishing — lista de destinatários, template de e-mail, página de destino (landing page) e perfil de envio (SMTP) — e instrumenta cada e-mail e link com identificadores únicos para rastrear com precisão quando cada destinatário abriu o e-mail, clicou no link ou submeteu dados no formulário, consolidando tudo em métricas por campanha.

## Como usar
Após subir o servidor (`./gophish`), acessa-se o painel web administrativo (padrão `localhost:3333`) para cadastrar um perfil de envio, um template de e-mail, uma landing page e o grupo de destinatários; ao lançar a campanha, o painel exibe em tempo real a taxa de abertura, clique e submissão.

## Casos de uso
- Programas recorrentes de conscientização em segurança corporativa
- Métricas de taxa de clique/submissão para medir maturidade organizacional

## Alternativas
[[Social-Engineer Toolkit (SET)]]

## Categoria
[[MOC - Engenharia Social]]

## Link oficial
https://getgophish.com/
