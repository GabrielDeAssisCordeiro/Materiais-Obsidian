---
tags:
  - docker
  - volumes
  - armazenamento
  - backup
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Persistência de bancos de dados]]"
  - "[[Volumes nomeados]]"
  - "[[Permissões e UID GID em volumes]]"
---

# Backup e restauração de volumes

## Backup de um volume (arquivo tar)

```bash
# Container temporário monta o volume (somente leitura) e um diretório de saída
docker run --rm \
  -v pgdata:/dados:ro \
  -v "$PWD":/backup \
  alpine:3.20 \
  tar czf /backup/pgdata-$(date +%F).tar.gz -C /dados .
```

## Restauração

```bash
docker volume create pgdata-restaurado
docker run --rm \
  -v pgdata-restaurado:/dados \
  -v "$PWD":/backup:ro \
  alpine:3.20 \
  sh -c 'cd /dados && tar xzf /backup/pgdata-AAAA-MM-DD.tar.gz'
```

## Bancos de dados: prefira backup lógico

Copiar arquivos de um banco **em execução** pode gerar um backup inconsistente. Use as ferramentas do banco:

```bash
# PostgreSQL
docker exec pg pg_dump -U postgres -d appdb > appdb.sql
cat appdb.sql | docker exec -i pg psql -U postgres -d appdb

# MySQL / MariaDB
docker exec mysql sh -c 'mysqldump -u root -p"$MYSQL_ROOT_PASSWORD" appdb' > appdb.sql
```

> [!warning] Teste a restauração
> Um backup só vale se a restauração foi testada. Agende restaurações periódicas em ambiente separado.

> [!tip] Automatize e guarde fora do host
> Rotacione backups, guarde em armazenamento externo (S3, outro servidor) e criptografe se houver dados sensíveis.

## Exercício

Faça backup e restauração do volume do exercício anterior em um volume novo, e confirme os dados iniciando um container com o volume restaurado.

## Veja também

- [[Persistência de bancos de dados]]
- [[Volumes nomeados]]
- [[Permissões e UID GID em volumes]]
- [[MOC - Volumes e Armazenamento]]
