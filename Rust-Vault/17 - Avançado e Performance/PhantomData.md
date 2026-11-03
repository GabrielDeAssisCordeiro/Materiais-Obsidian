---
tags: [rust, avancado, tipos, unsafe]
aliases: ["PhantomData", "marker types", "tipos fantasma", "unidades de medida"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Newtype]]", "[[Typestate]]", "[[Genéricos]]", "[[Send e Sync]]", "[[Raw pointers]]"]
---

# PhantomData

`PhantomData<T>` é um tipo de tamanho **zero** que informa ao compilador "este tipo age como se contivesse um `T`", sem armazenar nada. Serve para parâmetros de tipo que não aparecem nos campos.

```rust
// ❌ NÃO COMPILA: parâmetro de tipo não usado
struct Id<T> {
    valor: u32,
}
fn main() {}
```

```text
error[E0392]: type parameter `T` is never used
```

```rust
use std::marker::PhantomData;

// IDs tipados: impossível misturar Id<Usuario> com Id<Pedido>
struct Id<T> {
    valor: u32,
    _marca: PhantomData<T>,
}

impl<T> Id<T> {
    fn novo(valor: u32) -> Self {
        Id { valor, _marca: PhantomData }
    }
}

// Clone/Copy manuais: derive exigiria T: Clone
impl<T> Clone for Id<T> {
    fn clone(&self) -> Self {
        *self
    }
}
impl<T> Copy for Id<T> {}

struct Usuario;
struct Pedido;

fn busca_usuario(id: Id<Usuario>) -> String {
    format!("usuário #{}", id.valor)
}

// Unidades de medida em tempo de compilação
struct Metros;
struct Segundos;

struct Qtd<U> {
    v: f64,
    _u: PhantomData<U>,
}

impl<U> Qtd<U> {
    fn new(v: f64) -> Self {
        Qtd { v, _u: PhantomData }
    }
}

impl<U> std::ops::Add for Qtd<U> {
    type Output = Qtd<U>;
    fn add(self, o: Self) -> Self::Output {
        Qtd::new(self.v + o.v)
    }
}

fn main() {
    let u: Id<Usuario> = Id::novo(7);
    let _p: Id<Pedido> = Id::novo(7);
    println!("{}", busca_usuario(u));
    // busca_usuario(_p); // erro de tipo: esperado Id<Usuario>

    let d = Qtd::<Metros>::new(3.0) + Qtd::<Metros>::new(4.5);
    println!("{} m", d.v);
    let _t: Qtd<Segundos> = Qtd::new(1.0);
    // d + _t; // erro: Metros != Segundos
}
```

## Outros usos

| Uso | Efeito |
|---|---|
| Marcar propriedade de dados (`PhantomData<T>` em wrapper de `*mut T`) | o *drop check* entende que há um `T` |
| Variância e lifetimes (`PhantomData<&'a T>`) | liga o tipo a um lifetime |
| `PhantomData<*const ()>` | torna o tipo `!Send` e `!Sync` |
| Estados em [[Typestate]] | custo zero em tempo de execução |

## Veja também

- [[Newtype]]
- [[Typestate]]
- [[Genéricos]]
- [[Send e Sync]]
- [[Raw pointers]]
