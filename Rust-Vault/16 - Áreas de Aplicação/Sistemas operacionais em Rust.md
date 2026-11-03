---
tags: [rust, areas, no_std]
aliases: ["driver", "OSDev", "Rust for Linux", "Redox"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Embarcados e no_std]]", "[[Unsafe Rust]]", "[[Raw pointers]]", "[[Invariantes e boas práticas de unsafe]]"]
---

# Sistemas operacionais em Rust

Escrever partes de um sistema operacional em Rust significa trabalhar **sem `std`**, com muito [[Unsafe Rust]] encapsulado em abstrações seguras.

## Projetos de referência

| Projeto | Descrição |
|---|---|
| **Rust for Linux** | suporte oficial a drivers em Rust no kernel Linux |
| **Redox OS** | SO completo, microkernel, escrito em Rust |
| **Tock** | SO embarcado seguro com isolamento de processos |
| **Android / Windows** | componentes internos reescritos em Rust |
| **Blog "Writing an OS in Rust"** (os.phil-opp.com) | tutorial clássico passo a passo |

## Ingredientes de um kernel mínimo

```rust
// trecho: esqueleto de kernel x86_64 (exige target bare-metal)
#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panico(_info: &PanicInfo) -> ! {
    loop {}
}

#[unsafe(no_mangle)]
pub extern "C" fn _start() -> ! {
    // escrever no buffer de vídeo VGA (0xb8000), por exemplo
    let vga = 0xb8000 as *mut u8;
    for (i, &b) in b"Ola, Rust!".iter().enumerate() {
        // SAFETY: endereço do buffer VGA é memória mapeada válida em modo texto
        unsafe {
            *vga.add(i * 2) = b;
            *vga.add(i * 2 + 1) = 0x0b; // ciano sobre preto
        }
    }
    loop {}
}
```

- Alocador próprio (`#[global_allocator]`), paginação, interrupções e escalonador viram módulos com API segura.
- Acesso a hardware via *memory-mapped I/O* usa ponteiros voláteis (`read_volatile`/`write_volatile`) — veja [[Raw pointers]].

> [!question] Verificar na documentação oficial
> O estado do suporte a Rust no kernel Linux evolui por versão; consulte rust-for-linux.com.

## Veja também

- [[Embarcados e no_std]]
- [[Unsafe Rust]]
- [[Raw pointers]]
- [[Invariantes e boas práticas de unsafe]]
