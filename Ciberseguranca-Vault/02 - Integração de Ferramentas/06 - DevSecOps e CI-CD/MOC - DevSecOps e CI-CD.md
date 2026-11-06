---
titulo: "MOC - DevSecOps e CI-CD"
aliases: ["MOC DevSecOps"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - moc
  - devsecops
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[MOC - Integração de Ferramentas]]"
  - "[[Security Gates e Shift-Left]]"
  - "[[MOC - Integração com Ferramentas de Segurança]]"
---

# MOC - DevSecOps e CI-CD

## Resumo

Segurança integrada ao pipeline: gates, CI/CD, cadeia de suprimentos e políticas como código. Volte à [[MOC - Integração de Ferramentas]].

## Conceitos-chave

Shift-left, proveniência, assinatura, SBOM e políticas versionadas.

## Como funciona

Comece pelos gates, passe pelas plataformas de CI e conclua com cadeia de suprimentos e políticas.

## Notas

- [[Security Gates e Shift-Left]] — Shift-left e gates bloqueantes calibrados.
- [[GitHub Actions]] — Workflows seguros, permissões e SARIF.
- [[GitLab CI e Jenkins]] — Templates de segurança e Jenkinsfile endurecido.
- [[Pré-commit Hooks]] — Verificações locais antes do commit.
- [[SBOM - CycloneDX e SPDX]] — Inventário de componentes com CycloneDX e SPDX.
- [[Assinatura de Artefatos - Sigstore e cosign]] — Assinatura keyless e verificação de identidade.
- [[SLSA]] — Níveis de garantia da cadeia de build.
- [[Políticas como Código - OPA e Rego]] — Policy as code com Rego e Conftest.
- [[IaC Scanning - Checkov e tfsec]] — Checkov e Trivy config para infraestrutura.

## Exemplo prático

Um PR dispara [[GitHub Actions]] com varreduras; a imagem gera [[SBOM - CycloneDX e SPDX]], é assinada ([[Assinatura de Artefatos - Sigstore e cosign]]) e verificada por políticas ([[Políticas como Código - OPA e Rego]]).

## Boas práticas

Pipeline como código crítico, com revisão e privilégio mínimo.

## Erros comuns

Gates que travam o time e verificações nunca consumidas.

## Referências para aprofundar

- [[SDLC e SSDLC]]

## Veja também

- [[MOC - Integração de Ferramentas]]
- [[MOC - Integração com Ferramentas de Segurança]]
- [[MOC - Automação e Orquestração]]
