---
tags:
  - docker
  - desenvolvimento
  - reprodutibilidade
  - compose
aliases: []
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Dev Containers no VS Code]]"
  - "[[Múltiplos arquivos e overrides]]"
  - "[[Bancos de dados locais]]"
  - "[[Hot reload em containers]]"
---

# Ambientes de desenvolvimento reproduzíveis

Objetivo: **`git clone` + um comando = ambiente funcionando**, igual para toda a equipe e igual ao CI.

## Estrutura recomendada

```text
projeto/
├── compose.yaml              # serviços base (app, db, cache)
├── compose.override.yaml     # ajustes de desenvolvimento (bind mounts, portas, debug)
├── Dockerfile                # estágios: dev, test, prod
├── .env.example              # variáveis (sem segredos reais)
├── .dockerignore
└── Makefile                  # atalhos: make up, make test, make down
```

`Makefile` (atalhos):

```makefile
up:
	docker compose up -d --build

logs:
	docker compose logs -f

test:
	docker compose run --rm app pytest

down:
	docker compose down

reset:
	docker compose down -v
```

## Princípios

| Princípio | Prática |
|---|---|
| Versões **fixas** | Imagens e dependências com versão (nada de `latest`) |
| Tudo em código | Banco, filas e ferramentas no Compose |
| Dados de exemplo | Scripts de *seed* e migrações automáticas |
| Paridade com produção | Mesma imagem base e mesmos serviços, em escala menor |
| Segredos fora do Git | `.env` ignorado; `.env.example` versionado |
| Documentação mínima | README com 3 comandos: clonar, subir, testar |

```bash
cp .env.example .env
make up
make test
```

> [!tip] Um Dockerfile, vários alvos
> Use estágios `dev`, `test` e `prod` e escolha com `build.target` no Compose. Assim ninguém mantém Dockerfiles divergentes.

> [!info] Ferramentas complementares
> Dev Containers, Compose Watch e Docker Init aceleram o processo. Veja [[Compose Watch]] e [[Docker Init]].

## Exercício

Transforme um projeto seu em "clonar e subir": adicione `compose.yaml`, `.env.example` e `Makefile`, e peça a alguém para testar em outra máquina.

## Veja também

- [[Dev Containers no VS Code]]
- [[Múltiplos arquivos e overrides]]
- [[Bancos de dados locais]]
- [[Hot reload em containers]]
- [[MOC - Desenvolvimento]]
