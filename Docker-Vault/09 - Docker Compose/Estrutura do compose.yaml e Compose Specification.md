---
tags:
  - docker
  - compose
aliases: []
tipo: referencia
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Visão geral do Docker Compose]]"
  - "[[Serviços com image e build]]"
  - "[[Projetos nomeados no Compose]]"
---

# Estrutura do compose.yaml e Compose Specification

## Elementos de nível superior

| Chave | Função |
|---|---|
| `name` | Nome do projeto (opcional) |
| `services` | **Obrigatório.** Containers da aplicação |
| `networks` | Redes personalizadas |
| `volumes` | Volumes nomeados |
| `configs` | Arquivos de configuração (somente leitura) |
| `secrets` | Segredos montados em `/run/secrets` |
| `include` | Inclui outros arquivos Compose |

```yaml
name: loja

services:
  api:
    image: traefik/whoami:v1.10
    networks: [backend]

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets: [db_password]
    volumes:
      - dbdata:/var/lib/postgresql/data
    networks: [backend]

networks:
  backend:

volumes:
  dbdata:

secrets:
  db_password:
    file: ./db_password.txt
```

## Nomes de arquivo reconhecidos

`compose.yaml` (preferido), `compose.yml`, `docker-compose.yaml` e `docker-compose.yml`. Para outro nome: `docker compose -f arquivo.yaml ...`.

## Validação

```bash
docker compose config            # valida, interpola variáveis e mostra o arquivo final
docker compose config --quiet    # só valida (útil em CI)
docker compose config --services # lista serviços
```

> [!warning] Não use o campo `version`
> Ele é **obsoleto** na Compose Specification. O Compose v2 o ignora e emite um aviso (*"the attribute `version` is obsolete"*).

> [!tip] YAML
> Indentação com **espaços** (nunca tabs). Valores como `"8080:80"` devem ficar entre aspas, pois o YAML pode interpretar `xx:yy` como número em base 60.

## Exercício

Valide o exemplo com `docker compose config` e crie propositalmente um erro de indentação para ver a mensagem de erro.

## Veja também

- [[Visão geral do Docker Compose]]
- [[Serviços com image e build]]
- [[Projetos nomeados no Compose]]
- [[MOC - Docker Compose]]
