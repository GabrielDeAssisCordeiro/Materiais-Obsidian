---
tags:
  - docker
  - build-avancado
  - reprodutibilidade
  - supply-chain
aliases: []
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[SBOM e provenance]]"
  - "[[Tags e digests de imagens]]"
  - "[[Sintaxe do Dockerfile e syntax directive]]"
---

# Builds reproduzíveis

Um build é **reproduzível** quando as mesmas entradas geram imagens idênticas (mesmo digest). Na prática, busca-se o máximo de **determinismo**.

## Fontes comuns de variação

| Fonte | Mitigação |
|---|---|
| Imagem base mutável | Fixar por **digest** |
| Pacotes (`apt`, `pip`, `npm`) sem versão | Usar *lockfiles* (`package-lock.json`, `requirements.txt` com hashes) e versões fixas |
| Timestamps | Definir `SOURCE_DATE_EPOCH` e usar `rewrite-timestamp` |
| Frontend do Dockerfile | Fixar `# syntax=docker/dockerfile:1.x` |
| Ordem de arquivos, metadados | Evitar `COPY . .` com arquivos variáveis |
| Downloads sem verificação | `ADD --checksum` ou verificar `sha256sum` |

```bash
# Build com timestamps normalizados
SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct) \
docker buildx build \
  --build-arg SOURCE_DATE_EPOCH \
  --output type=image,name=app:1.0,rewrite-timestamp=true .
```

```dockerfile
FROM python:3.12-slim@sha256:<digest>
RUN pip install --no-cache-dir --require-hashes -r requirements.txt
```

> [!question] Verificar na documentação oficial
> O suporte a `rewrite-timestamp` e a reprodutibilidade completa dependem da versão do BuildKit/Buildx. Consulte "Reproducible builds" na documentação do BuildKit.

> [!tip] Reprodutibilidade parcial já vale ouro
> Mesmo sem digest idêntico, fixar versões e registrar provenance permite reconstruir e auditar uma imagem.

## Exercício

Construa a mesma imagem duas vezes com `--no-cache` e compare os digests. Aplique `SOURCE_DATE_EPOCH` e verifique se algo muda.

## Veja também

- [[SBOM e provenance]]
- [[Tags e digests de imagens]]
- [[Sintaxe do Dockerfile e syntax directive]]
- [[MOC - Build Avançado]]
