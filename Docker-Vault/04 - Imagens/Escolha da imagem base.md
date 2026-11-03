---
tags:
  - docker
  - imagens
  - distroless
  - comparativo
aliases: []
tipo: comparativo
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Imagens oficiais, verificadas e de editores]]"
  - "[[Introdução ao Dockerfile]]"
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Camadas de uma imagem]]"
---

# Escolha da imagem base

A imagem base (`FROM`) define tamanho, superfície de ataque, compatibilidade e facilidade de depuração.

| Base | Tamanho aproximado | Características | Quando usar |
|---|---|---|---|
| `scratch` | 0 | Imagem vazia; sem shell nem libc | Binários estáticos (Go, Rust) |
| `distroless` | ~2–30 MB | Só runtime e libs; sem shell nem gerenciador de pacotes | Produção com superfície mínima |
| `alpine` | ~5–8 MB | musl libc + BusyBox + `apk` | Imagens pequenas; atenção a incompatibilidades com glibc |
| `debian:*-slim` | ~30–80 MB | glibc, `apt`, conjunto reduzido | Equilíbrio entre compatibilidade e tamanho |
| `debian` / `ubuntu` | ~80–120 MB+ | Completa, muitas ferramentas | Compatibilidade máxima, depuração |
| Variantes de linguagem (`python:3.12-slim`, `node:22-alpine`) | varia | Runtime pronto | Padrão para aplicações |

```bash
# Compare tamanhos
docker pull -q alpine:3.20 && docker pull -q debian:bookworm-slim && docker pull -q ubuntu:24.04
docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}' | grep -E 'alpine|debian|ubuntu'
```

> [!warning] Alpine e musl
> Programas compilados para glibc (alguns pacotes Python com *wheels* binárias, Node.js addons, JVMs) podem falhar ou ficar lentos no Alpine. Teste ou use `-slim`.

> [!tip] Distroless e depuração
> Sem shell, o `docker exec` não funciona. Use imagens de depuração (`:debug`), `docker debug` ou containers auxiliares compartilhando namespaces.

> [!info] Docker Hardened Images
> A Docker oferece imagens base endurecidas e mantidas com foco em segurança; veja a pasta de novidades.

> [!question] Verificar na documentação oficial
> Os tamanhos são aproximados e variam a cada release. Para a lista atual de variantes, consulte a página de cada imagem no Docker Hub.

## Exercício

Construa a mesma aplicação "Hello World" em Python sobre `python:3.12`, `python:3.12-slim` e `python:3.12-alpine`, e compare o tamanho final das três imagens.

## Veja também

- [[Imagens oficiais, verificadas e de editores]]
- [[Introdução ao Dockerfile]]
- [[Princípio do menor privilégio - Docker]]
- [[Camadas de uma imagem]]
- [[MOC - Imagens]]
