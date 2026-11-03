---
tags: [rust, structs]
aliases: ["impl", "self", "funções associadas", "construtor"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Structs]]", "[[Enums]]", "[[Traits]]"]
---

# Métodos e funções associadas

Blocos `impl` definem **métodos** (primeiro parâmetro `self`) e **funções associadas** (sem `self`, chamadas com `::`).

```rust
#[derive(Debug)]
struct Retangulo {
    largura: f64,
    altura: f64,
}

impl Retangulo {
    // Função associada: construtor por convenção chamado new
    fn new(largura: f64, altura: f64) -> Self {
        Self { largura, altura }
    }

    fn quadrado(lado: f64) -> Self {
        Self::new(lado, lado)
    }

    // &self: empresta para leitura
    fn area(&self) -> f64 {
        self.largura * self.altura
    }

    // &mut self: empresta para alterar
    fn escala(&mut self, fator: f64) {
        self.largura *= fator;
        self.altura *= fator;
    }

    // self: toma posse (consome a instância)
    fn into_tupla(self) -> (f64, f64) {
        (self.largura, self.altura)
    }
}

fn main() {
    let mut r = Retangulo::new(2.0, 3.0);
    println!("{}", r.area());
    r.escala(2.0);
    println!("{:?}", r);
    let q = Retangulo::quadrado(4.0);
    println!("{:?}", q.into_tupla()); // q consumido
}
```

| Receptor | Significado | Equivale a |
|---|---|---|
| `&self` | só lê | `self: &Self` |
| `&mut self` | altera | `self: &mut Self` |
| `self` | consome | `self: Self` |

> [!info] Múltiplos blocos impl
> Você pode ter vários blocos `impl` para o mesmo tipo (úteis com genéricos e traits).

## Exercício

Adicione ao `Retangulo` um método `eh_quadrado(&self) -> bool`.

## Veja também

- [[Structs]]
- [[Enums]]
- [[Traits]]
