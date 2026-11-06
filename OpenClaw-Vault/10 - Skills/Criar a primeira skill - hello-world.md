---
titulo: "Criar a primeira skill - hello-world"
tags:
  - openclaw
  - conceito
  - skills
tipo: conceito
aliases: ['Primeira skill', 'hello-world']
nivel: iniciante
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/tools/creating-skills"
relacionados:
  - "[[O que são skills e como o OpenClaw as carrega]]"
  - "[[Anatomia do SKILL.md e requisitos de elegibilidade]]"
  - "[[A CLI openclaw skills]]"
  - "[[Arquivos do workspace do agente]]"
---

# Criar a primeira skill - hello-world

## Objetivo

Criar, carregar e testar uma skill mínima no workspace, seguindo o tutorial oficial, e depois evoluí-la para algo útil.

## Explicação

Skills do workspace vivem em `~/.openclaw/workspace/skills/` (o workspace padrão; veja [[Arquivos do workspace do agente]]). Cada skill é uma pasta com um `SKILL.md`. Você pode agrupar em subpastas: a skill continua sendo identificada pelo `name` do frontmatter, não pelo caminho.

Regras de nome confirmadas: `name` usa minúsculas, dígitos e hífens; pasta e `name` devem coincidir; `description` em uma linha com menos de 160 caracteres.

### Passo a passo

1. Crie a pasta.
2. Escreva o `SKILL.md`.
3. Confirme que carregou.
4. Teste pela CLI ou no chat.

## Exemplo prático

```bash
mkdir -p ~/.openclaw/workspace/skills/hello-world
cat > ~/.openclaw/workspace/skills/hello-world/SKILL.md <<'EOF'
---
name: hello-world
description: Uma skill simples que imprime uma saudacao.
---

# Hello World

Quando o usuario pedir uma saudacao, use a ferramenta `exec` para rodar:

echo "Ola da minha skill personalizada!"
EOF
openclaw skills list
```

Teste:

```bash
openclaw agent --message "me de uma saudacao"
```

Ou no chat: `/skill hello-world`. O OpenClaw observa os `SKILL.md` por padrão; se o observador estiver desligado ou você estiver numa sessão antiga, abra uma sessão nova (`/new`) ou reinicie:

```bash
openclaw gateway restart
```

### Evoluindo a skill

Uma versão mais útil define **entradas, passos e limites**:

```markdown
---
name: resumo-diario
description: Resume as notas de hoje do workspace em cinco linhas.
---

# Resumo diario

1. Leia apenas arquivos em memory/ com a data de hoje.
2. Nao leia nada fora do workspace.
3. Responda em ate cinco linhas.
4. Se nao houver notas, diga isso, sem inventar.
```

> [!tip] Escreva limites
> Instruções negativas e de escopo ("não leia fora do workspace") reduzem o risco quando a skill roda com a ferramenta `exec` ou com arquivos (veja [[Confiança, permissões e riscos de agentes]]).

## Armadilhas comuns

- Pasta `hello_world` com `name: hello-world`: divergência.
- Skill criada fora de `skills/` e fora de `extraDirs`: não carrega.
- Esperar que o texto seja seguido ao pé da letra; modelos interpretam.
- Testar com sessão antiga e achar que a skill não existe.

## Resumo

- Pasta em `skills/` + `SKILL.md` com `name` e `description`.
- `openclaw skills list` confirma; `/skill <nome>` invoca.
- `openclaw agent --message` testa pela CLI.

## Relacionados

- [[O que são skills e como o OpenClaw as carrega]]
- [[Anatomia do SKILL.md e requisitos de elegibilidade]]
- [[A CLI openclaw skills]]
- [[ClawHub - publicar, versões e verificação]]
- [[Arquivos do workspace do agente]]

## Exercícios

1. Em que pasta ficam as skills do workspace padrão?
2. Como invocar uma skill explicitamente no chat?
3. O que fazer se o observador de arquivos estiver desligado e a skill não aparecer?
4. Escreva uma `description` válida (uma linha, menos de 160 caracteres) para uma skill de tradução.
