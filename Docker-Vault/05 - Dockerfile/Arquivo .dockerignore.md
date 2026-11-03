---
tags:
  - docker
  - dockerfile
  - build
  - contexto
aliases: []
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Instruções COPY e ADD]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Introdução ao Dockerfile]]"
---

# Arquivo .dockerignore

O `.dockerignore` fica na raiz do contexto e lista o que **não** deve ser enviado ao builder. Benefícios: builds mais rápidos, menos cache invalidado e menos risco de vazar segredos.

```text
# .dockerignore
.git
.gitignore
**/node_modules
**/__pycache__
*.log
.env
.env.*
Dockerfile
docker-compose*.yml
compose*.yaml
*.md
!README.md
dist
coverage
.vscode
.idea
```

## Sintaxe

| Padrão | Efeito |
|---|---|
| `*.log` | Arquivos `.log` na raiz do contexto |
| `**/*.log` | Em qualquer nível |
| `!README.md` | Exceção (inclui mesmo que um padrão anterior exclua) |
| `#` | Comentário |

```bash
# Veja o tamanho do contexto enviado (BuildKit mostra "transferring context")
docker build --progress=plain -t teste . 2>&1 | grep -i context
```

> [!danger] Vazamento de segredos
> Sem `.dockerignore`, um `COPY . .` pode levar `.env`, chaves SSH, `.git` e credenciais para a imagem. Quem baixar a imagem poderá extraí-los.

> [!tip] Estratégia "lista de permissão"
> Para controle máximo, ignore tudo e libere só o necessário:
> ```text
> *
> !src/
> !package.json
> !package-lock.json
> ```

## Exercício

Crie um projeto com `node_modules` grande, meça o tempo de `docker build` com e sem `.dockerignore` e compare a mensagem "transferring context".

## Veja também

- [[Instruções COPY e ADD]]
- [[Cache de camadas e ordem das instruções]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
