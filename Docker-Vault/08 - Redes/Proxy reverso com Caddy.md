---
tags:
  - docker
  - redes
  - proxy-reverso
  - https
  - compose
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Proxy reverso com Nginx]]"
  - "[[Proxy reverso com Traefik]]"
  - "[[Volumes nomeados]]"
---

# Proxy reverso com Caddy

O **Caddy** destaca-se pela configuração mínima e por **HTTPS automático** (certificados Let's Encrypt/ZeroSSL, ou CA interna para `localhost`).

`Caddyfile`:

```text
whoami.localhost {
    reverse_proxy whoami:80
}
```

`compose.yaml`:

```yaml
services:
  caddy:
    image: caddy:2
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data          # certificados e estado (persistir!)
      - caddy_config:/config

  whoami:
    image: traefik/whoami:v1.10

volumes:
  caddy_data:
  caddy_config:
```

```bash
docker compose up -d
curl -k https://whoami.localhost       # -k: o certificado local é de uma CA interna do Caddy
docker compose down
```

> [!tip] Em produção
> Troque `whoami.localhost` por seu domínio público (com DNS apontando para o servidor e portas 80/443 abertas) e o Caddy obtém e renova certificados sozinho. **Persista** `/data`, ou você perderá certificados e atingirá limites do Let's Encrypt.

> [!info] Tag `caddy:2`
> A tag de versão maior acompanha atualizações compatíveis. Em produção, prefira fixar uma versão menor ou digest.

## Exercício

Acrescente um segundo site no `Caddyfile` apontando para outro serviço e acesse ambos pelo nome com HTTPS local.

## Veja também

- [[Proxy reverso com Nginx]]
- [[Proxy reverso com Traefik]]
- [[Volumes nomeados]]
- [[MOC - Redes]]
