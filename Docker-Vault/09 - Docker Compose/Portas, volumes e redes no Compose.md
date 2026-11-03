---
tags:
  - docker
  - compose
  - volumes
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Publicação de portas]]"
  - "[[Volume vs bind mount vs tmpfs]]"
  - "[[Redes bridge]]"
  - "[[Visão geral do Docker Compose]]"
---

# Portas, volumes e redes no Compose

```yaml
services:
  app:
    image: nginx:1.27
    ports:
      - "8080:80"                    # HOST:CONTAINER
      - "127.0.0.1:8443:443"         # somente loopback
      - target: 80                   # sintaxe longa
        published: "9090"
        protocol: tcp
    expose:
      - "3000"                       # documenta/permite entre serviços (não publica)
    volumes:
      - dados:/var/lib/app           # volume nomeado
      - ./config:/etc/app:ro         # bind mount somente leitura
      - type: tmpfs
        target: /tmp
    networks:
      - frontend
      - backend

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: senha-de-laboratorio
    networks:
      - backend

networks:
  frontend:
  backend:
    internal: true                   # sem acesso externo

volumes:
  dados:
```

## Pontos-chave

| Tema | Comportamento |
|---|---|
| Rede padrão | Sem `networks`, o Compose cria `<projeto>_default` e conecta todos os serviços |
| DNS | Cada serviço é alcançável pelo **nome do serviço** |
| Aliases | `networks: backend: aliases: [banco]` |
| IP fixo | `ipv4_address:` (exige `ipam` com sub-rede) |
| Volumes | Prefixados pelo projeto (`<projeto>_dados`) |
| Volume externo | `volumes: dados: external: true` (já existe fora do Compose) |

```yaml
volumes:
  dados-compartilhados:
    external: true           # criado antes com `docker volume create`
```

> [!danger] `ports` no banco de dados
> Evite publicar a porta do banco em `0.0.0.0`. Se precisar acessar do host, use `127.0.0.1:5432:5432`; entre serviços, a rede interna basta.

## Exercício

Monte uma stack com duas redes (`frontend` e `backend` interna), onde só o proxy publica porta e o banco fica isolado. Teste a conectividade com `docker compose exec`.

## Veja também

- [[Publicação de portas]]
- [[Volume vs bind mount vs tmpfs]]
- [[Redes bridge]]
- [[Visão geral do Docker Compose]]
- [[MOC - Docker Compose]]
