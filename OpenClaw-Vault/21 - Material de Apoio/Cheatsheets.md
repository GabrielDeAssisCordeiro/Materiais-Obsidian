---
titulo: "Cheatsheets"
tags:
  - openclaw
  - cheatsheet
tipo: cheatsheet
aliases: ['Cola de comandos', 'Cheat sheets']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/"
relacionados:
  - "[[Glossário#OpenClaw]]"
  - "[[Rotina de manutenção e checklist de operação]]"
  - "[[Auditoria com openclaw security audit]]"
  - "[[A CLI openclaw skills]]"
---

# Cheatsheets

## Objetivo

Reunir em uma página os comandos mais usados, agrupados por tarefa. Todos foram citados em notas do vault a partir da documentação oficial; para detalhes e flags, abra a nota indicada ou use `--help`.

> [!warning] Versões
> A CLI evolui rápido (calendário v2026.10.x). Se um comando falhar, rode `openclaw <grupo> --help`.

## Explicação

### Instalar e verificar

```bash
curl -fsSL https://openclaw.ai/install.sh | bash       # macOS, Linux, WSL2
openclaw onboard --install-daemon
openclaw --version
openclaw doctor
openclaw gateway status --deep
openclaw dashboard
```

Veja [[Requisitos e escolha do método de instalação]] e [[Onboarding e verificação pós-instalação]].

### Gateway e serviço

```bash
openclaw gateway install | status | start | stop | restart | uninstall
openclaw gateway probe
openclaw config get <chave>
openclaw config set <chave> <valor>
openclaw config validate
openclaw config schema
```

### Canais e pareamento

```bash
openclaw channels add --channel telegram --token "$TELEGRAM_BOT_TOKEN"
openclaw channels login --channel whatsapp
openclaw channels status --probe
openclaw pairing list telegram
openclaw pairing approve telegram <CODIGO>
```

### Modelos

```bash
openclaw models list
openclaw models status
openclaw models set <provedor>/<modelo>
openclaw models fallbacks add <modelo>
```

### Skills

```bash
openclaw skills list --eligible
openclaw skills search "calendar"
openclaw skills verify @autor/slug
openclaw skills install @autor/slug --version 1.0.0
openclaw skills update --all
```

### Ferramentas, MCP e aprovações

```bash
openclaw config set tools.exec.mode ask      # deny | allowlist | ask | auto | full
openclaw exec-policy show
openclaw approvals get
openclaw mcp list
openclaw mcp doctor <nome> --probe
openclaw mcp tools <nome> --include "search_*"
```

### Automação

```bash
openclaw automations list
openclaw automations runs <job-id>
openclaw hooks list
openclaw hooks check
```

### Segurança

```bash
openclaw security audit --deep
openclaw security audit --fix
openclaw secrets audit --check
openclaw secrets reload
openclaw sandbox explain
```

### Operação

```bash
openclaw update status
openclaw update --dry-run
openclaw backup create --output ~/Backups/openclaw --verify
openclaw backup restore <arquivo> --target <dir-novo>
openclaw logs --follow
openclaw doctor --fix
openclaw uninstall --dry-run --all
```

### Comandos de chat

```text
/status   /context list   /context detail   /compact   /new   /reset
/usage tokens   /usage full   /usage cost   /usage reset
/think   /queue   /activation   /skill <nome>
```

### Escada de diagnóstico (60 segundos)

```bash
openclaw status
openclaw status --all
openclaw gateway probe
openclaw gateway status
openclaw doctor
openclaw channels status --probe
openclaw logs --follow
```

Detalhes em [[Sem resposta no chat - pareamento, menção e allowlist]].

## Exemplo prático

Rotina semanal de uma passada:

```bash
openclaw update status && openclaw doctor --lint --severity-min warning && openclaw security audit
```

## Armadilhas comuns

- Rodar `doctor --fix` ou `uninstall` sem backup.
- Esquecer o perfil (`OPENCLAW_PROFILE`) em um dos comandos.
- Colar tokens em comandos que ficam no histórico do shell.

## Resumo

- Comandos por tarefa; chat à parte.
- Escada de 60 segundos para qualquer problema.
- Confirme flags com `--help`.

## Relacionados

- [[Glossário#OpenClaw]]
- [[Rotina de manutenção e checklist de operação]]
- [[Auditoria com openclaw security audit]]
- [[A CLI openclaw skills]]
- [[Fontes]]

## Exercícios

1. Escreva de memória a escada de diagnóstico.
2. Que comando valida a configuração antes de reiniciar?
3. Como instalar uma skill com versão fixa?
4. Qual comando de chat mostra o custo estimado?
