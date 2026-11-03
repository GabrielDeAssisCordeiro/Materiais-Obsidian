---
titulo: "pfSense"
tipo: ferramenta
nome: "pfSense"
categoria: "Defensivo/IDS-IPS-Firewall"
subcategoria: "Firewall/Roteador Open Source"
plataformas: ["FreeBSD (appliance)"]
licenca: "Apache-2.0"
linguagem: "PHP/C"
mitre_attack: []
nivel: iniciante
situacao: ativo
link_oficial: "https://www.pfsense.org/"
tags:
  - ciberseguranca
  - ferramenta
  - defensivo/ids-ips
---

# pfSense

> Distribuição de firewall/roteador open source baseada em FreeBSD, com interface web completa.

## Como funciona
Constrói sobre o `pf` (packet filter) do FreeBSD uma interface web completa para gestão de regras de firewall, NAT, VPN (IPsec/OpenVPN) e, via pacotes adicionais, integração nativa com Snort/Suricata para funcionar também como IDS/IPS na borda da rede.

## Como usar
A administração é majoritariamente feita pela interface web: regras de firewall são criadas por interface (WAN/LAN) especificando origem, destino, porta e ação; pacotes adicionais (Package Manager) adicionam funcionalidades como o pacote Suricata para inspeção de tráfego.

## Casos de uso
- Firewall perimetral para pequenas e médias redes
- Base para laboratórios de segmentação de rede e VPN

## Alternativas
[[OPNsense]]

## Categoria
[[MOC - IDS, IPS e Firewall]]

## Link oficial
https://www.pfsense.org/
