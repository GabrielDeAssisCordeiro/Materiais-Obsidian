---
tags:
  - docker
  - build-avancado
  - buildkit
  - ssh
  - seguranca
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Secret mounts]]"
  - "[[Buildx e BuildKit]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# SSH mounts

O **SSH mount** encaminha o `ssh-agent` do host ao build, permitindo clonar repositórios privados **sem copiar chaves privadas** para a imagem.

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine:3.20
RUN apk add --no-cache git openssh-client

# Adiciona a chave do host do GitHub para evitar prompts
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts

RUN --mount=type=ssh git clone git@github.com:ORG/REPO-PRIVADO.git /src
```

```bash
# Inicie o agente e carregue sua chave
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Construa encaminhando o agente
docker build --ssh default -t app .
```

> [!danger] Nunca copie chaves privadas para a imagem
> ```dockerfile
> # ❌ INSEGURO: a chave fica gravada na camada
> COPY id_rsa /root/.ssh/id_rsa
> ```

> [!warning] `ssh-keyscan` confia no primeiro uso
> Para máxima segurança, verifique a impressão digital oficial da chave do host e use um arquivo `known_hosts` fixado.

> [!tip] Alternativas
> Em CI, tokens de acesso com escopo restrito e [[Secret mounts]] costumam ser mais simples que SSH.

## Exercício

Em laboratório, use `--mount=type=ssh` para clonar um repositório privado seu e confirme que `~/.ssh` não existe na imagem final.

## Veja também

- [[Secret mounts]]
- [[Buildx e BuildKit]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Build Avançado]]
