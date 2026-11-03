---
tags: [rust, fundamentos, compilador]
aliases: ["Como o rustc compila", "MIR", "LLVM"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Edições do Rust]]"]
---

# Pipeline de compilação

O `rustc` transforma o código em um executável por várias etapas:

```mermaid
graph LR
    A[Código-fonte .rs] --> B[Parsing / AST]
    B --> C[Expansão de macros]
    C --> D[HIR]
    D --> E[Checagem de tipos e traits]
    E --> F[MIR]
    F --> G[Borrow checker]
    G --> H[Monomorfização + otimizações]
    H --> I[LLVM IR]
    I --> J[Código de máquina]
```

| Etapa | O que acontece |
|---|---|
| Expansão de macros | `macro_rules!` e macros procedurais são expandidas |
| Tipos e traits | Inferência de tipos e resolução de traits |
| MIR | Representação intermediária usada pelo borrow checker |
| Monomorfização | Cada uso de genérico gera uma versão especializada (zero-cost) |
| LLVM | Otimizações finais e geração de código nativo |

> [!info] cargo check
> O `cargo check` executa as etapas até a checagem, sem gerar código de máquina, por isso é bem mais rápido.

> [!tip] Tempo de compilação
> A monomorfização e o LLVM são as partes mais caras; perfis `dev` usam menos otimização para compilar rápido.

## Veja também

- [[Cargo básico]]
- [[Edições do Rust]]
