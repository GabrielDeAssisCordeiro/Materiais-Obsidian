---
titulo: "Ferramentas de memória e busca"
tags:
  - openclaw
  - conceito
  - memoria
tipo: conceito
aliases: ['memory_search', 'memory_get', 'Busca híbrida']
nivel: avancado
fontes:
  - "[[Fontes]]"
  - "https://docs.openclaw.ai/concepts/memory"
  - "https://cdn.jsdelivr.net/npm/activeclaw@2026.4.9/docs/concepts/memory.md"
relacionados:
  - "[[Arquivos de memória em Markdown]]"
  - "[[Boas práticas de memória e janela de contexto]]"
  - "[[Uso de ferramentas e tool calling]]"
  - "[[Memória e contexto em agentes]]"
---

# Ferramentas de memória e busca

## Objetivo

Conhecer as ferramentas pelas quais o agente consulta a memória e as opções de busca, sabendo o que está confirmado e o que vem de uma cópia antiga da documentação.

## Explicação

**Confirmado na página atual:** as ferramentas `memory_search` e `memory_get` indexam e recuperam as notas diárias. A página as nomeia, mas não descreve seus parâmetros. O menu da documentação lista ainda: **Builtin memory engine**, **Honcho memory**, **Memory LanceDB**, **Memory wiki**, **Active memory**, "Memory search" e a "Memory configuration reference". Essas páginas **não foram lidas** nesta sessão.

> [!warning] Detalhes abaixo vêm de uma cópia antiga
> Os itens a seguir vêm de uma cópia da documentação em um pacote de terceiros de **abril de 2026** (`activeclaw@2026.4.9`), anterior às versões atuais (`2026.10.x`). Tratam-se como pista, não como referência. Confirme em `docs.openclaw.ai/reference/memory-config` com o seu `openclaw config schema`.

**Na cópia antiga:**

- `memory_search`: recuperação semântica sobre trechos indexados. `memory_get`: leitura pontual de arquivo ou faixa de linhas; para arquivo inexistente devolve `{ text: "", path }` em vez de erro.
- As ferramentas vêm do plugin de memória ativo (padrão `memory-core`); desativa-se com `plugins.slots.memory = "none"`.
- Busca vetorial em `agents.defaults.memorySearch`, indexando `MEMORY.md` e `memory/**/*.md`, com observador de arquivos que marca o índice como sujo. Escolha automática de provedor de embeddings: `local` (se houver `local.modelPath`), `openai`, `gemini`, `voyage`, `mistral`; `ollama` só se configurado explicitamente.
- **Busca híbrida** (`query.hybrid`) combina pontuação vetorial e BM25 (`vectorWeight`, `textWeight`, `candidateMultiplier`), com etapas opcionais, desligadas por padrão: MMR (diversidade) e decaimento temporal (recência).
- Um backend experimental (QMD) podia substituir a recuperação, com retorno ao gerenciador SQLite embutido em caso de falha.

```mermaid
flowchart LR
  Q["Pergunta do agente"] --> S["memory_search"]
  S --> V["Vetorial"]
  S --> B["BM25 (texto)"]
  V --> H["Combinação híbrida"]
  B --> H
  H --> T["Trechos para o contexto"]
  T --> G["memory_get: ler arquivo ou linhas"]
```

**O que isso significa na prática.** A busca semântica envia trechos da sua memória a um provedor de embeddings, se o provedor for remoto. Se a privacidade importa, prefira um embedding local ou confira para onde vão os trechos (veja [[Memória como superfície de ataque e privacidade]]).

## Exemplo prático

Peça ao agente algo que só está na memória e observe se ele usa a ferramenta:

```markdown
Qual foi a decisão que tomamos sobre o servidor de backup? Procure na memória.
```

Nos registros (`openclaw logs --follow`) confirme a chamada de `memory_search`. Se o agente não achar, verifique se o assunto está em `MEMORY.md` ou em `memory/` e se o índice está atualizado.

## Armadilhas comuns

- Assumir que a busca é determinística: é aproximada.
- Esperar que a memória "lembre" sem ter sido gravada em arquivo.
- Mandar a memória inteira a um provedor de embeddings remoto sem avaliar o risco.

## Resumo

- `memory_search` (recuperação) e `memory_get` (leitura pontual) são as ferramentas nomeadas.
- Há várias engines e plugins de memória na documentação; confirme na sua versão.
- Busca híbrida (vetor + BM25) e provedores de embeddings vêm de uma cópia antiga: valide.

## Relacionados

- [[Arquivos de memória em Markdown]]
- [[Boas práticas de memória e janela de contexto]]
- [[Uso de ferramentas e tool calling]]
- [[Memória como superfície de ataque e privacidade]]

## Exercícios

1. Quais ferramentas o agente usa para consultar a memória?
2. O que significa "busca híbrida"?
3. Por que as chaves de `memorySearch` devem ser confirmadas na sua versão?
4. Que risco de privacidade existe com embeddings remotos?
