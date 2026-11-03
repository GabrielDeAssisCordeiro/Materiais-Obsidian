---
tags:
  - docker
  - dockerfile
  - build
  - sintaxe
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Instrução RUN]]"
  - "[[Instruções COPY e ADD]]"
  - "[[Sintaxe do Dockerfile e syntax directive]]"
---

# Heredocs no Dockerfile

Com BuildKit e o frontend do Dockerfile recente, é possível usar **heredocs** em `RUN` e `COPY`, evitando longas cadeias de `&&` e `\`.

```dockerfile
# syntax=docker/dockerfile:1
FROM debian:bookworm-slim

# Vários comandos em um só RUN, legíveis
RUN <<EOF
set -eux
apt-get update
apt-get install -y --no-install-recommends curl ca-certificates
rm -rf /var/lib/apt/lists/*
EOF

# Cria um arquivo diretamente
COPY <<EOF /etc/app/config.ini
[app]
modo = producao
EOF

# Script Python inline
RUN <<EOF python3
print("executado durante o build")
EOF
```

> [!warning] Requer BuildKit e sintaxe recente
> Declare `# syntax=docker/dockerfile:1` na primeira linha para garantir o suporte. O builder clássico não entende heredocs.

> [!tip] Expansão de variáveis
> Por padrão, `$VAR` é expandida no corpo do heredoc. Use `<<'EOF'` (aspas) para impedir a expansão.

## Exercício

Reescreva um `RUN apt-get update && apt-get install ... && rm ...` usando heredoc e confirme que o build continua funcionando.

## Veja também

- [[Instrução RUN]]
- [[Instruções COPY e ADD]]
- [[Sintaxe do Dockerfile e syntax directive]]
- [[MOC - Dockerfile]]
