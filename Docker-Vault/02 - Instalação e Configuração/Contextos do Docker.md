---
tags:
  - docker
  - instalacao
  - contexto
  - ssh
  - cli
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Docker CLI e API]]"
  - "[[Docker Desktop vs Docker Engine]]"
  - "[[Arquivo daemon.json]]"
  - "[[Docker Daemon dockerd]]"
---

# Contextos do Docker

Um **contexto** (*context*) guarda o endereço e as credenciais de um daemon Docker (ou de um cluster Kubernetes). Ele permite alternar entre ambientes (local, servidor remoto, Docker Desktop) sem alterar variáveis de ambiente.

```bash
# Lista contextos (o ativo tem asterisco)
docker context ls

# Cria um contexto para um servidor remoto via SSH
docker context create producao --docker "host=ssh://usuario@servidor.exemplo.com"

# Usa o contexto para todos os comandos seguintes
docker context use producao
docker ps

# Usa o contexto apenas em um comando
docker --context producao ps

# Volta ao local
docker context use default

# Inspeciona e remove
docker context inspect producao
docker context rm producao
```

## Contextos típicos

| Contexto | Quando aparece |
|---|---|
| `default` | Daemon local (Engine em Linux, socket padrão). |
| `desktop-linux` | Docker Desktop (macOS, Windows com WSL ou Linux). |
| Contextos criados por você | Servidores remotos via SSH ou TLS. |

> [!tip] SSH é o jeito seguro
> O transporte `ssh://` reutiliza sua autenticação por chave e não exige expor a porta TCP do daemon. Requer a CLI `docker` instalada no servidor e acesso ao socket pelo usuário.

> [!warning] Precedência
> `DOCKER_HOST` e `DOCKER_CONTEXT` têm precedência sobre o contexto selecionado com `docker context use`. Se um comando "vai para o lugar errado", verifique `env | grep DOCKER`.

## Exercício

Crie um contexto fictício com `docker context create teste --docker "host=ssh://user@exemplo.local"`, liste-o, inspecione-o e remova-o.

## Veja também

- [[Docker CLI e API]]
- [[Docker Desktop vs Docker Engine]]
- [[Arquivo daemon.json]]
- [[Docker Daemon dockerd]]
- [[MOC - Instalação e Configuração]]
