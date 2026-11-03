---
tags:
  - docker
  - projetos
  - nginx
  - iniciante
  - compose
aliases: []
tipo: projeto
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Introdução ao Dockerfile]]"
  - "[[Bind mounts]]"
  - "[[Healthchecks em containers]]"
  - "[[Visão geral do Docker Compose]]"
  - "[[Projeto 02 - API Node.js containerizada]]"
---

# Projeto 01 - Site estático com Nginx

## Objetivos

- Construir uma imagem própria com Nginx servindo um site estático.
- Executar como **usuário não-root**, com **healthcheck** e configuração customizada.
- Usar Compose para produção (imagem) e desenvolvimento (bind mount).

**Nível:** iniciante · **Tempo estimado:** 30 min

## Estrutura de pastas

```text
site-estatico/
├── Dockerfile
├── compose.yaml
├── compose.override.yaml
├── default.conf
├── .dockerignore
└── site/
    ├── index.html
    └── estilo.css
```

## Arquivos

`site/index.html`:

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Meu site em Docker</title>
  <link rel="stylesheet" href="estilo.css">
</head>
<body>
  <main>
    <h1>Olá, Docker! 🐳</h1>
    <p>Este site é servido por um container Nginx.</p>
  </main>
</body>
</html>
```

`site/estilo.css`:

```css
body { font-family: system-ui, sans-serif; display: grid; place-items: center; min-height: 100vh; margin: 0; background: #0b1d33; color: #e8f1ff; }
main { text-align: center; }
```

`default.conf` (Nginx sem privilégios escuta na porta 8080):

```nginx
server {
  listen 8080;
  server_name _;

  root  /usr/share/nginx/html;
  index index.html;

  gzip on;
  gzip_types text/css application/javascript application/json image/svg+xml;

  add_header X-Content-Type-Options "nosniff" always;
  add_header X-Frame-Options "DENY" always;
  add_header Referrer-Policy "no-referrer" always;

  location / {
    try_files $uri $uri/ =404;
  }

  location = /health {
    access_log off;
    default_type text/plain;
    return 200 "ok\n";
  }
}
```

`.dockerignore`:

```text
.git
compose*.yaml
Dockerfile
*.md
```

`Dockerfile`:

```dockerfile
# syntax=docker/dockerfile:1
FROM nginxinc/nginx-unprivileged:1.27-alpine

# Configuração e conteúdo do site
COPY default.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:8080/health || exit 1
```

`compose.yaml`:

```yaml
services:
  web:
    build: .
    image: site-estatico:1.0
    ports:
      - "127.0.0.1:8080:8080"
    restart: unless-stopped
    read_only: true
    tmpfs:
      - /tmp
      - /var/cache/nginx
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
```

`compose.override.yaml` (desenvolvimento: edita e atualiza o navegador sem rebuild):

```yaml
services:
  web:
    volumes:
      - ./site:/usr/share/nginx/html:ro
      - ./default.conf:/etc/nginx/conf.d/default.conf:ro
```

## Passo a passo

```bash
mkdir -p site-estatico/site && cd site-estatico
# crie os arquivos acima

docker compose up -d --build
docker compose ps
```

## Verificação

```bash
curl -I http://localhost:8080                 # 200 OK e cabeçalhos de segurança
curl http://localhost:8080/health             # ok
docker compose exec web id                    # usuário não-root (uid 101)
docker inspect --format '{{.State.Health.Status}}' $(docker compose ps -q web)   # healthy
```

Abra `http://localhost:8080` no navegador. Edite `site/index.html` e recarregue: a mudança aparece (por causa do override de desenvolvimento).

Para testar **como produção** (sem o override):

```bash
docker compose -f compose.yaml up -d --build
```

## Solução de problemas

| Sintoma | Causa provável | Solução |
|---|---|---|
| `bind: address already in use` | Porta 8080 ocupada | Mude para `127.0.0.1:8081:8080` |
| 403 Forbidden | Permissões do bind mount | `chmod -R a+rX site` |
| `mkdir() "/var/cache/nginx/..." failed` com `read_only` | Falta `tmpfs` | Mantenha os `tmpfs` do exemplo |
| Mudanças não aparecem | Está rodando sem o override | Use `docker compose up -d` (carrega o override) |
| `unhealthy` | `wget` ausente ou rota errada | Verifique `docker inspect` e a rota `/health` |

## Extensões sugeridas

1. Adicionar **HTTPS** com Caddy na frente ([[Proxy reverso com Caddy]]).
2. Usar um **estágio de build** (Vite/Hugo) com multi-stage para gerar o site estático ([[Multi-stage builds]]).
3. Publicar a imagem no **GHCR** com GitHub Actions ([[GitHub Actions para build e push]]).
4. Adicionar cache e compressão (Brotli) e uma página 404 personalizada.

## Exercício

Adicione uma página `sobre.html`, uma 404 personalizada (`error_page 404 /404.html;`) e comprove os dois comportamentos com `curl -i`.

## Veja também

- [[Introdução ao Dockerfile]]
- [[Bind mounts]]
- [[Healthchecks em containers]]
- [[Visão geral do Docker Compose]]
- [[Projeto 02 - API Node.js containerizada]]
- [[MOC - Projetos - Docker]]
