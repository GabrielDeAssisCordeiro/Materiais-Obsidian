---
tags: [rust, fundamentos]
aliases: ["Linha do tempo do Rust"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[O que é Rust]]", "[[Edições do Rust]]", "[[Toolchains stable beta nightly]]"]
---

# História do Rust

| Ano | Marco |
|---|---|
| 2006 | Graydon Hoare começa Rust como projeto pessoal |
| 2009 | A Mozilla passa a patrocinar o projeto |
| 2015 | **Rust 1.0**: promessa de estabilidade e compatibilidade retroativa |
| 2018 | Edição 2018 (módulos simplificados, `async` reservado) |
| 2018 | NLL (non-lexical lifetimes) entra na edição 2018 |
| 2019 | `async/await` estável (Rust 1.39) |
| 2021 | Edição 2021; criação da Rust Foundation |
| 2022 | Rust é aceito no kernel Linux (a partir do Linux 6.1) |
| 2025 | Edição 2024 (Rust 1.85) |

## Modelo de lançamento

O Rust lança uma versão estável a cada **6 semanas**, seguindo o modelo de trens (*release train*): `nightly` → `beta` → `stable`. Detalhes em [[Toolchains stable beta nightly]].

> [!tip] Estabilidade
> "Stability without stagnation": o compilador novo compila código antigo. Mudanças que quebrariam código só entram por [[Edições do Rust|edições]], e cada crate escolhe a sua.

## Veja também

- [[O que é Rust]]
- [[Edições do Rust]]
- [[Toolchains stable beta nightly]]
