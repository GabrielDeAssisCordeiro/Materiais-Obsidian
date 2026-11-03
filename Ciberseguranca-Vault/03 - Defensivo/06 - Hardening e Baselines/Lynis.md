---
titulo: "Lynis"
tipo: ferramenta
nome: "Lynis"
categoria: "Defensivo/Hardening-e-Baselines"
subcategoria: "Auditoria de Hardening (Unix/Linux)"
plataformas: ["Linux", "macOS", "BSD"]
licenca: "GPLv3"
linguagem: "Shell"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://cisofy.com/lynis/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/hardening
---

# Lynis

> Ferramenta open source de auditoria de segurança e hardening para sistemas Unix/Linux.

## Como funciona
Executa centenas de testes locais (configuração de kernel, serviços em execução, permissões de arquivos sensíveis, políticas de senha, atualizações pendentes) sem necessidade de instalação de agente permanente, atribuindo um 'hardening index' geral e listando sugestões específicas de endurecimento para cada achado.

## Como usar
A execução é direta: `lynis audit system` roda a bateria completa de testes localmente e produz um relatório no terminal com avisos, sugestões e o índice de hardening final; o log detalhado fica salvo em `/var/log/lynis.log` para revisão posterior.

## Casos de uso
- Auditoria rápida de hardening sem necessidade de agente
- Checklist de segurança antes de colocar um servidor em produção

## Alternativas
[[CIS-CAT (CIS Benchmarks)]]

## Categoria
[[MOC - Hardening e Baselines]]

## Link oficial
https://cisofy.com/lynis/
