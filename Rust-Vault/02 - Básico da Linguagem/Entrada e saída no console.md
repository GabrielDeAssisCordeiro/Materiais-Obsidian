---
tags: [rust, basico, io]
aliases: ["stdin", "read_line", "print", "eprintln"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Strings String vs str]]", "[[Formatação com println]]", "[[Operador de interrogação]]"]
---

# Entrada e saída no console

```rust
use std::io::{self, Write};

fn main() {
    print!("Digite um número: ");
    io::stdout().flush().unwrap(); // garante que o prompt apareça antes da leitura

    let mut linha = String::new();
    io::stdin().read_line(&mut linha).expect("falha ao ler");

    // trim remove o \n final; parse converte o texto em número
    match linha.trim().parse::<i32>() {
        Ok(n) => println!("Dobro: {}", n * 2),
        Err(e) => eprintln!("Entrada inválida: {e}"), // stderr
    }
}
```

- `print!`/`println!` escrevem em **stdout**; `eprint!`/`eprintln!` em **stderr**.
- `read_line` **acrescenta** à `String` (inclui a quebra de linha).
- Para ler tudo: `io::read_to_string(io::stdin())`.

> [!tip] Lendo várias linhas
> `for linha in io::stdin().lines()` itera sobre cada linha como `io::Result<String>`.

## Exercício

Leia dois números em linhas separadas e imprima a soma, tratando o erro de conversão.

## Veja também

- [[Strings String vs str]]
- [[Formatação com println]]
- [[Operador de interrogação]]
