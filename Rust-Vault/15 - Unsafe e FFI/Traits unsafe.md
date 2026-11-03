---
tags: [rust, unsafe, traits]
aliases: ["unsafe trait", "unsafe impl"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Unsafe Rust]]", "[[Send e Sync]]", "[[Traits]]"]
---

# Traits unsafe

Uma trait é `unsafe` quando implementá-la incorretamente pode causar UB; quem a implementa assume um **contrato que o compilador não verifica**.

```rust
/// # Safety
///
/// Implementadores devem garantir que o padrão de bits "tudo zero" é um valor válido do tipo.
unsafe trait Zerado: Sized {
    fn zero() -> Self {
        // SAFETY: garantido pelo contrato da trait
        unsafe { std::mem::zeroed() }
    }
}

// O implementador assume a responsabilidade com `unsafe impl`
unsafe impl Zerado for u32 {}
unsafe impl Zerado for f64 {}

// Exemplo clássico: um tipo com ponteiro cru que é seguro entre threads por construção
struct Handle(*mut u8);

// SAFETY: o ponteiro é usado só por uma thread por vez (garantido pela API do tipo)
unsafe impl Send for Handle {}

fn main() {
    println!("{} {}", u32::zero(), f64::zero());
    let _h = Handle(std::ptr::null_mut());
}
```

- `Send` e `Sync` são `unsafe trait` porque o compilador as deriva automaticamente, mas ponteiros crus e FFI desativam essa dedução.
- Pessoas usam `unsafe trait` quando a **correção de outro código `unsafe`** depende da trait (ex.: `GlobalAlloc`, `bytemuck::Pod`).

> [!tip] Quando criar uma
> Se o seu código `unsafe` genérico precisa confiar em uma propriedade que o sistema de tipos não expressa, uma `unsafe trait` documentada é a forma correta de registrar essa obrigação.

## Veja também

- [[Unsafe Rust]]
- [[Send e Sync]]
- [[Traits]]
