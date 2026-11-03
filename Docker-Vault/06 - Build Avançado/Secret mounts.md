---
tags:
  - docker
  - build-avancado
  - buildkit
  - seguranca
  - segredos
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Instruções ENV e ARG]]"
  - "[[SSH mounts]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Secret mounts

Um **secret mount** expõe um segredo ao comando `RUN` **apenas durante a execução**, sem gravá-lo em nenhuma camada nem no histórico.

```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
WORKDIR /app
COPY package.json package-lock.json ./

# O arquivo aparece em /run/secrets/npmrc (ou no target indicado) só neste RUN
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm ci
COPY . .
```

```bash
# Fornecendo um arquivo
docker build --secret id=npmrc,src=$HOME/.npmrc -t app .

# Fornecendo uma variável de ambiente do host
export NPM_TOKEN=exemplo-de-laboratorio
docker build --secret id=NPM_TOKEN,env=NPM_TOKEN -t app .
```

```dockerfile
# Lendo de variável de ambiente exposta pelo secret
RUN --mount=type=secret,id=NPM_TOKEN,env=NPM_TOKEN \
    sh -c 'echo "token tem ${#NPM_TOKEN} caracteres"'
```

> [!danger] O que NÃO fazer (antipadrão ilustrativo)
> ```dockerfile
> # ❌ INSEGURO: o token fica no histórico da imagem (docker history) e em metadados
> ARG NPM_TOKEN
> RUN echo "//registry.npmjs.org/:_authToken=${NPM_TOKEN}" > ~/.npmrc && npm ci && rm ~/.npmrc
> ```
> Mesmo removendo o arquivo depois, o valor permanece visível no histórico e na camada anterior. Use sempre secret mounts.

> [!tip] Verifique o resultado
> Depois do build, rode `docker history --no-trunc IMAGEM` e `docker run --rm IMAGEM ls /run/secrets` para confirmar que o segredo não ficou na imagem.

> [!info] Segredos em tempo de execução
> Secret mounts servem para o **build**. Para execução, use Docker/Swarm/Compose secrets (veja [[Princípio do menor privilégio - Docker]]).

## Exercício

Crie um arquivo `token.txt`, construa uma imagem que lê seu tamanho via secret mount e prove com `docker history` que o conteúdo não aparece.

## Veja também

- [[Instruções ENV e ARG]]
- [[SSH mounts]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Build Avançado]]
