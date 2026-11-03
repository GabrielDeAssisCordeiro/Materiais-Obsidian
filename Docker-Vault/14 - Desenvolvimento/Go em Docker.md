---
tags:
  - docker
  - desenvolvimento
  - dockerfile
  - distroless
  - multi-stage
aliases: []
tipo: procedimento
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Multi-stage builds]]"
  - "[[Superfície de ataque e imagens mínimas]]"
  - "[[Build multiplataforma]]"
  - "[[Rust em Docker]]"
---

# Go em Docker

Go gera **binários estáticos**, ideais para imagens mínimas.

`main.go`:

```go
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Olá, Docker!")
	})
	log.Println("escutando em :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

`Dockerfile`:

```dockerfile
# syntax=docker/dockerfile:1

# ---------- Build ----------
FROM golang:1.24 AS build
WORKDIR /src
COPY go.mod ./
RUN --mount=type=cache,target=/go/pkg/mod go mod download
COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/app .

# ---------- Produção ----------
FROM gcr.io/distroless/static-debian12:nonroot AS prod
COPY --from=build /out/app /app
EXPOSE 8080
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

```bash
go mod init exemplo.com/ola      # cria o go.mod (no host, ou em um container golang)
docker build -t go-demo:1.0 .
docker images go-demo:1.0        # poucos MB
docker run -d --name go -p 8080:8080 go-demo:1.0
curl http://localhost:8080
docker rm -f go
```

## Desenvolvimento com recarga (air)

```dockerfile
FROM golang:1.24 AS dev
WORKDIR /app
# Fixe a versão do air em projetos reais
RUN go install github.com/air-verse/air@latest
COPY go.mod go.sum* ./
RUN go mod download
CMD ["air"]
```

> [!tip] Variáveis para multiplataforma
> Use `--platform=$BUILDPLATFORM`, `GOOS=$TARGETOS` e `GOARCH=$TARGETARCH` para cross-compilar. Veja [[Build multiplataforma]].

> [!warning] `CGO_ENABLED=0`
> Garante binário estático compatível com `scratch`/distroless static. Bibliotecas que exigem CGO precisam de uma base com libc (`distroless/base` ou `debian-slim`).

## Exercício

Containerize o servidor acima, compare o tamanho com uma versão sobre `golang:1.24` (sem multi-stage) e anote a diferença.

## Veja também

- [[Multi-stage builds]]
- [[Superfície de ataque e imagens mínimas]]
- [[Build multiplataforma]]
- [[Rust em Docker]]
- [[MOC - Desenvolvimento]]
