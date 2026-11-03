---
tags:
  - docker
  - producao
  - hospedagem
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Aplicações 12-factor em containers]]"
  - "[[Checklist de produção]]"
  - "[[Hospedagem em VPS com Compose]]"
---

# Fly.io

O **Fly.io** executa containers (como *Machines* Firecracker) próximos aos usuários, em várias regiões, com deploy por CLI.

```bash
# Instale o flyctl (veja a documentação do seu sistema) e autentique
fly auth login

# Dentro do projeto com Dockerfile
fly launch              # detecta o Dockerfile, cria o app e gera o fly.toml
fly deploy              # constrói e implanta
fly status
fly logs
fly scale count 2       # número de máquinas
fly secrets set DATABASE_URL="postgres://..."   # segredos
```

`fly.toml` (exemplo):

```toml
app = "meu-app"
primary_region = "gru"

[build]
  dockerfile = "Dockerfile"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = "stop"
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  size = "shared-cpu-1x"
  memory = "512mb"
```

| Recurso | Observação |
|---|---|
| Regiões | Multi-região; `gru` = São Paulo |
| Volumes | Volumes locais por máquina (estado exige cuidado) |
| Rede privada | `.internal` entre apps da mesma organização |
| Escala a zero | `auto_stop_machines` / `auto_start_machines` |

> [!question] Verificar na documentação oficial
> Planos, preços, nomes de campos do `fly.toml` e tamanhos de VM mudam; consulte a documentação do Fly.io. Prefira implantar imagens já construídas com `fly deploy --image` para promover a **mesma** imagem entre ambientes.

> [!tip] Banco de dados
> Avalie serviços gerenciados de banco para evitar operar o estado sozinho.

## Exercício

Implante o exemplo "Olá, Docker" no Fly.io, escale para 2 máquinas e observe os logs com `fly logs`.

## Veja também

- [[Aplicações 12-factor em containers]]
- [[Checklist de produção]]
- [[Hospedagem em VPS com Compose]]
- [[MOC - Produção]]
