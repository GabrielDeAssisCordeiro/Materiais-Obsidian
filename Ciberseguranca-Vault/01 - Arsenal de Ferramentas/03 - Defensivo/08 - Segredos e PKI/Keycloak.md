---
titulo: "Keycloak"
tipo: ferramenta
nome: "Keycloak"
categoria: "Defensivo/Segredos-e-PKI"
subcategoria: "IAM / SSO Open Source"
plataformas: ["Linux", "Docker"]
licenca: "Apache-2.0"
linguagem: "Java"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.keycloak.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/pki
  - arsenal-de-ferramentas
---

# Keycloak

> Plataforma open source de gestão de identidade e acesso (IAM) com suporte a SSO, OAuth2/OIDC e SAML.

## Como funciona
Centraliza a autenticação e autorização de múltiplas aplicações em um único provedor de identidade, implementando os protocolos padrão da indústria (OAuth2, OpenID Connect, SAML) e federando-se opcionalmente com diretórios externos (LDAP/Active Directory), permitindo single sign-on, MFA e políticas de acesso centralizadas sem que cada aplicação precise implementar sua própria lógica de autenticação.

## Como usar
Cria-se um 'Realm' representando o domínio de identidade da organização, cadastram-se os 'Clients' (aplicações que usarão o Keycloak para autenticação) e configuram-se fluxos de autenticação (incluindo MFA); aplicações integram-se via bibliotecas padrão OIDC/SAML apontando para o endpoint do Keycloak.

## Casos de uso
- SSO centralizado para múltiplas aplicações internas
- Federação de identidade com Active Directory/LDAP existente

## Alternativas
[[HashiCorp Vault]]

## Categoria
[[MOC - Segredos e PKI]]

## Link oficial
https://www.keycloak.org/
