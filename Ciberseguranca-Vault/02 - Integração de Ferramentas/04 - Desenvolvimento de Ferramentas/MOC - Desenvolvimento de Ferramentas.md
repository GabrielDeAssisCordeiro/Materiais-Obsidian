---
titulo: "MOC - Desenvolvimento de Ferramentas"
aliases: ["MOC Desenvolvimento"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - moc
  - desenvolvimento-de-ferramentas
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[MOC - Integração de Ferramentas]]"
  - "[[Escolha de Linguagem - Python e Go]]"
  - "[[MOC - APIs e Autenticação]]"
---

# MOC - Desenvolvimento de Ferramentas

## Resumo

Como construir ferramentas de segurança de forma organizada, testável e segura. Volte à [[MOC - Integração de Ferramentas]].

## Conceitos-chave

Estrutura, CLI, extensibilidade, parsing defensivo, testes e empacotamento.

## Como funciona

Siga a ordem: linguagem, estrutura, CLI, plugins, parsing, testes, empacotamento e logging.

## Notas

- [[Escolha de Linguagem - Python e Go]] — Python vs. Go e critérios de decisão.
- [[Estrutura de Projeto]] — Layout, camadas e fronteiras do projeto.
- [[CLI de Segurança]] — Argumentos, saídas e exit codes como gate.
- [[Plugins e Extensões]] — Extensibilidade com entry points e allowlist.
- [[Parsing de Formatos - SARIF JSON e XML]] — SARIF, JSON e XML com parsing defensivo.
- [[Testes - Unitários Integração e Contratos]] — Unitários, integração e contratos.
- [[Empacotamento e Containers]] — Wheel, binário e containers mínimos.
- [[Logging e Configuração Segura]] — Logs estruturados, redação e configuração segura.

## Exemplo prático

Uma CLI ([[CLI de Segurança]]) lê SARIF ([[Parsing de Formatos - SARIF JSON e XML]]) e devolve exit code para o gate.

## Boas práticas

Domínio sem I/O, segredos fora do código e logs redigidos.

## Erros comuns

Parsers sem validação e containers como root.

## Referências para aprofundar

- [[SDLC e SSDLC]]

## Veja também

- [[MOC - Integração de Ferramentas]]
- [[MOC - APIs e Autenticação]]
- [[MOC - Integração com Ferramentas de Segurança]]
