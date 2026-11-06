---
titulo: "Orçamento de bootstrap e tamanho do contexto"
tags:
  - openclaw
  - conceito
  - memoria
tipo: conceito
aliases: ['bootstrapMaxChars', 'Orçamento de contexto']
nivel: avancado
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/reference/token-use.md"
  - "https://docs.openclaw.ai/concepts/context"
  - "https://docs.openclaw.ai/concepts/agent-workspace"
relacionados:
  - "[[Montagem de contexto e o comando context]]"
  - "[[Arquivos do workspace do agente]]"
  - "[[Poda de sessão e compactação]]"
  - "[[Custo e escolha de modelo]]"
---

# Orçamento de bootstrap e tamanho do contexto

## Objetivo

Ajustar quanto do contexto é gasto com arquivos de bootstrap, imagens e instruções fixas, para sobrar espaço para a conversa e reduzir custo.

## Explicação

Parte do contexto é **fixa em toda execução**: system prompt, lista de skills, esquemas de ferramentas e arquivos de bootstrap do workspace. Quanto maior essa parte, menos espaço sobra e mais você paga a cada rodada. A página de custos cita estas chaves e seus padrões:

| Chave | Padrão | Efeito |
|---|---|---|
| `agents.defaults.bootstrapMaxChars` | `20000` | Teto de caracteres por arquivo de bootstrap injetado |
| `agents.defaults.bootstrapTotalMaxChars` | `60000` | Teto somado dos arquivos de bootstrap |
| `agents.defaults.imageMaxDimensionPx` | `1200` | Dimensão máxima de imagens enviadas ao modelo |

Arquivos grandes são truncados com um marcador (a cópia em disco fica intacta). Para ver o peso real de cada parte, use os comandos de inspeção:

```markdown
/context list
/context detail
/context map
```

`/context detail` acrescenta o tamanho por arquivo, por esquema de ferramenta e por entrada de skill; `/context map` gera um treemap. O medidor da Control UI chama a estimativa de **Prompt budget (last run)**; ultrapassá-la pode disparar redução de resultados de ferramentas ou compactação.

**Estratégia de enxugamento (por ordem de retorno):**

1. Reduza o que é fixo: encurte `AGENTS.md`, `SOUL.md` e descrições de skills; mantenha só o que o agente usa sempre.
2. Mova conteúdo de referência para notas buscáveis (memória) em vez de bootstrap.
3. Desligue skills e ferramentas que você não usa (ver [[MOC - Skills|Skills]]).
4. Reduza `imageMaxDimensionPx` em fluxos com muitas capturas de tela.
5. Compacte e pode (veja [[Poda de sessão e compactação]]).

Exemplo de ajuste, com validação:

```bash
openclaw config set agents.defaults.bootstrapMaxChars 12000
openclaw config set agents.defaults.imageMaxDimensionPx 1000
openclaw config validate
```

Os valores 12000 e 1000 são ilustrativos; escolha os seus a partir do que `/context detail` mostrar.

> [!tip] Meça antes
> Reduzir o teto não ajuda se o seu bootstrap já cabe com folga. Veja primeiro `/context list`.

## Exemplo prático

1. Rode `/context detail` e anote os três maiores contribuintes.
2. Enxugue o maior (por exemplo, divida um `AGENTS.md` de 18 mil caracteres: o essencial fica, o resto vira nota em `memory/`).
3. Rode `/context list` de novo e compare.

## Armadilhas comuns

- Cortar o teto sem ler o que está sendo truncado e perder instruções importantes.
- Deixar descrições de skills muito longas.
- Enviar imagens em resolução máxima sem necessidade.

## Resumo

- Contexto fixo (prompt, ferramentas, skills, bootstrap) é cobrado em toda rodada.
- Chaves: `bootstrapMaxChars` (20000), `bootstrapTotalMaxChars` (60000), `imageMaxDimensionPx` (1200).
- `/context list|detail|map` mostram o peso de cada parte.

## Relacionados

- [[Montagem de contexto e o comando context]]
- [[Arquivos do workspace do agente]]
- [[Poda de sessão e compactação]]
- [[Custo e escolha de modelo]]

## Exercícios

1. Quais partes do contexto são fixas em toda execução?
2. Quais são os padrões de `bootstrapMaxChars` e `bootstrapTotalMaxChars`?
3. Que comando detalha o tamanho por arquivo, ferramenta e skill?
4. Cite duas formas de reduzir o contexto fixo.
