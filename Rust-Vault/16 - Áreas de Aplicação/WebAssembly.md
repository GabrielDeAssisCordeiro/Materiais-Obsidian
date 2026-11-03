---
tags: [rust, areas, web]
aliases: ["wasm-pack", "wasm32"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Targets e cross-compilation]]", "[[FFI com C e C++]]", "[[tauri]]", "[[Áreas de Aplicação]]"]
---

# WebAssembly

**WebAssembly (Wasm)** é um formato binário portátil que roda no navegador, no *edge* e em runtimes como Wasmtime. Rust é a linguagem mais popular para gerá-lo: sem GC, binários pequenos e boa integração com JavaScript.

## Alvos

| Target | Uso |
|---|---|
| `wasm32-unknown-unknown` | navegador (com `wasm-bindgen`) |
| `wasm32-wasip1` | WASI: fora do navegador, com acesso a arquivos/rede controlados |

```bash
rustup target add wasm32-unknown-unknown
cargo install wasm-pack
wasm-pack build --target web
```

## Exportando uma função para JavaScript

```toml
[lib]
crate-type = ["cdylib"]

[dependencies]
wasm-bindgen = "0.2"
```

```rust
// requer crate: wasm-bindgen
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn fibonacci(n: u32) -> u64 {
    let (mut a, mut b) = (0u64, 1u64);
    for _ in 0..n {
        (a, b) = (b, a + b);
    }
    a
}

#[wasm_bindgen]
extern "C" {
    // importa window.alert do JavaScript
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn saudar(nome: &str) {
    alert(&format!("Olá, {nome}!"));
}
```

```javascript
import init, { fibonacci } from "./pkg/meu_wasm.js";
await init();
console.log(fibonacci(50)); // BigInt: 12586269025n
```

## Dicas

- Reduza o tamanho: `opt-level = "z"`, `lto = true`, `wasm-opt -Oz`.
- Fronteira JS↔Wasm tem custo: passe **blocos de dados**, não muitas chamadas pequenas.
- Frameworks de UI em Rust compilados para Wasm: Yew, Leptos, Dioxus.
- Fora do navegador: Wasmtime e Wasmer executam módulos WASI (plugins seguros, funções no edge).

> [!question] Verificar na documentação oficial
> Os nomes dos targets WASI mudaram (`wasm32-wasi` → `wasm32-wasip1`/`wasip2`). Confirme em doc.rust-lang.org/rustc/platform-support.html e rustwasm.github.io.

## Veja também

- [[Targets e cross-compilation]]
- [[FFI com C e C++]]
- [[tauri]]
- [[Áreas de Aplicação]]
