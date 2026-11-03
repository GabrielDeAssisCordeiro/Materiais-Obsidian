---
tags: [rust, avancado, genericos]
aliases: ["const generics", "const N", "arrays genéricos", "const fn"]
tipo: conceito
nivel: avancado
criado: 2026-10-24
relacionados: ["[[Genéricos]]", "[[Tipos escalares]]", "[[PhantomData]]", "[[Zero-cost abstractions]]"]
---

# Const generics

**Const generics** permitem parametrizar tipos e funções por **valores constantes** (inteiros, `bool`, `char`), tipicamente o tamanho de arrays.

```rust
use std::ops::Add;

// Uma matriz com dimensões verificadas em compilação
#[derive(Debug, Clone, Copy, PartialEq)]
struct Matriz<const L: usize, const C: usize> {
    dados: [[i32; C]; L],
}

impl<const L: usize, const C: usize> Matriz<L, C> {
    fn zero() -> Self {
        Matriz { dados: [[0; C]; L] }
    }

    fn transposta(&self) -> Matriz<C, L> {
        let mut r = Matriz::<C, L>::zero();
        for i in 0..L {
            for j in 0..C {
                r.dados[j][i] = self.dados[i][j];
            }
        }
        r
    }
}

// Somar só matrizes do mesmo formato
impl<const L: usize, const C: usize> Add for Matriz<L, C> {
    type Output = Self;
    fn add(self, o: Self) -> Self {
        let mut r = Self::zero();
        for i in 0..L {
            for j in 0..C {
                r.dados[i][j] = self.dados[i][j] + o.dados[i][j];
            }
        }
        r
    }
}

// Função genérica sobre o tamanho do array
fn soma<const N: usize>(a: [i32; N]) -> i32 {
    a.iter().sum()
}

// const fn: avaliada em tempo de compilação
const fn fatorial(n: u32) -> u32 {
    if n == 0 { 1 } else { n * fatorial(n - 1) }
}

const F5: u32 = fatorial(5);

fn main() {
    let m = Matriz::<2, 3> { dados: [[1, 2, 3], [4, 5, 6]] };
    println!("{:?}", m.transposta()); // 3x2
    println!("{:?}", (m + m).dados);
    println!("{} {}", soma([1, 2, 3]), soma([10; 5]));
    println!("{F5}");
}
```

```rust
// ❌ NÃO COMPILA: formatos diferentes
#[derive(Clone, Copy)]
struct M<const L: usize, const C: usize>([[i32; C]; L]);

fn soma_m<const L: usize, const C: usize>(_a: M<L, C>, _b: M<L, C>) {}

fn main() {
    let a = M::<2, 2>([[0; 2]; 2]);
    let b = M::<3, 3>([[0; 3]; 3]);
    soma_m(a, b);
}
```

```text
error[E0308]: mismatched types
  expected `M<2, 2>`, found `M<3, 3>`
```

> [!info] Limitações atuais
> Expressões aritméticas em parâmetros const (como `[T; N + 1]`) em tipos genéricos ainda dependem de `generic_const_exprs` (nightly).
> [!question] Verificar na documentação oficial
> Confirme o estado de `generic_const_exprs` no Rust Reference e no tracking issue do projeto.

## Veja também

- [[Genéricos]]
- [[Tipos escalares]]
- [[PhantomData]]
- [[Zero-cost abstractions]]
