---
tags:
  - docker
  - ia
  - novidades
  - seguranca
  - supply-chain
aliases:
  - DHI
  - Hardened Images
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Superfície de ataque e imagens mínimas]]"
  - "[[Docker Scout]]"
  - "[[SBOM e provenance]]"
  - "[[Escolha da imagem base]]"
---

# Docker Hardened Images

As **Docker Hardened Images (DHI)** são imagens base **mínimas e endurecidas**, mantidas pela Docker com foco em segurança: poucos pacotes, sem componentes desnecessários, reconstruídas quando surgem correções e acompanhadas de **SBOM**, **provenance** e assinatura.

## Pontos principais

| Característica | Detalhe |
|---|---|
| Base | Construídas sobre **Debian** e **Alpine** |
| Superfície reduzida | Variantes de runtime sem shell/gerenciador de pacotes e variantes `-dev` para build |
| Transparência | Definições abertas (Apache 2.0) |
| Atestados | SBOM, provenance, assinatura e VEX |
| Catálogo | Mais de mil imagens e Helm charts (bases, runtimes, bancos de dados, etc.) |
| Edição comercial | Há uma versão Enterprise com SLAs e suporte estendido |

## Uso

```bash
# Registry próprio das DHI; exige autenticação com sua conta Docker
docker login dhi.io
docker pull dhi.io/python:3.12
docker run --rm dhi.io/python:3.12 python -c "print('olá de uma imagem endurecida')"
```

Em um Dockerfile multi-stage:

```dockerfile
# syntax=docker/dockerfile:1
FROM dhi.io/python:3.12-dev AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt
COPY . .

FROM dhi.io/python:3.12
WORKDIR /app
COPY --from=build /install /usr/local
COPY --from=build /app /app
CMD ["python", "app.py"]
```

```bash
# Compare vulnerabilidades com a imagem comunitária
docker scout cves dhi.io/python:3.12
docker scout cves python:3.12
```

> [!question] Verificar na documentação oficial
> Nomes de tags, variantes (`-dev`, `-fips`), políticas de acesso e o modelo de licenciamento das DHI foram alterados recentemente. Confirme no catálogo oficial (dhi.io) e na documentação do Docker.

> [!tip] Quando usar
> Em produção, como base padrão para reduzir CVEs e esforço de manutenção. Lembre-se: imagem endurecida **não substitui** as demais práticas (usuário não-root, limites, segredos).

## Exercício

Reconstrua uma imagem sua sobre uma Docker Hardened Image equivalente e compare tamanho e número de CVEs com a versão anterior.

## Veja também

- [[Superfície de ataque e imagens mínimas]]
- [[Docker Scout]]
- [[SBOM e provenance]]
- [[Escolha da imagem base]]
- [[MOC - IA e Novidades]]
