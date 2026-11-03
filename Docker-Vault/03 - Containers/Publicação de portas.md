---
tags:
  - docker
  - containers
  - rede
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Redes bridge]]"
  - "[[Comando docker run]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Publicação de portas

Containers têm IP próprio em uma rede interna. Para que **o host ou a rede externa** acesse um serviço, é preciso **publicar** a porta.

```bash
# HOST:CONTAINER — porta 8080 do host → 80 do container
docker run -d --name web -p 8080:80 nginx:1.27

# Somente na interface local (não exposto à rede)
docker run -d --name web-local -p 127.0.0.1:8081:80 nginx:1.27

# Porta aleatória do host
docker run -d --name web-rand -p 80 nginx:1.27
docker port web-rand

# UDP
docker run -d --name dns -p 5353:53/udp alpine:3.20 sleep 300

# Publica todas as portas declaradas com EXPOSE em portas altas aleatórias
docker run -d -P nginx:1.27
```

## `EXPOSE` não publica

No Dockerfile, `EXPOSE 80` apenas **documenta** a porta. Sem `-p` ou `-P`, ela não fica acessível fora do host Docker.

| Formato | Escuta em |
|---|---|
| `-p 8080:80` | Todas as interfaces do host (`0.0.0.0`) |
| `-p 127.0.0.1:8080:80` | Apenas loopback |
| `-p 8080:80/udp` | Protocolo UDP |

> [!danger] Publicar ignora o firewall de muitas distros
> O Docker insere regras próprias no `iptables`/`nftables`, e portas publicadas podem ficar acessíveis mesmo com `ufw` ou `firewalld` bloqueando. Em servidores, publique em `127.0.0.1` e exponha por proxy reverso, ou configure regras na cadeia `DOCKER-USER`.

> [!bug] "port is already allocated" / "address already in use"
> Outra aplicação ou container usa a porta do host. Descubra com `sudo ss -ltnp | grep :8080` ou `docker ps --format '{{.Names}} {{.Ports}}'` e escolha outra porta.

## Exercício

Publique o Nginx em `127.0.0.1:8082` e tente acessar a partir de outra máquina da rede. Depois republique em `0.0.0.0` e compare.

## Veja também

- [[Redes bridge]]
- [[Comando docker run]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Containers]]
