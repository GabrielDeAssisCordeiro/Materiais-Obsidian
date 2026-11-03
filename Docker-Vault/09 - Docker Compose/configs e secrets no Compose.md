---
tags:
  - docker
  - compose
  - secrets
  - configs
  - seguranca
aliases: []
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Variáveis de ambiente e env_file]]"
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Secret mounts]]"
---

# configs e secrets no Compose

## secrets

Montados como **arquivos** em `/run/secrets/<nome>` (em memória, somente leitura), sem aparecer em `docker inspect` como variável de ambiente.

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt      # arquivo local (fora do Git!)
  # alternativa: valor vindo de uma variável de ambiente do host
  # api_key:
  #   environment: API_KEY
```

```bash
mkdir -p secrets && printf 'senha-de-laboratorio' > secrets/db_password.txt
echo "secrets/" >> .gitignore
docker compose up -d
docker compose exec db ls -l /run/secrets
```

## configs

Arquivos de configuração **não sensíveis** montados no container (padrão: `/<nome>` na raiz).

```yaml
services:
  proxy:
    image: nginx:1.27
    configs:
      - source: nginx_conf
        target: /etc/nginx/nginx.conf

configs:
  nginx_conf:
    file: ./nginx.conf
```

| | `secrets` | `configs` |
|---|---|---|
| Para | Senhas, chaves, tokens | Arquivos de configuração |
| Local no container | `/run/secrets/NOME` | Caminho em `target` |
| Visível no `inspect` | Não como variável | Sim como montagem |

> [!warning] No Compose (fora do Swarm), secrets são montagens de arquivo
> A proteção é menor do que no Swarm, que os armazena criptografados no Raft. Mesmo assim, evitam variáveis de ambiente e vazamentos em logs. Seu aplicativo precisa **ler o arquivo**.

> [!danger] Nunca versione os arquivos de segredo
> Adicione-os ao `.gitignore` e gerencie-os por cofre de segredos (Vault, SOPS, gerenciadores da nuvem) em produção.

## Exercício

Crie um `secrets/db_password.txt`, suba o Postgres com `POSTGRES_PASSWORD_FILE` e confirme que `docker inspect` não mostra a senha em `Env`.

## Veja também

- [[Variáveis de ambiente e env_file]]
- [[Princípio do menor privilégio - Docker]]
- [[Secret mounts]]
- [[MOC - Docker Compose]]
