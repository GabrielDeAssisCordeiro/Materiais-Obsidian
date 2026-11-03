---
tags:
  - docker
  - seguranca
  - distroless
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Escolha da imagem base]]"
  - "[[Multi-stage builds]]"
  - "[[Varredura de vulnerabilidades com Trivy e Grype]]"
  - "[[Docker Hardened Images]]"
---

# Superfície de ataque e imagens mínimas

Cada pacote, shell e utilitário em uma imagem é **superfície de ataque** potencial. Menos conteúdo = menos CVEs e menos ferramentas à disposição de um invasor.

## Como reduzir

| Ação | Efeito |
|---|---|
| Base `-slim`, Alpine ou **distroless** | Menos pacotes |
| **Multi-stage** | Compiladores e ferramentas ficam fora |
| `scratch` para binários estáticos | Zero pacotes |
| Sem shell, `curl`, `wget`, gerenciador de pacotes | Dificulta pós-exploração |
| Atualizar a base com frequência | Correções de segurança |
| Tag fixa e digest | Evita trocas inesperadas |

```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.24 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/app ./cmd/app

# Sem shell, sem gerenciador de pacotes, usuário não-root
FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/app /app
ENTRYPOINT ["/app"]
```

```bash
docker run --rm gcr.io/distroless/static-debian12:nonroot sh 2>&1 | head -n 1   # sem shell
```

> [!info] Depuração sem shell
> Use `docker debug`, containers auxiliares compartilhando namespaces ou variantes `:debug` apenas em ambientes de teste. Veja [[Comando docker exec e attach]].

> [!tip] Mantenha a base atualizada
> Automatize com Renovate/Dependabot; uma imagem mínima desatualizada ainda carrega CVEs.

## Exercício

Reconstrua uma imagem sua sobre distroless ou scratch e compare o número de CVEs (Trivy) e o tamanho com a versão original.

## Veja também

- [[Escolha da imagem base]]
- [[Multi-stage builds]]
- [[Varredura de vulnerabilidades com Trivy e Grype]]
- [[Docker Hardened Images]]
- [[MOC - Segurança]]
