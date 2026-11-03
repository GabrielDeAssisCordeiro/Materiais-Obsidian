---
tags:
  - docker
  - producao
  - gcp
  - serverless
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Google Artifact Registry]]"
  - "[[Aplicações 12-factor em containers]]"
  - "[[Checklist de produção]]"
---

# Google Cloud Run

O **Cloud Run** executa containers **stateless** de forma serverless: escala de **zero** a N instâncias conforme as requisições, com cobrança por uso.

## Requisitos do container

- Escuta HTTP na porta indicada pela variável de ambiente **`PORT`** (padrão 8080) em `0.0.0.0`.
- Sem estado local persistente (disco efêmero).
- Inicialização rápida e encerramento gracioso.

## Deploy a partir de uma imagem

```bash
REGIAO=southamerica-east1

gcloud run deploy meu-app \
  --image $REGIAO-docker.pkg.dev/PROJETO/containers/meu-app:1.4.2 \
  --region $REGIAO \
  --port 8080 \
  --memory 512Mi --cpu 1 \
  --min-instances 0 --max-instances 5 \
  --set-env-vars APP_ENV=producao \
  --allow-unauthenticated

# URL do serviço
gcloud run services describe meu-app --region $REGIAO --format 'value(status.url)'
```

## Deploy direto do código (build na nuvem)

```bash
gcloud run deploy meu-app --source . --region $REGIAO
```

| Recurso | Observação |
|---|---|
| Revisões e tráfego | Cada deploy cria uma revisão; divida o tráfego entre revisões (canary) |
| Segredos | Integração com Secret Manager |
| Conexão a bancos | Cloud SQL via conector |
| Cold start | Primeira requisição após zero instâncias é mais lenta (`--min-instances 1` evita) |

```bash
# Canary: 10% para a nova revisão
gcloud run services update-traffic meu-app --region $REGIAO --to-revisions NOVA_REVISAO=10
```

> [!tip] Ideal para
> APIs e sites com tráfego variável, jobs (Cloud Run Jobs) e serviços sem estado.

> [!warning] Não é para tudo
> Workloads com estado local, conexões longas persistentes ou necessidade de controle fino de rede podem se encaixar melhor em GKE/VMs.

## Exercício

Faça o deploy de uma imagem simples (por exemplo, `us-docker.pkg.dev/cloudrun/container/hello`) no Cloud Run e experimente dividir o tráfego entre duas revisões.

## Veja também

- [[Google Artifact Registry]]
- [[Aplicações 12-factor em containers]]
- [[Checklist de produção]]
- [[MOC - Produção]]
