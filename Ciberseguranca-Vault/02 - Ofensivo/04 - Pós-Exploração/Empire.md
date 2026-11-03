---
titulo: "Empire"
tipo: ferramenta
nome: "Empire"
categoria: "Ofensivo/Pos-Exploracao"
subcategoria: "Framework C2 Pós-Exploração"
plataformas: ["Linux (servidor)"]
licenca: "BSD-3-Clause"
linguagem: "Python/PowerShell/C#"
mitre_attack: ["T1059", "T1071"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/BC-SECURITY/Empire"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/pos-exploracao
---

# Empire

> Framework de pós-exploração com agentes PowerShell/Python/C#, mantido atualmente pela BC Security.

## Como funciona
Funciona em arquitetura cliente-servidor: o servidor gerencia 'listeners' (canais de C2) e 'agents' (implantes ativos em máquinas comprometidas), que se comunicam periodicamente (callback) e executam 'módulos' (equivalentes a scripts PowerSploit) sob demanda, com suporte a ofuscação de tráfego e de código para reduzir detecção.

## Como usar
Inicia-se o servidor (`./ps-empire server`) e, em outro terminal, o cliente (`./ps-empire client`); cria-se um listener (`listeners`, `uselistener http`), gera-se um stager (payload inicial) e, após o callback do agente, módulos são executados via `usemodule` dentro da sessão do agente.

## Casos de uso
- Simulação de adversário pós-comprometimento sem custo de licença
- Treinamento de resposta a incidentes contra C2 conhecido

## Alternativas
[[PowerSploit]] · [[Sliver]] · [[Cobalt Strike]]

## Categoria
[[MOC - Pós-Exploração]]

## Link oficial
https://github.com/BC-SECURITY/Empire
