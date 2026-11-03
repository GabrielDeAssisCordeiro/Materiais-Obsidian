---
tags:
  - docker
  - cicd
  - deploy
  - compose
  - ssh
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Contextos do Docker]]"
  - "[[Pipeline CI-CD com Docker]]"
  - "[[Estratégias de rollout]]"
  - "[[Hospedagem em VPS com Compose]]"
---

# Deploy com Compose via SSH

Para um único servidor, **Compose + SSH** é um deploy simples e eficaz.

## Servidor (uma vez)

```bash
# No servidor: usuário dedicado e diretório da aplicação
sudo adduser --disabled-password deploy
sudo usermod -aG docker deploy      # atenção: o grupo docker equivale a root
sudo mkdir -p /srv/app && sudo chown deploy:deploy /srv/app
```

`/srv/app/compose.yaml` (usa imagem do registry, tag vinda de variável):

```yaml
services:
  app:
    image: ghcr.io/org/app:${APP_TAG:?defina APP_TAG}
    restart: unless-stopped
    env_file: .env
    ports:
      - "127.0.0.1:8080:8080"
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://127.0.0.1:8080/health || exit 1"]
      interval: 10s
      timeout: 3s
      retries: 5
```

## Deploy com contexto SSH (do CI ou da sua máquina)

```bash
docker context create producao --docker "host=ssh://deploy@servidor.exemplo.com"

export APP_TAG=1.4.2
docker --context producao compose -f compose.yaml pull
docker --context producao compose -f compose.yaml up -d --remove-orphans --wait
docker --context producao image prune -f
```

## Deploy com script remoto

```bash
#!/usr/bin/env bash
set -euo pipefail
TAG="${1:?Informe a tag}"
ssh deploy@servidor.exemplo.com "cd /srv/app && \
  APP_TAG=$TAG docker compose pull && \
  APP_TAG=$TAG docker compose up -d --remove-orphans --wait && \
  docker image prune -f"
```

## Em GitHub Actions (trecho)

```yaml
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: producao
    steps:
      - uses: actions/checkout@v4
      - name: Chave SSH
        run: |
          install -m 700 -d ~/.ssh
          echo "${{ secrets.DEPLOY_SSH_KEY }}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
          ssh-keyscan -H servidor.exemplo.com >> ~/.ssh/known_hosts
      - name: Deploy
        run: ./scripts/deploy.sh "${{ github.ref_name }}"
```

> [!tip] `--wait`
> Faz o comando esperar os serviços ficarem saudáveis e **falhar** se não ficarem, interrompendo o pipeline.

> [!warning] Segurança do acesso SSH
> Use uma chave dedicada ao deploy, restrita ao servidor e com `known_hosts` fixado (evite `ssh-keyscan` cego em produção). O usuário `deploy` no grupo `docker` tem poderes de root efetivos.

> [!danger] `docker compose up` recria o container
> Há uma breve indisponibilidade a cada deploy com um único container. Veja [[Estratégias de rollout]] para reduzi-la.

## Exercício

Em uma VM de laboratório, configure o usuário `deploy` e execute um deploy via contexto SSH, alterando `APP_TAG` entre duas versões.

## Veja também

- [[Contextos do Docker]]
- [[Pipeline CI-CD com Docker]]
- [[Estratégias de rollout]]
- [[Hospedagem em VPS com Compose]]
- [[MOC - CI-CD e DevOps]]
