---
tags: [markdown, diagramas]
aliases: [Mermaid, Fluxogramas]
tipo: referencia
nivel: intermediario
criado: 2026-10-23
relacionados: ["[[Blocos de código]]", "[[Canvas]]", "[[Sintaxe estendida]]"]
---

# Diagramas Mermaid

Escreva diagramas como texto dentro de um bloco `mermaid`.

## Fluxograma
````markdown
```mermaid
flowchart LR
  A[Captura] --> B[Processamento]
  B --> C[Conexão]
  C --> D[Saída]
```
````

## Sequência
````markdown
```mermaid
sequenceDiagram
  Usuário->>Obsidian: Abre nota
  Obsidian-->>Usuário: Renderiza
```
````

## Outros tipos
`classDiagram`, `stateDiagram-v2`, `gantt`, `pie`, `erDiagram`, `mindmap`, `timeline`.

> [!info] Links internos
> Em diagramas Mermaid, nós podem receber a classe `internal-link` para apontar para notas.
>
> > [!question] Verificar na documentação oficial
> > Confirme a sintaxe atual de links internos em Mermaid na documentação do Obsidian.

## Mermaid × Canvas
Mermaid é texto versionável e rápido; [[Canvas]] é visual e livre. Escolha conforme o objetivo.

## Veja também
- [[Blocos de código]]
- [[Excalidraw]]

## Exercício
Desenhe seu fluxo de [[Captura, processamento, conexão e saída]] em um fluxograma Mermaid.
