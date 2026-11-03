---
tags: [rust, concorrencia, traits]
aliases: ["Send", "auto traits", "unsafe impl Send"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Concorrência sem medo]]", "[[Arc]]", "[[Rc]]", "[[Mutex e RwLock]]"]
---

# Send e Sync

Duas **auto traits** (implementadas automaticamente quando todos os campos as implementam) controlam o que pode cruzar threads:

| Trait | Significado | Exemplo |
|---|---|---|
| `Send` | o valor pode ser **movido** para outra thread | `i32`, `String`, `Arc<T>` (se `T: Send + Sync`) |
| `Sync` | `&T` pode ser **compartilhada** entre threads (`T: Sync` ⇔ `&T: Send`) | `i32`, `Mutex<T>` (se `T: Send`) |

| Tipo | `Send` | `Sync` | Por quê |
|---|---|---|---|
| `Rc<T>` | não | não | contagem não atômica |
| `Cell<T>`, `RefCell<T>` | sim* | **não** | mutação sem sincronização |
| `Arc<T>` | se `T: Send+Sync` | se `T: Send+Sync` | contagem atômica |
| `Mutex<T>` | se `T: Send` | se `T: Send` | sincroniza o acesso |
| `MutexGuard<T>` | **não** | se `T: Sync` | deve ser liberado na mesma thread |
| ponteiros crus `*const T` | não | não | sem garantias |

\* se `T: Send`

```rust
fn exige_send<T: Send>(_: &T) {}
fn exige_sync<T: Sync>(_: &T) {}

fn main() {
    exige_send(&5);
    exige_sync(&String::new());
    exige_send(&std::sync::Arc::new(1));
    exige_sync(&std::sync::Mutex::new(Vec::<i32>::new()));
    println!("tudo certo");
}
```

```rust
// ❌ NÃO COMPILA: Cell não é Sync
use std::cell::Cell;

fn exige_sync<T: Sync>(_: &T) {}

fn main() {
    exige_sync(&Cell::new(1));
}
```

```text
error[E0277]: `Cell<i32>` cannot be shared between threads safely
```

> [!warning] Implementação manual
> Implementar `Send`/`Sync` à mão exige `unsafe impl`, e você garante os invariantes. É o que bibliotecas como `Arc` e `Mutex` fazem internamente; veja [[Unsafe Rust]].

> [!info] `thread::spawn` exige `F: Send + 'static`
> Por isso `Rc` não pode ser capturado por uma thread, e referências locais exigem `move` ou `thread::scope`.

## Veja também

- [[Concorrência sem medo]]
- [[Arc]]
- [[Rc]]
- [[Mutex e RwLock]]
