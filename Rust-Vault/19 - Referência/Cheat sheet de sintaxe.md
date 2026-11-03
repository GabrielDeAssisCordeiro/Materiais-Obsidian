---
tags: [rust, referencia, cheatsheet, sintaxe]
aliases: ["Sintaxe rápida"]
tipo: cheatsheet
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Variáveis e mutabilidade]]", "[[Funções]]", "[[match]]", "[[Structs]]", "[[Enums]]", "[[Traits]]", "[[Cheat sheet de ownership]]"]
---

# Cheat sheet de sintaxe

Um programa com a sintaxe essencial reunida. Compile e experimente alterar partes.

```rust
use std::collections::HashMap;

const MAX: u32 = 10;
static NOME: &str = "rust";

// ---- tipos ----
#[derive(Debug, Clone, PartialEq)]
struct Ponto {
    x: i32,
    y: i32,
}

struct Metros(f64); // struct tupla
struct Marcador; // unit struct

#[derive(Debug)]
enum Forma {
    Circulo(f64),
    Retangulo { l: f64, a: f64 },
    Vazia,
}

// ---- implementações ----
impl Ponto {
    fn novo(x: i32, y: i32) -> Self {
        Ponto { x, y }
    }
    fn dist2(&self) -> i32 {
        self.x * self.x + self.y * self.y
    }
    fn mover_x(&mut self, dx: i32) {
        self.x += dx;
    }
}

trait Area {
    fn area(&self) -> f64;
}

impl Area for Forma {
    fn area(&self) -> f64 {
        match self {
            Forma::Circulo(r) => std::f64::consts::PI * r * r,
            Forma::Retangulo { l, a } => l * a,
            Forma::Vazia => 0.0,
        }
    }
}

// ---- funções ----
fn maior<T: PartialOrd>(a: T, b: T) -> T {
    if a > b { a } else { b }
}

fn dividir(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err("divisão por zero".into())
    } else {
        Ok(a / b)
    }
}

fn calcular() -> Result<i32, String> {
    let q = dividir(10, 2)?; // propaga o erro
    Ok(q * 2)
}

fn main() {
    // variáveis
    let x = 5;
    let mut y = 10;
    y += x;
    let y = y * 2; // shadowing
    let t: (i32, &str) = (1, "a");
    let (n, _texto) = t;
    let arr = [1, 2, 3];
    let fatia = &arr[1..];
    let v: Vec<i32> = (1..=5).collect();

    // controle de fluxo
    if n > 0 && y > 0 {
        println!("positivos");
    }
    let rotulo = if n == 1 { "um" } else { "outro" };
    let achado = loop {
        break 42;
    };
    'externo: for i in 0..3 {
        for j in 0..3 {
            if i * j == 2 {
                break 'externo;
            }
        }
    }
    while let Some(_) = None::<i32> {}
    for (i, e) in v.iter().enumerate() {
        if i == 0 {
            println!("primeiro = {e}");
        }
    }

    // match e patterns
    match n {
        0 => println!("zero"),
        1..=9 => println!("um dígito"),
        n if n < 0 => println!("negativo"),
        _ => println!("grande"),
    }
    let Ok(q) = dividir(6, 3) else {
        return;
    };
    if let Some(p) = v.first() {
        println!("{p} {q}");
    }

    // coleções
    let mut mapa: HashMap<&str, i32> = HashMap::new();
    mapa.insert("a", 1);
    *mapa.entry("a").or_insert(0) += 1;

    // closures
    let dobro = |n: i32| n * 2;
    let soma: i32 = v.iter().map(|&n| dobro(n)).sum();

    // structs e enums
    let mut p = Ponto::novo(3, 4);
    p.mover_x(1);
    let _m = Metros(2.5);
    let _u = Marcador;
    let formas = [Forma::Circulo(1.0), Forma::Retangulo { l: 2.0, a: 3.0 }, Forma::Vazia];
    let areas: Vec<f64> = formas.iter().map(|f| f.area()).collect();

    println!("{MAX} {NOME} {rotulo} {achado} {fatia:?} {soma} {} {:?}", p.dist2(), areas);
    println!("{} {}", maior(3, 7), maior("a", "b"));
    println!("{:?}", calcular());
    println!("{:>6.2}|{:<5}|{:^7}|{:08.3}|{:#x}|{:#b}", 3.14159, "ab", "mid", 2.5, 255, 5);
}
```

## Tipos primitivos

| Categoria | Tipos |
|---|---|
| Inteiros com sinal | `i8 i16 i32 i64 i128 isize` |
| Inteiros sem sinal | `u8 u16 u32 u64 u128 usize` |
| Ponto flutuante | `f32 f64` |
| Outros | `bool`, `char` (4 bytes, Unicode), `()` (unit), `!` (never) |
| Compostos | `(A, B)`, `[T; N]`, `&[T]`, `&str`, `String`, `Vec<T>` |

## Literais e sufixos

| Forma | Exemplo |
|---|---|
| Decimal, hex, octal, binário | `98_222`, `0xff`, `0o77`, `0b1111_0000` |
| Byte | `b'A'`, `b"bytes"` |
| Sufixo de tipo | `10u8`, `2.5f32` |
| String crua | `r"C:\caminho"`, `r#"com "aspas""#` |

## Operadores mais usados

| Operador | Uso |
|---|---|
| `?` | propaga `Err`/`None` |
| `..` / `..=` | intervalo exclusivo / inclusivo |
| `&` / `&mut` | referência compartilhada / exclusiva |
| `*` | desreferência |
| `as` | conversão numérica explícita |
| `::` | caminho / turbofish `parse::<i32>()` |
| `\|x\| expr` | closure |
| `=>` | braço de `match` |

Veja os detalhes em [[Operadores]], [[Tipos escalares]] e [[Formatação com println]].

## Veja também

- [[Variáveis e mutabilidade]]
- [[Funções]]
- [[match]]
- [[Structs]]
- [[Enums]]
- [[Traits]]
- [[Cheat sheet de ownership]]
