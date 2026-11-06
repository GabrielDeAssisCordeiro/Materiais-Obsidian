---
titulo: "Trilha de aprendizado - Assembly"
aliases: []
tags:
  - assembly
  - guia
tipo: guia
nivel: iniciante
criado: 2026-11-04
relacionados:
  - "[[Home - Assembly]]"
  - "[[Índice - Assembly]]"
---

# Trilha de aprendizado - Assembly

Ordem sugerida de estudo do curso de Assembly, do básico ao avançado, e os destinos possíveis depois dele. Os módulos estão listados no [[Índice - Assembly]].

## Roadmap visual

```mermaid
flowchart TD
    A["00 - Índice e Ambiente"] --> B["01 - Fundamentos"]
    B --> C["02 - Registradores e Memória"]
    C --> D["03 - Instruções e Fluxo"]
    D --> E["04 - Stack e Calling Conventions"]
    E --> F["05 - E/S e System Calls"]
    E --> G["06 - Estruturas de Dados"]
    F --> H["07 - Assembly Avançado"]
    G --> H
    H --> I["08 - ARM e AArch64"]
    H --> J["09 - Otimização e SIMD"]
    I --> K["10 - Laboratórios e Projeto Final"]
    J --> K
    K --> L["11 - Recursos e Continuidade"]
    L --> M["Reverse Engineering"]
    L --> N["Desenvolvimento de SO"]
    L --> O["Embedded e Firmware"]
    L --> P["Compiladores e JIT"]

    classDef basico fill:#d4edda,stroke:#28a745,color:#000
    classDef inter fill:#fff3cd,stroke:#e0a800,color:#000
    classDef avanc fill:#f8d7da,stroke:#dc3545,color:#000
    classDef destino fill:#d1ecf1,stroke:#17a2b8,color:#000
    class A,B,C,D basico
    class E,F,G inter
    class H,I,J,K avanc
    class L,M,N,O,P destino
```

**Legenda:** verde = básico, amarelo = intermediário, vermelho = avançado, azul = destinos após o curso.

> [!note] Trilhas alternativas
> - **Foco em Reverse Engineering:** 01 → 02 → 03 → 04 → 05 → 07 (inline/PIC/exceções) → 11.
> - **Foco em performance:** 01 → 04 → 06 → 07 → 09.
> - **Foco em mobile/embarcado (ARM):** 01 → 02 → 03 → 04 → 08, comparando sempre com x64.

## Veja também

- [[Home - Assembly]]
- [[Índice - Assembly]]
- [[Glossário#Assembly (x86-64 e ARM)]]
