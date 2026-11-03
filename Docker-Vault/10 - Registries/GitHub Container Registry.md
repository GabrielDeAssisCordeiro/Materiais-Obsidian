---
tags:
  - docker
  - registries
  - ghcr
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Login e tokens de acesso]]"
  - "[[Registries]]"
  - "[[Automação de publicação de imagens]]"
---

# GitHub Container Registry

O **GHCR** (`ghcr.io`) é o registry do GitHub, integrado ao GitHub Actions e às permissões do repositório/organização.

## Publicação manual

```bash
# Token (PAT) com escopo write:packages (e read:packages)
echo "$GHCR_TOKEN" | docker login ghcr.io -u SEU_USUARIO --password-stdin

# O nome deve ser em minúsculas
docker build -t ghcr.io/seu-usuario/meu-app:1.0 .
docker push ghcr.io/seu-usuario/meu-app:1.0
```

## Vincular a imagem ao repositório

```dockerfile
LABEL org.opencontainers.image.source="https://github.com/seu-usuario/meu-repo"
```

Essa label associa o pacote ao repositório, herdando suas permissões e README.

## Em GitHub Actions (resumo)

```yaml
permissions:
  contents: read
  packages: write
steps:
  - uses: docker/login-action@v3
    with:
      registry: ghcr.io
      username: ${{ github.actor }}
      password: ${{ secrets.GITHUB_TOKEN }}
```

> [!info] Visibilidade
> Pacotes novos são **privados** por padrão; torne-os públicos na página do pacote se quiser permitir `pull` anônimo.

> [!tip] Sem tokens pessoais
> Em workflows, prefira o `GITHUB_TOKEN` com `packages: write` ao PAT de usuário.

## Exercício

Publique uma imagem no GHCR de um repositório seu, adicione a label `org.opencontainers.image.source` e verifique a ligação na página do pacote.

## Veja também

- [[Login e tokens de acesso]]
- [[Registries]]
- [[Automação de publicação de imagens]]
- [[MOC - Registries]]
