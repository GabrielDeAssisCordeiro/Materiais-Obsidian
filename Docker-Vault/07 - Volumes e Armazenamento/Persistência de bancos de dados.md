---
tags:
  - docker
  - volumes
  - armazenamento
  - banco-de-dados
  - postgres
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Volumes nomeados]]"
  - "[[Backup e restauração de volumes]]"
  - "[[Variáveis de ambiente em containers]]"
  - "[[Healthchecks em containers]]"
---

# Persistência de bancos de dados

Bancos de dados em container **devem** usar volumes. Sem eles, os dados vivem na camada gravável e somem ao remover o container.

```bash
# PostgreSQL com volume nomeado
docker run -d --name pg \
  -e POSTGRES_PASSWORD=senha-de-laboratorio \
  -e POSTGRES_DB=appdb \
  -v pgdata:/var/lib/postgresql/data \
  -p 127.0.0.1:5432:5432 \
  postgres:16

# Cria uma tabela e insere dados
docker exec -it pg psql -U postgres -d appdb \
  -c "CREATE TABLE notas(id serial primary key, texto text);" \
  -c "INSERT INTO notas(texto) VALUES ('persistiu');"

# Destrói o container; os dados ficam no volume
docker rm -f pg

# Novo container, mesmo volume
docker run -d --name pg2 -e POSTGRES_PASSWORD=senha-de-laboratorio \
  -v pgdata:/var/lib/postgresql/data postgres:16
sleep 5
docker exec pg2 psql -U postgres -d appdb -c "SELECT * FROM notas;"

docker rm -f pg2
```

## Pontos de atenção

| Ponto | Recomendação |
|---|---|
| Um volume, **um** container de banco | Dois bancos no mesmo diretório corrompem os dados |
| Atualização de versão maior | Siga o procedimento do banco (dump/restore ou `pg_upgrade`); não troque a tag direto |
| Senhas | Use secrets (`POSTGRES_PASSWORD_FILE`) em vez de variáveis |
| Porta | Publique em `127.0.0.1` ou não publique; acesse pela rede interna |
| Parada | Dê tempo ao `docker stop` (`-t 30`) para encerramento limpo |

> [!question] Verificar na documentação oficial
> Em versões recentes da imagem `postgres` (a partir da 18) o diretório de dados padrão e o ponto de montagem recomendado do volume mudaram. Consulte a página da imagem no Docker Hub antes de usar uma tag nova. Os exemplos aqui usam `postgres:16`.

> [!danger] Não use bind mounts de bancos no macOS/Windows em produção de desenvolvimento pesado
> Problemas de desempenho e de permissão são comuns. Prefira volumes nomeados.

## Exercício

Reproduza o experimento: crie dados, destrua o container, recrie com o mesmo volume e consulte os dados. Depois repita sem volume e observe a perda.

## Veja também

- [[Volumes nomeados]]
- [[Backup e restauração de volumes]]
- [[Variáveis de ambiente em containers]]
- [[Healthchecks em containers]]
- [[MOC - Volumes e Armazenamento]]
