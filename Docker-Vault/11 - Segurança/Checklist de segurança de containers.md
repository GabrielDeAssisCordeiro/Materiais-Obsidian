---
tags:
  - docker
  - seguranca
  - checklist
  - boas-praticas
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Princípio do menor privilégio - Docker]]"
  - "[[Varredura de vulnerabilidades com Trivy e Grype]]"
  - "[[Gerenciamento de segredos]]"
  - "[[Boas práticas de Dockerfile]]"
  - "[[Hardening do host Docker]]"
---

# Checklist de segurança de containers

## Imagem

- [ ] Base oficial/verificada e **mínima**; tag fixa ou digest.
- [ ] **Multi-stage**; sem ferramentas de build na imagem final.
- [ ] Sem segredos (ENV, ARG, COPY, camadas, histórico).
- [ ] Varredura de vulnerabilidades no CI e periódica.
- [ ] SBOM e provenance gerados; imagem **assinada** e verificada.

## Execução

- [ ] Usuário **não-root** (UID numérico).
- [ ] `--read-only` com `tmpfs`/volumes para escrita.
- [ ] `--cap-drop ALL` e `--cap-add` apenas do necessário.
- [ ] `no-new-privileges:true`.
- [ ] seccomp e AppArmor/SELinux **ativos** (nunca `unconfined`).
- [ ] **Sem** `--privileged`, `docker.sock`, `--pid/--network=host` sem justificativa.
- [ ] Limites de CPU, memória e PIDs.
- [ ] Healthcheck e política de restart.

## Rede e dados

- [ ] Redes segmentadas (`frontend`/`backend`, `internal` para bancos).
- [ ] Portas publicadas no mínimo e em `127.0.0.1` quando possível; proxy reverso com TLS.
- [ ] Volumes com permissões corretas; bind mounts `:ro` quando possível.
- [ ] Backups testados.

## Plataforma

- [ ] Docker, containerd, runc e kernel atualizados.
- [ ] Daemon sem exposição TCP sem TLS; acesso via SSH/TLS.
- [ ] Logs centralizados, rotação configurada, auditoria ativa.
- [ ] Docker Bench/CIS executado e itens tratados.

> [!tip] Automatize
> Valide parte desta lista no CI (Hadolint, `docker build --check`, Trivy `config`, políticas OPA/Conftest sobre Compose e manifests).

## Exercício

Aplique este checklist a uma aplicação sua, marque cada item como atendido ou não e crie um plano de ação priorizado.

## Veja também

- [[Princípio do menor privilégio - Docker]]
- [[Varredura de vulnerabilidades com Trivy e Grype]]
- [[Gerenciamento de segredos]]
- [[Boas práticas de Dockerfile]]
- [[Hardening do host Docker]]
- [[MOC - Segurança]]
