---
tags:
  - docker
  - compose
  - projeto
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Comandos do Docker Compose]]"
  - "[[extends e include]]"
  - "[[Portas, volumes e redes no Compose]]"
---

# Projetos nomeados no Compose

O Compose agrupa recursos em um **projeto**. O nome do projeto prefixa containers, redes e volumes.

## Como o nome é definido (maior precedência primeiro)

1. Flag `-p` / `--project-name`
2. Variável `COMPOSE_PROJECT_NAME`
3. Chave `name:` no `compose.yaml`
4. Nome do diretório do projeto

```bash
docker compose -p loja up -d
docker compose ls                                  # projetos ativos
docker compose -p loja ps
docker compose -p loja down
```

## Nomes gerados

| Recurso | Padrão |
|---|---|
| Container | `<projeto>-<serviço>-<n>` (ex.: `loja-api-1`) |
| Rede | `<projeto>_default` |
| Volume | `<projeto>_<volume>` |

```bash
# Duas cópias independentes da mesma stack (portas diferentes via variável)
HTTP_PORT=8081 docker compose -p stack-a up -d
HTTP_PORT=8082 docker compose -p stack-b up -d
```

> [!warning] `container_name` fixo impede escala e cópias
> Definir `container_name:` quebra `--scale` e a execução de múltiplos projetos. Use somente se realmente necessário.

> [!tip] Escalar serviços
> `docker compose up -d --scale web=3` cria 3 réplicas (não publique uma porta fixa do host para o serviço escalado).

## Exercício

Suba a mesma stack com dois nomes de projeto diferentes e confirme que containers, redes e volumes não colidem.

## Veja também

- [[Comandos do Docker Compose]]
- [[extends e include]]
- [[Portas, volumes e redes no Compose]]
- [[MOC - Docker Compose]]
