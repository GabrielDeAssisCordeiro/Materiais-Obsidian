---
tags:
  - docker
  - projetos
  - mysql
  - compose
  - secrets
aliases: []
tipo: projeto
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Persistência de bancos de dados]]"
  - "[[configs e secrets no Compose]]"
  - "[[depends_on com condition e healthcheck]]"
  - "[[Backup e restauração de volumes]]"
  - "[[Projeto 04 - Stack com Postgres, API e frontend]]"
---

# Projeto 03 - WordPress com MySQL

## Objetivos

- Subir um **WordPress** com **MySQL** usando Compose, volumes nomeados e **secrets** para senhas.
- Aguardar o banco ficar saudável antes de iniciar o WordPress.
- Fazer **backup e restauração** e usar o **WP-CLI** em container.

**Nível:** intermediário · **Tempo estimado:** 45 min

## Estrutura

```text
wordpress/
├── compose.yaml
├── uploads.ini
├── .gitignore
└── secrets/
    ├── db_password.txt
    └── db_root_password.txt
```

## Arquivos

Crie os segredos (sem quebra de linha final) e ignore-os no Git:

```bash
mkdir -p wordpress/secrets && cd wordpress
printf '%s' "$(openssl rand -base64 24)" > secrets/db_password.txt
printf '%s' "$(openssl rand -base64 24)" > secrets/db_root_password.txt
chmod 644 secrets/*.txt            # leitura pelos containers (ambiente local)
echo "secrets/" > .gitignore
```

`uploads.ini` (aumenta limites de upload):

```ini
file_uploads = On
upload_max_filesize = 64M
post_max_size = 64M
memory_limit = 256M
max_execution_time = 120
```

`compose.yaml`:

```yaml
services:
  db:
    image: mysql:8.4
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wp
      MYSQL_PASSWORD_FILE: /run/secrets/db_password
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_root_password
    secrets:
      - db_password
      - db_root_password
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h 127.0.0.1 -uroot -p\"$$(cat /run/secrets/db_root_password)\" --silent"]
      interval: 10s
      timeout: 5s
      retries: 12
      start_period: 30s

  wordpress:
    image: wordpress:6-apache
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_USER: wp
      WORDPRESS_DB_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    ports:
      - "127.0.0.1:8080:80"
    volumes:
      - wp_data:/var/www/html
      - ./uploads.ini:/usr/local/etc/php/conf.d/uploads.ini:ro
    networks:
      - backend
      - frontend

  wpcli:
    image: wordpress:cli
    profiles: ["tools"]
    user: "33:33"                     # www-data
    depends_on:
      db:
        condition: service_healthy
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_USER: wp
      WORDPRESS_DB_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - wp_data:/var/www/html
    networks:
      - backend

networks:
  backend:
    internal: true         # o banco não acessa a Internet
  frontend:

volumes:
  db_data:
  wp_data:

secrets:
  db_password:
    file: ./secrets/db_password.txt
  db_root_password:
    file: ./secrets/db_root_password.txt
```

> [!info] `$$` no healthcheck
> No Compose, `$$` produz um `$` literal, de modo que `$(cat ...)` seja avaliado **dentro** do container e não pelo Compose.

## Passo a passo

```bash
docker compose up -d
docker compose ps          # aguarde "healthy" no db
docker compose logs -f wordpress
```

Acesse `http://localhost:8080` e conclua o assistente de instalação (idioma, título, usuário administrador).

## Verificação

```bash
docker compose exec db sh -c 'mysql -uwp -p"$(cat /run/secrets/db_password)" -e "SHOW DATABASES;"'
docker compose --profile tools run --rm wpcli core version
docker compose --profile tools run --rm wpcli plugin list
```

Confirme a **persistência**:

```bash
docker compose down            # sem -v!
docker compose up -d
# o site e o conteúdo continuam lá
```

## Backup e restauração

```bash
# Banco
docker compose exec -T db sh -c 'mysqldump -uroot -p"$(cat /run/secrets/db_root_password)" --single-transaction wordpress' > backup-db.sql

# Arquivos (temas, plugins, uploads)
docker run --rm -v wordpress_wp_data:/dados:ro -v "$PWD":/backup alpine:3.20 \
  tar czf /backup/backup-wp.tar.gz -C /dados .

# Restauração do banco
docker compose exec -T db sh -c 'mysql -uroot -p"$(cat /run/secrets/db_root_password)" wordpress' < backup-db.sql
```

> [!warning] Nome do volume
> O volume real é prefixado pelo projeto (`<pasta>_wp_data`). Confira com `docker volume ls` e ajuste o nome no comando de backup.

## Solução de problemas

| Sintoma | Causa provável | Solução |
|---|---|---|
| "Error establishing a database connection" | Banco não pronto ou credenciais erradas | `docker compose logs db`; confira os secrets; aguarde o healthcheck |
| Banco "unhealthy" | Senha do root diferente da usada na primeira inicialização | Em laboratório, `docker compose down -v` e recomece (apaga dados) |
| Upload falha por tamanho | Limites de PHP | Verifique o `uploads.ini` montado |
| Permissões ao instalar plugins | Dono dos arquivos incorreto | Use o `wpcli` com `user: "33:33"` ou `chown -R www-data` no volume |
| Tela em branco após migrar de domínio | URLs salvas no banco | `wp search-replace 'http://antigo' 'https://novo'` pelo WP-CLI |

> [!question] Verificar na documentação oficial
> A compatibilidade do WordPress com versões do MySQL/MariaDB muda; consulte os requisitos do WordPress e a página da imagem oficial. Se houver problemas de autenticação, a alternativa comum é o `mariadb:11`.

## Extensões sugeridas

1. **HTTPS** com Traefik ou Caddy ([[Projeto 05 - Proxy reverso com Traefik e HTTPS]]).
2. **Cache de objetos** com Redis (plugin + serviço `redis:7`).
3. **Backups automáticos** agendados ([[Backups em produção]]).
4. Monitorar com cAdvisor/Prometheus ([[Projeto 06 - Monitoramento com Prometheus e Grafana]]).

## Exercício

Instale um plugin pelo WP-CLI (`plugin install ... --activate`), faça backup, destrua tudo com `down -v`, restaure e prove que o plugin e o conteúdo voltaram.

## Veja também

- [[Persistência de bancos de dados]]
- [[configs e secrets no Compose]]
- [[depends_on com condition e healthcheck]]
- [[Backup e restauração de volumes]]
- [[Projeto 04 - Stack com Postgres, API e frontend]]
- [[MOC - Projetos - Docker]]
