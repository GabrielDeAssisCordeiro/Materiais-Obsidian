---
tags: [rust, exercicios, erros, traits, genericos]
aliases: ["Exercícios de traits"]
tipo: exercicio
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[Erros customizados]]", "[[Traits]]", "[[Genéricos]]", "[[Sobrecarga de operadores]]", "[[Exercícios de coleções e iteradores]]", "[[Exercícios de concorrência]]"]
---

# Exercícios de erros, traits e genéricos

## Exercícios

1. **Erro próprio.** Escreva `parse_ponto("3, 4") -> Result<(i32, i32), ErroPonto>` com um enum de erro (`Formato` e `Numero(ParseIntError)`), `Display` e `From<ParseIntError>` para usar `?`.
2. **Trait e `dyn`.** Defina a trait `Forma` com `area` e `nome` (com implementação padrão). Implemente-a para `Quadrado` e `Circulo` e some as áreas de um `Vec<Box<dyn Forma>>`.
3. **Genérico.** `maior_de<T>(&[T]) -> Option<T>` para tipos comparáveis e `Copy`.
4. **Operadores e `Display`.** Crie `Matriz2` (2×2 de `i32`) com `Add` e `Display`.
5. **Tipo genérico.** Implemente `Pilha<T>` com `push`, `pop`, `topo` e `tamanho`.

Notas relacionadas: [[Erros customizados]], [[Conversão de erros com From]], [[Traits]], [[impl Trait e dyn Trait]], [[Genéricos]], [[Sobrecarga de operadores]], [[Cheat sheet de traits]].

## Gabarito

<details>
<summary>Solução 1</summary>

```rust
use std::fmt;
use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
enum ErroPonto {
    Formato,
    Numero(ParseIntError),
}

impl fmt::Display for ErroPonto {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ErroPonto::Formato => write!(f, "formato esperado: x,y"),
            ErroPonto::Numero(e) => write!(f, "número inválido: {e}"),
        }
    }
}

impl std::error::Error for ErroPonto {}

impl From<ParseIntError> for ErroPonto {
    fn from(e: ParseIntError) -> Self {
        ErroPonto::Numero(e)
    }
}

fn parse_ponto(s: &str) -> Result<(i32, i32), ErroPonto> {
    let (a, b) = s.split_once(',').ok_or(ErroPonto::Formato)?;
    // `?` converte ParseIntError em ErroPonto via From
    Ok((a.trim().parse()?, b.trim().parse()?))
}

fn main() {
    assert_eq!(parse_ponto("3, 4"), Ok((3, 4)));
    assert_eq!(parse_ponto("34"), Err(ErroPonto::Formato));
    assert!(matches!(parse_ponto("3,x"), Err(ErroPonto::Numero(_))));
    println!("{}", parse_ponto("a,b").unwrap_err());
}
```

</details>
<details>
<summary>Solução 2</summary>

```rust
trait Forma {
    fn area(&self) -> f64;
    fn nome(&self) -> String {
        "forma".to_string() // implementação padrão
    }
}

struct Quadrado(f64);
struct Circulo(f64);

impl Forma for Quadrado {
    fn area(&self) -> f64 {
        self.0 * self.0
    }
    fn nome(&self) -> String {
        "quadrado".to_string()
    }
}

impl Forma for Circulo {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.0 * self.0
    }
}

fn area_total(formas: &[Box<dyn Forma>]) -> f64 {
    formas.iter().map(|f| f.area()).sum()
}

fn main() {
    let formas: Vec<Box<dyn Forma>> = vec![Box::new(Quadrado(2.0)), Box::new(Circulo(1.0))];
    let total = area_total(&formas);
    assert!((total - (4.0 + std::f64::consts::PI)).abs() < 1e-12);
    assert_eq!(formas[0].nome(), "quadrado");
    assert_eq!(formas[1].nome(), "forma");
    println!("área total = {total:.3}");
}
```

</details>
<details>
<summary>Solução 3</summary>

```rust
fn maior_de<T: PartialOrd + Copy>(v: &[T]) -> Option<T> {
    let mut it = v.iter().copied();
    let primeiro = it.next()?; // None para fatia vazia
    Some(it.fold(primeiro, |m, x| if x > m { x } else { m }))
}

fn main() {
    assert_eq!(maior_de(&[3, 9, 2]), Some(9));
    assert_eq!(maior_de(&[1.5, -2.0]), Some(1.5));
    assert_eq!(maior_de(&['a', 'z', 'm']), Some('z'));
    assert_eq!(maior_de::<i32>(&[]), None);
    println!("ok");
}
```

</details>
<details>
<summary>Solução 4</summary>

```rust
use std::fmt;
use std::ops::Add;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Matriz2([[i32; 2]; 2]);

impl Add for Matriz2 {
    type Output = Matriz2;

    fn add(self, outra: Matriz2) -> Matriz2 {
        let mut r = [[0; 2]; 2];
        for i in 0..2 {
            for j in 0..2 {
                r[i][j] = self.0[i][j] + outra.0[i][j];
            }
        }
        Matriz2(r)
    }
}

impl fmt::Display for Matriz2 {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "[{} {}; {} {}]",
            self.0[0][0], self.0[0][1], self.0[1][0], self.0[1][1]
        )
    }
}

fn main() {
    let a = Matriz2([[1, 2], [3, 4]]);
    let b = Matriz2([[10, 20], [30, 40]]);
    let c = a + b;
    assert_eq!(c, Matriz2([[11, 22], [33, 44]]));
    assert_eq!(c.to_string(), "[11 22; 33 44]");
    println!("{c}");
}
```

</details>
<details>
<summary>Solução 5</summary>

```rust
#[derive(Debug)]
struct Pilha<T> {
    itens: Vec<T>,
}

impl<T> Pilha<T> {
    fn nova() -> Self {
        Pilha { itens: Vec::new() }
    }

    fn push(&mut self, item: T) {
        self.itens.push(item);
    }

    fn pop(&mut self) -> Option<T> {
        self.itens.pop()
    }

    fn topo(&self) -> Option<&T> {
        self.itens.last()
    }

    fn tamanho(&self) -> usize {
        self.itens.len()
    }
}

fn main() {
    let mut p = Pilha::nova();
    p.push("a");
    p.push("b");
    assert_eq!(p.topo(), Some(&"b"));
    assert_eq!(p.tamanho(), 2);
    assert_eq!(p.pop(), Some("b"));
    assert_eq!(p.pop(), Some("a"));
    assert_eq!(p.pop(), None);
    println!("{p:?}");
}
```

</details>

## Veja também

- [[Erros customizados]]
- [[Traits]]
- [[Genéricos]]
- [[Sobrecarga de operadores]]
- [[Exercícios de coleções e iteradores]]
- [[Exercícios de concorrência]]
