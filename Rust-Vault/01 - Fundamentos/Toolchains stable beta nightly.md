---
tags: [rust, fundamentos, rustup]
aliases: ["Canais de lançamento", "stable", "nightly"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Instalação com rustup]]", "[[História do Rust]]", "[[Edições do Rust]]"]
---

# Toolchains stable beta nightly

Rust publica em três **canais**:

| Canal | Frequência | Uso |
|---|---|---|
| `stable` | A cada 6 semanas | Produção; recomendado |
| `beta` | Candidata à próxima stable | Testar se seu código quebra em CI |
| `nightly` | Todas as noites | Recursos instáveis (`#![feature(...)]`), Miri, ferramentas experimentais |

```mermaid
graph LR
    N[nightly] -->|6 semanas| B[beta] -->|6 semanas| S[stable]
```

## Trocando de toolchain

```bash
# Roda um comando com outra toolchain sem trocar o padrão
cargo +nightly build

# Fixa a toolchain de um projeto: crie rust-toolchain.toml na raiz
```

```toml
# rust-toolchain.toml
[toolchain]
channel = "stable"
components = ["rustfmt", "clippy"]
```

> [!warning] Nightly em produção
> Recursos `#![feature]` podem mudar ou sumir. Use nightly só quando precisar (Miri, benchmarks internos, experimentos).

## Veja também

- [[Instalação com rustup]]
- [[História do Rust]]
- [[Edições do Rust]]
