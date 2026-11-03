---
tags: [rust, pattern-matching]
aliases: ["guards", "bindings @", "ranges em padrões", "ref"]
tipo: conceito
nivel: intermediario
criado: 2026-10-24
relacionados: ["[[match]]", "[[Desestruturação]]", "[[Enums]]", "[[if let e let else]]"]
---

# Pattern matching avançado

Padrões aparecem em `match`, `if let`, `while let`, `for`, `let` e parâmetros de função.

## Tipos de padrão

```rust
fn main() {
    // Literais, alternativas e ranges
    let n = 7;
    match n {
        1 | 2 => println!("pouco"),
        3..=9 => println!("médio"),
        _ => println!("muito"),
    }

    // Guard (condição extra)
    let par = (4, 4);
    match par {
        (a, b) if a == b => println!("iguais"),
        _ => println!("diferentes"),
    }

    // Binding com @: captura o valor E testa o padrão
    match 15 {
        v @ 10..=20 => println!("{v} está entre 10 e 20"),
        v => println!("{v} fora"),
    }

    // Ignorar partes com _ e ..
    let tupla = (1, 2, 3, 4, 5);
    let (primeiro, .., ultimo) = tupla;
    println!("{primeiro} {ultimo}");
}
```

## Aninhados e em enums

```rust
enum Forma {
    Retangulo { largura: f64, altura: f64 },
    Circulo { raio: f64 },
}

enum Cmd {
    Desenha(Forma),
    Limpa,
}

fn main() {
    let c = Cmd::Desenha(Forma::Retangulo { largura: 2.0, altura: 3.0 });
    match c {
        Cmd::Desenha(Forma::Retangulo { largura, altura }) => println!("{}", largura * altura),
        Cmd::Desenha(Forma::Circulo { raio }) => println!("{}", 3.14 * raio * raio),
        Cmd::Limpa => println!("limpar"),
    }
}
```

## Referências em padrões

Com *match ergonomics*, casar em `&T` dá bindings por referência automaticamente.

```rust
fn main() {
    let opcao: Option<String> = Some(String::from("texto"));

    match &opcao {
        Some(s) => println!("{s}"), // s: &String; opcao continua inteira
        None => {}
    }
    println!("{:?}", opcao);

    // Slice patterns
    let v = [1, 2, 3, 4];
    match v {
        [primeiro, .., ultimo] => println!("{primeiro}..{ultimo}"),
    }
    match &v[..] {
        [] => println!("vazio"),
        [x] => println!("um: {x}"),
        [x, resto @ ..] => println!("{x} e mais {}", resto.len()),
    }
}
```

> [!warning] Armadilha com `_` e posse
> `let _ = valor;` **não** move; `let _x = valor;` move. O padrão `_` não faz binding.

## Veja também

- [[match]]
- [[Desestruturação]]
- [[Enums]]
- [[if let e let else]]
