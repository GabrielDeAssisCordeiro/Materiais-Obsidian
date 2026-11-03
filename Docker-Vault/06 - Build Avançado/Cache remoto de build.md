---
tags:
  - docker
  - build-avancado
  - cache
  - ci
  - registry
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Builders do Buildx]]"
  - "[[Otimização de tamanho e tempo de build]]"
---

# Cache remoto de build

Em CI, runners são efêmeros e o cache local desaparece a cada execução. O BuildKit permite **exportar e importar cache** para um backend externo.

```bash
# Registry como backend
docker buildx build \
  --cache-from type=registry,ref=meuusuario/app:buildcache \
  --cache-to   type=registry,ref=meuusuario/app:buildcache,mode=max \
  -t meuusuario/app:1.0 --push .

# Diretório local (persistido pelo CI)
docker buildx build \
  --cache-from type=local,src=/tmp/buildx-cache \
  --cache-to   type=local,dest=/tmp/buildx-cache,mode=max \
  -t app .

# Cache do GitHub Actions
docker buildx build \
  --cache-from type=gha \
  --cache-to   type=gha,mode=max \
  -t app .
```

| Backend | Observações |
|---|---|
| `registry` | Funciona em qualquer CI; armazena como imagem |
| `local` | Simples; precisa ser salvo/restaurado pelo CI |
| `gha` | Integrado ao GitHub Actions |
| `inline` | Embute o cache na própria imagem (apenas `mode=min`) |

| `mode` | Efeito |
|---|---|
| `min` | Exporta camadas do estágio final |
| `max` | Exporta **todas** as camadas, inclusive estágios intermediários (melhor reuso) |

> [!question] Verificar na documentação oficial
> O backend `gha` e seus limites mudaram ao longo do tempo (nova API de cache do GitHub). Confira a documentação atual do Buildx antes de adotar.

> [!warning] Exige builder com driver docker-container
> O cache externo não é suportado pelo driver `docker` clássico. Veja [[Builders do Buildx]].

## Exercício

Configure `--cache-to type=local,dest=./cache,mode=max` em um build, apague as imagens locais e reconstrua com `--cache-from type=local,src=./cache` para ver as etapas CACHED.

## Veja também

- [[Cache de camadas e ordem das instruções]]
- [[Builders do Buildx]]
- [[Otimização de tamanho e tempo de build]]
- [[MOC - Build Avançado]]
