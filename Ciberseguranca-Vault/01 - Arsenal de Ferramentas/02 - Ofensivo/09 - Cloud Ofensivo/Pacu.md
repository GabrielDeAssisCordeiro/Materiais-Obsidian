---
titulo: "Pacu"
tipo: ferramenta
nome: "Pacu"
categoria: "Ofensivo/Cloud"
subcategoria: "Framework de Exploração AWS"
plataformas: ["Linux", "macOS"]
licenca: "BSD-3-Clause"
linguagem: "Python"
mitre_attack: ["T1078.004"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/RhinoSecurityLabs/pacu"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/cloud
  - arsenal-de-ferramentas
---

# Pacu

> Framework de exploração ofensiva para ambientes AWS: escalonamento de privilégio, persistência e exfiltração.

## Como funciona
Organiza-se em módulos que chamam diretamente a API da AWS usando credenciais fornecidas (chaves de acesso ou tokens assumidos), automatizando cadeias de ataque conhecidas em IAM — como enumerar permissões efetivas de uma credencial, identificar políticas mal configuradas que permitem escalonamento de privilégio, e explorar essas brechas de forma sequencial — mantendo um banco de dados de sessão com o que já foi descoberto.

## Como usar
No console interativo (`pacu`), importam-se credenciais (`import_keys --all`) e executam-se módulos específicos, como `run iam__enum_permissions` para mapear privilégios efetivos ou módulos de escalonamento de privilégio que testam automaticamente cadeias de abuso conhecidas de IAM.

## Casos de uso
- Avaliação de configurações IAM mal implementadas
- Simulação de escalonamento de privilégio em conta AWS de teste

## Alternativas
[[ScoutSuite]] · [[Prowler]]

## Categoria
[[MOC - Cloud Ofensivo]]

## Link oficial
https://github.com/RhinoSecurityLabs/pacu
