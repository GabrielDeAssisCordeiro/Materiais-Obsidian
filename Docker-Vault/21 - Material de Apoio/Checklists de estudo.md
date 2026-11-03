---
tags:
  - docker
  - anexos
  - checklist
  - estudos
aliases: []
tipo: anexo
nivel: iniciante
criado: 2026-10-24
relacionados:
  - "[[Trilha de aprendizado - Docker]]"
  - "[[Roteiro de estudo por semanas]]"
  - "[[Glossário#Docker]]"
---

# Checklists de estudo

Marque conforme domina cada ponto (sem consultar).

## Iniciante

- [ ] Explico imagem vs container, e container vs VM.
- [ ] Instalo e valido o Docker.
- [ ] Uso `run`, `ps`, `logs`, `exec`, `stop`, `rm`, `inspect`.
- [ ] Publico portas e uso variáveis de ambiente.
- [ ] Entendo tags e digests; evito `latest` em produção.
- [ ] Faço `pull`, `tag`, `push` e limpo o ambiente com `prune`.

## Intermediário

- [ ] Escrevo um Dockerfile com cache eficiente, multi-stage e usuário não-root.
- [ ] Diferencio `CMD`/`ENTRYPOINT`, `COPY`/`ADD`, `ARG`/`ENV`, shell/exec.
- [ ] Uso volumes, bind mounts e tmpfs; faço backup e restauração.
- [ ] Crio redes definidas pelo usuário e isolo camadas.
- [ ] Monto stacks com Compose (healthchecks, profiles, overrides, secrets).
- [ ] Publico em registries e uso tokens de acesso.

## Avançado

- [ ] Uso BuildKit: cache mounts, secret mounts, multiplataforma, Bake e cache remoto.
- [ ] Aplico menor privilégio (`cap-drop`, `read-only`, seccomp, rootless).
- [ ] Gerencio segredos e escaneio imagens; entendo SBOM e assinatura.
- [ ] Diagnostico reinícios, OOM e rede com método.
- [ ] Monitoro com Prometheus/Grafana e centralizo logs.
- [ ] Construo pipelines CI/CD com scan, deploy e rollback.
- [ ] Implanto em produção (VPS, nuvem ou Swarm) com estratégia de rollout e backups testados.
- [ ] Sei quando migrar para Kubernetes.

## Meta final

- [ ] Concluí os 9 projetos de [[MOC - Projetos - Docker]].
- [ ] Fiz o [[Simulado de múltipla escolha]] com pelo menos 80%.
- [ ] Concluí ao menos 3 dos [[Desafios finais]].

## Veja também

- [[Trilha de aprendizado - Docker]]
- [[Roteiro de estudo por semanas]]
- [[Glossário#Docker]]
