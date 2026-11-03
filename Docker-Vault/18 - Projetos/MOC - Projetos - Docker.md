---
tags:
  - docker
  - moc
aliases: []
tipo: moc
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Home - Docker]]"
---

# MOC - Projetos - Docker

Nove projetos guiados, do simples ao avançado. Cada um traz **objetivos**, **estrutura de pastas**, `Dockerfile`, `compose.yaml`, **comandos**, **verificação**, **solução de problemas** e **extensões sugeridas**.

| # | Projeto | Nível | Conceitos principais |
|---|---|---|---|
| 01 | [[Projeto 01 - Site estático com Nginx]] | Iniciante | Dockerfile, Nginx não-root, healthcheck, override de dev |
| 02 | [[Projeto 02 - API Node.js containerizada]] | Iniciante | Multi-stage, dev/test/prod, graceful shutdown |
| 03 | [[Projeto 03 - WordPress com MySQL]] | Intermediário | Secrets, volumes, depends_on, WP-CLI, backup |
| 04 | [[Projeto 04 - Stack com Postgres, API e frontend]] | Intermediário | Redes isoladas, proxy interno, secrets |
| 05 | [[Projeto 05 - Proxy reverso com Traefik e HTTPS]] | Avançado | Let's Encrypt, labels, socket-proxy |
| 06 | [[Projeto 06 - Monitoramento com Prometheus e Grafana]] | Avançado | cAdvisor, node-exporter, alertas, provisioning |
| 07 | [[Projeto 07 - Pipeline CI-CD completo]] | Avançado | GitHub Actions, scan, SBOM, deploy SSH, rollback |
| 08 | [[Projeto 08 - Cluster Swarm com stack de produção]] | Avançado | Swarm, overlay, secrets/configs, rolling update |
| 09 | [[Projeto 09 - IA local com Ollama e aplicação]] | Intermediário | LLM local, volumes de modelos, GPU opcional |

> [!tip] Trilha sugerida
> 01 → 02 → 04 → 03 → 05 → 06 → 07 → 08 → 09. Faça cada projeto do zero, **sem copiar e colar às cegas**: leia, execute e quebre de propósito para aprender com os erros.

> [!warning] Ambiente de laboratório
> Os projetos usam senhas e domínios de exemplo. Em qualquer ambiente real, gere segredos fortes, use domínios seus e siga o [[Checklist de produção]].

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Projeto 01 - Site estático com Nginx]] — Nginx não-root com healthcheck e override de desenvolvimento
- [[Projeto 02 - API Node.js containerizada]] — Express multi-stage com dev/test/prod e shutdown gracioso
- [[Projeto 03 - WordPress com MySQL]] — WordPress + MySQL com secrets, healthcheck, WP-CLI e backup
- [[Projeto 04 - Stack com Postgres, API e frontend]] — Três camadas com redes isoladas, secrets e healthchecks encadeados
- [[Projeto 05 - Proxy reverso com Traefik e HTTPS]] — Traefik com Let's Encrypt, redirecionamento e socket-proxy
- [[Projeto 06 - Monitoramento com Prometheus e Grafana]] — node-exporter, cAdvisor, Prometheus, Grafana e alertas
- [[Projeto 07 - Pipeline CI-CD completo]] — Testes, scan, build multiplataforma, push e deploy SSH com rollback
- [[Projeto 08 - Cluster Swarm com stack de produção]] — 3 nós, stack com config/secret, rolling update e drain
- [[Projeto 09 - IA local com Ollama e aplicação]] — Ollama em container, API FastAPI e persistência de modelos

## Veja também

- [[Home - Docker]]
