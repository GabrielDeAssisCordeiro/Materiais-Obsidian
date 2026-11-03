---
tags:
  - docker
  - seguranca
aliases: []
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados:
  - "[[Hardening do host Docker]]"
  - "[[Checklist de segurança de containers]]"
  - "[[Arquivo daemon.json]]"
---

# CIS Docker Benchmark e Docker Bench for Security

O **CIS Docker Benchmark** é um guia de configuração segura mantido pelo *Center for Internet Security*. Ele cobre:

1. Configuração do host
2. Configuração do daemon
3. Arquivos de configuração do daemon
4. Imagens de container e Dockerfiles
5. Runtime dos containers
6. Operações de segurança
7. Configuração do Swarm

## Docker Bench for Security

Script oficial (open source) que verifica automaticamente dezenas dessas recomendações **no host onde roda**. Use apenas em **máquinas suas ou autorizadas**.

```bash
git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security
sudo sh docker-bench-security.sh
```

A saída classifica cada item: `[PASS]`, `[WARN]`, `[INFO]`, `[NOTE]`.

| Exemplo de WARN | Correção típica |
|---|---|
| Containers sem limite de memória | `--memory` / `deploy.resources` |
| Containers como root | `USER` não-root |
| Sem HEALTHCHECK | Adicionar `HEALTHCHECK` |
| Sem auditoria dos arquivos do Docker | Regras do `auditd` |
| `live-restore` desabilitado | Habilitar no `daemon.json` |

> [!tip] Use como ponto de partida
> Nem todo item se aplica ao seu contexto. Avalie risco x custo, documente exceções e reexecute após mudanças.

> [!question] Verificar na documentação oficial
> A versão do benchmark e do script acompanham as versões do Docker; consulte o repositório do projeto e o site do CIS para a edição vigente (o download do PDF exige cadastro no CIS).

## Exercício

Execute o Docker Bench no seu host de laboratório, selecione três WARN e corrija cada um, reexecutando para confirmar.

## Veja também

- [[Hardening do host Docker]]
- [[Checklist de segurança de containers]]
- [[Arquivo daemon.json]]
- [[MOC - Segurança]]
