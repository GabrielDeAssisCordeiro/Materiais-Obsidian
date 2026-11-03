---
tags: [rust, unsafe, ffi]
aliases: ["FFI", "extern \"C\"", "repr(C)", "CString", "CStr", "no_mangle", "cdylib"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Unsafe Rust]]", "[[bindgen e cbindgen]]", "[[cxx e PyO3]]", "[[build.rs]]"]
---

# FFI com C e C++

**FFI** (*Foreign Function Interface*) permite chamar código C (ou compatível com a ABI C) a partir de Rust e vice-versa.

## Chamando C a partir de Rust

Na edição 2024, blocos `extern` devem ser declarados `unsafe extern`; funções comprovadamente seguras podem ser marcadas `safe`.

```rust
use std::ffi::{c_char, c_int, CStr, CString};

unsafe extern "C" {
    // A libc já é ligada pelo Rust na maioria das plataformas
    safe fn abs(x: c_int) -> c_int;          // seguro chamar sem unsafe
    fn strlen(s: *const c_char) -> usize;    // exige unsafe
}

fn main() {
    println!("{}", abs(-5));

    // Strings C são terminadas em NUL: use CString (Rust -> C) e CStr (C -> Rust)
    let c = CString::new("olá").unwrap();
    let n = unsafe { strlen(c.as_ptr()) };
    println!("{n} bytes"); // 5 (á ocupa 2 bytes em UTF-8)

    let volta: &CStr = c.as_c_str();
    println!("{}", volta.to_str().unwrap());
}
```

## Expondo Rust para C

```rust
// `unsafe(no_mangle)` é a sintaxe exigida na edição 2024
#[unsafe(no_mangle)]
pub extern "C" fn soma_c(a: i32, b: i32) -> i32 {
    a + b
}

// repr(C) garante o layout compatível com C
#[repr(C)]
pub struct Ponto {
    pub x: f64,
    pub y: f64,
}

#[unsafe(no_mangle)]
pub extern "C" fn norma(p: Ponto) -> f64 {
    (p.x * p.x + p.y * p.y).sqrt()
}

// Callbacks: ponteiros de função extern "C"
pub extern "C" fn dobra(x: i32) -> i32 {
    x * 2
}

pub fn aplica(f: extern "C" fn(i32) -> i32, v: i32) -> i32 {
    f(v)
}
```

```toml
[lib]
crate-type = ["cdylib"]     # biblioteca dinâmica para C (ou "staticlib")
```

```c
/* cabeçalho C correspondente */
typedef struct { double x; double y; } Ponto;
int soma_c(int a, int b);
double norma(Ponto p);
```

## Regras de ouro

| Regra | Motivo |
|---|---|
| Use tipos `repr(C)` e primitivos C (`c_int`, `c_char`, `*const T`) na fronteira | layout estável |
| Não deixe **panics** cruzarem a fronteira | UB; use `std::panic::catch_unwind` ou retorne códigos de erro |
| Documente quem **libera** a memória (C ou Rust) | evita double free e vazamentos |
| `Box::into_raw` / `Box::from_raw` para entregar/receber objetos | mantém a desalocação no lado que alocou |
| Valide ponteiros e comprimentos recebidos | C não oferece garantias |

> [!warning] Alocador
> Memória alocada por `malloc` deve ser liberada por `free`; a alocada pelo Rust, pelo Rust. Misturar é UB.

## Veja também

- [[Unsafe Rust]]
- [[bindgen e cbindgen]]
- [[cxx e PyO3]]
- [[build.rs]]
