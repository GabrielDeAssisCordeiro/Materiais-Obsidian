---
titulo: "MOC — Classes e POO"
tags: [cpp, moc, poo, classes]
aliases: ["MOC Classes e POO", "Programação Orientada a Objetos"]
tipo: moc
nivel: iniciante
padrao: C++11
criado: 2026-10-24
relacionados: ["[[Home - Cpp]]", "[[MOC - Ponteiros e Memória]]"]
---

# MOC — Classes e POO

Como definir tipos próprios, proteger invariantes e modelar relações com herança e polimorfismo.

## Fundamentos de classes

- [[Classes e Structs]]
- [[Construtores e Destrutores]]
- [[Lista de Inicialização]]
- [[this e Membros Estáticos]]
- [[const em Métodos]]
- [[Encapsulamento e friend]]

## Herança e polimorfismo

- [[Herança]]
- [[Polimorfismo e Funções Virtuais]]
- [[Classes Abstratas e Interfaces]]
- [[override e final]]
- [[Herança Múltipla e Virtual]]
- [[vtable]]
- [[Slicing]]

## Tipos que se comportam como nativos

- [[Sobrecarga de Operadores - Cpp]]
- [[Conversões Implícitas e explicit]]
- [[default e delete]]

## Próximo passo

As funções membro especiais e o gerenciamento de recursos (RAII, Regra do 0/3/5, movimento) continuam na seção seguinte da trilha.

## Ordem de leitura sugerida

```mermaid
flowchart LR
    A[Classes e Structs] --> B[Construtores e Destrutores]
    B --> C[Lista de Inicialização]
    C --> D[const em Métodos]
    D --> E[Encapsulamento e friend]
    E --> F[Herança]
    F --> G[Polimorfismo e Funções Virtuais]
    G --> H[override e final]
    H --> I[vtable]
    I --> J[Sobrecarga de Operadores]
    J --> K[default e delete]
```

## Veja também

- [[Home - Cpp]]
- [[MOC - Ponteiros e Memória]]
- [[MOC - Básico da Linguagem - Cpp]]
