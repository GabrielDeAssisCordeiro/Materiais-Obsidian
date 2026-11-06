---
titulo: "step-ca"
tipo: ferramenta
nome: "step-ca"
categoria: "Defensivo/Segredos-e-PKI"
subcategoria: "Autoridade Certificadora Online"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "Apache-2.0"
linguagem: "Go"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://smallstep.com/certificates/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/pki
  - arsenal-de-ferramentas
---

# step-ca

> Autoridade certificadora (CA) online de código aberto com foco em automação e certificados de curta duração.

## Como funciona
Opera como um serviço de CA sempre ativo, expondo um protocolo compatível com ACME (o mesmo usado pelo Let's Encrypt) para emissão automática de certificados internos, com suporte nativo a diversos métodos de provisionamento (OIDC, tokens JWK, webhooks) que permitem automatizar completamente a emissão sem intervenção manual a cada renovação.

## Como usar
Após inicializar a CA (`step ca init`) e subir o serviço (`step-ca config/ca.json`), clientes solicitam certificados via `step ca certificate` ou via protocolo ACME padrão, com renovação automatizável por scripts/cron antes da expiração do certificado de curta duração.

## Casos de uso
- PKI interna totalmente automatizada com renovação contínua
- Certificados de curta duração para reduzir impacto de vazamento de chave

## Alternativas
[[CFSSL]] · [[HashiCorp Vault]]

## Categoria
[[MOC - Segredos e PKI]]

## Link oficial
https://smallstep.com/certificates/
