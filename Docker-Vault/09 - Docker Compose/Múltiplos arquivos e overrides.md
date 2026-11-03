---
tags:
  - docker
  - compose
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Profiles]]"
  - "[[extends e include]]"
  - "[[Interpolação e arquivo .env]]"
  - "[[Comandos do Docker Compose]]"
---

# Múltiplos arquivos e overrides

O Compose pode **mesclar** vários arquivos, com os posteriores sobrescrevendo ou estendendo os anteriores. É a base para separar **desenvolvimento** e **produção**.

## Arquivo override automático

Se existirem `compose.yaml` e `compose.override.yaml` na pasta, o Compose carrega **ambos** automaticamente.

`compose.yaml` (base, igual para todos os ambientes):

```yaml
services:
  api:
    image: meuusuario/api:1.0
    environment:
      LOG_LEVEL: info
```

`compose.override.yaml` (desenvolvimento local):

```yaml
services:
  api:
    build: ./api
    ports:
      - "3000:3000"
    environment:
      LOG_LEVEL: debug
    volumes:
      - ./api/src:/app/src
```

## Arquivos explícitos (produção)

`compose.prod.yaml`:

```yaml
services:
  api:
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512M
```

```bash
# Desenvolvimento: base + override (automático)
docker compose up -d

# Produção: base + prod (o override NÃO é lido quando se usa -f)
docker compose -f compose.yaml -f compose.prod.yaml up -d

# Ver o resultado da mesclagem
docker compose -f compose.yaml -f compose.prod.yaml config
```

## Regras de mesclagem

| Tipo | Comportamento |
|---|---|
| Valores simples (`image`, `command`) | O último arquivo vence |
| Mapas (`environment`, `labels`) | Mesclados chave a chave |
| Listas (`ports`, `volumes`) | Concatenadas |
| `!reset` | Remove o valor herdado |
| `!override` | Substitui em vez de mesclar |

```yaml
services:
  api:
    ports: !override
      - "8080:3000"
```

> [!question] Verificar na documentação oficial
> As tags YAML `!reset` e `!override` exigem versões recentes do Compose v2. Confirme em "Merge" na documentação.

> [!tip] Variável COMPOSE_FILE
> `COMPOSE_FILE=compose.yaml:compose.prod.yaml` define os arquivos sem repetir `-f` (separador `:` no Linux/macOS, `;` no Windows).

## Exercício

Monte `compose.yaml` + `compose.override.yaml` + `compose.prod.yaml`, e compare a saída de `docker compose config` em cada combinação.

## Veja também

- [[Profiles]]
- [[extends e include]]
- [[Interpolação e arquivo .env]]
- [[Comandos do Docker Compose]]
- [[MOC - Docker Compose]]
