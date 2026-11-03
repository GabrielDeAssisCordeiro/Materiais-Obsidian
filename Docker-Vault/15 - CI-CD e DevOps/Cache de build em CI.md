---
tags:
  - docker
  - cicd
  - cache
  - buildkit
  - desempenho
aliases: []
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Cache remoto de build]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[GitHub Actions para build e push]]"
  - "[[Otimização de tamanho e tempo de build]]"
---

# Cache de build em CI

Runners de CI são geralmente **efêmeros**: sem cache, cada build começa do zero. Opções:

| Estratégia | Como | Quando usar |
|---|---|---|
| **Cache de registry** | `--cache-to/--cache-from type=registry,ref=...:buildcache` | Funciona em qualquer CI; recomendado |
| **Cache do GitHub Actions** | `type=gha` | Projetos no GitHub Actions |
| **Cache local persistido** | `type=local` + cache do CI | CIs com cache de diretório |
| **Builders persistentes** | Builder BuildKit remoto/Build Cloud | Equipes grandes, builds pesados |
| **Cache de pacotes** | `--mount=type=cache` + persistência própria | Gerenciadores de pacotes lentos |

```bash
docker buildx build \
  --cache-from type=registry,ref=ghcr.io/org/app:buildcache \
  --cache-to   type=registry,ref=ghcr.io/org/app:buildcache,mode=max \
  -t ghcr.io/org/app:${TAG} --push .
```

## Boas práticas

- Estruture o Dockerfile para **cache efetivo** (dependências antes do código).
- Use `mode=max` para cachear estágios intermediários de multi-stage.
- Fixe imagens base por digest (ou atualize deliberadamente) para evitar invalidações aleatórias.
- Limpe caches antigos para controlar custo de armazenamento.

> [!bug] Cache "não pega"
> Causas comuns: contexto com arquivos mutáveis (`.git`, logs), `ARG` com valor que muda a cada build (data/hora) antes das camadas pesadas, ou `COPY . .` muito cedo.

## Exercício

Meça o tempo de um build em CI sem cache e com cache de registry; registre a diferença e a causa de qualquer invalidação inesperada.

## Veja também

- [[Cache remoto de build]]
- [[Cache de camadas e ordem das instruções]]
- [[GitHub Actions para build e push]]
- [[Otimização de tamanho e tempo de build]]
- [[MOC - CI-CD e DevOps]]
