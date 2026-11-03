---
tags:
  - docker
  - redes
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Redes bridge]]"
  - "[[Arquivo daemon.json]]"
  - "[[iptables e firewall com Docker]]"
---

# IPv6 no Docker

O IPv6 não é habilitado por padrão nas redes bridge do Docker.

## Em uma rede definida pelo usuário

```bash
docker network create --ipv6 --subnet 2001:db8:1::/64 rede6

docker run --rm --network rede6 alpine:3.20 ip -6 addr
docker network rm rede6
```

> [!info] Prefixo de documentação
> `2001:db8::/32` é reservado para documentação. Em ambientes reais, use um prefixo **delegado pelo seu provedor** (GUA) ou um prefixo privado ULA (`fd00::/8`).

## Na rede bridge padrão (daemon.json)

```json
{
  "ipv6": true,
  "fixed-cidr-v6": "2001:db8:1::/64"
}
```

```bash
sudo systemctl restart docker
```

| Ponto | Observação |
|---|---|
| Publicação de portas | Também funciona em IPv6 (`-p`) |
| NAT | O IPv6 tende a ser roteado; confira o comportamento do seu Engine |
| Firewall | Regras `ip6tables` acompanham as de IPv4 |

> [!question] Verificar na documentação oficial
> As opções de IPv6 (inclusive NAT66, `ip6tables` e os campos de `daemon.json`) mudaram nas últimas versões. Consulte "IPv6 with Docker" na documentação oficial.

## Exercício

Crie uma rede com `--ipv6` usando um prefixo ULA (`fd00:...`), conecte um container e confirme o endereço IPv6.

## Veja também

- [[Redes bridge]]
- [[Arquivo daemon.json]]
- [[iptables e firewall com Docker]]
- [[MOC - Redes]]
