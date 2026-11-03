---
tags: [rust, enums, tipos]
aliases: ["enum", "variantes", "tipos soma", "ADT"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Option e Result]]", "[[Pattern matching avançado]]", "[[match]]", "[[Structs]]"]
---

# Enums

Um **enum** representa um valor que é **uma entre várias variantes**; cada variante pode carregar dados diferentes (tipos soma).

```rust
#[derive(Debug)]
enum Mensagem {
    Sair,                        // sem dados
    Mover { x: i32, y: i32 },    // campos nomeados
    Escrever(String),            // tupla
    Cor(u8, u8, u8),
}

impl Mensagem {
    fn processa(&self) {
        match self {
            Mensagem::Sair => println!("saindo"),
            Mensagem::Mover { x, y } => println!("mover para {x},{y}"),
            Mensagem::Escrever(t) => println!("texto: {t}"),
            Mensagem::Cor(r, g, b) => println!("cor {r},{g},{b}"),
        }
    }
}

fn main() {
    let msgs = vec![
        Mensagem::Mover { x: 1, y: 2 },
        Mensagem::Escrever(String::from("oi")),
        Mensagem::Cor(255, 0, 0),
        Mensagem::Sair,
    ];
    for m in &msgs {
        m.processa();
    }
}
```

## Valores discriminantes

```rust
#[derive(Debug, Clone, Copy, PartialEq)]
enum Dia {
    Segunda = 1,
    Terca,    // 2
    Quarta,   // 3
}

fn main() {
    println!("{}", Dia::Quarta as i32); // 3
    println!("{:?}", Dia::Segunda);
}
```

> [!tip] Estados impossíveis não representáveis
> Modele o domínio com enums para que combinações inválidas sejam impossíveis de escrever. O `match` exaustivo garante que você trate todos os casos.

## Exercício

Modele `Forma` com variantes `Circulo(f64)` e `Retangulo(f64, f64)` e implemente `area(&self)`.

## Veja também

- [[Option e Result]]
- [[Pattern matching avançado]]
- [[match]]
- [[Structs]]
