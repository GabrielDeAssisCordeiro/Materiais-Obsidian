---
tags:
  - docker
  - compose
aliases: []
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Múltiplos arquivos e overrides]]"
  - "[[Estrutura do compose.yaml e Compose Specification]]"
  - "[[Projetos nomeados no Compose]]"
---

# extends e include

## `include`: reutiliza outros arquivos Compose completos

Cada arquivo incluído é um **modelo independente** (com seus próprios caminhos relativos), e seus serviços passam a fazer parte do projeto.

`compose.yaml`:

```yaml
include:
  - path: ./infra/banco.yaml
  - path: ./infra/monitoramento.yaml

services:
  api:
    image: traefik/whoami:v1.10
    depends_on:
      - db            # serviço vindo de infra/banco.yaml
```

`infra/banco.yaml`:

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: senha-de-laboratorio
    volumes:
      - dbdata:/var/lib/postgresql/data
volumes:
  dbdata:
```

## `extends`: herda a configuração de **um serviço**

`base.yaml`:

```yaml
services:
  servico-base:
    restart: unless-stopped
    environment:
      TZ: America/Sao_Paulo
    logging:
      driver: local
```

`compose.yaml`:

```yaml
services:
  worker:
    extends:
      file: base.yaml
      service: servico-base
    image: alpine:3.20
    command: sleep 3600
```

| | `include` | `extends` |
|---|---|---|
| Unidade | Arquivo inteiro (modelo completo) | Um serviço |
| Caminhos relativos | Resolvidos no arquivo incluído | Resolvidos no arquivo atual (atenção) |
| Uso típico | Equipes/serviços compartilhados | Reaproveitar configurações comuns |

> [!tip] Alternativa: âncoras YAML
> Para repetir blocos no **mesmo** arquivo, use `x-` extensions com âncoras:
> ```yaml
> x-comum: &comum
>   restart: unless-stopped
>   logging: { driver: local }
>
> services:
>   a: { <<: *comum, image: alpine:3.20, command: sleep 3600 }
>   b: { <<: *comum, image: alpine:3.20, command: sleep 3600 }
> ```

> [!question] Verificar na documentação oficial
> `include` exige uma versão mínima do Compose v2 (série 2.20+); confirme com `docker compose version`.

## Exercício

Separe uma stack com banco e aplicação em dois arquivos, usando `include`, e valide com `docker compose config`.

## Veja também

- [[Múltiplos arquivos e overrides]]
- [[Estrutura do compose.yaml e Compose Specification]]
- [[Projetos nomeados no Compose]]
- [[MOC - Docker Compose]]
