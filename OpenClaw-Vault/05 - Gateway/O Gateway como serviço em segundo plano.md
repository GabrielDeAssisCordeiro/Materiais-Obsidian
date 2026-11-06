---
titulo: "O Gateway como serviço em segundo plano"
tags:
  - openclaw
  - conceito
  - gateway
tipo: conceito
aliases: ['Daemon', 'gateway install']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/pt-BR/cli/daemon.md"
  - "https://docs.openclaw.ai/start/getting-started"
  - "https://docs.openclaw.ai/"
relacionados:
  - "[[O processo Gateway e a porta 18789]]"
  - "[[Configuração do Gateway em openclaw.json]]"
  - "[[Acesso remoto - SSH, Tailscale e modos de bind]]"
  - "[[Tour rápido de instalação e primeira conversa]]"
---

# O Gateway como serviço em segundo plano

## Objetivo

Gerenciar o Gateway como serviço do sistema (launchd, systemd ou schtasks) e reiniciá-lo com segurança.

## Explicação

O Quick start do onboarding deixa o Gateway em **primeiro plano**. Para mantê-lo rodando depois que você fecha o terminal, instale o serviço. A documentação atual recomenda os comandos em `openclaw gateway ...`; `openclaw daemon` é um **alias legado** com os mesmos controles.

```bash
openclaw gateway install
openclaw gateway status
openclaw gateway start
openclaw gateway stop
openclaw gateway restart
openclaw gateway uninstall
```

(As páginas listam esses subcomandos sob o nome `daemon`; a forma `gateway` é a recomendada.)

| Subcomando | Flags documentadas |
|---|---|
| `status` | `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json` |
| `install` | `--port`, `--runtime <node>`, `--token`, `--wrapper <path>`, `--force`, `--json` |
| `start` | `--json` |
| `stop` | `--json`, `--disable` (somente launchd) |
| `restart` | `--force`, `--safe`, `--skip-deferral`, `--wait <duração>`, `--json` |
| `uninstall` | `--json` |

**Comportamentos que importam:**

- `status` mostra o estado do serviço (launchd, systemd ou schtasks) e checa a saúde do Gateway.
- `restart --safe` pede ao Gateway que **espere o trabalho ativo terminar** e agende um único reinício. A espera é limitada por `gateway.reload.deferralTimeoutMs` (padrão 300000 ms, 5 minutos; `0` espera indefinidamente). Vencido o prazo, o reinício é forçado. Com `--skip-deferral` (exige `--safe`), reinicia na hora.
- `install` valida que um SecretRef de `gateway.auth.token` resolve, mas **nunca grava o valor resolvido** nos metadados de ambiente do serviço.
- Se `gateway.auth.token` e `gateway.auth.password` estiverem definidos e `gateway.auth.mode` não, o `install` é **bloqueado** até você definir o modo.
- No macOS, o `install` mantém plists e arquivos gerados com permissão só do dono (0600/0700), para não embutir segredos.

```mermaid
flowchart LR
  A["Quick start: Gateway em primeiro plano"] -->|"Ctrl+C"| B["openclaw gateway install"]
  B --> C["Serviço ativo"]
  C --> D["status / restart --safe"]
```

## Exemplo prático

Depois de mudar configurações que exigem reinício, prefira o reinício seguro para não cortar uma execução do agente no meio:

```bash
openclaw gateway restart --safe
openclaw gateway status
```

Confirme, no `status`, que o serviço voltou saudável.

## Armadilhas comuns

- Usar `restart --force` com uma tarefa longa em andamento.
- Definir token e senha ao mesmo tempo sem escolher o modo de autenticação.
- Seguir um tutorial que usa só `openclaw daemon` sem checar se a sua versão ainda o aceita.

## Resumo

- Instale o serviço com `openclaw gateway install`; gerencie com `status`, `start`, `stop`, `restart`, `uninstall`.
- `daemon` é alias legado de `gateway`.
- `restart --safe` espera o trabalho ativo; o prazo padrão é de 5 minutos.
- O `install` protege segredos e bloqueia modo de autenticação ambíguo.

## Relacionados

- [[O processo Gateway e a porta 18789]]
- [[Configuração do Gateway em openclaw.json]]
- [[Acesso remoto - SSH, Tailscale e modos de bind]]
- [[MOC - Operação e Manutenção|Operação e Manutenção]]

## Exercícios

1. Qual a diferença entre `openclaw daemon` e `openclaw gateway`?
2. O que `restart --safe` faz e qual é o prazo padrão?
3. Por que o `install` se recusa a continuar com token e senha definidos e sem modo?
4. Que gerenciadores de serviço o `status` reconhece?
