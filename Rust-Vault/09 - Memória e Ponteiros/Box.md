---
tags: [rust, memoria, ponteiros]
aliases: ["Box<T>", "alocação na heap", "tipo recursivo"]
tipo: tipo-de-dado
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Stack, heap e layout de memória]]", "[[Rc]]", "[[impl Trait e dyn Trait]]", "[[Deref e AsRef]]"]
---

# Box

`Box<T>` aloca um valor na **heap** e é seu único dono. Quando o `Box` sai de escopo, o valor é liberado.

## Quando usar

1. **Tipos recursivos** (tamanho desconhecido em compilação).
2. **Trait objects**: `Box<dyn Trait>`.
3. Mover dados grandes sem copiá-los (só o ponteiro é movido).

```rust
// ❌ NÃO COMPILA: tamanho infinito
enum Lista {
    Cons(i32, Lista),
    Nil,
}

fn main() {}
```

```text
error[E0072]: recursive type `Lista` has infinite size
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`)
```

```rust
// Com Box, o tamanho é conhecido (um ponteiro)
enum Lista {
    Cons(i32, Box<Lista>),
    Nil,
}

use Lista::{Cons, Nil};

fn soma(l: &Lista) -> i32 {
    match l {
        Cons(v, resto) => v + soma(resto),
        Nil => 0,
    }
}

fn main() {
    let l = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
    println!("{}", soma(&l));

    let b = Box::new(5);
    println!("{}", *b + 1); // Box implementa Deref

    // Mover o valor para fora do Box
    let s = Box::new(String::from("oi"));
    let dentro: String = *s;
    println!("{dentro}");
}
```

> [!tip] Árvores
> Estruturas como árvores binárias usam `Option<Box<No>>` para os filhos.

```rust
struct No {
    valor: i32,
    esquerda: Option<Box<No>>,
    direita: Option<Box<No>>,
}

impl No {
    fn novo(valor: i32) -> Self {
        No { valor, esquerda: None, direita: None }
    }

    fn insere(&mut self, v: i32) {
        let destino = if v < self.valor { &mut self.esquerda } else { &mut self.direita };
        match destino {
            Some(no) => no.insere(v),
            None => *destino = Some(Box::new(No::novo(v))),
        }
    }

    fn em_ordem(&self, saida: &mut Vec<i32>) {
        if let Some(e) = &self.esquerda {
            e.em_ordem(saida);
        }
        saida.push(self.valor);
        if let Some(d) = &self.direita {
            d.em_ordem(saida);
        }
    }
}

fn main() {
    let mut raiz = No::novo(5);
    for v in [3, 8, 1, 4, 9] {
        raiz.insere(v);
    }
    let mut v = Vec::new();
    raiz.em_ordem(&mut v);
    println!("{:?}", v); // [1, 3, 4, 5, 8, 9]
}
```

## Exercício

Implemente `fn contem(&self, v: i32) -> bool` para a árvore binária acima.

## Veja também

- [[Stack, heap e layout de memória]]
- [[Rc]]
- [[impl Trait e dyn Trait]]
- [[Deref e AsRef]]
