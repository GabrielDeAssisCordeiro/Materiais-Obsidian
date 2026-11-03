---
titulo: "MOC — Módulos e Organização"
tags: [cpp, moc, organizacao, modulos]
aliases: ["MOC Módulos e Organização", "Módulos e Organização"]
tipo: moc
nivel: intermediario
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Strings e IO]]", "[[MOC - Templates e Concepts]]"]
---

# MOC — Módulos e Organização

Como dividir um programa em arquivos, o que o compilador e o linker fazem com eles, e como empacotar o resultado.

```mermaid
flowchart LR
    H[Headers vs Sources] --> G[Include Guards]
    H --> D[Declaração vs Definição / ODR]
    D --> L[Linkage]
    H --> F[Forward Declarations]
    G --> P[Pré-processador]
    P --> M[Módulos C++20]
    L --> B[Bibliotecas]
    B --> A[ABI]
    B --> E[Estrutura de Projetos]
```

## Notas

- [[Headers vs Sources]]
- [[Include Guards e pragma once]]
- [[Declaração vs Definição e ODR]]
- [[Linkage]]
- [[Forward Declarations]]
- [[Pré-processador e Macros]]
- [[Módulos Cpp20]]
- [[Estrutura de Projetos]]
- [[Bibliotecas Estáticas e Dinâmicas]]
- [[ABI]]

## Ordem sugerida

[[Headers vs Sources]] → [[Include Guards e pragma once]] → [[Declaração vs Definição e ODR]] → [[Linkage]] → [[Forward Declarations]] → [[Pré-processador e Macros]] → [[Estrutura de Projetos]] → [[Bibliotecas Estáticas e Dinâmicas]] → [[ABI]] → [[Módulos Cpp20]]

## Veja também

- [[Home - Cpp]]
- [[MOC - Strings e IO]]
- [[MOC - Templates e Concepts]]
- [[Pipeline de Compilação - Cpp]]
