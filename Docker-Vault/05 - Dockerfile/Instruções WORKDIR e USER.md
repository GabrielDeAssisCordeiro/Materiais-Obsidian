---
tags:
  - docker
  - dockerfile
  - instrucao
  - seguranca
aliases: []
tipo: instrucao
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Instruções COPY e ADD]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instruções WORKDIR e USER

## WORKDIR

Define o diretório de trabalho para as instruções seguintes (`RUN`, `CMD`, `COPY`...). Cria o diretório se necessário. Prefira-o a `RUN cd ...`.

```dockerfile
WORKDIR /app
COPY . .                 # copia para /app
RUN ls                   # executa em /app
```

## USER

Define o usuário (e grupo) com que as instruções seguintes e o container serão executados. **Por padrão, containers executam como root.**

```dockerfile
# Debian/Ubuntu
RUN groupadd --system --gid 10001 app \
 && useradd  --system --uid 10001 --gid app --no-create-home app
USER app

# Alpine
RUN addgroup -S -g 10001 app && adduser -S -u 10001 -G app app
USER app

# Ou simplesmente um UID numérico
USER 10001:10001
```

```dockerfile
# Copiando arquivos já com o dono correto
COPY --chown=app:app . /app
```

> [!tip] UID numérico
> Orquestradores como Kubernetes validam `runAsNonRoot` mais facilmente com UID numérico. Imagens oficiais como `nginx-unprivileged` e variantes `nonroot` do distroless já vêm prontas.

> [!danger] Rodar como root aumenta o impacto de uma invasão
> Combine `USER` não-root com `--read-only`, `--cap-drop ALL` e `no-new-privileges`. Veja [[Princípio do menor privilégio - Docker]].

> [!bug] "Permission denied" ao escrever
> Com usuário não-root, diretórios de escrita precisam pertencer a ele (`--chown`, `chown` em um `RUN` antes do `USER`) e portas abaixo de 1024 não podem ser abertas sem a capability apropriada.

## Exercício

Altere o Dockerfile do exemplo para executar como usuário `app` (UID 10001) e confirme com `docker exec CONTAINER id`.

## Veja também

- [[Princípio do menor privilégio - Docker]]
- [[Instruções COPY e ADD]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
