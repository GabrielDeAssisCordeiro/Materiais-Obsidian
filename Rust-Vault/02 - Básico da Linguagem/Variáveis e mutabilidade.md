---
tags: [rust, basico, variaveis]
aliases: ["let", "mut", "imutabilidade"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Shadowing]]", "[[Constantes e statics]]", "[[Tipos escalares]]"]
---

# Variáveis e mutabilidade

Em Rust, variáveis são **imutáveis por padrão**. Para alterar o valor, declare com `mut`.

```rust
fn main() {
    let x = 5;          // imutável
    println!("x = {x}");

    let mut y = 10;     // mutável
    y += 1;
    println!("y = {y}");

    // Tipo explícito quando a inferência não basta
    let z: u8 = 255;
    println!("z = {z}");
}
```

```rust
// ❌ NÃO COMPILA: atribuição dupla a variável imutável
fn main() {
    let x = 5;
    x = 6;
    println!("{x}");
}
```

Erro do compilador:

```text
error[E0384]: cannot assign twice to immutable variable `x`
```

**Correção:** declare `let mut x = 5;`.

> [!tip] Por que imutável por padrão?
> Facilita raciocinar sobre o código e é a base para o compilador provar ausência de data races em [[Concorrência sem medo]].

> [!info] Inicialização tardia
> Uma variável pode ser declarada e inicializada depois, desde que o compilador prove que todo caminho a inicializa antes do uso.

```rust
fn main() {
    let valor: i32;
    let condicao = true;
    if condicao {
        valor = 1;
    } else {
        valor = 2;
    }
    println!("{valor}");
}
```

## Exercício

Declare uma variável `contador` mutável, incremente-a três vezes e imprima o resultado.

## Veja também

- [[Shadowing]]
- [[Constantes e statics]]
- [[Tipos escalares]]
