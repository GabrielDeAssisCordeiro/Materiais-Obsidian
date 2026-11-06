---
titulo: "CFSSL"
tipo: ferramenta
nome: "CFSSL"
categoria: "Defensivo/Segredos-e-PKI"
subcategoria: "Toolkit de PKI/TLS"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "BSD-2-Clause"
linguagem: "Go"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/cloudflare/cfssl"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/pki
  - arsenal-de-ferramentas
---

# CFSSL

> Toolkit da Cloudflare para criação e gestão de autoridades certificadoras (CA) e certificados TLS internos.

## Como funciona
Fornece tanto uma biblioteca quanto ferramentas de linha de comando para as operações completas de uma PKI (geração de chave, assinatura de CSR, emissão e revogação de certificados), podendo operar como uma API HTTP de assinatura centralizada para automatizar a emissão de certificados internos em escala, sem depender de uma CA pública.

## Como usar
Define-se um arquivo de configuração de CA (`ca-config.json`) com perfis de assinatura (validade, usos permitidos) e gera-se a CA raiz (`cfssl gencert -initca csr.json`); certificados de serviços internos são então assinados contra essa CA (`cfssl gencert -ca ca.pem -ca-key ca-key.pem`).

## Casos de uso
- Emissão de certificados TLS internos para microsserviços
- Automação de PKI interna via API de assinatura

## Alternativas
[[step-ca]]

## Categoria
[[MOC - Segredos e PKI]]

## Link oficial
https://github.com/cloudflare/cfssl
