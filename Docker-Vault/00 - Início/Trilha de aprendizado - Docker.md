---
tags:
  - docker
  - anexos
  - trilha
  - estudos
aliases: []
tipo: anexo
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Roteiro de estudo por semanas]]"
  - "[[Checklists de estudo]]"
---

# Trilha de aprendizado - Docker

Três níveis, com o essencial de cada um. Veja também o mapa visual em [[Trilha de Aprendizado em Docker.canvas]].

## Nível 1: Iniciante

Objetivo: entender o modelo e executar containers com segurança básica.

1. [[MOC - Fundamentos - Docker]]: [[O que é Docker]], [[Containers vs Máquinas Virtuais]], [[Imagens vs Containers]]
2. [[MOC - Instalação e Configuração]]: instalar e validar com [[Verificando com hello-world]]
3. [[MOC - Containers]]: [[Comando docker run]], [[Ciclo de vida do container]], [[Publicação de portas]]
4. [[MOC - Imagens]]: [[Comando docker pull]], [[Tags e digests de imagens]]
5. Projetos: [[Projeto 01 - Site estático com Nginx]], [[Projeto 02 - API Node.js containerizada]]

## Nível 2: Intermediário

Objetivo: construir imagens próprias e compor aplicações.

1. [[MOC - Dockerfile]]: [[Introdução ao Dockerfile]], [[Multi-stage builds]], [[Cache de camadas e ordem das instruções]]
2. [[MOC - Volumes e Armazenamento]]: [[Volumes nomeados]], [[Volume vs bind mount vs tmpfs]]
3. [[MOC - Redes]]: [[Redes bridge]], [[DNS interno e descoberta de serviços]]
4. [[MOC - Docker Compose]]: [[Visão geral do Docker Compose]], [[depends_on com condition e healthcheck]]
5. [[MOC - Registries]]: [[Docker Hub]], [[Login e tokens de acesso]]
6. Projetos: [[Projeto 03 - WordPress com MySQL]], [[Projeto 04 - Stack com Postgres, API e frontend]]

## Nível 3: Avançado

Objetivo: segurança, automação e produção.

1. [[MOC - Build Avançado]]: [[Buildx e BuildKit]], [[Secret mounts]], [[Build multiplataforma]]
2. [[MOC - Segurança]]: [[Princípio do menor privilégio - Docker]], [[Gerenciamento de segredos]]
3. [[MOC - Swarm e Orquestração]] e [[Compose vs Swarm vs Kubernetes]]
4. [[MOC - Observabilidade e Depuração]]
5. [[MOC - CI-CD e DevOps]] e [[MOC - Produção]]
6. Projetos: [[Projeto 05 - Proxy reverso com Traefik e HTTPS]], [[Projeto 06 - Monitoramento com Prometheus e Grafana]], [[Projeto 07 - Pipeline CI-CD completo]], [[Projeto 08 - Cluster Swarm com stack de produção]]

## Especialização

- [[MOC - Desenvolvimento]]: Dev Containers, Testcontainers, Dockerfiles por linguagem.
- [[MOC - IA e Novidades]]: [[Docker Model Runner]], [[Docker Hardened Images]], [[MCP e containers]]; projeto [[Projeto 09 - IA local com Ollama e aplicação]].
- Consolidação: [[MOC - Exercícios - Docker]] e [[MOC - Referência - Docker]].

## Veja também

- [[Roteiro de estudo por semanas]]
- [[Checklists de estudo]]
