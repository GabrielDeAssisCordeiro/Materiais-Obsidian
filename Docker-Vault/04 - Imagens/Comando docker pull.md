---
tags:
  - docker
  - imagens
  - comandos
aliases: []
tipo: comando
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Tags e digests de imagens]]"
  - "[[Registries]]"
  - "[[Listar e inspecionar imagens]]"
  - "[[Docker Hub]]"
---

# Comando docker pull

`docker pull` baixa uma imagem (ou todas as tags de um repositório) de um registry.

```bash
docker pull nginx:1.27                      # tag específica
docker pull nginx                           # equivale a nginx:latest (evite)
docker pull alpine:3.20@sha256:<digest>     # por digest (imutável)
docker pull ghcr.io/OWNER/IMAGEM:TAG        # outro registry
docker pull --platform linux/arm64 alpine:3.20   # arquitetura específica
docker pull -a alpine                       # todas as tags (pode ser enorme!)
docker pull -q nginx:1.27                   # saída silenciosa
```

## O que acontece

1. O cliente resolve o nome para `registry/repositório:tag`.
2. Baixa o **manifest** (e, se for multiplataforma, escolhe o da arquitetura do host).
3. Baixa **somente as camadas que faltam**, em paralelo.
4. Verifica os digests e registra a imagem localmente.

> [!tip] Pull automático
> `docker run` faz o pull se a imagem não estiver presente. Use `--pull always` para forçar a verificação de uma nova versão da tag, ou `--pull never` para impedir downloads.

> [!bug] Erros comuns
> - `manifest unknown`: a tag não existe (erro de digitação ou tag removida).
> - `pull access denied`: repositório privado ou inexistente; faça `docker login`.
> - `toomanyrequests`: limite de pulls anônimos do Docker Hub; autentique-se ou use um espelho (*mirror*).
> - `no matching manifest for linux/arm64`: a imagem não é publicada para sua arquitetura.

## Exercício

Baixe `alpine:3.20` e `alpine:3.19`. Observe a saída de `docker pull` e responda: quantas camadas cada uma tem e por que o segundo pull foi mais rápido ou não?

## Veja também

- [[Tags e digests de imagens]]
- [[Registries]]
- [[Listar e inspecionar imagens]]
- [[Docker Hub]]
- [[MOC - Imagens]]
