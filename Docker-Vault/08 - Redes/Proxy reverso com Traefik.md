---
tags:
  - docker
  - redes
  - proxy-reverso
  - traefik
  - compose
  - labels
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Proxy reverso com Nginx]]"
  - "[[Proxy reverso com Caddy]]"
  - "[[Nomes e labels]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Proxy reverso com Traefik

O **Traefik** descobre serviços automaticamente lendo **labels** dos containers (provider Docker), sem recarregar configuração.

`compose.yaml`:

```yaml
services:
  traefik:
    image: traefik:v3.6
    command:
      - --providers.docker=true
      - --providers.docker.exposedbydefault=false   # só expõe quem pedir
      - --entrypoints.web.address=:80
      - --api.insecure=true                         # dashboard SOMENTE para laboratório
    ports:
      - "80:80"
      - "127.0.0.1:8081:8080"                       # dashboard apenas em loopback
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro

  whoami:
    image: traefik/whoami:v1.10
    labels:
      - traefik.enable=true
      - traefik.http.routers.whoami.rule=Host(`whoami.localhost`)
      - traefik.http.routers.whoami.entrypoints=web
```

```bash
docker compose up -d
curl -H "Host: whoami.localhost" http://localhost
docker compose down
```

> [!danger] O socket do Docker no Traefik
> Montar `docker.sock` dá ao Traefik (e a quem o comprometer) poder sobre o host, mesmo com `:ro` (a leitura da API ainda permite descobrir informações e, em alguns casos, ações). Em produção use um **proxy de socket** com permissões mínimas (por exemplo, `tecnativa/docker-socket-proxy`).

> [!bug] "client version ... is too old"
> Versões antigas do Traefik usam uma versão de API do Docker muito baixa e podem ser rejeitadas por Engines novos. Atualize o Traefik para uma versão recente (ou verifique a versão mínima de API suportada pelo daemon).

> [!question] Verificar na documentação oficial
> Confirme a tag estável mais recente do Traefik e a política de versão mínima de API do Engine instalado. A configuração de HTTPS automático (Let's Encrypt) está no projeto prático de proxy com Traefik.

> [!tip] Dashboard
> Nunca exponha `--api.insecure=true` publicamente. Em produção, proteja o dashboard com autenticação e TLS.

## Exercício

Adicione um segundo serviço com outro `Host(...)` e confirme o roteamento por cabeçalho `Host` usando `curl -H`.

## Veja também

- [[Proxy reverso com Nginx]]
- [[Proxy reverso com Caddy]]
- [[Nomes e labels]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Redes]]
