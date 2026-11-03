---
tags:
  - docker
  - volumes
  - armazenamento
  - bind-mount
  - desenvolvimento
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Volumes nomeados]]"
  - "[[Volume vs bind mount vs tmpfs]]"
  - "[[Permissões e UID GID em volumes]]"
  - "[[Sintaxe -v vs --mount]]"
---

# Bind mounts

Um **bind mount** monta um **diretório ou arquivo do host** dentro do container. Alterações são visíveis nos dois lados instantaneamente.

```bash
# Código-fonte local acessível no container (ideal para desenvolvimento)
docker run --rm -v "$PWD":/app -w /app node:22-alpine node -v

# Somente leitura
docker run -d --name web -p 8080:80 \
  -v "$PWD/site":/usr/share/nginx/html:ro \
  nginx:1.27

# Um único arquivo (configuração)
docker run -d --name proxy -p 8081:80 \
  -v "$PWD/nginx.conf":/etc/nginx/nginx.conf:ro \
  nginx:1.27
```

> [!info] Caminho absoluto
> Com `-v`, use caminho absoluto no host (`$PWD`, `${PWD}`, `$(pwd)`). Um nome sem `/` é interpretado como **volume nomeado**.

## Quando usar

| Cenário | Bind mount? |
|---|---|
| Código-fonte em desenvolvimento (hot reload) | **Sim** |
| Arquivos de configuração do host | Sim (`:ro`) |
| Dados de produção | Prefira volumes |
| Compartilhar arquivos com o host (logs, exportações) | Sim |

## Particularidades por sistema

| Sistema | Observação |
|---|---|
| Linux | Acesso nativo; atenção a UID/GID e SELinux (`:z` ou `:Z`) |
| macOS | Compartilhamento de arquivos via VM; pode ser mais lento |
| Windows | Prefira o sistema de arquivos do WSL2 (`~/projetos`), não `C:\` |

```bash
# SELinux (Fedora/RHEL): rotula o conteúdo para o container
docker run --rm -v "$PWD":/app:Z alpine:3.20 ls /app
```

> [!danger] Bind mounts expõem o host
> Montar `/`, `/etc`, `/var/run/docker.sock` ou `$HOME` dá ao container acesso potencialmente total ao host. Monte somente o necessário, preferindo `:ro`.

> [!bug] Diretório vazio no container
> Um bind mount **sobrepõe** o conteúdo da imagem no destino. Se o diretório do host está vazio, o container verá vazio, diferente de volumes nomeados, que são populados na criação.

## Exercício

Crie uma pasta `site` com um `index.html`, sirva-a com Nginx via bind mount `:ro`, edite o arquivo e atualize o navegador para ver a mudança sem recriar o container.

## Veja também

- [[Volumes nomeados]]
- [[Volume vs bind mount vs tmpfs]]
- [[Permissões e UID GID em volumes]]
- [[Sintaxe -v vs --mount]]
- [[MOC - Volumes e Armazenamento]]
