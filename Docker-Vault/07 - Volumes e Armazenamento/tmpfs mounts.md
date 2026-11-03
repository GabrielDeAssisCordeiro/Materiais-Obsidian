---
tags:
  - docker
  - volumes
  - armazenamento
  - seguranca
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Volume vs bind mount vs tmpfs]]"
  - "[[Sintaxe -v vs --mount]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# tmpfs mounts

Um **tmpfs mount** armazena dados **somente na memória RAM** do host. Nada é gravado em disco e o conteúdo some quando o container para. Disponível apenas em Linux.

```bash
# Forma curta
docker run --rm --tmpfs /tmp:rw,size=64m,mode=1777 alpine:3.20 df -h /tmp

# Forma --mount
docker run --rm \
  --mount type=tmpfs,destination=/cache,tmpfs-size=128m \
  alpine:3.20 df -h /cache
```

## Usos típicos

- Dados sensíveis temporários que **não devem tocar o disco** (tokens, caches de sessão).
- Diretórios de escrita para containers `--read-only`.
- Acelerar I/O temporário (compilação, testes).

```bash
# Container somente leitura, com escrita só em /tmp e /run
docker run --rm --read-only \
  --tmpfs /tmp --tmpfs /run \
  alpine:3.20 sh -c 'touch /tmp/ok && echo escreveu em /tmp'
```

> [!warning] Consome memória
> O conteúdo conta como memória do host (e pode ser afetado por `--memory`). Defina `size` para evitar esgotar a RAM.

> [!tip] Hardening
> Combinar `--read-only` com `--tmpfs` é uma prática de segurança recomendada. Veja [[Princípio do menor privilégio - Docker]].

## Exercício

Rode um container `--read-only` e tente gravar em `/` e depois em um `--tmpfs /tmp`. Explique os resultados.

## Veja também

- [[Volume vs bind mount vs tmpfs]]
- [[Sintaxe -v vs --mount]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Volumes e Armazenamento]]
