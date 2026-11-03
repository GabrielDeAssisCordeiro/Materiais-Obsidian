---
tags: [rust, crates, referencia]
aliases: ["crates populares", "ecossistema Rust"]
tipo: referencia
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Escolhendo e avaliando crates]]", "[[serde e serde_json]]", "[[Tokio]]"]
---

# Outros crates úteis

| Categoria | Crate | Para quê |
|---|---|---|
| Erros | `anyhow`, `thiserror` | ver [[thiserror e anyhow]] |
| Async | `tokio`, `futures`, `async-trait` | ver [[Tokio]] |
| Concorrência | `rayon`, `crossbeam`, `parking_lot`, `dashmap` | ver [[Rayon]], [[Crossbeam]] |
| Serialização | `serde`, `bincode`, `toml`, `serde_yaml` | formatos de dados |
| HTTP/Web | `hyper`, `tower`, `tower-http`, `tonic` (gRPC) | infraestrutura de rede |
| Bytes e buffers | `bytes`, `byteorder` | protocolos binários |
| IDs | `uuid`, `ulid` | identificadores únicos |
| Terminal | `indicatif`, `colored`, `dialoguer`, `crossterm` | barras de progresso, cores, prompts |
| Arquivos | `walkdir`, `ignore`, `tempfile`, `notify` | percorrer, temporários, observar mudanças |
| Parsing | `nom`, `pest`, `winnow`, `logos` | analisadores sintáticos |
| Compressão e hash | `flate2`, `zstd`, `sha2`, `blake3` | |
| Criptografia | `ring`, `rustls`, `RustCrypto` | **use bibliotecas auditadas; não invente criptografia** |
| Testes | `proptest`, `criterion`, `mockall`, `insta` (snapshots), `assert_cmd` | ver [[MOC - Testes e Qualidade]] |
| Macros | `syn`, `quote`, `proc-macro2` | ver [[syn e quote]] |
| FFI | `libc`, `bindgen`, `cxx`, `pyo3` | ver [[FFI com C e C++]] |
| WebAssembly | `wasm-bindgen`, `web-sys`, `js-sys` | ver [[WebAssembly]] |

> [!tip] Onde descobrir
> **blessed.rs**, **lib.rs** e as categorias do **crates.io** são bons pontos de partida.

## Veja também

- [[Escolhendo e avaliando crates]]
- [[serde e serde_json]]
- [[Tokio]]
