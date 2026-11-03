---
titulo: "Aircrack-ng"
tipo: ferramenta
nome: "Aircrack-ng"
categoria: "Ofensivo/Wireless"
subcategoria: "Auditoria Wi-Fi"
plataformas: ["Linux", "Windows"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: ["T1110"]
nivel: intermediario
situacao: ativo
link_oficial: "https://www.aircrack-ng.org/"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/wireless
---

# Aircrack-ng

> Suíte completa para avaliação de segurança Wi-Fi: captura, injeção de pacotes e quebra de chaves WEP/WPA.

## Como funciona
Coloca a interface wireless em modo monitor (capturando todos os quadros 802.11 ao alcance, não apenas os destinados ao host), captura o handshake de autenticação WPA/WPA2 (ou vetores de inicialização, no caso de WEP) e, a partir desse material capturado, tenta reconstruir a chave pré-compartilhada testando candidatos de uma wordlist contra o handshake capturado offline.

## Como usar
`airmon-ng start wlan0` ativa o modo monitor; `airodump-ng wlan0mon` lista redes e clientes próximos, permitindo focar a captura em um BSSID específico; uma desautenticação forçada (`aireplay-ng --deauth`) acelera a captura do handshake ao forçar a reconexão de um cliente; por fim, `aircrack-ng captura.cap -w wordlist.txt` tenta quebrar a chave.

## Casos de uso
- Auditoria de robustez de senha WPA2 em redes corporativas autorizadas
- Treinamento sobre vulnerabilidades de protocolos wireless

## Alternativas
[[Wifite]] · [[Bettercap]]

## Categoria
[[MOC - Wireless]]

## Link oficial
https://www.aircrack-ng.org/
