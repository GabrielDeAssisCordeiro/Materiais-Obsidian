---
tags: [rust, unsafe, ffi, crates, python]
aliases: ["cxx", "PyO3", "maturin", "Python"]
tipo: ferramenta
nivel: avancado
criado: 2026-10-24
relacionados: ["[[FFI com C e C++]]", "[[bindgen e cbindgen]]", "[[Ciência de dados com Rust]]"]
---

# cxx e PyO3

## `cxx`: Rust ↔ C++ seguro

O crate **cxx** define a fronteira em um módulo `#[cxx::bridge]` e gera os dois lados, verificando tipos de ambos os lados.

```rust
// requer crate: cxx
#[cxx::bridge]
mod ffi {
    // Tipos compartilhados (layout idêntico dos dois lados)
    struct Config {
        nome: String,
        tentativas: u32,
    }

    extern "Rust" {
        fn processa(c: &Config) -> usize;
    }

    unsafe extern "C++" {
        include!("meu_projeto/include/cliente.h");
        type ClienteHttp;
        fn novo_cliente() -> UniquePtr<ClienteHttp>;
        fn busca(self: &ClienteHttp, url: &str) -> String;
    }
}

fn processa(c: &ffi::Config) -> usize {
    c.nome.len() + c.tentativas as usize
}
```

## PyO3: módulos Python em Rust

```toml
[lib]
name = "meu_modulo"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.24", features = ["extension-module"] }
```

```rust
// requer crate: pyo3
use pyo3::prelude::*;

/// Soma dois números (exposta ao Python).
#[pyfunction]
fn soma(a: u64, b: u64) -> PyResult<u64> {
    Ok(a + b)
}

#[pymodule]
fn meu_modulo(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(soma, m)?)?;
    Ok(())
}
```

```bash
pip install maturin
maturin develop --release     # compila e instala no virtualenv atual
python -c "import meu_modulo; print(meu_modulo.soma(2, 3))"
```

> [!question] Verificar na documentação oficial
> Tanto `cxx` quanto `PyO3` evoluem rapidamente (por exemplo, a API `Bound` do PyO3 e novas formas de declarar módulos). Confirme em cxx.rs e pyo3.rs.

| Ferramenta | Alvo | Ponto forte |
|---|---|---|
| `bindgen` | C/C++ (cabeçalhos) | automático, mas `unsafe` |
| `cxx` | C++ | tipos seguros e sem `unsafe` na maior parte |
| `PyO3` + `maturin` | Python | acelerar gargalos de Python com Rust |

## Veja também

- [[FFI com C e C++]]
- [[bindgen e cbindgen]]
- [[Ciência de dados com Rust]]
