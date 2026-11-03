---
tags: [rust, performance, memoria]
aliases: ["alocador", "GlobalAlloc", "bump allocator"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Stack, heap e layout de memória]]", "[[Otimização de desempenho]]", "[[Box]]", "[[Raw pointers]]"]
---

# Alocadores e memória

O Rust usa o alocador do sistema por padrão, mas você pode trocá-lo globalmente com `#[global_allocator]`.

```rust
use std::alloc::{GlobalAlloc, Layout, System};
use std::sync::atomic::{AtomicUsize, Ordering};

// Alocador "contador": envolve o do sistema e conta bytes alocados
struct Contador;

static ALOCADO: AtomicUsize = AtomicUsize::new(0);

unsafe impl GlobalAlloc for Contador {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        ALOCADO.fetch_add(layout.size(), Ordering::Relaxed);
        // SAFETY: delega ao alocador do sistema com o mesmo layout
        unsafe { System.alloc(layout) }
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        ALOCADO.fetch_sub(layout.size(), Ordering::Relaxed);
        // SAFETY: ptr foi alocado por este alocador com este layout
        unsafe { System.dealloc(ptr, layout) }
    }
}

#[global_allocator]
static GLOBAL: Contador = Contador;

fn main() {
    let antes = ALOCADO.load(Ordering::Relaxed);
    let v: Vec<u64> = Vec::with_capacity(1000);
    let depois = ALOCADO.load(Ordering::Relaxed);
    println!("Vec reservou {} bytes", depois - antes);
    drop(v);
}
```

## Alternativas prontas

| Alocador | Característica |
|---|---|
| `mimalloc` | rápido, simples de adotar, bom em multi-thread |
| `jemalloc` (`tikv-jemallocator`) | menos fragmentação em servidores de longa duração |
| musl malloc | **lento** em multi-thread: troque ao usar alvos musl |

```rust
// requer crate: mimalloc
use mimalloc::MiMalloc;

#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;

fn main() {
    println!("usando mimalloc");
}
```

## Arenas e *bump allocators*

Para muitas alocações pequenas com vida útil comum (um compilador, uma requisição), uma **arena** (`bumpalo`, `typed-arena`) aloca incrementando um ponteiro e libera tudo de uma vez.

> [!tip] Menos alocação > alocador melhor
> Antes de trocar o alocador, [[Perfilamento]] mostra se o problema é a quantidade de alocações.

## Veja também

- [[Stack, heap e layout de memória]]
- [[Otimização de desempenho]]
- [[Box]]
- [[Raw pointers]]
