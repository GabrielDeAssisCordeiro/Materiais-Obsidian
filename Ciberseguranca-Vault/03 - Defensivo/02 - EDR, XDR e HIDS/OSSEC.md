---
titulo: "OSSEC"
tipo: ferramenta
nome: "OSSEC"
categoria: "Defensivo/EDR-XDR-HIDS"
subcategoria: "HIDS"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.ossec.net/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/edr
---

# OSSEC

> Sistema de detecção de intrusão baseado em host (HIDS), predecessor da arquitetura usada pelo Wazuh.

## Como funciona
Um agente instalado em cada host monitora logs do sistema, verifica integridade de arquivos críticos (comparando hashes ao longo do tempo), detecta rootkits conhecidos e audita políticas de configuração, enviando os achados a um servidor central que aplica regras de decodificação e correlação para gerar alertas.

## Como usar
Instala-se o servidor central e os agentes nos hosts monitorados, registrando cada agente via chave de autenticação; regras de detecção (XML) podem ser customizadas e os alertas são consultados via logs locais ou integrações com um SIEM (como o próprio Wazuh, seu fork mais ativo).

## Casos de uso
- Monitoramento de integridade de arquivos em servidores críticos
- Detecção de rootkits e mudanças não autorizadas de configuração

## Alternativas
[[Wazuh]]

## Categoria
[[MOC - EDR, XDR e HIDS]]

## Link oficial
https://www.ossec.net/
