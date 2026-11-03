---
tags:
  - docker
  - desenvolvimento
  - dockerfile
  - compose
aliases: []
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Introdução ao Dockerfile]]"
  - "[[Visão geral do Docker Compose]]"
  - "[[Boas práticas de Dockerfile]]"
---

# Docker Init

O **`docker init`** gera automaticamente `Dockerfile`, `compose.yaml`, `.dockerignore` e um `README.Docker.md` adaptados ao seu projeto, seguindo boas práticas (multi-stage, usuário não-root, cache).

```bash
cd meu-projeto
docker init
```

Ele pergunta (de forma interativa) a **plataforma** do projeto e parâmetros, como versão da linguagem, porta e comando de início.

| Plataformas oferecidas (principais) |
|---|
| Node.js, Python, Go, Rust, Java, PHP com Apache, ASP.NET Core, e "Other" (genérico) |

## Fluxo recomendado

1. Rode `docker init` em um projeto de exemplo.
2. **Leia** os arquivos gerados e o README: eles ensinam boas práticas.
3. Ajuste ao seu caso (variáveis, healthcheck, dependências).
4. Teste: `docker compose up --build`.

```bash
docker compose up --build
docker compose down
```

> [!tip] Ótimo para aprender
> Gere um Dockerfile para sua linguagem e compare com o que você escreveria à mão; é uma referência atualizada de boas práticas.

> [!question] Verificar na documentação oficial
> O `docker init` é distribuído com o Docker Desktop e como plugin da CLI; a disponibilidade em instalações do Engine, as linguagens suportadas e as perguntas variam por versão. Consulte a documentação.

> [!warning] Revise antes de usar em produção
> Arquivos gerados são um ponto de partida. Revise permissões, portas, segredos e versões de imagem.

## Exercício

Rode `docker init` em um projeto simples (Node ou Python), suba com `docker compose up --build` e liste três boas práticas que o Dockerfile gerado aplica.

## Veja também

- [[Introdução ao Dockerfile]]
- [[Visão geral do Docker Compose]]
- [[Boas práticas de Dockerfile]]
- [[MOC - Desenvolvimento]]
