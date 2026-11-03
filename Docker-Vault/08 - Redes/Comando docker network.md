---
tags:
  - docker
  - redes
  - comandos
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Redes bridge]]"
  - "[[Comunicação entre containers]]"
  - "[[Visão geral das redes Docker]]"
---

# Comando docker network

```bash
docker network ls                                  # lista
docker network create [opções] NOME                # cria
docker network inspect NOME                        # detalhes (sub-rede, containers)
docker network connect [--alias A] [--ip IP] REDE CONTAINER
docker network disconnect REDE CONTAINER
docker network rm NOME
docker network prune                               # remove redes sem uso
```

## Opções de `create`

| Opção | Efeito |
|---|---|
| `--driver`, `-d` | bridge (padrão), overlay, macvlan, ipvlan |
| `--subnet`, `--gateway`, `--ip-range` | Endereçamento |
| `--internal` | Sem acesso externo |
| `--attachable` | Permite containers avulsos em overlay |
| `--ipv6` | Habilita IPv6 |
| `--opt` | Opções específicas do driver |
| `--label` | Metadados |

```bash
docker network create --subnet 10.20.0.0/24 app-net
docker run -d --name web --network app-net --ip 10.20.0.10 nginx:1.27
docker network inspect app-net --format '{{range .Containers}}{{.Name}}={{.IPv4Address}} {{end}}'
docker rm -f web && docker network rm app-net
```

> [!bug] "network has active endpoints"
> Ainda existem containers conectados. Desconecte ou remova-os (`docker network inspect` lista quais).

## Exercício

Crie uma rede com sub-rede fixa, conecte um container já em execução a ela com `docker network connect` e depois desconecte.

## Veja também

- [[Redes bridge]]
- [[Comunicação entre containers]]
- [[Visão geral das redes Docker]]
- [[MOC - Redes]]
