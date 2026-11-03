---
tags:
  - docker
  - containers
  - comandos
  - run
aliases:
  - docker run
  - docker container run
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Ciclo de vida do container]]"
  - "[[Modos interativo e detached]]"
  - "[[Publicação de portas]]"
  - "[[Variáveis de ambiente em containers]]"
  - "[[Limites de recursos - Docker]]"
---

# Comando docker run

`docker run` = `docker create` + `docker start` (+ `docker attach` quando em primeiro plano). Se a imagem não existir localmente, faz `pull` antes.

## Sintaxe

```text
docker run [OPÇÕES] IMAGEM[:TAG|@DIGEST] [COMANDO] [ARGS...]
```

## Opções mais usadas

| Opção | Efeito |
|---|---|
| `-d` | Executa em segundo plano (*detached*). |
| `-it` | Terminal interativo (`-i` stdin aberto, `-t` pseudo-TTY). |
| `--name NOME` | Nome do container. |
| `--rm` | Remove o container automaticamente ao sair. |
| `-p HOST:CONTAINER` | Publica uma porta. |
| `-e CHAVE=VALOR` | Variável de ambiente. |
| `-v ORIGEM:DESTINO` | Monta volume ou diretório. |
| `--network REDE` | Conecta a uma rede. |
| `--restart POLITICA` | Política de reinício. |
| `-m`, `--cpus` | Limites de memória e CPU. |
| `-u USUARIO` | Usuário que executa o processo. |
| `-w DIR` | Diretório de trabalho. |
| `--entrypoint` | Sobrescreve o ENTRYPOINT da imagem. |

## Exemplos

```bash
# Executa um comando e remove o container ao terminar
docker run --rm alpine:3.20 echo "Olá do container"

# Shell interativo descartável
docker run --rm -it alpine:3.20 sh

# Servidor web em segundo plano com nome e porta publicada
docker run -d --name web -p 8080:80 nginx:1.27

# Banco de dados com variáveis, volume nomeado e restart
docker run -d --name db \
  -e POSTGRES_PASSWORD=senha-de-laboratorio \
  -v pgdata:/var/lib/postgresql/data \
  --restart unless-stopped \
  postgres:16

# Limpa o laboratório
docker rm -f web db && docker volume rm pgdata
```

> [!tip] Argumentos após a imagem
> Tudo que vem **depois** do nome da imagem é o comando (substitui o `CMD`) e seus argumentos. Opções do Docker devem vir **antes** da imagem.

> [!warning] Evite `latest` em ambientes reais
> Sem tag, o Docker usa `latest`, que muda ao longo do tempo. Fixe versões (`nginx:1.27`) para builds e deploys reproduzíveis. Veja [[Tags e digests de imagens]].

> [!bug] "docker: Error response from daemon: Conflict. The container name is already in use"
> Já existe um container (mesmo parado) com esse nome. Remova-o com `docker rm NOME` ou escolha outro nome.

## Exercício

Suba um Nginx com `--name`, `-p 8081:80` e `-d`; acesse com `curl`; veja os logs; e remova o container. Depois repita com `--rm` e compare o que sobra em `docker ps -a`.

## Veja também

- [[Ciclo de vida do container]]
- [[Modos interativo e detached]]
- [[Publicação de portas]]
- [[Variáveis de ambiente em containers]]
- [[Limites de recursos - Docker]]
- [[MOC - Containers]]
