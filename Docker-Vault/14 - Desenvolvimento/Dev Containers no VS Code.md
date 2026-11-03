---
tags:
  - docker
  - desenvolvimento
aliases:
  - devcontainer
  - devcontainer.json
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Ambientes de desenvolvimento reproduzíveis]]"
  - "[[Visão geral do Docker Compose]]"
  - "[[Hot reload em containers]]"
---

# Dev Containers no VS Code

**Dev Containers** permitem desenvolver **dentro de um container**: o VS Code se conecta a ele, e extensões, terminal e depurador rodam lá, com todas as ferramentas e versões definidas no repositório.

## Requisitos

- Docker (Desktop ou Engine) em execução.
- VS Code com a extensão **Dev Containers**.

## `.devcontainer/devcontainer.json` com uma imagem pronta

```json
{
  "name": "Python 3.12",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "forwardPorts": [8000],
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python"]
    }
  }
}
```

Abra a pasta no VS Code e use **Dev Containers: Reopen in Container**.

## Com Docker Compose (app + banco)

`.devcontainer/devcontainer.json`:

```json
{
  "name": "App com banco",
  "dockerComposeFile": "compose.yaml",
  "service": "app",
  "workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}",
  "shutdownAction": "stopCompose"
}
```

`.devcontainer/compose.yaml`:

```yaml
services:
  app:
    image: mcr.microsoft.com/devcontainers/python:3.12
    volumes:
      - ..:/workspaces/projeto:cached
    command: sleep infinity
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: senha-de-laboratorio
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

> [!tip] Benefícios
> Onboarding em minutos, mesma versão de runtime para toda a equipe, e o ambiente é versionado no Git. Funciona também no GitHub Codespaces.

> [!warning] Desempenho no macOS/Windows
> Mantenha o código em um volume do container ou no sistema de arquivos do WSL2 para evitar a lentidão de bind mounts.

> [!question] Verificar na documentação oficial
> As tags das imagens `mcr.microsoft.com/devcontainers/*` e os identificadores de *features* evoluem; consulte containers.dev para os valores atuais.

## Exercício

Crie um `.devcontainer` para um projeto seu com uma imagem Python ou Node e reabra no container. Confirme a versão do runtime com `python --version` ou `node -v`.

## Veja também

- [[Ambientes de desenvolvimento reproduzíveis]]
- [[Visão geral do Docker Compose]]
- [[Hot reload em containers]]
- [[MOC - Desenvolvimento]]
