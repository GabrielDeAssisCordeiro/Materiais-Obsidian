---
tags:
  - docker
  - redes
  - dns
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Redes bridge]]"
  - "[[Comunicação entre containers]]"
  - "[[Visão geral do Docker Compose]]"
---

# DNS interno e descoberta de serviços

Em redes definidas pelo usuário, o Docker oferece um **servidor DNS embutido** (endereço `127.0.0.11` dentro do container) que resolve **nomes de containers, aliases e nomes de serviços**.

```bash
docker network create app-net
docker run -d --name db --network app-net --network-alias banco \
  -e POSTGRES_PASSWORD=senha-de-laboratorio postgres:16

# Resolve por nome do container e por alias
docker run --rm --network app-net alpine:3.20 nslookup db
docker run --rm --network app-net alpine:3.20 nslookup banco

# Inspeciona o resolvedor dentro do container
docker run --rm --network app-net alpine:3.20 cat /etc/resolv.conf

docker rm -f db && docker network rm app-net
```

## Round-robin com aliases

Vários containers com o **mesmo alias** na rede fazem o DNS devolver todos os IPs (balanceamento simples por DNS).

```bash
docker network create rr
docker run -d --name web1 --network rr --network-alias web nginx:1.27
docker run -d --name web2 --network rr --network-alias web nginx:1.27
docker run --rm --network rr alpine:3.20 nslookup web
docker rm -f web1 web2 && docker network rm rr
```

## Configurar DNS externo

```bash
docker run --rm --dns 1.1.1.1 --dns-search exemplo.local alpine:3.20 cat /etc/resolv.conf
```

> [!info] Em Compose
> Cada **serviço** vira um nome DNS na rede do projeto. Em `compose.yaml`, a API acessa o banco simplesmente como `db`. Veja [[Visão geral do Docker Compose]].

> [!bug] "Name or service not known"
> Containers em redes diferentes não se enxergam. Confirme redes com `docker inspect --format '{{json .NetworkSettings.Networks}}' NOME` e conecte-os à mesma rede.

## Exercício

Crie dois containers com o mesmo alias e execute `nslookup` do alias para ver os dois IPs retornados.

## Veja também

- [[Redes bridge]]
- [[Comunicação entre containers]]
- [[Visão geral do Docker Compose]]
- [[MOC - Redes]]
