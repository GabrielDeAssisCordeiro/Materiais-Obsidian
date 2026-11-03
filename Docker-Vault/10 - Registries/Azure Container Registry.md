---
tags:
  - docker
  - registries
  - azure
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Login e tokens de acesso]]"
  - "[[Registries]]"
  - "[[Políticas de retenção e limpeza]]"
---

# Azure Container Registry

O **Azure Container Registry (ACR)** é o registry gerenciado da Microsoft, integrado ao AKS, Container Apps e Azure DevOps.

```bash
RG=meu-grupo
ACR=meuacrunico            # nome globalmente único, apenas letras e números

az group create --name $RG --location brazilsouth
az acr create --resource-group $RG --name $ACR --sku Basic

# Login (usa a sessão do az)
az acr login --name $ACR

docker tag meu-app:1.0 $ACR.azurecr.io/meu-app:1.0
docker push $ACR.azurecr.io/meu-app:1.0

# Lista repositórios e tags
az acr repository list --name $ACR -o table
az acr repository show-tags --name $ACR --repository meu-app -o table
```

| Recurso | Descrição |
|---|---|
| SKUs | Basic, Standard, Premium (replicação geográfica, retenção, endpoints privados) |
| ACR Tasks | Builds na própria nuvem (`az acr build`) |
| Identidade gerenciada | Pull sem senhas a partir de AKS/Container Apps |

```bash
# Build diretamente no ACR, sem Docker local
az acr build --registry $ACR --image meu-app:1.1 .
```

> [!warning] Evite a conta de administrador
> A opção `--admin-enabled` cria uma credencial compartilhada. Prefira identidades gerenciadas ou service principals com a função `AcrPush`/`AcrPull`.

## Exercício

Crie um ACR Basic de laboratório, publique uma imagem e liste as tags com `az acr repository show-tags`.

## Veja também

- [[Login e tokens de acesso]]
- [[Registries]]
- [[Políticas de retenção e limpeza]]
- [[MOC - Registries]]
