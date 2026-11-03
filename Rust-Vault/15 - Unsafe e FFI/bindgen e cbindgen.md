---
tags: [rust, unsafe, ffi, crates]
aliases: ["bindgen", "cbindgen", "gerar bindings"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[FFI com C e C++]]", "[[build.rs]]", "[[cxx e PyO3]]"]
---

# bindgen e cbindgen

| Ferramenta | Direção | O que gera |
|---|---|---|
| **bindgen** | C/C++ → Rust | declarações Rust (`extern`, structs `repr(C)`) a partir de cabeçalhos `.h` |
| **cbindgen** | Rust → C/C++ | cabeçalho `.h` a partir do código Rust com `extern "C"` |

## bindgen no `build.rs`

```toml
[build-dependencies]
bindgen = "0.71"
```

```rust
// requer crate: bindgen
// build.rs
use std::{env, path::PathBuf};

fn main() {
    println!("cargo::rerun-if-changed=wrapper.h");

    let bindings = bindgen::Builder::default()
        .header("wrapper.h") // inclui os cabeçalhos desejados
        .parse_callbacks(Box::new(bindgen::CargoCallbacks::new()))
        .generate()
        .expect("falha ao gerar bindings");

    let saida = PathBuf::from(env::var("OUT_DIR").unwrap());
    bindings.write_to_file(saida.join("bindings.rs")).unwrap();
}
```

```rust
// trecho: src/lib.rs (inclui o arquivo gerado)
#![allow(non_upper_case_globals, non_camel_case_types, non_snake_case)]
include!(concat!(env!("OUT_DIR"), "/bindings.rs"));
```

## cbindgen

```bash
cargo install cbindgen
cbindgen --lang c --crate meu_crate --output meu_crate.h
```

```toml
# cbindgen.toml
language = "C"
include_guard = "MEU_CRATE_H"
```

> [!question] Verificar na documentação oficial
> Confirme versões e a API do `bindgen` (`CargoCallbacks`) em docs.rs/bindgen e rust-lang.github.io/rust-bindgen.

> [!tip] Padrão `-sys`
> Por convenção, o crate com os bindings crus se chama `libfoo-sys`; um segundo crate `libfoo` oferece a API **segura** por cima.

## Veja também

- [[FFI com C e C++]]
- [[build.rs]]
- [[cxx e PyO3]]
