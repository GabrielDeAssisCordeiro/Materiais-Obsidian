---
tags:
  - docker
  - moc
aliases:
  - Redes
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Redes

Drivers de rede do Docker, DNS interno, isolamento, publicação de portas, firewall, IPv6 e proxies reversos (Nginx, Traefik e Caddy).

> [!tip] Resumo prático
> Use sempre **redes bridge definidas pelo usuário**, publique o mínimo de portas e coloque um **proxy reverso** na frente. Comece por [[Redes bridge]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Visão geral das redes Docker]] — Drivers e diagrama de topologia
- [[Redes bridge]] — Bridge padrão vs definida pelo usuário
- [[Rede host]] — Pilha de rede compartilhada com o host
- [[Rede none]] — Sem rede externa
- [[Rede overlay]] — Redes multi-host com VXLAN
- [[Redes macvlan e ipvlan]] — Containers diretamente na LAN
- [[DNS interno e descoberta de serviços]] — DNS embutido, aliases e round-robin
- [[Comunicação entre containers]] — Redes múltiplas, isolamento e host.docker.internal
- [[Comando docker network]] — create, connect, inspect e rm
- [[iptables e firewall com Docker]] — DOCKER-USER, ufw e publicação de portas
- [[IPv6 no Docker]] — Habilitar e usar IPv6
- [[Proxy reverso com Nginx]] — Nginx na frente de um serviço, via Compose
- [[Proxy reverso com Traefik]] — Roteamento dinâmico por labels
- [[Proxy reverso com Caddy]] — HTTPS automático com Caddyfile mínimo

## Veja também

- [[Home - Docker]]
