---
tags:
  - docker
  - seguranca
  - hardening
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[tmpfs mounts]]"
  - "[[Camada gravável do container]]"
---

# Sistema de arquivos somente leitura

`--read-only` monta o sistema de arquivos raiz do container como **somente leitura**. Um invasor não consegue gravar binários, scripts ou persistir modificações.

```bash
docker run --rm --read-only alpine:3.20 sh -c 'touch /arquivo' \
  || echo "bloqueado: sistema de arquivos somente leitura"

# Permite escrita apenas onde é necessário
docker run --rm --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=32m \
  -v dados:/dados \
  alpine:3.20 sh -c 'touch /tmp/ok /dados/ok && echo "escrita permitida em /tmp e /dados"'
```

## Em Compose

```yaml
services:
  web:
    image: nginx:1.27
    read_only: true
    tmpfs:
      - /var/cache/nginx
      - /var/run
      - /tmp
```

## Como descobrir onde a aplicação precisa escrever

```bash
# Rode normalmente, exercite a aplicação e veja o que mudou
docker diff NOME_DO_CONTAINER
```

> [!tip] Opções do tmpfs
> `noexec` impede executar binários gravados em `/tmp`; `nosuid` ignora bits setuid. Nem toda aplicação funciona com `noexec` (por exemplo, algumas JVMs e addons nativos).

> [!bug] "Read-only file system"
> A aplicação tenta gravar em um local não permitido (cache, PID, logs, `/tmp`). Mapeie esse caminho para `tmpfs` ou volume, ou redirecione logs para stdout.

## Exercício

Execute o Nginx com `--read-only` e use as mensagens de erro e o `docker diff` para descobrir quais diretórios precisam de `tmpfs`.

## Veja também

- [[Princípio do menor privilégio - Docker]]
- [[tmpfs mounts]]
- [[Camada gravável do container]]
- [[MOC - Segurança]]
