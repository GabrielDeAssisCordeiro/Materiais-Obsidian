---
tags: [rust, traits]
aliases: ["supertrait", "herança de traits", "trait Foo: Bar"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Traits padrão]]", "[[Object safety]]"]
---

# Supertraits

Uma trait pode **exigir** outras: `trait A: B` significa "quem implementa `A` precisa implementar `B`".

```rust
use std::fmt::{self, Display};

trait Descritivel: Display {
    // Pode usar Display porque é supertrait
    fn descreve(&self) -> String {
        format!("<<{}>>", self)
    }
}

struct Ponto(i32, i32);

impl Display for Ponto {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.0, self.1)
    }
}

impl Descritivel for Ponto {}

// Múltiplos supertraits
trait Entidade: std::fmt::Debug + Clone {}

#[derive(Debug, Clone)]
struct Usuario;
impl Entidade for Usuario {}

fn main() {
    println!("{}", Ponto(1, 2).descreve());
    let _u: Box<dyn std::fmt::Debug> = Box::new(Usuario);
}
```

> [!info] Não é herança de dados
> Supertraits compõem **contratos**. Não há herança de campos nem de implementação além dos métodos padrão.

## Veja também

- [[Traits]]
- [[Traits padrão]]
- [[Object safety]]
