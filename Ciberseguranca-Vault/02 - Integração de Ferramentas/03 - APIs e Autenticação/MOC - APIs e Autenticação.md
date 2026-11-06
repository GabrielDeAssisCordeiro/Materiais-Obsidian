---
titulo: "MOC - APIs e Autenticação"
aliases: ["MOC APIs"]
tags:
  - ciberseguranca
  - integracao-de-ferramentas
  - moc
  - apis-e-autenticacao
tipo: moc
nivel: intermediario
criado: 2026-10-26
relacionados:
  - "[[MOC - Integração de Ferramentas]]"
  - "[[REST e Design de APIs de Segurança]]"
  - "[[MOC - Arquitetura e Padrões de Integração]]"
---

# MOC - APIs e Autenticação

## Resumo

APIs e mecanismos de autenticação e autorização usados em integrações de segurança. Volte à [[MOC - Integração de Ferramentas]].

## Conceitos-chave

Contratos, tokens, identidade de máquina e menor privilégio.

## Como funciona

Comece por REST, depois estude autenticação e por fim contratos.

## Notas

- [[REST e Design de APIs de Segurança]] — Fundamentos de REST e riscos de API.
- [[GraphQL e gRPC]] — GraphQL e gRPC: contratos, riscos e controles.
- [[OAuth 2.0 e OIDC]] — Autorização delegada, fluxos e identidade.
- [[API Keys e Gestão de Credenciais]] — Ciclo de vida de chaves e segredos.
- [[mTLS]] — Autenticação mútua na camada de transporte.
- [[JWT]] — Formato, validação e armadilhas.
- [[Escopos e Menor Privilégio]] — Escopos, RBAC e menor privilégio.
- [[Paginação e Versionamento]] — Coleta confiável e evolução de APIs.
- [[OpenAPI]] — Contrato de API e validação automática.

## Exemplo prático

Um conector obtém token via [[OAuth 2.0 e OIDC]], com escopos mínimos ([[Escopos e Menor Privilégio]]), e pagina resultados ([[Paginação e Versionamento]]).

## Boas práticas

Credenciais efêmeras e validação rigorosa de tokens.

## Erros comuns

Autenticar sem autorizar por objeto.

## Referências para aprofundar

- [[OWASP Top 10 - Integração]]

## Veja também

- [[MOC - Integração de Ferramentas]]
- [[MOC - Arquitetura e Padrões de Integração]]
- [[MOC - Desenvolvimento de Ferramentas]]
