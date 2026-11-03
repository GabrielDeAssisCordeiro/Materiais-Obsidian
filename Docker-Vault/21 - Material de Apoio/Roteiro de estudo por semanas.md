---
tags:
  - docker
  - anexos
  - roteiro
  - estudos
aliases: []
tipo: anexo
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Trilha de aprendizado - Docker]]"
  - "[[Checklists de estudo]]"
  - "[[MOC - Exercícios - Docker]]"
---

# Roteiro de estudo por semanas

Plano de 12 semanas, com cerca de 5 a 8 horas por semana. Ajuste o ritmo ao seu tempo.

| Semana | Foco | Estudar | Praticar | Entregável |
|---|---|---|---|---|
| 1 | Fundamentos e instalação | [[MOC - Fundamentos - Docker]], [[MOC - Instalação e Configuração]] | `hello-world`, `docker version/info` | Docker funcionando + [[Exercícios de Fundamentos e Instalação]] |
| 2 | Containers | [[MOC - Containers]] | `run`, `exec`, `logs`, limites, healthchecks | [[Exercícios de Containers e Imagens]] |
| 3 | Imagens e registries básicos | [[MOC - Imagens]] | `pull`, `tag`, `save`, `prune` | [[Projeto 01 - Site estático com Nginx]] |
| 4 | Dockerfile | [[MOC - Dockerfile]] | Dockerfiles de 2 linguagens, multi-stage | [[Projeto 02 - API Node.js containerizada]] |
| 5 | Volumes e redes | [[MOC - Volumes e Armazenamento]], [[MOC - Redes]] | Persistência, backup, redes isoladas | [[Exercícios de Volumes e Redes]] |
| 6 | Compose | [[MOC - Docker Compose]] | Stack multi-serviço, secrets, profiles | [[Projeto 04 - Stack com Postgres, API e frontend]] |
| 7 | Registries e build avançado | [[MOC - Registries]], [[MOC - Build Avançado]] | Registry local, buildx multiplataforma, cache | [[Exercícios de Compose e Registries]] |
| 8 | Segurança | [[MOC - Segurança]] | Hardening, scan, secrets | [[Exercícios de Segurança e Swarm]] |
| 9 | Observabilidade | [[MOC - Observabilidade e Depuração]] | Prometheus/Grafana, diagnóstico | [[Projeto 06 - Monitoramento com Prometheus e Grafana]] |
| 10 | CI/CD | [[MOC - CI-CD e DevOps]] | GitHub Actions, deploy SSH | [[Projeto 07 - Pipeline CI-CD completo]] |
| 11 | Produção e orquestração | [[MOC - Produção]], [[MOC - Swarm e Orquestração]] | VPS, HTTPS, Swarm | [[Projeto 05 - Proxy reverso com Traefik e HTTPS]], [[Projeto 08 - Cluster Swarm com stack de produção]] |
| 12 | Revisão e especialização | [[MOC - IA e Novidades]], [[MOC - Desenvolvimento]] | Simulado, desafios, flashcards | [[Simulado de múltipla escolha]], [[Desafios finais]] |

## Rotina semanal sugerida

1. **Ler** (2 h): notas da semana, sem copiar e colar.
2. **Praticar** (3 h): comandos e projetos; quebre de propósito e conserte.
3. **Revisar** (1 h): [[Flashcards de Docker]] e exercícios.
4. **Registrar** (30 min): anotações próprias com o [[Template de anotação de estudo]].

> [!tip] Consistência vence intensidade
> Estudar pouco todo dia retém mais do que maratonas de fim de semana.

## Veja também

- [[Trilha de aprendizado - Docker]]
- [[Checklists de estudo]]
- [[MOC - Exercícios - Docker]]
