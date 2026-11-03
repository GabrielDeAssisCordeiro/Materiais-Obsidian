---
tags:
  - docker
  - compose
  - comandos
  - cli
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Docker Compose]]"
  - "[[Compose Watch]]"
  - "[[Projetos nomeados no Compose]]"
  - "[[Cheat sheet de comandos Docker]]"
---

# Comandos do Docker Compose

| Comando | Função |
|---|---|
| `docker compose up -d` | Cria e inicia (segundo plano) |
| `docker compose up -d --build` | Reconstrói imagens antes |
| `docker compose up -d --force-recreate` | Recria containers mesmo sem mudanças |
| `docker compose up -d --remove-orphans` | Remove containers de serviços que saíram do arquivo |
| `docker compose up -d --wait` | Aguarda serviços saudáveis |
| `docker compose down` | Para e remove containers e redes |
| `docker compose down -v` | Também remove volumes **(apaga dados!)** |
| `docker compose down --rmi local` | Também remove imagens construídas |
| `docker compose ps [-a]` | Lista serviços |
| `docker compose logs -f [serviço]` | Logs |
| `docker compose exec serviço sh` | Executa em container em execução |
| `docker compose run --rm serviço cmd` | Container **novo** para um comando pontual |
| `docker compose build [serviço]` | Constrói |
| `docker compose pull` / `push` | Baixa / envia imagens |
| `docker compose stop` / `start` / `restart` | Controle sem remover |
| `docker compose config` | Valida e mostra o modelo final |
| `docker compose watch` | Desenvolvimento com sincronização |
| `docker compose ls` | Projetos em execução |
| `docker compose top` / `port` / `cp` / `events` | Utilitários |

```bash
docker compose up -d
docker compose ps
docker compose logs -f --tail 50 web
docker compose exec web sh
docker compose run --rm web nginx -t     # testa a configuração em um container novo
docker compose down
```

> [!warning] `exec` vs `run`
> `exec` usa o container **existente**; `run` cria um **novo** (sem publicar portas por padrão, a menos que use `--service-ports`) e deve levar `--rm`.

> [!danger] `down -v`
> Remove volumes nomeados do projeto. Em bancos de dados, significa perder dados.

> [!info] `docker compose` vs `docker-compose`
> Use sempre a forma com espaço (plugin v2). O binário `docker-compose` (v1) está obsoleto.

## Exercício

Use `up`, `ps`, `logs`, `exec`, `run --rm` e `down` na stack do exemplo e descreva o que cada comando altera.

## Veja também

- [[Visão geral do Docker Compose]]
- [[Compose Watch]]
- [[Projetos nomeados no Compose]]
- [[Cheat sheet de comandos Docker]]
- [[MOC - Docker Compose]]
