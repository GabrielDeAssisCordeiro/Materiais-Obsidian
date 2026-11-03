---
tags: [rust, fundamentos]
aliases: ["Hello World"]
tipo: procedimento
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Cargo básico]]", "[[Instalação com rustup]]", "[[Macros básicas]]"]
---

# Primeiro programa Hello World

## Com `rustc` direto

Crie `ola.rs`:

```rust
// Ponto de entrada de todo programa binário
fn main() {
    // println! é uma macro (note o !)
    println!("Olá, mundo!");
}
```

```bash
rustc ola.rs   # gera o executável ./ola
./ola
```

## Anatomia

- `fn main()` declara a função de entrada.
- `println!` é uma **macro**, não uma função (por isso o `!`); veja [[Macros básicas]].
- Instruções terminam com `;`.
- Corpo entre chaves `{ }`.

> [!tip] Indentação
> O padrão é 4 espaços; o `rustfmt` cuida disso.

## Exercício

Altere o programa para imprimir seu nome e a linguagem favorita em duas linhas.

## Veja também

- [[Cargo básico]]
- [[Instalação com rustup]]
- [[Macros básicas]]
