---
tags:
  - docker
  - desenvolvimento
  - banco-de-dados
  - postgres
  - mysql
  - compose
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Persistência de bancos de dados]]"
  - "[[depends_on com condition e healthcheck]]"
  - "[[Volumes nomeados]]"
  - "[[Ambientes de desenvolvimento reproduzíveis]]"
---

# Bancos de dados locais

Rodar bancos em containers evita instalar nada no host e permite várias versões.

`compose.yaml` (todos publicados somente em loopback):

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: senha-de-laboratorio
      POSTGRES_DB: appdb
    ports:
      - "127.0.0.1:5432:5432"
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app -d appdb"]
      interval: 5s
      timeout: 3s
      retries: 10

  mysql:
    image: mysql:8.4
    environment:
      MYSQL_ROOT_PASSWORD: senha-de-laboratorio
      MYSQL_DATABASE: appdb
    ports:
      - "127.0.0.1:3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-psenha-de-laboratorio"]
      interval: 10s
      timeout: 5s
      retries: 10

  mongo:
    image: mongo:7
    environment:
      MONGO_INITDB_ROOT_USERNAME: app
      MONGO_INITDB_ROOT_PASSWORD: senha-de-laboratorio
    ports:
      - "127.0.0.1:27017:27017"
    volumes:
      - mongo_data:/data/db
    healthcheck:
      test: ["CMD", "mongosh", "--quiet", "--eval", "db.adminCommand('ping').ok"]
      interval: 10s
      timeout: 5s
      retries: 10

  redis:
    image: redis:7
    command: ["redis-server", "--appendonly", "yes"]
    ports:
      - "127.0.0.1:6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 10

volumes:
  pg_data:
  mysql_data:
  mongo_data:
  redis_data:
```

```bash
docker compose up -d postgres redis          # suba apenas o que precisa
docker compose exec postgres psql -U app -d appdb -c '\dt'
docker compose exec redis redis-cli set chave valor
```

## Inicialização com scripts

As imagens executam arquivos de `/docker-entrypoint-initdb.d/` (`*.sql`, `*.sh`) **apenas na primeira inicialização** (volume vazio).

```yaml
    volumes:
      - ./initdb:/docker-entrypoint-initdb.d:ro
```

> [!warning] Senhas de exemplo
> `senha-de-laboratorio` é só para ambiente local. Em qualquer ambiente real, use secrets.

> [!bug] Script de inicialização não rodou
> O banco já tinha dados no volume. Para reexecutar em laboratório: `docker compose down -v` (apaga os dados!).

> [!info] Imagens de terceiros
> Prefira as **imagens oficiais** acima. Algumas coleções populares mudaram suas políticas de publicação/versionamento recentemente; verifique a procedência e a manutenção da imagem antes de adotar.

## Exercício

Suba o PostgreSQL com um script em `initdb/` que cria uma tabela e conecte com `psql`. Em seguida, recrie o container e confirme que os dados persistiram.

## Veja também

- [[Persistência de bancos de dados]]
- [[depends_on com condition e healthcheck]]
- [[Volumes nomeados]]
- [[Ambientes de desenvolvimento reproduzíveis]]
- [[MOC - Desenvolvimento]]
