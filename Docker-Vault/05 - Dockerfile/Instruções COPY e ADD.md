---
tags:
  - docker
  - dockerfile
  - instrucao
  - comparativo
aliases: []
tipo: instrucao
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Arquivo .dockerignore]]"
  - "[[Multi-stage builds]]"
  - "[[Cache de camadas e ordem das instruções]]"
  - "[[Instrução RUN]]"
---

# Instruções COPY e ADD

```dockerfile
COPY package.json package-lock.json ./
COPY --chown=10001:10001 src/ /app/src/
COPY --chmod=0755 entrypoint.sh /usr/local/bin/
COPY --from=build /out/app /usr/local/bin/app     # de outro estágio
```

## COPY vs ADD

| | `COPY` | `ADD` |
|---|---|---|
| Copia arquivos e diretórios do contexto | Sim | Sim |
| Baixa de URL | Não | Sim |
| Extrai arquivos `.tar` locais automaticamente | Não | Sim |
| Previsibilidade | **Alta** | Menor (comportamentos implícitos) |
| Recomendação | **Preferir sempre** | Só para extrair tar local; em URLs, use `--checksum` |

```dockerfile
# ADD com URL e verificação de integridade (BuildKit)
ADD --checksum=sha256:<hash> https://exemplo.com/ferramenta.tar.gz /tmp/

# Extração automática de tar local
ADD rootfs.tar.gz /
```

> [!tip] `COPY --link` e `--exclude`
> Com BuildKit e sintaxe recente (`# syntax=docker/dockerfile:1`), `COPY --link` cria camadas independentes e melhora o reuso de cache; `--exclude` ignora padrões na cópia.

> [!question] Verificar na documentação oficial
> A disponibilidade de `--link`, `--exclude` e `ADD --checksum` depende da versão do frontend do Dockerfile. Confirme na referência de Dockerfile.

> [!warning] Copie só o necessário
> `COPY . .` copia tudo do contexto (inclusive `.git`, `.env`, `node_modules`). Use um `.dockerignore` e, quando possível, copie arquivos específicos.

> [!bug] "COPY failed: file not found in build context"
> O caminho é relativo ao **contexto**, e não é possível copiar de fora dele (`../arquivo`). Ajuste o contexto ou o `-f`.

## Exercício

Escreva um Dockerfile que copie `package.json` antes do restante do código e explique, em termos de cache, por que essa ordem acelera builds.

## Veja também

- [[Arquivo .dockerignore]]
- [[Multi-stage builds]]
- [[Cache de camadas e ordem das instruções]]
- [[Instrução RUN]]
- [[MOC - Dockerfile]]
