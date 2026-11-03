---
tags:
  - docker
  - observabilidade
  - rede
  - depuracao
  - troubleshooting
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Redes bridge]]"
  - "[[DNS interno e descoberta de serviços]]"
  - "[[Publicação de portas]]"
  - "[[iptables e firewall com Docker]]"
---

# Depuração de rede

## Roteiro

```bash
# 1) O serviço está escutando? E em qual interface?
docker exec app ss -tlnp            # ou netstat -tlnp
# 0.0.0.0:3000  → acessível pela rede
# 127.0.0.1:3000 → só dentro do container (não funciona com -p!)

# 2) A porta foi publicada?
docker port app
docker ps --format '{{.Names}}: {{.Ports}}'

# 3) Os containers estão na mesma rede?
docker inspect --format '{{json .NetworkSettings.Networks}}' app
docker network inspect minha-rede

# 4) O DNS funciona?
docker exec app nslookup db
docker exec app cat /etc/resolv.conf    # 127.0.0.11 em redes definidas pelo usuário

# 5) Há conectividade?
docker exec app wget -qO- http://api:8080/health
```

## Container de ferramentas de rede

```bash
# Compartilha o namespace de rede do alvo, com ping, curl, tcpdump, dig, etc.
docker run -it --rm --network container:app nicolaka/netshoot
# dentro: curl -v http://localhost:3000 ; tcpdump -i eth0 -n port 80 ; ss -tlnp
```

## Problemas comuns

| Sintoma | Causa | Solução |
|---|---|---|
| "Connection refused" ao acessar de fora | App escuta em `127.0.0.1` | Fazer a app escutar em `0.0.0.0` |
| Container não resolve outro por nome | Bridge padrão ou redes diferentes | Rede definida pelo usuário/mesma rede |
| Funciona entre containers, não do host | Falta `-p` | Publicar a porta |
| Funciona local, não de outra máquina | Firewall / publicação em `127.0.0.1` | Ver [[iptables e firewall com Docker]] |
| Falhas intermitentes em VPN | Conflito de sub-redes ou MTU | `default-address-pools`; ajustar MTU da rede |
| `localhost` no container não alcança o host | `localhost` é o próprio container | `host.docker.internal` |

> [!tip] `curl` sem estar na imagem
> Use `wget`, ou o container `netshoot` compartilhando a rede, sem alterar a imagem da aplicação.

## Exercício

Suba uma aplicação que escuta apenas em `127.0.0.1`, publique com `-p` e demonstre a falha. Corrija o bind para `0.0.0.0`.

## Veja também

- [[Redes bridge]]
- [[DNS interno e descoberta de serviços]]
- [[Publicação de portas]]
- [[iptables e firewall com Docker]]
- [[MOC - Observabilidade e Depuração]]
