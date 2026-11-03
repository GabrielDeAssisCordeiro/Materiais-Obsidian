---
tags:
  - docker
  - volumes
  - armazenamento
aliases:
  - Volumes
  - docker volume
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Bind mounts]]"
  - "[[Volume vs bind mount vs tmpfs]]"
  - "[[Persistência de bancos de dados]]"
  - "[[Backup e restauração de volumes]]"
  - "[[Camada gravável do container]]"
---

# Volumes nomeados

**Volumes** são o mecanismo preferido do Docker para **persistir dados**. São gerenciados pelo Docker, independem do ciclo de vida dos containers e funcionam igual em Linux, Windows e macOS.

```bash
# Criar, listar, inspecionar
docker volume create dados
docker volume ls
docker volume inspect dados

# Usar em um container (cria o volume automaticamente se não existir)
docker run -d --name db -v dados:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=senha-de-laboratorio postgres:16

# O volume sobrevive à remoção do container
docker rm -f db
docker run --rm -v dados:/dados alpine:3.20 ls /dados

# Remover (apenas se nenhum container o usa)
docker volume rm dados
docker volume prune          # volumes anônimos sem uso
```

## Características

| Característica | Detalhe |
|---|---|
| Localização (Linux) | `/var/lib/docker/volumes/NOME/_data` (não edite diretamente) |
| Inicialização | Na primeira montagem, o volume é **populado** com o conteúdo do diretório da imagem naquele caminho |
| Compartilhamento | Vários containers podem montar o mesmo volume |
| Backup/migração | Mais simples que bind mounts |
| Drivers | Suporte a NFS, nuvem e armazenamento remoto via plugins |
| Desempenho | Bom em todas as plataformas (inclusive Docker Desktop) |

## Volume anônimo vs nomeado

```bash
docker run -d -v /dados alpine:3.20 sleep 300    # anônimo: nome aleatório (hash)
docker run -d -v dados:/dados alpine:3.20 sleep 300   # nomeado: fácil de gerenciar
```

> [!warning] Volumes anônimos se acumulam
> Prefira sempre **volumes nomeados** para dados que importam. Volumes anônimos são difíceis de identificar e removidos por `docker volume prune`.

> [!danger] `docker compose down -v` apaga os volumes
> A flag `-v` remove volumes nomeados declarados no Compose. Use com cuidado em ambientes com dados reais.

## Exercício

Crie um volume, grave um arquivo nele com um container `alpine`, remova o container e leia o arquivo com outro container.

## Veja também

- [[Bind mounts]]
- [[Volume vs bind mount vs tmpfs]]
- [[Persistência de bancos de dados]]
- [[Backup e restauração de volumes]]
- [[Camada gravável do container]]
- [[MOC - Volumes e Armazenamento]]
