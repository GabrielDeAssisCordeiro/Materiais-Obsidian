---
tags:
  - docker
  - producao
  - checklist
  - boas-praticas
aliases: []
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados:
  - "[[Aplicações 12-factor em containers]]"
  - "[[Resiliência em produção]]"
  - "[[Checklist de segurança de containers]]"
  - "[[Backups em produção]]"
  - "[[Monitoramento em produção]]"
---

# Checklist de produção

## Imagem e build

- [ ] Imagem **mínima**, multi-stage, **tag fixa/digest**, sem segredos.
- [ ] Varredura de vulnerabilidades e SBOM; imagem assinada e verificada.
- [ ] Pipeline automatizado com tags rastreáveis (`1.4.2`, `sha-...`).

## Execução

- [ ] Usuário não-root, `read_only`, `cap_drop: [ALL]`, `no-new-privileges`.
- [ ] **Limites** de CPU/memória/PIDs.
- [ ] `restart: unless-stopped` (ou política do orquestrador) e `init: true`.
- [ ] **Healthcheck** e *graceful shutdown* (`stop_grace_period`).
- [ ] Logs em stdout/stderr com **rotação** e centralização.
- [ ] Configuração por variáveis e **secrets** (nunca na imagem).

## Rede e acesso

- [ ] Proxy reverso com **TLS**; apenas 80/443 expostas.
- [ ] Bancos e serviços internos em redes `internal`, sem portas publicadas.
- [ ] Firewall de borda e regras em `DOCKER-USER`; SSH endurecido.

## Dados

- [ ] Volumes nomeados para o estado; **backups** automatizados, criptografados e **testados**.
- [ ] Migrações de banco retrocompatíveis.

## Operação

- [ ] **Monitoramento** (disponibilidade, métricas, logs) e **alertas** definidos.
- [ ] Estratégia de **rollout** e **rollback** documentada e ensaiada.
- [ ] Atualização regular do host, Docker, containerd e imagens base.
- [ ] Documentação e *runbooks* de incidentes.
- [ ] Limpeza periódica (`image prune`, retenção no registry).

> [!tip] Use como revisão pré-lançamento
> Faça uma "reunião de prontidão de produção" percorrendo este checklist com a equipe antes do primeiro deploy.

## Exercício

Aplique o checklist ao seu projeto, marque o que falta e priorize os três itens de maior risco para resolver primeiro.

## Veja também

- [[Aplicações 12-factor em containers]]
- [[Resiliência em produção]]
- [[Checklist de segurança de containers]]
- [[Backups em produção]]
- [[Monitoramento em produção]]
- [[MOC - Produção]]
