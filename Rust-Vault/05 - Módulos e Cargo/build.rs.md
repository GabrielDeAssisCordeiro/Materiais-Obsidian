---
tags: [rust, cargo]
aliases: ["build.rs", "script de build", "OUT_DIR", "cargo::rerun-if-changed"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Cargo.toml e dependências]]", "[[Features de Cargo]]", "[[Targets e cross-compilation]]"]
---

# build.rs

`build.rs` na raiz do package é um **programa Rust executado antes da compilação** do crate. Serve para gerar código, compilar C/C++, procurar bibliotecas do sistema e embutir informações de build.

```rust
// build.rs
use std::env;

fn main() {
    // Só reexecuta se este arquivo mudar (evita rebuilds desnecessários)
    println!("cargo::rerun-if-changed=build.rs");

    // Injeta uma variável de ambiente acessível via env!() no código
    println!("cargo::rustc-env=PERFIL_BUILD={}", env::var("PROFILE").unwrap_or_default());

    // Diretório de saída para arquivos gerados
    let saida = env::var("OUT_DIR").unwrap_or_default();
    println!("saída em {saida}");
}
```

```rust
// trecho: src/main.rs (usa a variável definida pelo build.rs)
fn main() {
    println!("perfil: {}", env!("PERFIL_BUILD"));
}
```

| Diretiva `cargo::` | Efeito |
|---|---|
| `rerun-if-changed=ARQ` | reexecuta se o arquivo mudar |
| `rerun-if-env-changed=VAR` | reexecuta se a variável mudar |
| `rustc-link-lib=nome` | liga com uma biblioteca |
| `rustc-link-search=DIR` | caminho de busca de bibliotecas |
| `rustc-env=CHAVE=VALOR` | variável para `env!` |
| `rustc-cfg=flag` | habilita `#[cfg(flag)]` |

> [!question] Verificar na documentação oficial
> A sintaxe `cargo::` (com dois dois-pontos) exige Rust recente; versões antigas usavam `cargo:`. Confirme no Cargo Book.

## Usos comuns

- Compilar C/C++ com o crate **`cc`**.
- Gerar bindings com **`bindgen`** (veja [[FFI com C e C++]]).
- Compilar arquivos `.proto` (`prost-build`, `tonic-build`).
- Embutir hash do Git e data da build.

> [!warning] Use com moderação
> `build.rs` aumenta o tempo de compilação e a complexidade. Evite-o se uma macro ou `const` resolver.

## Veja também

- [[Cargo.toml e dependências]]
- [[Features de Cargo]]
- [[Targets e cross-compilation]]
