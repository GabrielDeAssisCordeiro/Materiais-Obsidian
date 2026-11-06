---
titulo: "Cheatsheet de Pivoting/Tunneling"
tipo: cheatsheet
nome: "Cheatsheet de Pivoting/Tunneling"
categoria: "Fundamentos/Cheatsheets"
subcategoria: "Referência Rápida"
plataformas: ["Linux", "Windows"]
licenca: "N/A (referência)"
linguagem: "N/A"
mitre_attack: ["T1090", "T1572"]
nivel: avancado
situacao: ativo
link_oficial: "https://github.com/jpillora/chisel"
tags:
  - ciberseguranca
  - cheatsheet
  - fundamentos
  - arsenal-de-ferramentas
---

# Cheatsheet de Pivoting/Tunneling

> Referência consolidada de técnicas de pivoteamento e tunelamento para alcançar redes internas segmentadas.

## Como funciona
Cataloga as diferentes técnicas disponíveis conforme a ferramenta já presente no host comprometido (encaminhamento de porta via SSH, túneis HTTP via Chisel, proxies SOCKS via ligolo-ng, port forwarding nativo do Windows), cada uma com trade-offs específicos de furtividade, performance e protocolos suportados, orientando qual escolher conforme o cenário de rede encontrado.

## Como usar
Avalia-se qual ferramenta/protocolo já está disponível ou pode ser levado ao host comprometido (SSH quase sempre disponível em Linux, Chisel portável para qualquer SO) e aplica-se o comando correspondente para expor a rede interna alcançável a partir daquele host à máquina do operador.

## Casos de uso
- Escolha da técnica de pivoteamento adequada a cada cenário de rede
- Referência rápida durante movimentação lateral em pentest de infraestrutura

## Alternativas
[[Chisel]]

## Categoria
[[MOC - Cheatsheets]]

## Link oficial
https://github.com/jpillora/chisel
