---
titulo: "Chisel"
tipo: ferramenta
nome: "Chisel"
categoria: "Ofensivo/Pos-Exploracao"
subcategoria: "Pivoteamento e Tunelamento"
plataformas: ["Linux", "Windows", "macOS"]
licenca: "MIT"
linguagem: "Go"
mitre_attack: ["T1090", "T1572"]
nivel: intermediario
situacao: ativo
link_oficial: "https://github.com/jpillora/chisel"
tags:
  - ciberseguranca
  - ferramenta
  - ofensivo/pos-exploracao
  - arsenal-de-ferramentas
---

# Chisel

> Túnel TCP/UDP sobre HTTP com suporte a SOCKS5, usado para pivoteamento em redes segmentadas.

## Como funciona
Estabelece uma conexão cliente-servidor sobre HTTP/WebSocket (que atravessa a maioria dos firewalls de saída) e, dentro desse túnel criptografado (SSH embutido no protocolo), multiplexa conexões TCP/UDP arbitrárias — incluindo um proxy SOCKS5 completo — permitindo alcançar redes internas não diretamente roteáveis a partir do host do operador.

## Como usar
No modo mais comum de pivoteamento reverso, sobe-se o servidor na máquina do operador (`chisel server -p 8080 --reverse`) e, a partir do host comprometido, conecta-se o cliente de volta (`chisel client servidor:8080 R:socks`), criando um proxy SOCKS que outras ferramentas (Nmap, Metasploit) podem usar via proxychains.

## Casos de uso
- Pivoteamento para redes internas a partir de host comprometido
- Bypass de firewalls restritivos usando túnel HTTP

## Alternativas
ligolo-ng · SSH port forwarding

## Categoria
[[MOC - Pós-Exploração]]

## Link oficial
https://github.com/jpillora/chisel
