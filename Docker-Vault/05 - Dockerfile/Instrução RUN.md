---
tags:
  - docker
  - dockerfile
  - instrucao
  - run
  - camadas
aliases: []
tipo: instrucao
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Forma shell vs forma exec]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Cache mounts]]"
  - "[[Heredocs no Dockerfile]]"
---

# Instrução RUN

`RUN` executa comandos **durante o build** e grava o resultado em uma nova camada.

```dockerfile
# Forma shell (usa /bin/sh -c)
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Forma exec (sem shell, sem expansão de variáveis)
RUN ["/bin/bash", "-c", "echo $HOME"]
```

## Regras de ouro

1. **Agrupe** comandos relacionados no mesmo `RUN` e **limpe no mesmo `RUN`**; apagar em outra camada não reduz o tamanho.
2. Em Debian/Ubuntu, `apt-get update` e `apt-get install` devem estar **no mesmo `RUN`** (evita cache obsoleto).
3. Use `--no-install-recommends` e remova `/var/lib/apt/lists/*`.
4. Em Alpine, use `apk add --no-cache`.
5. Use `set -e` (ou `&&`) para falhar no primeiro erro; para pipes, `set -o pipefail`.

```dockerfile
# Alpine
RUN apk add --no-cache curl ca-certificates

# Pipes com falha detectada (veja a instrução SHELL)
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -fsSL https://exemplo.com/arquivo | sha256sum
```

> [!bug] "Instalei e apaguei, mas a imagem continua grande"
> ```dockerfile
> # ❌ ANTIPADRÃO: o arquivo continua na camada anterior
> RUN wget https://exemplo.com/grande.tar.gz
> RUN tar xzf grande.tar.gz && rm grande.tar.gz
>
> # ✅ Tudo na mesma camada
> RUN wget https://exemplo.com/grande.tar.gz \
>  && tar xzf grande.tar.gz \
>  && rm grande.tar.gz
> ```

> [!danger] Não coloque segredos em `RUN`
> Tokens em argumentos ou arquivos ficam no histórico da camada. Use [[Secret mounts]].

## Exercício

Construa duas imagens: uma instalando e removendo um pacote em `RUN` separados e outra no mesmo `RUN`. Compare os tamanhos com `docker images`.

## Veja também

- [[Forma shell vs forma exec]]
- [[Cache de camadas e ordem das instruções]]
- [[Cache mounts]]
- [[Heredocs no Dockerfile]]
- [[MOC - Dockerfile]]
