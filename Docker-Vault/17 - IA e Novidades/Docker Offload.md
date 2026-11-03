---
tags:
  - docker
  - ia
  - novidades
  - nuvem
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker Model Runner]]"
  - "[[Containers com GPU e NVIDIA Container Toolkit]]"
  - "[[Buildx e BuildKit]]"
---

# Docker Offload

O **Docker Offload** permite que o Docker Desktop **delegue a execução** de builds e containers a uma infraestrutura **em nuvem** (incluindo máquinas com GPU), mantendo o fluxo de trabalho local (`docker run`, `docker compose up`).

## Para quê

| Cenário | Benefício |
|---|---|
| Notebook sem GPU | Treinar/testar modelos em GPUs na nuvem |
| Ambientes restritos (VDI, máquinas limitadas) | Executar containers sem recursos locais |
| Builds pesados | Aproveitar capacidade remota |

```bash
# Conceito (a sintaxe exata pode variar por versão)
docker offload start        # ativa a sessão de offload
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
docker offload stop         # encerra a sessão
```

## Relacionado: Docker Build Cloud

Builders remotos para acelerar builds e compartilhar cache entre a equipe, usados via Buildx (`--driver cloud`).

> [!question] Verificar na documentação oficial
> O Docker Offload e o Build Cloud são serviços da Docker, com planos, créditos e disponibilidade próprios, e o recurso é recente. Confirme comandos, requisitos e custos na documentação oficial antes de usar.

> [!warning] Dados na nuvem
> Ao executar remotamente, código, dados e imagens trafegam para um ambiente de terceiros. Avalie requisitos de privacidade e conformidade.

## Exercício

Liste três cargas de trabalho que se beneficiariam de offload para GPU em nuvem e três que **não** devem sair da sua máquina por motivos de dados.

## Veja também

- [[Docker Model Runner]]
- [[Containers com GPU e NVIDIA Container Toolkit]]
- [[Buildx e BuildKit]]
- [[MOC - IA e Novidades]]
