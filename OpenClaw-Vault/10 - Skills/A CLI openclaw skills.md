---
titulo: "A CLI openclaw skills"
tags:
  - openclaw
  - conceito
  - skills
tipo: conceito
aliases: ['openclaw skills', 'Comandos de skills']
nivel: intermediario
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/cli/skills.md"
relacionados:
  - "[[Anatomia do SKILL.md e requisitos de elegibilidade]]"
  - "[[ClawHub - publicar, versões e verificação]]"
  - "[[Criar a primeira skill - hello-world]]"
  - "[[Configuração de skills em openclaw.json]]"
---

# A CLI openclaw skills

## Objetivo

Dominar os subcomandos de `openclaw skills` confirmados na página `cli/skills`: inventário, descoberta, instalação, atualização e verificação.

## Explicação

`list` é o padrão quando nenhum subcomando é informado. Os subcomandos se agrupam por finalidade.

### Inventário e prontidão

| Comando | Flags | Uso |
|---|---|---|
| `openclaw skills list` | `--eligible`, `--json`, `--verbose`, `--agent <id>` | Lista skills |
| `openclaw skills info <nome>` | `--json`, `--agent <id>` | Detalha uma skill |
| `openclaw skills check` | `--agent <id>`, `--json` | Inventário, prontidão e visibilidade |

### Descoberta e instalação

| Comando | Observação |
|---|---|
| `openclaw skills search "calendar"` | Busca no ClawHub; `--limit <n>`, `--json`; sem consulta mostra os destaques |
| `openclaw skills install @dono/slug` | ClawHub; `--version`, `--force`, `--force-install`, `--acknowledge-install-policy-warning`, `--agent`, `--global` |
| `openclaw skills install git:dono/repo[@ref]` | Clona de um repositório Git |
| `openclaw skills install ./caminho --as nome` | Instala de um diretório local |
| `openclaw skills install skills-sh:dono/repo/slug` | Listagem externa resolvida pelo ClawHub |

### Atualização e verificação

| Comando | Uso |
|---|---|
| `openclaw skills update @dono/slug` | Atualiza uma skill rastreada |
| `openclaw skills update --all` | Atualiza todas as instalações rastreadas do ClawHub |
| `openclaw skills verify @dono/slug` | Verifica; `--json`, `--version`, `--tag`, `--card`, `--global` |

Existem também `openclaw skills workshop ...` (skills aprendidas: `list`, `changes`, `show`, `archive`, `restore`) e `openclaw skills library ...` (biblioteca pessoal). **Remover** uma skill do ClawHub usa a CLI separada: `clawhub uninstall @dono/minha-skill`.

> [!warning] Flags de força
> `--force-install` e `--acknowledge-install-policy-warning` existem para contornar avisos de política. Use apenas depois de ler o código da skill e entender o aviso; veja a nota sobre ClawHub no ecossistema ([[ClawHub, plugins e o ecossistema]]).

## Exemplo prático

Fluxo seguro de instalação de uma skill de terceiros:

```bash
openclaw skills search "calendar" --limit 5
openclaw skills verify @autor/calendario --json
openclaw skills install @autor/calendario --version 1.2.0
openclaw skills info calendario
openclaw skills check
```

Fixar `--version` evita que uma atualização silenciosa mude o comportamento.

## Armadilhas comuns

- Usar `--global` sem querer e instalar para todos os agentes.
- Esquecer `--agent <id>` em instalações com vários agentes.
- Procurar `openclaw skills uninstall`: a remoção é feita pelo `clawhub`.
- Confundir `search` (ClawHub) com `list` (instaladas).

## Resumo

- `list`, `info`, `check` para inventário.
- `search`, `install`, `update`, `verify` para o ciclo de vida.
- Fixe versões e verifique antes de instalar.

## Relacionados

- [[Anatomia do SKILL.md e requisitos de elegibilidade]]
- [[ClawHub - publicar, versões e verificação]]
- [[Criar a primeira skill - hello-world]]
- [[Configuração de skills em openclaw.json]]
- [[ClawHub, plugins e o ecossistema]]

## Exercícios

1. Qual comando mostra só skills elegíveis?
2. Como instalar uma versão específica de uma skill do ClawHub?
3. Que comando remove uma skill instalada do ClawHub?
4. Para que serve `openclaw skills verify`?
