---
tags: [rust, unsafe, ponteiros]
aliases: ["*const T", "*mut T", "ponteiros crus", "NonNull", "Box::into_raw"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Unsafe Rust]]", "[[Box]]", "[[Invariantes e boas práticas de unsafe]]"]
---

# Raw pointers

Ponteiros crus (`*const T` e `*mut T`) não têm garantias: podem ser nulos, pendentes ou desalinhados, e não seguem as regras de empréstimo. **Criá-los é seguro; desreferenciá-los não é.**

```rust
use std::ptr;

fn main() {
    let mut a = [1, 2, 3, 4];
    let p = a.as_mut_ptr(); // *mut i32 para o primeiro elemento

    unsafe {
        *p.add(2) = 30;           // aritmética: p + 2 elementos
        ptr::swap(p, p.add(3));   // troca o primeiro com o último
    }
    println!("{:?}", a); // [4, 2, 30, 1]

    // Entregar o ownership de um Box para ponteiro cru e recuperá-lo
    let b = Box::new(String::from("oi"));
    let raw = Box::into_raw(b);
    unsafe {
        (*raw).push('!');
        let de_volta = Box::from_raw(raw); // reassume o ownership (será liberado ao sair)
        println!("{de_volta}");
    }

    let nulo: *const i32 = ptr::null();
    println!("{}", nulo.is_null());
}
```

| API | Uso |
|---|---|
| `p.add(n)`, `p.sub(n)`, `p.offset(n)` | aritmética (em unidades de `T`) |
| `p.read()`, `p.write(v)` | lê/escreve sem desreferenciar |
| `ptr::copy`, `ptr::copy_nonoverlapping` | equivalente a `memmove`/`memcpy` |
| `ptr::swap`, `ptr::replace` | trocas |
| `NonNull<T>` | ponteiro **não nulo** (permite otimização de nicho em `Option<NonNull<T>>`) |
| `&raw const x` / `&raw mut x` | cria ponteiro cru sem passar por `&`/`&mut` |

> [!warning] Requisitos de validade
> Para desreferenciar, o ponteiro deve ser **não nulo, alinhado, apontar para memória alocada e inicializada** e respeitar as regras de aliasing (nenhum `&mut` ativo para o mesmo dado).

## Veja também

- [[Unsafe Rust]]
- [[Box]]
- [[Invariantes e boas práticas de unsafe]]
