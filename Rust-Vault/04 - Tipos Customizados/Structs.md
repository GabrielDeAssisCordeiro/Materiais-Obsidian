---
tags: [rust, structs, tipos]
aliases: ["struct", "registro", "struct com campos nomeados"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Structs tupla e unit]]", "[[Métodos e funções associadas]]", "[[Enums]]", "[[Lifetimes em structs]]"]
---

# Structs

Uma **struct** agrupa dados nomeados em um novo tipo.

```rust
#[derive(Debug, Clone)]
struct Usuario {
    nome: String,
    email: String,
    ativo: bool,
    logins: u32,
}

fn novo_usuario(nome: String, email: String) -> Usuario {
    Usuario {
        nome,    // abreviação: campo com mesmo nome da variável
        email,
        ativo: true,
        logins: 1,
    }
}

fn main() {
    let mut u1 = novo_usuario("Ana".to_string(), "ana@exemplo.com".to_string());
    u1.logins += 1; // para alterar campos, a instância toda precisa ser mut

    // Sintaxe de atualização: copia/move o restante de u1
    let u2 = Usuario {
        nome: String::from("Bia"),
        ..u1.clone()
    };
    println!("{:?}\n{:#?}", u1, u2);
}
```

- A mutabilidade é da **instância inteira**; não existe campo `mut` individual.
- Com `..outra` (struct update), campos não `Copy` são **movidos** da outra instância.
- `#[derive(Debug)]` permite imprimir com `{:?}`.

> [!tip] Campos privados
> Por padrão, campos são privados ao módulo. Use `pub` para expor; veja [[Visibilidade e pub]].

## Exercício

Defina `Retangulo { largura: f64, altura: f64 }` e uma função `area(&Retangulo) -> f64`.

## Veja também

- [[Structs tupla e unit]]
- [[Métodos e funções associadas]]
- [[Enums]]
- [[Lifetimes em structs]]
