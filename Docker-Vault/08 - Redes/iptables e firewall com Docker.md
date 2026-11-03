---
tags:
  - docker
  - redes
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Publicação de portas]]"
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Rede overlay]]"
  - "[[Redes bridge]]"
---

# iptables e firewall com Docker

O Docker gerencia regras de firewall automaticamente (iptables, ou nftables em versões recentes) para NAT, isolamento entre redes e publicação de portas.

## Cadeias importantes (iptables)

| Cadeia | Função |
|---|---|
| `DOCKER` | Regras de publicação de portas para containers |
| `DOCKER-USER` | **Sua** cadeia: avaliada antes das regras do Docker; o Docker não a sobrescreve |
| `DOCKER-ISOLATION-STAGE-*` | Isolamento entre redes |
| `POSTROUTING` (nat) | Mascaramento (saída dos containers) |

```bash
sudo iptables -L DOCKER-USER -n -v --line-numbers
sudo iptables -t nat -L -n -v | head -30
```

## O problema: portas publicadas "furam" o ufw/firewalld

Como o Docker insere regras antes das do `ufw`, uma porta publicada com `-p 8080:80` pode ficar acessível de fora **mesmo que o ufw a bloqueie**.

## Soluções

```bash
# 1) Publique somente em loopback e use proxy reverso na frente
docker run -d -p 127.0.0.1:8080:80 nginx:1.27

# 2) Restrinja na cadeia DOCKER-USER (exemplo: só a LAN 192.168.1.0/24 acessa; interface externa eth0)
sudo iptables -I DOCKER-USER -i eth0 ! -s 192.168.1.0/24 -j DROP

# 3) Para publicar em um IP específico do host
docker run -d -p 192.168.1.5:8080:80 nginx:1.27
```

> [!danger] Não desligue o gerenciamento de iptables sem planejar
> A opção `"iptables": false` no `daemon.json` quebra NAT e DNS de containers; você teria de manter todas as regras manualmente.

> [!info] nftables
> Versões recentes do Engine introduzem suporte a **nftables** como backend de firewall (inicialmente experimental). A opção é configurada no `daemon.json`.

> [!question] Verificar na documentação oficial
> O nome da opção do backend nftables, seu estado (experimental ou estável) e mudanças de comportamento de publicação de portas nas versões 28 e 29 devem ser confirmados em "Packet filtering and firewalls" na documentação do Docker.

> [!tip] Em produção
> Combine: publicar o mínimo, proxy reverso com TLS, firewall de borda (security groups) e regras em `DOCKER-USER`.

## Exercício

Publique um Nginx em `0.0.0.0:8085`, bloqueie a porta com `ufw` e teste de outra máquina. Depois repita publicando em `127.0.0.1` e comente a diferença.

## Veja também

- [[Publicação de portas]]
- [[Princípio do menor privilégio - Docker]]
- [[Rede overlay]]
- [[Redes bridge]]
- [[MOC - Redes]]
