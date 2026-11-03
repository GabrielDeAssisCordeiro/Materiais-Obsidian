---
tags:
  - docker
  - exercicios
  - compose
  - registries
aliases: []
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Docker Compose]]"
  - "[[depends_on com condition e healthcheck]]"
  - "[[Múltiplos arquivos e overrides]]"
  - "[[Registry privado local com registry 2]]"
  - "[[Docker Hub]]"
---

# Exercícios de Compose e Registries

## Questões

1. Escreva um `compose.yaml` com `web` (`nginx:1.27`, porta 8080) e `cache` (`redis:7`) na mesma rede.
2. Faça a porta do `web` vir de uma variável (`HTTP_PORT`, padrão 8080) e falhar com mensagem clara se `APP_ENV` não estiver definida.
3. Faça um serviço `api` esperar um `db` Postgres ficar **saudável**.
4. Crie um serviço `adminer` que só sobe com o profile `debug`.
5. Separe desenvolvimento e produção usando `compose.override.yaml` e `compose.prod.yaml`; como subir cada um?
6. Passe a senha do Postgres por **secret** (arquivo), não por variável de ambiente.
7. Qual comando mostra o arquivo final já interpolado e mesclado?
8. Qual a diferença entre `docker compose exec` e `docker compose run`?
9. Suba um registry local, publique `alpine:3.20` como `localhost:5000/lab/alpine:3.20` e consulte as tags pela API.
10. Escreva o esquema de tags SemVer para a versão `2.3.1`.

## Gabarito

**1.**

```yaml
services:
  web:
    image: nginx:1.27
    ports:
      - "8080:80"
  cache:
    image: redis:7
```

**2.**

```yaml
services:
  web:
    image: nginx:1.27
    ports:
      - "${HTTP_PORT:-8080}:80"
    environment:
      APP_ENV: ${APP_ENV:?Defina APP_ENV}
```

**3.**

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: senha-de-laboratorio
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 3s
      retries: 10
  api:
    image: traefik/whoami:v1.10
    depends_on:
      db:
        condition: service_healthy
```

**4.**

```yaml
services:
  adminer:
    image: adminer:4
    profiles: ["debug"]
    ports:
      - "127.0.0.1:8081:8080"
```

Suba com `docker compose --profile debug up -d`.

**5.** Desenvolvimento: `docker compose up -d` (lê `compose.yaml` + `compose.override.yaml` automaticamente). Produção: `docker compose -f compose.yaml -f compose.prod.yaml up -d` (com `-f`, o override automático **não** é lido).

**6.**

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
secrets:
  db_password:
    file: ./secrets/db_password.txt
```

**7.** `docker compose config`.

**8.** `exec` executa um comando em um container **já em execução**; `run` cria um **container novo** para o comando (use `--rm`).

**9.**

```bash
docker run -d --name registry -p 127.0.0.1:5000:5000 registry:2
docker pull alpine:3.20
docker tag alpine:3.20 localhost:5000/lab/alpine:3.20
docker push localhost:5000/lab/alpine:3.20
curl -s http://localhost:5000/v2/lab/alpine/tags/list
```

**10.** `2.3.1`, `2.3`, `2` e `sha-<commit>`; produção usa a tag exata (`2.3.1`) ou o digest.

## Veja também

- [[Visão geral do Docker Compose]]
- [[depends_on com condition e healthcheck]]
- [[Múltiplos arquivos e overrides]]
- [[Registry privado local com registry 2]]
- [[Docker Hub]]
- [[MOC - Exercícios - Docker]]
