---
titulo: "HashiCorp Vault"
tipo: ferramenta
nome: "HashiCorp Vault"
categoria: "Defensivo/Segredos-e-PKI"
subcategoria: "Gestão de Segredos"
plataformas: ["Linux", "Windows", "macOS", "Cloud"]
licenca: "BUSL-1.1 (Community) / Comercial"
linguagem: "Go"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://www.vaultproject.io/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/pki
  - arsenal-de-ferramentas
---

# HashiCorp Vault

> Plataforma de gestão centralizada de segredos (senhas, chaves de API, certificados) com controle de acesso granular.

## Como funciona
Armazena segredos de forma criptografada em repouso e os entrega dinamicamente a aplicações/usuários autenticados através de 'engines de segredo' especializadas (KV estático, credenciais dinâmicas de banco de dados geradas sob demanda e com expiração automática, certificados PKI emitidos on-the-fly), reduzindo drasticamente a vida útil e a exposição de credenciais estáticas espalhadas em código ou arquivos de configuração.

## Como usar
Após inicializar e destravar o Vault (`vault operator init`/`unlock`), habilita-se uma 'secrets engine' (`vault secrets enable -path=secret kv`) e políticas de acesso definem quem pode ler/escrever cada caminho; aplicações autenticam via um método (token, AppRole, Kubernetes) e solicitam segredos dinamicamente em tempo de execução.

## Casos de uso
- Eliminação de credenciais estáticas hardcoded em aplicações
- Emissão de credenciais de banco de dados/certificados de curta duração

## Alternativas
[[step-ca]]

## Categoria
[[MOC - Segredos e PKI]]

## Link oficial
https://www.vaultproject.io/
