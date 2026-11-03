---
tags:
  - docker
  - producao
  - aws
  - nuvem
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[AWS ECR]]"
  - "[[Docker com Terraform e Ansible]]"
  - "[[Checklist de produção]]"
---

# AWS ECS com Fargate

O **Amazon ECS** orquestra containers; com **Fargate** você não gerencia servidores: define CPU/memória e a AWS executa.

## Conceitos

| Conceito | Descrição |
|---|---|
| **Cluster** | Agrupamento lógico |
| **Task definition** | "Receita" do container(s): imagem, CPU, memória, portas, logs, variáveis |
| **Task** | Instância em execução da task definition |
| **Service** | Mantém N tasks, integra com Load Balancer e faz rolling updates |

## Task definition mínima (JSON)

```json
{
  "family": "meu-app",
  "requiresCompatibilities": ["FARGATE"],
  "networkMode": "awsvpc",
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::123456789012:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "app",
      "image": "123456789012.dkr.ecr.sa-east-1.amazonaws.com/meu-app:1.4.2",
      "essential": true,
      "portMappings": [{ "containerPort": 8080, "protocol": "tcp" }],
      "environment": [{ "name": "APP_ENV", "value": "producao" }],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/meu-app",
          "awslogs-region": "sa-east-1",
          "awslogs-stream-prefix": "app"
        }
      }
    }
  ]
}
```

```bash
aws ecs create-cluster --cluster-name producao
aws ecs register-task-definition --cli-input-json file://taskdef.json
aws ecs create-service \
  --cluster producao --service-name meu-app \
  --task-definition meu-app --desired-count 2 --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-AAAA,subnet-BBBB],securityGroups=[sg-CCCC],assignPublicIp=DISABLED}"

# Deploy de nova versão: registre nova task definition e atualize o serviço
aws ecs update-service --cluster producao --service meu-app --task-definition meu-app --force-new-deployment
```

> [!info] Segredos
> Use `secrets` na definição do container referenciando **AWS Secrets Manager** ou **SSM Parameter Store**, em vez de `environment`.

> [!warning] Integração antiga do Docker com ECS
> A integração `docker compose` → ECS (`docker ecs`) foi descontinuada. Use Terraform, CloudFormation/CDK, ou ferramentas da AWS.

> [!question] Verificar na documentação oficial
> Os valores de CPU/memória aceitos, as ferramentas recomendadas pela AWS para ECS e os custos mudam com frequência; consulte a documentação do ECS e o simulador de preços.

## Exercício

Em uma conta de laboratório, publique a imagem no ECR, registre a task definition e crie um serviço Fargate com 1 task. Depois destrua tudo para evitar custos.

## Veja também

- [[AWS ECR]]
- [[Docker com Terraform e Ansible]]
- [[Checklist de produção]]
- [[MOC - Produção]]
