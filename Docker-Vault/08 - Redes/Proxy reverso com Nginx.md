---
tags:
  - docker
  - redes
  - proxy-reverso
  - nginx
  - compose
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Proxy reverso com Traefik]]"
  - "[[Proxy reverso com Caddy]]"
  - "[[DNS interno e descoberta de serviços]]"
  - "[[Visão geral do Docker Compose]]"
---

# Proxy reverso com Nginx

Um **proxy reverso** recebe o tráfego externo e o encaminha aos serviços internos, que **não precisam publicar portas**. Também concentra TLS, compressão e roteamento.

Estrutura:

```text
proxy-nginx/
├── compose.yaml
└── nginx.conf
```

`nginx.conf`:

```nginx
events {}

http {
  server {
    listen 80;

    # Encaminha para o serviço "app" (resolvido pelo DNS interno)
    location / {
      proxy_pass http://app:80;
      proxy_set_header Host              $host;
      proxy_set_header X-Real-IP         $remote_addr;
      proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
}
```

`compose.yaml`:

```yaml
services:
  proxy:
    image: nginx:1.27
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
    networks:
      - frontend

  app:
    image: traefik/whoami:v1.10     # serviço de teste que ecoa a requisição
    networks:
      - frontend                    # sem "ports": só o proxy é exposto

networks:
  frontend:
```

```bash
docker compose up -d
curl -s http://localhost:8080 | head
docker compose down
```

> [!warning] Resolução de nomes no startup
> O Nginx resolve `app` ao iniciar; se o serviço não existir ainda, o Nginx falha. `depends_on` ajuda na ordem, e em cenários dinâmicos é preciso configurar `resolver 127.0.0.11` com variáveis em `proxy_pass`.

> [!tip] HTTPS
> Para TLS automático (Let's Encrypt), [[Proxy reverso com Traefik]] e [[Proxy reverso com Caddy]] simplificam muito. Com Nginx, use `certbot` ou `nginx-proxy` + `acme-companion`.

## Exercício

Adicione um segundo serviço `app2` e crie `location /app2/` no Nginx encaminhando para ele.

## Veja também

- [[Proxy reverso com Traefik]]
- [[Proxy reverso com Caddy]]
- [[DNS interno e descoberta de serviços]]
- [[Visão geral do Docker Compose]]
- [[MOC - Redes]]
