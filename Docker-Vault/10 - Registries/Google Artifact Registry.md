---
tags:
  - docker
  - registries
  - gcp
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Login e tokens de acesso]]"
  - "[[Registries]]"
  - "[[Políticas de retenção e limpeza]]"
---

# Google Artifact Registry

O **Artifact Registry** (sucessor do Container Registry) do Google Cloud armazena imagens Docker e outros artefatos.

```bash
REGIAO=southamerica-east1
PROJETO=meu-projeto
REPO=containers

# Cria o repositório Docker
gcloud artifacts repositories create $REPO \
  --repository-format=docker \
  --location=$REGIAO \
  --description="Imagens da aplicação"

# Configura o Docker para autenticar com gcloud
gcloud auth configure-docker $REGIAO-docker.pkg.dev

# Publica
docker tag meu-app:1.0 $REGIAO-docker.pkg.dev/$PROJETO/$REPO/meu-app:1.0
docker push $REGIAO-docker.pkg.dev/$PROJETO/$REPO/meu-app:1.0
```

| Recurso | Descrição |
|---|---|
| Políticas de limpeza (*cleanup policies*) | Excluem versões por idade ou quantidade |
| Escaneamento de vulnerabilidades | Integrado ao Artifact Analysis |
| Repositórios remotos e virtuais | Espelhamento do Docker Hub e agregação |

> [!tip] Autenticação em CI
> Prefira **Workload Identity Federation** em vez de chaves JSON de service account de longa duração.

## Exercício

Crie um repositório Docker no Artifact Registry e configure uma política de limpeza que mantenha apenas as 10 versões mais recentes.

## Veja também

- [[Login e tokens de acesso]]
- [[Registries]]
- [[Políticas de retenção e limpeza]]
- [[MOC - Registries]]
