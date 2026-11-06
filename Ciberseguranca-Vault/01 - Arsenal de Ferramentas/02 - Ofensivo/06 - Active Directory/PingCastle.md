---
titulo: "PingCastle"
tipo: ferramenta
nome: "PingCastle"
categoria: "Ofensivo/Active-Directory"
subcategoria: "Auditoria de Active Directory"
plataformas: ["Windows"]
licenca: "Comercial (Basic gratuito não-comercial)"
linguagem: "C#"
mitre_attack: ["T1482"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.pingcastle.com/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/ad
  - arsenal-de-ferramentas
---

# PingCastle

> Audita a postura de segurança de um domínio AD e gera relatório de risco com mapa de maturidade.

## Como funciona
Executa, a partir de uma conta de domínio comum (sem necessidade de privilégio elevado), uma bateria de consultas LDAP que avaliam dezenas de indicadores de risco conhecidos (delegações inseguras, políticas de senha fracas, objetos obsoletos, confianças mal configuradas), pontuando o domínio em categorias de risco segundo uma metodologia própria inspirada em frameworks de maturidade.

## Como usar
Executa-se `PingCastle.exe --healthcheck` a partir de uma máquina ingressada no domínio; o resultado é um relatório HTML com pontuação de risco por categoria (Stale Objects, Privileged Accounts, Trusts, Anomalies) e recomendações específicas de remediação.

## Casos de uso
- Avaliação rápida de risco de AD sem exploração ativa
- Relatório executivo de maturidade de segurança para gestão

## Alternativas
[[BloodHound]]

## Categoria
[[MOC - Active Directory]]

## Link oficial
https://www.pingcastle.com/
