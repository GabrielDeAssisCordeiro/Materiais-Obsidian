---
tags:
  - docker
  - exercicios
  - projetos
aliases: []
tipo: exercicio
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Projeto 03 - WordPress com MySQL]]"
  - "[[Projeto 07 - Pipeline CI-CD completo]]"
  - "[[Projeto 08 - Cluster Swarm com stack de produção]]"
  - "[[Hardening do host Docker]]"
---

# Desafios finais

Desafios abertos, sem gabarito único. Cada um traz **critérios de aceite** para você autoavaliar.

## Desafio 1: Plataforma de blog resiliente

Implante WordPress + MySQL atrás do Traefik com HTTPS.

**Critérios de aceite**
- [ ] HTTPS válido (ou autoassinado em laboratório) e redirecionamento HTTP → HTTPS.
- [ ] Senhas por secrets; nenhuma porta de banco publicada.
- [ ] Healthchecks e `restart` configurados; limites de recursos.
- [ ] Backup automático (banco + uploads) e **restauração testada** em outra máquina.

## Desafio 2: API com pipeline completo

Containerize uma API sua e crie CI/CD (testes, scan, push, deploy com rollback).

**Critérios de aceite**
- [ ] Tags `semver` + `sha`; deploy por tag.
- [ ] Falha proposital em `/health` dispara **rollback automático**.
- [ ] SBOM/provenance gerados; scan bloqueia CVEs críticas.

## Desafio 3: Hardening com evidências

Pegue um serviço existente e endureça-o.

**Critérios de aceite**
- [ ] Docker Bench antes e depois, com a lista de itens corrigidos.
- [ ] Usuário não-root, `read_only`, `cap_drop: ALL`, `no-new-privileges`.
- [ ] Imagem mínima; CVEs HIGH/CRITICAL reduzidas e **medidas**.
- [ ] Documento curto justificando cada exceção.

## Desafio 4: Cluster tolerante a falhas

Monte um Swarm com 3 managers e 2 workers e implante uma stack de 3 camadas.

**Critérios de aceite**
- [ ] Derrubar um manager não interrompe o serviço.
- [ ] Atualização progressiva sem queda (medida com um loop de `curl`).
- [ ] Banco com estratégia de dados definida e documentada.

## Desafio 5: Modernizar uma aplicação legada

Pegue uma aplicação "tradicional" (instalada em servidor) e containerize aplicando 12-factor.

**Critérios de aceite**
- [ ] Configuração 100% por variáveis/secrets; logs em stdout.
- [ ] Estado externo (volume/banco); containers descartáveis.
- [ ] `docker compose up` sobe tudo, com README de três comandos.
- [ ] Lista de limitações e plano de evolução.

> [!tip] Registre
> Documente decisões, erros e soluções. Isso vira portfólio e seu próprio [[Erros comuns e soluções]].

## Veja também

- [[Projeto 03 - WordPress com MySQL]]
- [[Projeto 07 - Pipeline CI-CD completo]]
- [[Projeto 08 - Cluster Swarm com stack de produção]]
- [[Hardening do host Docker]]
- [[MOC - Exercícios - Docker]]
