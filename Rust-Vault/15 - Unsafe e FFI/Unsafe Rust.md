---
tags: [rust, unsafe]
aliases: ["unsafe", "unsafe block", "unsafe fn", "static mut", "union"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Raw pointers]]", "[[Traits unsafe]]", "[[Invariantes e boas práticas de unsafe]]", "[[Miri]]", "[[Send e Sync]]"]
---

# Unsafe Rust

`unsafe` **não desliga** o borrow checker nem os tipos. Ele libera apenas cinco operações que o compilador não consegue verificar; **você** garante que são válidas.

## As cinco "superpoderes"

1. Desreferenciar um **ponteiro cru** (`*const T`, `*mut T`).
2. Chamar uma função ou método `unsafe` (inclusive `extern`).
3. Acessar ou modificar uma variável `static mut`.
4. Implementar uma trait `unsafe` (`Send`, `Sync`...).
5. Acessar campos de uma `union`.

```rust
// ❌ NÃO COMPILA: desreferenciar ponteiro cru exige unsafe
fn main() {
    let x = 5;
    let p = &x as *const i32;
    println!("{}", *p);
}
```

```text
error[E0133]: dereference of raw pointer is unsafe and requires unsafe function or block
```

```rust
// unsafe fn: o chamador assume as obrigações descritas em # Safety
/// # Safety
///
/// `p` deve ser não nulo, alinhado e apontar para um `i32` válido e exclusivo.
unsafe fn dobra(p: *mut i32) {
    // Na edição 2024, operações unsafe dentro de uma unsafe fn exigem um bloco unsafe explícito
    unsafe {
        *p *= 2;
    }
}

union IntOuFloat {
    i: u32,
    f: f32,
}

static mut CONTADOR: u32 = 0;

fn main() {
    let mut n = 10;
    let p = &raw mut n; // ponteiro cru sem criar referência intermediária
    unsafe {
        dobra(p);
    }
    println!("{n}"); // 20

    let u = IntOuFloat { f: 1.0 };
    println!("{:#x}", unsafe { u.i }); // 0x3f800000: bits de 1.0f32

    unsafe {
        CONTADOR += 1;
        let valor = CONTADOR; // copia: não cria referência a static mut
        println!("{valor}");
    }
}
```

> [!warning] `static mut`
> Criar **referências** a `static mut` é negado por lint na edição 2024 (`static_mut_refs`). Prefira `AtomicU32`, `Mutex` em `static` ou `OnceLock`; veja [[Atômicos]] e [[LazyLock e OnceLock]].

> [!tip] Regra de ouro
> Mantenha blocos `unsafe` **pequenos**, com um comentário `// SAFETY:` explicando por que a operação é válida, e embrulhe-os em uma API **segura**; veja [[Invariantes e boas práticas de unsafe]].

> [!info] Comportamento indefinido (UB)
> Violar as regras (ponteiro inválido, data race, referências que se sobrepõem de forma proibida, valor inválido para um tipo) é UB: o programa pode "funcionar" hoje e falhar amanhã. Use [[Miri]] para detectar.

## Veja também

- [[Raw pointers]]
- [[Traits unsafe]]
- [[Invariantes e boas práticas de unsafe]]
- [[Miri]]
- [[Send e Sync]]
