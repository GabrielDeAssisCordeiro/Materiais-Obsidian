---
titulo: "CrowdStrike Falcon"
tipo: ferramenta
nome: "CrowdStrike Falcon"
categoria: "Defensivo/EDR-XDR-HIDS"
subcategoria: "EDR/XDR Comercial"
plataformas: ["Windows", "Linux", "macOS"]
licenca: "Comercial"
linguagem: "N/A"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.crowdstrike.com/platform/endpoint-security/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/edr
  - arsenal-de-ferramentas
---

# CrowdStrike Falcon

> Plataforma EDR/XDR comercial baseada em agente leve e análise comportamental na nuvem.

## Como funciona
Um sensor leve instalado no endpoint coleta telemetria detalhada (processos, chamadas de API, conexões de rede) e a envia para a nuvem da CrowdStrike, onde modelos de detecção comportamental e indicadores de ataque (IOAs) — que observam sequências de comportamento suspeito, não apenas assinaturas — identificam atividade maliciosa em tempo quase real, permitindo resposta remota (isolamento de host, kill de processo) a partir do console.

## Como usar
Após implantação do sensor via GPO/MDM/script, toda a telemetria e alertas ficam disponíveis no console web Falcon; analistas investigam a 'process tree' do alerta, aplicam ações de contenção (Network Containment) diretamente pelo console e usam o módulo de caça a ameaças (Falcon Discover/OverWatch) para buscas proativas.

## Casos de uso
- Detecção e resposta a endpoint em ambientes corporativos
- Caça a ameaças (threat hunting) com telemetria rica

## Alternativas
[[Microsoft Defender for Endpoint]] · [[Wazuh]]

## Categoria
[[MOC - EDR, XDR e HIDS]]

## Link oficial
https://www.crowdstrike.com/platform/endpoint-security/
