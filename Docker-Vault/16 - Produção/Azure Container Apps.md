---
tags:
  - docker
  - producao
  - azure
  - serverless
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Azure Container Registry]]"
  - "[[Aplicações 12-factor em containers]]"
  - "[[Checklist de produção]]"
---

# Azure Container Apps

O **Azure Container Apps** executa containers sem gerenciar Kubernetes, com escala automática (inclusive a zero), revisões e ingress HTTPS.

```bash
az extension add --name containerapp --upgrade

RG=meu-grupo
AMBIENTE=ambiente-apps
APP=meu-app
ACR=meuacrunico

az group create --name $RG --location brazilsouth

# Ambiente (inclui Log Analytics)
az containerapp env create --name $AMBIENTE --resource-group $RG --location brazilsouth

# Aplicação a partir de uma imagem no ACR (usando identidade do registry)
az containerapp create \
  --name $APP \
  --resource-group $RG \
  --environment $AMBIENTE \
  --image $ACR.azurecr.io/meu-app:1.4.2 \
  --registry-server $ACR.azurecr.io \
  --registry-identity system \
  --target-port 8080 \
  --ingress external \
  --min-replicas 0 --max-replicas 5 \
  --cpu 0.5 --memory 1.0Gi \
  --env-vars APP_ENV=producao

# Nova versão
az containerapp update --name $APP --resource-group $RG --image $ACR.azurecr.io/meu-app:1.5.0
```

| Recurso | Descrição |
|---|---|
| Escala | Regras HTTP, fila, CPU, KEDA |
| Revisões | Dividem tráfego (blue-green/canary) |
| Dapr | Integração opcional para microsserviços |
| Segredos | `--secrets` e referências ao Key Vault |

> [!question] Verificar na documentação oficial
> Parâmetros de identidade de registry (`--registry-identity`) e atribuição de permissão `AcrPull` à identidade podem exigir passos adicionais. Consulte "Quickstart: Deploy to Azure Container Apps".

> [!tip] Quando escolher
> Bom meio-termo entre App Service e AKS: microsserviços e APIs sem a complexidade do Kubernetes.

## Exercício

Publique uma imagem de teste em um Container App com ingress externo e escale para zero; confirme o cold start ao acessar novamente.

## Veja também

- [[Azure Container Registry]]
- [[Aplicações 12-factor em containers]]
- [[Checklist de produção]]
- [[MOC - Produção]]
