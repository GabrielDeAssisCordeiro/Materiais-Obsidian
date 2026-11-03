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

# MOC - Containers

Tudo sobre executar e gerenciar containers: ciclo de vida, `docker run`, portas, variáveis, limites de recursos, healthchecks, restart e depuração.

> [!tip] Fluxo recomendado
> Leia [[Ciclo de vida do container]] e [[Comando docker run]], pratique com [[Modos interativo e detached]] e avance para configuração e resiliência.

> [!info] Navegação
> Volte para [[Home - Docker]] a qualquer momento.

## Notas desta seção

- [[Ciclo de vida do container]] — Estados e transições (diagrama), códigos de saída
- [[Comando docker run]] — Sintaxe, opções principais e exemplos
- [[Modos interativo e detached]] — -it, -d e como sair do terminal
- [[Comandos create, start, stop, restart e kill]] — Controlar o ciclo de vida com comandos
- [[Comandos ps e rm]] — Listar, filtrar e remover
- [[Comando docker logs]] — Ler, filtrar e seguir logs
- [[Comando docker exec e attach]] — exec vs attach e depuração
- [[Comando docker inspect]] — JSON e --format com Go templates
- [[Comandos stats e top]] — Consumo de recursos e processos
- [[Comandos cp, diff e commit]] — Copiar, comparar e commitar
- [[Variáveis de ambiente em containers]] — -e, --env-file e boas práticas
- [[Publicação de portas]] — -p, -P, EXPOSE e riscos de firewall
- [[Políticas de restart]] — no, on-failure, always e unless-stopped
- [[Limites de recursos - Docker]] — Memória, CPU, PIDs e ulimits
- [[Healthchecks em containers]] — --health-* e estados
- [[Nomes e labels]] — --name, --hostname e --label
- [[Init, PID 1 e sinais]] — Sinais, zumbis, forma exec e --init

## Veja também

- [[Home - Docker]]
