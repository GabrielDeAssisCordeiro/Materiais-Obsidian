---
titulo: "Honeyd"
tipo: ferramenta
nome: "Honeyd"
categoria: "Defensivo/Deception-Honeypots"
subcategoria: "Honeypot de Baixa Interação"
plataformas: ["Linux", "BSD"]
licenca: "GPLv2"
linguagem: "C"
mitre_attack: []
nivel: intermediario
situacao: legado
link_oficial: "https://www.honeyd.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/deception
  - arsenal-de-ferramentas
---

# Honeyd

> Framework clássico para simular topologias de rede inteiras com hosts e serviços falsos de baixa interação.

## Como funciona
Responde a requisições de rede simulando a 'personalidade' de sistemas operacionais e serviços específicos (através de um banco de assinaturas de stack TCP/IP semelhante ao usado pelo Nmap), podendo emular milhares de hosts virtuais com endereços IP distintos a partir de uma única máquina física, sem implementar de fato os serviços completos — apenas o suficiente para enganar um scanner de reconhecimento.

## Como usar
Define-se um arquivo de configuração descrevendo os 'templates' de host (SO emulado, serviços e portas respondendo) e a topologia de rede desejada; o daemon (`honeyd -f config`) então responde ao tráfego destinado àqueles IPs virtuais de acordo com o template configurado.

## Casos de uso
- Simulação de topologia de rede completa para desviar reconhecimento
- Pesquisa histórica sobre varreduras automatizadas

## Alternativas
[[Cowrie]] · [[T-Pot]]

## Categoria
[[MOC - Deception e Honeypots]]

## Link oficial
https://www.honeyd.org/
