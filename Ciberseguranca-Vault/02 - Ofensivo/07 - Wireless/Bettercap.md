---
titulo: "Bettercap"
tipo: ferramenta
nome: "Bettercap"
categoria: "Ofensivo/Wireless"
subcategoria: "Framework de Ataques de Rede/MITM"
plataformas: ["Linux", "macOS"]
licenca: "GPLv3"
linguagem: "Go"
mitre_attack: ["T1557"]
nivel: avancado
situacao: ativo
link_oficial: "https://www.bettercap.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/wireless
---

# Bettercap

> Framework modular para ataques MITM, sniffing de rede e reconhecimento wireless/BLE.

## Como funciona
Estrutura-se em módulos independentes ativáveis sob demanda (spoofing ARP/DNS, proxy transparente HTTP/HTTPS, reconhecimento de rede, varredura Bluetooth Low Energy), todos orquestrados por um núcleo comum com API REST e console interativo, permitindo encadear reconhecimento e ataque ativo na mesma sessão.

## Como usar
No console interativo (`bettercap -iface wlan0`), ativam-se módulos com comandos como `net.probe on` (descoberta de hosts), `arp.spoof on` (envenenamento ARP para interceptação) e `net.sniff on` (captura de tráfego); módulos de caixa de ferramentas web (`http.proxy`) permitem injeção de conteúdo no tráfego interceptado.

## Casos de uso
- Demonstração de ataques ARP spoofing/MITM em rede local autorizada
- Reconhecimento de dispositivos Bluetooth Low Energy

## Alternativas
[[Aircrack-ng]] · Ettercap

## Categoria
[[MOC - Wireless]]

## Link oficial
https://www.bettercap.org/
