---
titulo: "Kismet"
tipo: ferramenta
nome: "Kismet"
categoria: "Ofensivo/Wireless"
subcategoria: "Detecção e Sniffing Wireless"
plataformas: ["Linux", "macOS"]
licenca: "GPLv2"
linguagem: "C++"
mitre_attack: ["T1040"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.kismetwireless.net/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/wireless
  - arsenal-de-ferramentas
---

# Kismet

> Detector e sniffer passivo para Wi-Fi, Bluetooth e outros protocolos sem fio, com mapeamento de dispositivos.

## Como funciona
Opera de forma inteiramente passiva, apenas escutando quadros 802.11/Bluetooth/outros protocolos suportados por hardware compatível, sem nunca transmitir pacotes; constrói progressivamente um inventário de access points, clientes e dispositivos detectados, incluindo redes ocultas (SSID não divulgado) identificadas pelo tráfego de clientes associados.

## Como usar
`kismet -c wlan0` inicia a captura na interface informada; a interface web embutida (porta 2501 por padrão) exibe em tempo real os dispositivos e redes detectados, com opção de alertas para comportamentos anômalos (ex.: possível ataque de desautenticação em andamento).

## Casos de uso
- Mapeamento passivo de dispositivos wireless em área física
- Detecção de access points não autorizados (rogue APs)

## Alternativas
[[Aircrack-ng]] · [[Bettercap]]

## Categoria
[[MOC - Wireless]]

## Link oficial
https://www.kismetwireless.net/
