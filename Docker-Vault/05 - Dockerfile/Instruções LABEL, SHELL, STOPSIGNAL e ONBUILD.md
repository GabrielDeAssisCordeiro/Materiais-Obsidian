---
tags:
  - docker
  - dockerfile
  - instrucao
  - shell
aliases: []
tipo: instrucao
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Nomes e labels]]"
  - "[[Instrução RUN]]"
  - "[[Init, PID 1 e sinais]]"
  - "[[Introdução ao Dockerfile]]"
---

# Instruções LABEL, SHELL, STOPSIGNAL e ONBUILD

## LABEL

Metadados chave-valor. Use as chaves padronizadas da OCI.

```dockerfile
LABEL org.opencontainers.image.title="Minha API" \
      org.opencontainers.image.source="https://github.com/ORG/REPO" \
      org.opencontainers.image.licenses="MIT"
```

## SHELL

Troca o shell usado pela forma shell (`RUN`, `CMD`, `ENTRYPOINT`). Padrão: `["/bin/sh","-c"]` em Linux e `["cmd","/S","/C"]` no Windows.

```dockerfile
# Falha em qualquer erro de pipe
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -fsSL https://exemplo.com/script | tee /tmp/saida.txt
```

```dockerfile
# Windows
SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop';"]
```

## STOPSIGNAL

Sinal enviado por `docker stop` (padrão SIGTERM).

```dockerfile
FROM nginx:1.27
STOPSIGNAL SIGQUIT          # Nginx finaliza graciosamente com SIGQUIT
```

## ONBUILD

Registra instruções que executam **quando outra imagem usa esta como base**.

```dockerfile
FROM node:22-alpine
ONBUILD COPY package*.json /app/
ONBUILD RUN npm ci
```

> [!warning] ONBUILD é considerada prática antiga
> Esconde comportamento e dificulta depuração. Prefira build multi-stage e templates explícitos.

## Exercício

Adicione `SHELL ["/bin/bash","-o","pipefail","-c"]` a um Dockerfile e demonstre que um `RUN false | true` agora falha o build.

## Veja também

- [[Nomes e labels]]
- [[Instrução RUN]]
- [[Init, PID 1 e sinais]]
- [[Introdução ao Dockerfile]]
- [[MOC - Dockerfile]]
