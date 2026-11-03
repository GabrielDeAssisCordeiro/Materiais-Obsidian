---
tags: [rust, structs, tipos]
aliases: ["tuple struct", "unit struct"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Structs]]", "[[Desestruturação]]"]
---

# Structs tupla e unit

## Struct tupla

Campos sem nome, acessados por índice. Cria um **tipo distinto**, mesmo com a mesma forma.

```rust
struct Cor(u8, u8, u8);
struct Ponto(i32, i32, i32);

fn main() {
    let preto = Cor(0, 0, 0);
    let origem = Ponto(0, 0, 0);
    println!("{} {}", preto.0, origem.2);
    // let c: Cor = origem; // erro: tipos diferentes

    let Cor(r, g, b) = preto; // desestruturação
    println!("{r} {g} {b}");
}
```

## Newtype

Struct tupla com **um campo** para dar significado ao tipo e evitar misturar unidades.

```rust
struct Metros(f64);
struct Quilos(f64);

fn mostra(m: Metros) {
    println!("{} m", m.0);
}

fn main() {
    mostra(Metros(2.5));
    // mostra(Quilos(2.5)); // erro de tipo: não confunde unidades
    let _ = Quilos(1.0);
}
```

## Struct unit

Sem campos; útil como marcador ou ao implementar traits sem dados.

```rust
struct Marcador;

fn main() {
    let _m = Marcador;
    println!("{}", std::mem::size_of::<Marcador>()); // 0
}
```

## Veja também

- [[Structs]]
- [[Desestruturação]]
