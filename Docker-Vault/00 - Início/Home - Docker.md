---
tags:
  - docker
  - moc
aliases:
  - Docker - Material de Estudos
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[MOC - Fundamentos - Docker]]"
  - "[[MOC - Containers]]"
  - "[[MOC - Dockerfile]]"
  - "[[MOC - Docker Compose]]"
  - "[[MOC - Segurança]]"
  - "[[MOC - Projetos - Docker]]"
  - "[[Trilha de aprendizado - Docker]]"
  - "[[Índice geral - Docker]]"
---

# Home - Docker

Material completo, em português do Brasil, para aprender **Docker** do zero até a produção: fundamentos, imagens, Dockerfile, Compose, redes, volumes, segurança, Swarm, observabilidade, CI/CD, produção, IA e novidades, com **9 projetos guiados**, exercícios com gabarito e material de referência.

> [!tip] Primeira vez aqui?
> Leia [[Como usar este vault - Docker]], escolha uma rota em [[Trilha de aprendizado - Docker]] e siga o [[Roteiro de estudo por semanas]].

## Comece aqui

- [[Como usar este vault - Docker]]
- [[Trilha de aprendizado - Docker]] e o mapa visual [[Trilha de Aprendizado em Docker.canvas]]
- [[Roteiro de estudo por semanas]] (12 semanas)
- [[Índice geral - Docker]] (todas as notas em ordem alfabética)
- [[Glossário#Docker]] · [[Cheat sheet de comandos Docker]] · [[Erros comuns e soluções]]

## Mapa de seções (MOCs)

| # | Seção | Conteúdo |
|---|---|---|
| 01 | [[MOC - Fundamentos - Docker]] | O que é Docker, arquitetura, OCI, namespaces, cgroups, camadas |
| 02 | [[MOC - Instalação e Configuração]] | Linux, Windows (WSL2), macOS, daemon.json, contextos, rootless |
| 03 | [[MOC - Containers]] | Ciclo de vida, `docker run`, portas, variáveis, limites, healthchecks |
| 04 | [[MOC - Imagens]] | pull, tags e digests, push, save/load, prune, imagens base |
| 05 | [[MOC - Dockerfile]] | Todas as instruções, cache, multi-stage, heredocs, boas práticas |
| 06 | [[MOC - Build Avançado]] | BuildKit, Buildx, mounts, multiplataforma, Bake, cache, SBOM |
| 07 | [[MOC - Volumes e Armazenamento]] | Volumes, bind mounts, tmpfs, backup, permissões, overlay2 |
| 08 | [[MOC - Redes]] | Drivers, DNS, firewall, IPv6, proxies reversos |
| 09 | [[MOC - Docker Compose]] | compose.yaml, healthchecks, profiles, overrides, secrets, Watch |
| 10 | [[MOC - Registries]] | Docker Hub, GHCR, GitLab, ECR, GAR, ACR, registry local |
| 11 | [[MOC - Segurança]] | Menor privilégio, segredos, scan, assinatura, hardening |
| 12 | [[MOC - Swarm e Orquestração]] | Swarm, stacks, secrets, rolling updates, Kubernetes |
| 13 | [[MOC - Observabilidade e Depuração]] | Logs, eventos, métricas, OOM, rede, diagnóstico |
| 14 | [[MOC - Desenvolvimento]] | Dev Containers, bancos, filas, linguagens, Testcontainers |
| 15 | [[MOC - CI-CD e DevOps]] | GitHub Actions, GitLab CI, Jenkins, rollout, Terraform, GitOps |
| 16 | [[MOC - Produção]] | 12-factor, resiliência, backups, VPS, ECS, Cloud Run, checklist |
| 17 | [[MOC - IA e Novidades]] | Model Runner, GPU, MCP, Hardened Images, Wasm, alternativas |
| 18 | [[MOC - Projetos - Docker]] | Nove projetos guiados do simples ao avançado |
| 19 | [[MOC - Referência - Docker]] | Glossário, cheat sheets, erros, FAQ, antipadrões, flashcards |
| 20 | [[MOC - Exercícios - Docker]] | Exercícios com gabarito, desafios e simulado |

## Rota rápida por nível

**Iniciante:** [[O que é Docker]] → [[Verificando com hello-world]] → [[Comando docker run]] → [[Comando docker pull]] → [[Projeto 01 - Site estático com Nginx]]

**Intermediário:** [[Introdução ao Dockerfile]] → [[Multi-stage builds]] → [[Volumes nomeados]] → [[Redes bridge]] → [[Visão geral do Docker Compose]] → [[Projeto 04 - Stack com Postgres, API e frontend]]

**Avançado:** [[Buildx e BuildKit]] → [[Princípio do menor privilégio - Docker]] → [[Fluxo de diagnóstico de problemas]] → [[Pipeline CI-CD com Docker]] → [[Checklist de produção]] → [[Projeto 07 - Pipeline CI-CD completo]]

## Mapas conceituais (Canvas)

- [[Arquitetura do Docker.canvas]]
- [[Trilha de Aprendizado em Docker.canvas]]
- [[Mapa de Segurança em Docker.canvas]]

## Anexos e templates

- [[MOC - Material de Apoio]]: livros, cursos, certificações, comunidades, versões de referência
- Templates: [[Template de nota de conceito - Docker]], [[Template de nota de comando]], [[Template de projeto - Docker]], [[Template de anotação de estudo]]

## Antes de usar em produção

> [!warning] Conteúdo sujeito a mudanças
> Versões, imagens e ferramentas evoluem. Confira [[Versões de referência e fontes consultadas]] e verifique os itens marcados com o aviso *Verificar na documentação oficial* antes de adotar qualquer exemplo em produção.

> [!danger] Segurança
> Os exemplos de segurança têm fins **defensivos e educacionais** e devem ser executados somente em ambiente de laboratório próprio.

## Veja também

- [[Índice geral - Docker]]
- [[Trilha de aprendizado - Docker]]
- [[MOC - Projetos - Docker]]
