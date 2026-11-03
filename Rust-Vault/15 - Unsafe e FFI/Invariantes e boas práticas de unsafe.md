---
tags: [rust, unsafe, boas-praticas]
aliases: ["SAFETY", "abstração segura", "invariantes", "forbid(unsafe_code)"]
tipo: referencia
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Unsafe Rust]]", "[[Raw pointers]]", "[[Miri]]", "[[Drop e RAII]]"]
---

# Invariantes e boas práticas de unsafe

O objetivo: **encapsular** `unsafe` em módulos pequenos cuja API pública seja **impossível de usar de forma incorreta** (*sound*).

## Exemplo: abstração segura sobre memória crua

```rust
use std::alloc::{alloc, dealloc, Layout};
use std::ptr::NonNull;

/// Buffer de bytes de tamanho fixo, inicializado com zeros.
///
/// Invariantes (mantidos por todos os métodos):
/// - `ptr` aponta para `len` bytes alocados e inicializados;
/// - `len > 0`.
pub struct Buf {
    ptr: NonNull<u8>,
    len: usize,
}

impl Buf {
    pub fn novo(len: usize) -> Self {
        assert!(len > 0, "len deve ser positivo");
        let layout = Layout::array::<u8>(len).expect("tamanho inválido");
        // SAFETY: layout tem tamanho > 0
        let bruto = unsafe { alloc(layout) };
        let ptr = NonNull::new(bruto).expect("sem memória");
        // SAFETY: ptr é válido para `len` bytes de escrita
        unsafe { std::ptr::write_bytes(ptr.as_ptr(), 0, len) };
        Buf { ptr, len }
    }

    pub fn get(&self, i: usize) -> Option<u8> {
        if i < self.len {
            // SAFETY: i < len, e os `len` bytes estão inicializados (invariante)
            Some(unsafe { *self.ptr.as_ptr().add(i) })
        } else {
            None
        }
    }

    pub fn set(&mut self, i: usize, v: u8) {
        assert!(i < self.len, "índice fora do limite");
        // SAFETY: i < len; &mut self garante acesso exclusivo
        unsafe { *self.ptr.as_ptr().add(i) = v };
    }
}

impl Drop for Buf {
    fn drop(&mut self) {
        let layout = Layout::array::<u8>(self.len).unwrap();
        // SAFETY: ptr foi alocado com este mesmo layout e ainda não foi liberado
        unsafe { dealloc(self.ptr.as_ptr(), layout) };
    }
}

fn main() {
    let mut b = Buf::novo(4);
    b.set(1, 42);
    println!("{:?} {:?} {:?}", b.get(1), b.get(0), b.get(9));
}
```

## Checklist

- [ ] Cada bloco `unsafe` tem um comentário `// SAFETY:` justificando as condições.
- [ ] Cada `unsafe fn` público tem uma seção `# Safety` na documentação.
- [ ] Os **invariantes** do tipo estão escritos e todo método os preserva.
- [ ] A API pública **segura** não permite violar os invariantes (nem com `panic`/reentrância).
- [ ] Blocos `unsafe` são pequenos e isolados em um módulo.
- [ ] Testes rodam sob **Miri** e, quando aplicável, *sanitizers* e fuzzing.
- [ ] Use `#![forbid(unsafe_code)]` nos crates que **não** precisam de `unsafe`.
- [ ] Considere `#![warn(unsafe_op_in_unsafe_fn)]` (padrão na edição 2024) e `cargo geiger` para medir o uso de `unsafe`.

> [!tip] Antes de escrever `unsafe`
> Procure na `std` ou em crates auditados (`bytemuck`, `zerocopy`, `crossbeam`) a abstração que você precisa. Muitas vezes ela já existe.

## Veja também

- [[Unsafe Rust]]
- [[Raw pointers]]
- [[Miri]]
- [[Drop e RAII]]
