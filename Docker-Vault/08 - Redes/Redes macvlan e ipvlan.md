---
tags:
  - docker
  - redes
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Visão geral das redes Docker]]"
  - "[[Rede host]]"
  - "[[iptables e firewall com Docker]]"
---

# Redes macvlan e ipvlan

Permitem que containers apareçam **diretamente na rede física (LAN)**, como se fossem máquinas independentes, com IP próprio.

## macvlan

```bash
# Ajuste sub-rede, gateway e interface (parent) à sua rede
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  rede-lan

docker run -d --name servico --network rede-lan --ip 192.168.1.50 nginx:1.27
```

Cada container recebe um **MAC próprio**.

## ipvlan

```bash
docker network create -d ipvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 -o ipvlan_mode=l2 \
  rede-ipvlan
```

Containers **compartilham o MAC** da interface do host, com IPs distintos (modos L2 e L3).

| | macvlan | ipvlan |
|---|---|---|
| MAC por container | Sim | Não (compartilha) |
| Compatível com switches que limitam MACs por porta | Nem sempre | Sim |
| Requisito | Modo promíscuo na interface/VM | Menos exigente |

> [!warning] Limitações
> - Por padrão, o **host não consegue** falar com containers macvlan na mesma interface (use uma interface macvlan auxiliar no host).
> - Muitas redes Wi-Fi e provedores de nuvem **bloqueiam** múltiplos MACs.
> - Reserve a faixa de IPs para evitar conflito com o DHCP.

> [!question] Verificar na documentação oficial
> Detalhes de `ipvlan` L3, VLANs (`eth0.10`) e o suporte em Docker Desktop devem ser conferidos na documentação oficial de drivers de rede.

## Exercício

Em uma rede de laboratório, crie uma rede macvlan e acesse o container a partir de outro computador da LAN. Teste também acesso a partir do próprio host.

## Veja também

- [[Visão geral das redes Docker]]
- [[Rede host]]
- [[iptables e firewall com Docker]]
- [[MOC - Redes]]
