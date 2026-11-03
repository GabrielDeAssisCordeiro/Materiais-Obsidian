---
titulo: "Wifite"
tipo: ferramenta
nome: "Wifite"
categoria: "Ofensivo/Wireless"
subcategoria: "Automação de Ataques Wi-Fi"
plataformas: ["Linux"]
licenca: "GPLv2"
linguagem: "Python"
mitre_attack: ["T1110"]
nivel: iniciante
situacao: ativo
link_oficial: "https://github.com/derv82/wifite2"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/wireless
---

# Wifite

> Automatiza o fluxo do Aircrack-ng/Reaver/Hashcat para auditoria de múltiplas redes Wi-Fi em sequência.

## Como funciona
Orquestra, de forma automatizada e sequencial, o modo monitor, a listagem de redes, a escolha de alvos por sinal/criptografia e a aplicação da técnica de ataque mais adequada a cada rede (captura de handshake WPA, ataque PMKID, ou ataque WPS via Reaver), chamando internamente as ferramentas especializadas (Aircrack-ng suite, Reaver, Hashcat) sem exigir que o operador execute cada etapa manualmente.

## Como usar
Basta rodar `wifite` (ou `wifite --kill` para encerrar processos conflitantes antes) e selecionar interativamente, a partir da lista exibida, quais redes atacar; os resultados (handshakes, senhas quebradas) são salvos automaticamente em um diretório local.

## Casos de uso
- Auditoria rápida de várias redes WEP/WPA/WPS em campo
- Simplificação de fluxo para operadores menos experientes

## Alternativas
[[Aircrack-ng]]

## Categoria
[[MOC - Wireless]]

## Link oficial
https://github.com/derv82/wifite2
