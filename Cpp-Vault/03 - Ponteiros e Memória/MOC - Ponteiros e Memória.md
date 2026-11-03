---
titulo: "MOC — Ponteiros e Memória"
tags: [cpp, moc, memoria]
aliases: ["MOC Ponteiros e Memória", "Memória em C++"]
tipo: moc
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Básico da Linguagem - Cpp]]"]
---

# MOC — Ponteiros e Memória

Como o C++ acessa, organiza e gerencia memória. É o terreno onde moram a maior parte dos bugs graves — e onde o C++ moderno oferece as melhores defesas.

## Ponteiros e referências

- [[Ponteiros]]
- [[Aritmética de Ponteiros]]
- [[Referências - Cpp]]
- [[Lvalue e Rvalue]]
- [[nullptr]]

## Memória dinâmica

- [[Stack vs Heap]]
- [[new e delete]]
- [[Vazamentos e Dangling Pointers]]

## Organização e layout

- [[Layout de Memória de um Programa]]
- [[sizeof e alignof]]
- [[Alocadores Introdução]]

## Conexões com outras seções

- Escopo e duração de armazenamento: [[Escopo e Duração de Armazenamento]]
- Arrays e decay: [[Arrays e std array]]
- Comportamento indefinido: [[Comportamento Indefinido e Não Especificado]]

## Ordem de leitura sugerida

```mermaid
flowchart LR
    A[Ponteiros] --> B[Referências]
    B --> C[Lvalue e Rvalue]
    A --> D[Aritmética de Ponteiros]
    D --> E[Stack vs Heap]
    E --> F[new e delete]
    F --> G[Vazamentos e Dangling Pointers]
    G --> H[Layout de Memória de um Programa]
    H --> I[sizeof e alignof]
    I --> J[Alocadores Introdução]
```

## Veja também

- [[Home - Cpp]]
- [[MOC - Básico da Linguagem - Cpp]]
