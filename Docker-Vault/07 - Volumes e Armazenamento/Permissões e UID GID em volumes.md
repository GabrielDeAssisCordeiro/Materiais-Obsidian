---
tags:
  - docker
  - volumes
  - armazenamento
  - permissoes
  - seguranca
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Bind mounts]]"
  - "[[Instruções WORKDIR e USER]]"
  - "[[Modo rootless]]"
  - "[[Backup e restauração de volumes]]"
---

# Permissões e UID GID em volumes

Containers e host compartilham o **mesmo kernel**, e o dono dos arquivos é identificado por **UID/GID numéricos**, não por nomes. Daí vêm muitos erros de *permission denied*.

```bash
# O container roda como root (UID 0) e cria arquivo no bind mount → arquivo do root no host
docker run --rm -v "$PWD":/dados alpine:3.20 touch /dados/arquivo-do-root
ls -l arquivo-do-root

# Rodando com o seu UID/GID, arquivos ficam seus
docker run --rm -u "$(id -u):$(id -g)" -v "$PWD":/dados alpine:3.20 touch /dados/arquivo-meu
ls -l arquivo-meu
```

## Estratégias

| Problema | Solução |
|---|---|
| Arquivos criados como root no bind mount | `--user "$(id -u):$(id -g)"` ou `user:` no Compose |
| Aplicação não-root não escreve no volume | `chown` no Dockerfile antes do `USER`, ou no ponto de entrada |
| Volume novo com dono errado | `COPY --chown`, `mkdir` + `chown` no Dockerfile (o volume nomeado herda dono e permissões do diretório da imagem) |
| SELinux bloqueia | `:z` (compartilhado) ou `:Z` (privado) no `-v` |
| Modo rootless | UID 0 do container mapeia para seu UID no host; use `--userns=keep-id` (Podman) ou ajuste `subuid` |

```dockerfile
FROM python:3.12-slim
RUN useradd --system --uid 10001 app \
 && mkdir -p /dados \
 && chown app:app /dados
USER 10001
VOLUME /dados    # (ilustrativo; veja a nota sobre VOLUME)
```

```bash
# Corrige o dono de um volume com um container temporário
docker run --rm -v dados:/dados alpine:3.20 chown -R 10001:10001 /dados
```

> [!danger] Evite `chmod 777`
> Resolve o sintoma e abre uma brecha. Descubra o UID correto e ajuste o dono.

> [!info] Docker Desktop (macOS/Windows)
> A camada de compartilhamento de arquivos traduz propriedade; muitos problemas de UID/GID de Linux não aparecem nesses sistemas, mas aparecem no servidor de produção.

## Exercício

Reproduza o problema do arquivo criado como root em um bind mount e depois resolva com `--user`. Descreva a diferença de dono em `ls -ln`.

## Veja também

- [[Bind mounts]]
- [[Instruções WORKDIR e USER]]
- [[Modo rootless]]
- [[Backup e restauração de volumes]]
- [[MOC - Volumes e Armazenamento]]
