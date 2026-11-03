---
tags:
  - docker
  - seguranca
  - segredos
  - secrets
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Secret mounts]]"
  - "[[configs e secrets no Compose]]"
  - "[[Secrets e configs do Swarm]]"
  - "[[Princípio do menor privilégio - Docker]]"
---

# Gerenciamento de segredos

Segredos (senhas, tokens, chaves privadas, certificados) exigem cuidados em **três momentos**: build, execução e repositório.

| Momento | Prática segura | Evite |
|---|---|---|
| **Build** | `RUN --mount=type=secret` ([[Secret mounts]]) | `ARG`/`ENV`/`COPY` de segredos |
| **Execução (Compose)** | `secrets:` com arquivos em `/run/secrets` | `environment:` com senhas em texto puro |
| **Execução (Swarm)** | `docker secret` (criptografado no Raft) | Variáveis de ambiente |
| **Repositório** | Cofre externo (Vault, SOPS, AWS/GCP/Azure) | Commit de `.env` com segredos |

## Antipadrões (INSEGUROS)

```dockerfile
# ❌ Segredo gravado na imagem e no histórico
ENV DB_PASSWORD=minha-senha
COPY id_rsa /root/.ssh/id_rsa
```

```bash
# ❌ Visível em docker inspect, ps e histórico do shell
docker run -e API_KEY=abc123 minha-imagem
```

## Detectar vazamentos

```bash
# Procura segredos em um repositório e em uma imagem
docker run --rm -v "$PWD":/repo zricethezav/gitleaks:latest detect --source /repo
docker run --rm trufflesecurity/trufflehog:latest docker --image nginx:1.27
```

> [!danger] Se um segredo vazou, ele está comprometido
> Remover do histórico não basta: **revogue e rotacione** imediatamente. Imagens já publicadas podem ter sido baixadas.

> [!tip] Aplicações que leem arquivos
> Adote a convenção `VARIAVEL_FILE` (como `POSTGRES_PASSWORD_FILE`) e leia o valor do arquivo montado em `/run/secrets`.

> [!question] Verificar na documentação oficial
> Os nomes e tags das imagens de ferramentas (gitleaks, trufflehog) e seus parâmetros mudam; confirme na documentação de cada projeto e fixe versões em CI.

## Exercício

Audite um repositório seu com `gitleaks` e uma imagem com `trufflehog`. Para cada achado, descreva como rotacionaria e como evitaria o problema.

## Veja também

- [[Secret mounts]]
- [[configs e secrets no Compose]]
- [[Secrets e configs do Swarm]]
- [[Princípio do menor privilégio - Docker]]
- [[MOC - Segurança]]
