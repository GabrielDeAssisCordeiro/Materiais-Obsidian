---
tags: [rust, traits, operadores]
aliases: ["Add", "Mul", "Neg", "Index", "std::ops"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Traits padrão]]", "[[Tipos associados]]", "[[Orphan rule]]"]
---

# Sobrecarga de operadores

Operadores são açúcar para traits de `std::ops` (e `std::cmp`).

| Operador | Trait |
|---|---|
| `+` `-` `*` `/` `%` | `Add`, `Sub`, `Mul`, `Div`, `Rem` |
| `-x`, `!x` | `Neg`, `Not` |
| `+=` etc. | `AddAssign`, `SubAssign`... |
| `a[i]` | `Index`, `IndexMut` |
| `==`, `<` | `PartialEq`, `PartialOrd` |
| `*x` | `Deref` |

```rust
use std::ops::{Add, AddAssign, Index, Mul, Neg};

#[derive(Debug, Clone, Copy, PartialEq)]
struct V2 {
    x: f64,
    y: f64,
}

impl Add for V2 {
    type Output = V2;
    fn add(self, o: V2) -> V2 {
        V2 { x: self.x + o.x, y: self.y + o.y }
    }
}

impl Mul<f64> for V2 {
    type Output = V2;
    fn mul(self, k: f64) -> V2 {
        V2 { x: self.x * k, y: self.y * k }
    }
}

// Permite escrever 2.0 * v (o tipo V2 é local, então a regra órfã permite)
impl Mul<V2> for f64 {
    type Output = V2;
    fn mul(self, v: V2) -> V2 {
        v * self
    }
}

impl Neg for V2 {
    type Output = V2;
    fn neg(self) -> V2 {
        V2 { x: -self.x, y: -self.y }
    }
}

impl AddAssign for V2 {
    fn add_assign(&mut self, o: V2) {
        self.x += o.x;
        self.y += o.y;
    }
}

struct Matriz {
    dados: Vec<f64>,
    colunas: usize,
}

impl Index<(usize, usize)> for Matriz {
    type Output = f64;
    fn index(&self, (l, c): (usize, usize)) -> &f64 {
        &self.dados[l * self.colunas + c]
    }
}

fn main() {
    let a = V2 { x: 1.0, y: 2.0 };
    let b = V2 { x: 3.0, y: 4.0 };
    let mut c = a + b * 2.0;
    c += -a;
    println!("{:?} {:?}", c, 2.0_f64 * a);

    let m = Matriz { dados: vec![1.0, 2.0, 3.0, 4.0], colunas: 2 };
    println!("{}", m[(1, 0)]); // 3
}
```

> [!warning] Use com parcimônia
> Sobrecarregue operadores apenas quando o significado for óbvio (vetores, matrizes, números). Evite operadores com semântica surpreendente.

## Veja também

- [[Traits padrão]]
- [[Tipos associados]]
- [[Orphan rule]]
