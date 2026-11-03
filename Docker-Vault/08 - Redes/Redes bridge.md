---
tags:
  - docker
  - redes
  - dns
  - comparativo
aliases:
  - Rede bridge
  - bridge
  - docker0
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Visão geral das redes Docker]]"
  - "[[DNS interno e descoberta de serviços]]"
  - "[[Comunicação entre containers]]"
  - "[[Comando docker network]]"
  - "[[Publicação de portas]]"
---

# Redes bridge

A rede **bridge** é um switch virtual no host. Há dois tipos que se comportam de forma muito diferente.

## Bridge padrão (`bridge` / `docker0`) vs definida pelo usuário

| Característica | Bridge **padrão** | Bridge **definida pelo usuário** |
|---|---|---|
| Resolução de nomes (DNS) | **Não** (só por IP) | **Sim**, por nome e alias |
| Isolamento | Todos os containers sem rede explícita compartilham | Só os conectados à rede |
| Conectar/desconectar em execução | Não | **Sim** |
| Configuração (sub-rede, gateway, opções) | Limitada | Total |
| Recomendação | Evitar | **Usar sempre** |

```bash
# Rede definida pelo usuário
docker network create minha-rede

docker run -d --name api --network minha-rede nginx:1.27
docker run --rm --network minha-rede alpine:3.20 wget -qO- http://api

# Com sub-rede e gateway específicos
docker network create \
  --driver bridge \
  --subnet 172.30.0.0/24 \
  --gateway 172.30.0.1 \
  rede-fixa

# Rede interna: sem saída para fora do host
docker network create --internal rede-isolada

docker rm -f api
docker network rm minha-rede rede-fixa rede-isolada
```

> [!warning] Conflito de sub-redes
> VPNs e redes corporativas às vezes usam as mesmas faixas (`172.17.0.0/16`, `172.18.x.x`). Configure `default-address-pools` no [[Arquivo daemon.json]] ou use `--subnet` explícito.

> [!bug] "Could not resolve host" entre containers
> Ocorre na bridge padrão: não há DNS por nome. Crie uma rede definida pelo usuário e conecte ambos os containers a ela.

> [!tip] `--internal`
> Útil para bancos de dados: acessíveis pelos serviços na rede, sem rota para a Internet.

## Exercício

Suba dois containers na bridge padrão e tente `ping` por nome; repita em uma rede definida pelo usuário e compare.

## Veja também

- [[Visão geral das redes Docker]]
- [[DNS interno e descoberta de serviços]]
- [[Comunicação entre containers]]
- [[Comando docker network]]
- [[Publicação de portas]]
- [[MOC - Redes]]
