---
titulo: "Microsoft Defender for Endpoint"
tipo: ferramenta
nome: "Microsoft Defender for Endpoint"
categoria: "Defensivo/EDR-XDR-HIDS"
subcategoria: "EDR/XDR Microsoft"
plataformas: ["Windows", "Linux", "macOS"]
licenca: "Comercial (incluso em licenças M365)"
linguagem: "N/A"
mitre_attack: []
nivel: intermediario
situacao: ativo
link_oficial: "https://www.microsoft.com/security/business/endpoint-security/microsoft-defender-endpoint"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/edr
---

# Microsoft Defender for Endpoint

> Solução EDR/XDR nativa da Microsoft, integrada ao Windows e ao ecossistema Microsoft 365 Defender.

## Como funciona
Aproveita sensores já embutidos no kernel do Windows para coletar telemetria de processos, rede e sistema de arquivos sem necessidade de agente adicional, correlacionando esses dados na nuvem com inteligência de ameaças da Microsoft e com sinais de outros produtos do conjunto Defender (e-mail, identidade) para investigações XDR correlacionadas entre múltiplos vetores.

## Como usar
A ativação ocorre via política no Microsoft Intune/Endpoint Manager ou diretamente no portal Microsoft 365 Defender; alertas aparecem correlacionados por incidente (não apenas por host isolado), com ações de resposta como isolamento de dispositivo e execução de scan antivírus remoto disponíveis diretamente no portal.

## Casos de uso
- Proteção nativa de endpoints Windows sem agente adicional
- Correlação de alertas entre endpoint, e-mail e identidade (XDR)

## Alternativas
[[CrowdStrike Falcon]]

## Categoria
[[MOC - EDR, XDR e HIDS]]

## Link oficial
https://www.microsoft.com/security/business/endpoint-security/microsoft-defender-endpoint
