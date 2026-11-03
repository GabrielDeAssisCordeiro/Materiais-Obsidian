---
tags:
  - docker
  - referencia
  - cheat-sheet
  - redes
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Visão geral das redes Docker]]"
  - "[[Redes bridge]]"
  - "[[Comando docker network]]"
  - "[[Depuração de rede]]"
---

# Cheat sheet de redes Docker

```bash
docker network ls
docker network create [--driver bridge] [--subnet 172.30.0.0/24] [--internal] minha-rede
docker network inspect minha-rede
docker network connect [--alias a] minha-rede container
docker network disconnect minha-rede container
docker network rm minha-rede
docker network prune

docker run --network minha-rede --network-alias banco ...
docker run -p 8080:80 ...                  # publica 0.0.0.0:8080
docker run -p 127.0.0.1:8080:80 ...        # somente loopback
docker port container
docker run --rm --network container:alvo nicolaka/netshoot    # depuração
```

## Drivers

| Driver | Uso |
|---|---|
| `bridge` (definida pelo usuário) | **Padrão recomendado**; DNS por nome |
| `host` | Pilha de rede do host (sem isolamento) |
| `none` | Sem rede |
| `overlay` | Multi-host (Swarm) |
| `macvlan` / `ipvlan` | Container na LAN com IP próprio |

## Regras de ouro

- Bridge **padrão** não tem DNS por nome; use redes **definidas pelo usuário**.
- Containers da mesma rede **não precisam** publicar portas para se falar.
- Serviços devem escutar em **`0.0.0.0`**, não em `127.0.0.1`.
- `--internal` bloqueia saída à Internet.
- Do container, o host é `host.docker.internal` (no Linux: `--add-host=host.docker.internal:host-gateway`).
- Portas publicadas **contornam** `ufw`/`firewalld`; use `127.0.0.1` ou `DOCKER-USER`.

## Diagnóstico rápido

```bash
docker exec app ss -tlnp                # em que interface escuta?
docker exec app nslookup db             # DNS interno funciona?
docker exec app wget -qO- http://api:8080/health
docker network inspect minha-rede --format '{{range .Containers}}{{.Name}}={{.IPv4Address}} {{end}}'
```

## Veja também

- [[Visão geral das redes Docker]]
- [[Redes bridge]]
- [[Comando docker network]]
- [[Depuração de rede]]
- [[MOC - Referência - Docker]]
