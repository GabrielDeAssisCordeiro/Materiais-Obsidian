---
titulo: "Arquivos do workspace do agente"
tags:
  - openclaw
  - conceito
  - agent-runtime
tipo: conceito
aliases: ['Workspace', 'AGENTS.md', 'SOUL.md']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/concepts/agent"
  - "https://docs.openclaw.ai/concepts/agent-workspace"
  - "https://docs.openclaw.ai/skill.md"
relacionados:
  - "[[Montagem do system prompt]]"
  - "[[O agent runtime embutido]]"
  - "[[Onde o OpenClaw guarda estado em disco]]"
  - "[[Memória e contexto em agentes]]"
---

# Arquivos do workspace do agente

## Objetivo

Conhecer os arquivos que formam a "personalidade e memória em texto" do agente e quando eles são lidos.

## Explicação

O workspace é "a casa do agente": o diretório de trabalho das ferramentas de arquivo e do contexto. Ele é **separado de `~/.openclaw/`**, que guarda configuração, credenciais e sessões. O padrão é `~/.openclaw/workspace`; com `OPENCLAW_PROFILE` diferente de `default`, vira `~/.openclaw-<perfil>/workspace`; `OPENCLAW_WORKSPACE_DIR` sobrescreve ambos.

**Arquivos de bootstrap**, injetados no Project Context do system prompt **no primeiro turno de uma nova sessão**:

| Arquivo | Função |
|---|---|
| `AGENTS.md` | Instruções operacionais e "memória" de trabalho |
| `SOUL.md` | Persona, limites e tom |
| `IDENTITY.md` | Nome, estilo e emoji do agente |
| `USER.md` | Perfil do usuário e forma de tratamento |
| `BOOTSTRAP.md` | Ritual de primeira execução; criado só em workspace novo e **apagado ao concluir** |
| `MEMORY.md` | Memória de longo prazo na raiz; injetado **somente se existir** |

Regras de injeção: arquivos em branco são ignorados, arquivos grandes são truncados com um marcador e a falta de um arquivo (exceto `MEMORY.md`) injeta uma linha de "arquivo ausente". Para impedir a criação automática dos arquivos de bootstrap, use `agents.defaults.skipBootstrap: true`.

```json5
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      skipBootstrap: false,
    },
  },
}
```

> [!warning] Arquivos aposentados
> A documentação lista `HEARTBEAT.md` e `TOOLS.md` como arquivos de workspace **aposentados**. Guias antigos que mandam editá-los estão desatualizados. A documentação fornece modelos (templates) para `AGENTS.md`, `BOOT.md`, `BOOTSTRAP.md`, `IDENTITY`, `SOUL.md` e `USER`.

**Segurança.** O workspace é o diretório padrão, **não um sandbox rígido**: caminhos absolutos alcançam outras partes do host, a menos que o sandbox esteja ligado. Também não coloque segredos aí: os arquivos entram no contexto e podem ser versionados por engano. As seções da página indicam backup em Git privado, sem commitar segredos; confirme a orientação completa na página do workspace.

## Exemplo prático

Mude o comportamento do agente editando um arquivo de texto. Abra `SOUL.md` e ajuste o tom:

```markdown
# SOUL
Responda em português do Brasil, de forma direta, em no máximo 5 linhas.
Antes de executar comandos que alterem arquivos, peça confirmação.
```

Inicie uma sessão nova (`/new`) e verifique, com `/context list`, que o arquivo foi injetado. (Texto de exemplo; ajuste ao seu caso.)

## Armadilhas comuns

- Esperar que a edição apareça numa sessão já iniciada: o bootstrap entra no primeiro turno de uma sessão nova.
- Colocar chaves de API no `USER.md` ou no `AGENTS.md`.
- Deixar arquivos enormes: são truncados e custam tokens.

## Resumo

- Workspace padrão: `~/.openclaw/workspace`, separado do diretório de estado.
- Arquivos: `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `BOOTSTRAP.md` e `MEMORY.md` (se existir).
- Injetados no primeiro turno de nova sessão; `HEARTBEAT.md` e `TOOLS.md` estão aposentados.
- Não é sandbox e não deve conter segredos.

## Relacionados

- [[Montagem do system prompt]]
- [[O agent runtime embutido]]
- [[Onde o OpenClaw guarda estado em disco]]
- [[Memória e contexto em agentes]]

## Exercícios

1. Quando os arquivos de bootstrap são injetados?
2. O que acontece com o `BOOTSTRAP.md` depois do primeiro uso?
3. Que chave impede a criação automática dos arquivos de bootstrap?
4. Por que não guardar segredos no workspace?
