---
tags: [rust, traits, genericos]
aliases: ["associated types", "type Item", "Self::Item"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits]]", "[[Iteradores]]", "[[Sobrecarga de operadores]]"]
---

# Tipos associados

Um **tipo associado** é um "espaço reservado" de tipo dentro de uma trait, escolhido por quem implementa.

```rust
trait Contenedor {
    type Item;

    fn pega(&self, i: usize) -> Option<&Self::Item>;
    fn tamanho(&self) -> usize;
}

struct Lista(Vec<String>);

impl Contenedor for Lista {
    type Item = String;

    fn pega(&self, i: usize) -> Option<&String> {
        self.0.get(i)
    }
    fn tamanho(&self) -> usize {
        self.0.len()
    }
}

fn primeiro<C: Contenedor>(c: &C) -> Option<&C::Item> {
    c.pega(0)
}

fn main() {
    let l = Lista(vec!["a".to_string(), "b".to_string()]);
    println!("{:?} {}", primeiro(&l), l.tamanho());
}
```

## Tipo associado vs parâmetro genérico

| | `trait T { type X; }` | `trait T<X>` |
|---|---|---|
| Implementações por tipo | **Uma** | Várias (uma para cada `X`) |
| Uso | `Iterator::Item`, `Deref::Target` | `From<T>`, `Add<Rhs>` |
| Inferência | Mais simples | Pode exigir anotações |

> [!tip] Regra prática
> Se há **uma** escolha natural de tipo por implementador, use tipo associado.

## Veja também

- [[Traits]]
- [[Iteradores]]
- [[Sobrecarga de operadores]]
