---
tags: [rust, traits, trait-objects]
aliases: ["dyn compatibility", "object safety", "trait object"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[impl Trait e dyn Trait]]", "[[Supertraits]]", "[[Traits]]"]
---

# Object safety

Nem toda trait pode virar `dyn Trait`. Ela precisa ser **segura para objetos** (*object safe*; a documentação recente também usa *dyn compatible*).

## Principais regras

- Nenhum método pode retornar `Self` (sem `where Self: Sized`).
- Nenhum método pode ter parâmetros de tipo genéricos (sem `where Self: Sized`).
- A trait não pode exigir `Self: Sized`.
- Funções associadas sem `self` não podem ser chamadas via objeto (precisam de `where Self: Sized`).

```rust
// ❌ NÃO COMPILA: Clone-like retorna Self
trait Clonavel {
    fn clona(&self) -> Self;
}

fn usa(_x: &dyn Clonavel) {}

fn main() {}
```

```text
error[E0038]: the trait `Clonavel` is not dyn compatible
```

**Correção:** excluir o método do objeto com `where Self: Sized`.

```rust
trait Forma {
    fn area(&self) -> f64;

    // Fica fora da vtable: disponível apenas para tipos concretos
    fn dobrada(&self) -> Self
    where
        Self: Sized;
}

struct Q(f64);

impl Forma for Q {
    fn area(&self) -> f64 {
        self.0 * self.0
    }
    fn dobrada(&self) -> Self {
        Q(self.0 * 2.0)
    }
}

fn main() {
    let f: Box<dyn Forma> = Box::new(Q(2.0)); // OK
    println!("{}", f.area());
    println!("{}", Q(1.0).dobrada().area());
}
```

> [!tip] Por quê?
> A vtable só guarda ponteiros de função com assinatura fixa; métodos genéricos ou que dependem do tamanho de `Self` não podem ser despachados dinamicamente.

## Veja também

- [[impl Trait e dyn Trait]]
- [[Supertraits]]
- [[Traits]]
