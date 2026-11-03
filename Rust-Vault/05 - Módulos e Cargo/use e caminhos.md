---
tags: [rust, modulos]
aliases: ["use", "crate::", "self::", "super::", "glob import"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Módulos e mod]]", "[[Re-exports com pub use]]", "[[Visibilidade e pub]]"]
---

# use e caminhos

`use` traz um caminho para o escopo atual.

| Prefixo | Significado |
|---|---|
| `crate::` | a partir da raiz do crate atual |
| `self::` | módulo atual |
| `super::` | módulo pai |
| `std::` / nome do crate | crate externo |

```rust
mod geometria {
    pub fn area(l: f64) -> f64 {
        l * l
    }

    pub mod formas {
        pub fn dobro(l: f64) -> f64 {
            super::area(l) * 2.0
        }
        pub fn soma(l: f64) -> f64 {
            self::dobro(l) + crate::geometria::area(l)
        }
    }
}

use geometria::formas::{self, dobro};
use std::collections::HashMap as Mapa;
use std::io::{self, Write};

fn main() {
    println!("{} {}", dobro(2.0), formas::soma(2.0));

    let mut m: Mapa<&str, i32> = Mapa::new();
    m.insert("a", 1);
    println!("{:?}", m);

    io::stdout().flush().unwrap();
}
```

- **Aninhado:** `use std::{fmt, io::{self, Read}};`
- **Glob:** `use std::collections::*;` (evite fora de preludes e testes)
- **Renomear:** `use x as y;`
- Convenção: importe o **módulo** para funções (`use std::fs;` → `fs::read_to_string`) e o **tipo** para structs/enums (`use std::collections::HashMap;`).

> [!info] Prelude
> A biblioteca padrão importa automaticamente itens como `Option`, `Vec`, `String`, `Box` e `Iterator` (o *prelude*), por isso você não escreve `use` para eles.

## Veja também

- [[Módulos e mod]]
- [[Re-exports com pub use]]
- [[Visibilidade e pub]]
