---
tags:
  - docker
  - registries
  - aws
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Login e tokens de acesso]]"
  - "[[Registries]]"
  - "[[Políticas de retenção e limpeza]]"
---

# AWS ECR

O **Amazon Elastic Container Registry (ECR)** é o registry gerenciado da AWS, integrado a IAM, ECS, EKS e Lambda.

```bash
REGIAO=sa-east-1
CONTA=123456789012          # substitua pelo ID da sua conta

# Cria o repositório (tags imutáveis e varredura no push)
aws ecr create-repository \
  --repository-name meu-app \
  --image-tag-mutability IMMUTABLE \
  --image-scanning-configuration scanOnPush=true \
  --region $REGIAO

# Autentica o Docker (o token vale por 12 horas)
aws ecr get-login-password --region $REGIAO | \
  docker login --username AWS --password-stdin $CONTA.dkr.ecr.$REGIAO.amazonaws.com

# Publica
docker tag meu-app:1.0 $CONTA.dkr.ecr.$REGIAO.amazonaws.com/meu-app:1.0
docker push $CONTA.dkr.ecr.$REGIAO.amazonaws.com/meu-app:1.0
```

| Recurso | Descrição |
|---|---|
| Tags imutáveis | Impedem sobrescrever uma tag existente |
| Scan on push | Varredura de vulnerabilidades |
| Lifecycle policies | Remoção automática de imagens antigas |
| Replicação | Entre regiões/contas |
| Pull through cache | Espelha registries upstream |

> [!tip] Permissões mínimas
> A identidade que publica precisa de ações como `ecr:GetAuthorizationToken`, `ecr:BatchCheckLayerAvailability`, `ecr:PutImage`, `ecr:InitiateLayerUpload`, `ecr:UploadLayerPart` e `ecr:CompleteLayerUpload`. Conceda apenas ao repositório necessário.

> [!question] Verificar na documentação oficial
> Confirme as políticas IAM atuais e os custos de armazenamento/transferência na documentação da AWS.

## Exercício

Em uma conta de laboratório, crie um repositório ECR com tags imutáveis, publique uma imagem e tente sobrescrever a mesma tag para ver o erro.

## Veja também

- [[Login e tokens de acesso]]
- [[Registries]]
- [[Políticas de retenção e limpeza]]
- [[MOC - Registries]]
