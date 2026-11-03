---
tags: [rust, cargo, rustup]
aliases: ["rustup target", "musl"]
tipo: procedimento
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Instalação com rustup]]", "[[Debug vs release]]", "[[build.rs]]"]
---

# Targets e cross-compilation

Um **target** é identificado por um *triple* (`arquitetura-fornecedor-sistema[-ABI]`), por exemplo `x86_64-unknown-linux-gnu` ou `aarch64-apple-darwin`.

```bash
rustc --print target-list | head       # lista todos os targets conhecidos
rustup target list --installed         # os instalados
rustup target add x86_64-unknown-linux-musl
rustup target add wasm32-unknown-unknown
rustup target add aarch64-unknown-linux-gnu

cargo build --release --target x86_64-unknown-linux-musl   # binário estático
```

## Linker para outro sistema

```toml
# .cargo/config.toml
[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"

[build]
# target = "x86_64-unknown-linux-musl"   # alvo padrão do projeto
```

## Ferramentas que simplificam

| Ferramenta | Como ajuda |
|---|---|
| `cross` | usa contêineres Docker com toolchains prontos |
| `cargo-zigbuild` | usa o `zig cc` como linker |
| `cargo-dist` | empacota e distribui binários por plataforma |

> [!info] Alvos comuns
> `wasm32-unknown-unknown` (WebAssembly), `thumbv7em-none-eabihf` (microcontroladores ARM Cortex-M, `no_std`), `x86_64-pc-windows-gnu` (Windows via MinGW).

> [!tip] Código condicional
> Use `#[cfg(target_os = "linux")]`, `#[cfg(target_arch = "wasm32")]` e `cfg!(...)` para separar código por plataforma.

## Veja também

- [[Instalação com rustup]]
- [[Debug vs release]]
- [[build.rs]]
