---
tags:
  - docker
  - dockerfile
  - build
  - sintaxe
  - buildkit
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Heredocs no Dockerfile]]"
  - "[[Buildx e BuildKit]]"
  - "[[Instruções COPY e ADD]]"
---

# Sintaxe do Dockerfile e syntax directive

A primeira linha do Dockerfile pode conter uma **diretiva de parser**:

```dockerfile
# syntax=docker/dockerfile:1
```

Ela instrui o BuildKit a baixar e usar a versão do **frontend do Dockerfile** indicada (uma imagem), em vez da embutida no daemon. Assim você ganha novos recursos (heredocs, `COPY --link`, mounts) sem atualizar o Docker.

| Valor | Efeito |
|---|---|
| `docker/dockerfile:1` | Última versão estável da série 1 (recomendado) |
| `docker/dockerfile:1.x` | Versão específica (maior reprodutibilidade) |
| `docker/dockerfile:labs` | Recursos experimentais |

## Outras diretivas

```dockerfile
# escape=`          # muda o caractere de escape (útil no Windows)
# check=error=true  # trata avisos do build check como erros (BuildKit recente)
```

```bash
# Valida o Dockerfile sem construir (Build Checks)
docker build --check .
```

> [!question] Verificar na documentação oficial
> As diretivas `check` e o comando `docker build --check` (Build Checks) dependem da versão do Buildx/Dockerfile. Confirme na referência de Dockerfile.

> [!tip] Reprodutibilidade
> Fixe a versão do frontend (`docker/dockerfile:1.x`) e a imagem base por digest em builds críticos.

## Exercício

Adicione `# syntax=docker/dockerfile:1` a um Dockerfile, rode `docker build --progress=plain .` e localize a linha que baixa o frontend.

## Veja também

- [[Heredocs no Dockerfile]]
- [[Buildx e BuildKit]]
- [[Instruções COPY e ADD]]
- [[MOC - Dockerfile]]
