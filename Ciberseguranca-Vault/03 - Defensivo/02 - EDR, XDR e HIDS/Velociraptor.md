---
titulo: "Velociraptor"
tipo: ferramenta
nome: "Velociraptor"
categoria: "Defensivo/EDR-XDR-HIDS"
subcategoria: "DFIR/Caça a Ameaças em Endpoint"
plataformas: ["Windows", "Linux", "macOS"]
licenca: "AGPL-3.0"
linguagem: "Go"
mitre_attack: []
nivel: avancado
situacao: ativo
link_oficial: "https://docs.velociraptor.app/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/edr
---

# Velociraptor

> Plataforma open source de coleta forense e caça a ameaças em larga escala de endpoints.

## Como funciona
Usa uma linguagem de consulta própria (VQL — Velociraptor Query Language) para expressar coletas forenses e buscas de IOCs como consultas estruturadas, executadas sob demanda ou continuamente em milhares de endpoints simultaneamente através de agentes leves, permitindo investigação e resposta a incidentes em escala sem necessidade de acesso individual a cada máquina.

## Como usar
Sobe-se o servidor central e implantam-se os agentes (clients) nos endpoints monitorados; a partir da interface web, 'Hunts' (consultas VQL aplicadas a toda a frota) coletam artefatos forenses específicos (ex.: histórico de execução, conexões de rede) de todos os hosts simultaneamente para análise centralizada.

## Casos de uso
- Caça a ameaças e coleta forense em larga escala durante um incidente
- Resposta a incidentes distribuída sem necessidade de acesso físico/remoto individual

## Alternativas
[[Wazuh]]

## Categoria
[[MOC - EDR, XDR e HIDS]]

## Link oficial
https://docs.velociraptor.app/
