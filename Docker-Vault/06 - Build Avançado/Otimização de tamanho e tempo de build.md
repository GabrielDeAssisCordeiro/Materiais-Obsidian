---
tags:
  - docker
  - build-avancado
  - otimizacao
  - desempenho
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Multi-stage builds]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Cache mounts]]"
  - "[[Cache remoto de build]]"
  - "[[Escolha da imagem base]]"
---

# Otimização de tamanho e tempo de build

## Reduzir o tamanho da imagem

| Técnica | Efeito |
|---|---|
| Imagem base menor (`-slim`, `alpine`, distroless) | Reduz a base |
| **Multi-stage** | Remove compiladores e ferramentas |
| Instalar sem recomendados e limpar no mesmo `RUN` | Reduz camadas |
| `.dockerignore` | Menos arquivos copiados |
| Remover caches (`pip --no-cache-dir`, `npm cache clean --force`) | Menos lixo |
| Instalar só dependências de produção (`npm ci --omit=dev`) | Menos pacotes |
| Binários estáticos com `-ldflags="-s -w"` (Go) | Binário menor |

```bash
docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}'
docker history --human IMAGEM       # onde está o peso
docker run --rm -it wagoodman/dive IMAGEM   # (opcional) explorar camadas com a ferramenta dive
```

## Reduzir o tempo de build

| Técnica | Veja |
|---|---|
| Ordenar instruções pensando em cache | [[Cache de camadas e ordem das instruções]] |
| Cache mounts para gerenciadores de pacotes | [[Cache mounts]] |
| Cache remoto em CI | [[Cache remoto de build]] |
| Paralelismo com estágios independentes | [[Multi-stage builds]] |
| Contexto pequeno | [[Arquivo .dockerignore]] |
| Cross-compilation em vez de emulação | [[Build multiplataforma]] |

> [!warning] Menor nem sempre é melhor
> Imagens extremamente minimalistas dificultam depuração e podem trazer incompatibilidades (musl). Equilibre tamanho, segurança e manutenibilidade.

> [!tip] Meça antes de otimizar
> Use `--progress=plain` para ver o tempo por etapa e `docker history` para o tamanho por camada. Otimize os maiores ofensores primeiro.

## Exercício

Escolha uma imagem sua, meça tamanho e tempo de build, aplique três técnicas da tabela e registre os ganhos.

## Veja também

- [[Multi-stage builds]]
- [[Cache de camadas e ordem das instruções]]
- [[Cache mounts]]
- [[Cache remoto de build]]
- [[Escolha da imagem base]]
- [[MOC - Build Avançado]]
