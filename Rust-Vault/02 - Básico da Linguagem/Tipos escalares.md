---
tags: [rust, basico, tipos]
aliases: ["inteiros", "floats", "bool", "char", "i32", "f64"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Tuplas]]", "[[Arrays]]", "[[Conversão entre tipos]]", "[[Overflow aritmético]]"]
---

# Tipos escalares

Rust tem quatro tipos escalares: **inteiros**, **ponto flutuante**, **booleanos** e **caracteres**.

## Inteiros

| Tamanho | Com sinal | Sem sinal |
|---|---|---|
| 8 bits | `i8` | `u8` |
| 16 bits | `i16` | `u16` |
| 32 bits | `i32` (padrão) | `u32` |
| 64 bits | `i64` | `u64` |
| 128 bits | `i128` | `u128` |
| Dependente da arquitetura | `isize` | `usize` |

`usize` é usado para **índices e tamanhos**.

## Literais

```rust
fn main() {
    let decimal = 98_222;      // separador _ para legibilidade
    let hex = 0xff;
    let octal = 0o77;
    let binario = 0b1111_0000;
    let byte = b'A';           // u8
    let longo = 42u64;         // sufixo de tipo
    println!("{decimal} {hex} {octal} {binario} {byte} {longo}");
}
```

## Ponto flutuante

`f32` e `f64` (padrão, IEEE 754).

```rust
fn main() {
    let a = 2.5;         // f64
    let b: f32 = 1.5;
    println!("{} {}", a * 2.0, b / 2.0);
}
```

## Booleano e caractere

```rust
fn main() {
    let ativo: bool = true;
    let letra: char = 'ç';   // char tem 4 bytes e representa um valor escalar Unicode
    let emoji = '🦀';
    println!("{ativo} {letra} {emoji} {}", letra.len_utf8());
}
```

> [!info] Limites
> `i32::MAX`, `u8::MIN` etc. dão os limites de cada tipo. Veja [[Overflow aritmético]] para o que acontece ao ultrapassá-los.

## Exercício

Imprima `i8::MIN`, `i8::MAX` e `u64::MAX`.

## Veja também

- [[Tuplas]]
- [[Arrays]]
- [[Conversão entre tipos]]
- [[Overflow aritmético]]
