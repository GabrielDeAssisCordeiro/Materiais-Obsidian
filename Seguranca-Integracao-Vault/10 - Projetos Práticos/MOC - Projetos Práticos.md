---
titulo: "MOC - Projetos Práticos"
aliases: []
tags:
  - integracao-seguranca
  - moc
  - projetos
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[Home - Integração]]"
  - "[[Projeto 1 - Conector Trivy para Jira]]"
  - "[[MOC - Segurança da Própria Ferramenta]]"
---

# MOC - Projetos Práticos

## Resumo

Cinco projetos guiados que consolidam o conteúdo do vault. Cada um tem objetivo, pré-requisitos, passo a passo, código de referência, critérios de conclusão e extensões. Volte à [[Home - Integração]].

## Conceitos-chave

Integração, automação, pipeline seguro, enriquecimento e detecção como código.

## Como funciona

Faça na ordem sugerida; os projetos 3 e 4 se combinam naturalmente.

## Notas

- [[Projeto 1 - Conector Trivy para Jira]] — Ler Trivy, deduplicar e abrir issues no Jira.
- [[Projeto 2 - Pipeline CI com Gates de Segurança]] — GitHub Actions com gitleaks, Semgrep, Trivy, SBOM e gate.
- [[Projeto 3 - Enriquecedor de Alertas com VirusTotal e MISP]] — Serviço de reputação com cache, cotas e pontuação explicável.
- [[Projeto 4 - Mini-SOAR com Webhook Fila e Playbook]] — Webhook assinado, fila, playbook e aprovação humana.
- [[Projeto 5 - Pipeline de Detecção como Código com Sigma]] — Regras Sigma com validação, testes e conversão no CI.

> [!warning] Laboratório
> Use apenas ambientes isolados, dados sintéticos e credenciais de teste.

## Exemplo prático

Comece pelo [[Projeto 1 - Conector Trivy para Jira]] e evolua até o [[Projeto 4 - Mini-SOAR com Webhook Fila e Playbook]].

## Boas práticas

Versione tudo e escreva testes antes de integrar com serviços reais.

## Erros comuns

Pular os critérios de conclusão.

## Referências para aprofundar

- [[Home - Integração]]

## Veja também

- [[Home - Integração]]
- [[MOC - Segurança da Própria Ferramenta]]
- [[MOC - Revisão - Integração]]
