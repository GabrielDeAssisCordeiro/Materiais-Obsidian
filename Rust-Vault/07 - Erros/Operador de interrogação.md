---
tags: [rust, erros, result]
aliases: ["?", "operador ?", "propagação de erros", "try operator"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Option e Result]]", "[[Erros customizados]]", "[[Conversão de erros com From]]", "[[Box dyn Error]]"]
---

# Operador de interrogação

O operador `?` **propaga** o erro: se o valor é `Err(e)` (ou `None`), retorna imediatamente da função; se é `Ok(v)`, extrai `v`.

```rust
use std::fs;
use std::io;

// Sem ?: verboso
fn le_sem_operador(caminho: &str) -> Result<String, io::Error> {
    match fs::read_to_string(caminho) {
        Ok(s) => Ok(s),
        Err(e) => Err(e),
    }
}

// Com ?
fn le_com_operador(caminho: &str) -> Result<String, io::Error> {
    let texto = fs::read_to_string(caminho)?;
    Ok(texto.trim().to_string())
}

fn main() {
    println!("{:?}", le_sem_operador("nao_existe.txt").is_err());
    println!("{:?}", le_com_operador("nao_existe.txt").is_err());
}
```

## O `?` também faz conversão

Em caso de erro, `?` chama `From::from(erro)` para converter no tipo de erro da função. Veja [[Conversão de erros com From]].

## Com `Option`

```rust
fn primeira_letra_maiuscula(s: &str) -> Option<char> {
    let c = s.chars().next()?; // retorna None se a string for vazia
    Some(c.to_ascii_uppercase())
}

fn main() {
    println!("{:?} {:?}", primeira_letra_maiuscula("rust"), primeira_letra_maiuscula(""));
}
```

## `main` pode retornar `Result`

```rust
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let n: i32 = "42".parse()?;
    println!("{n}");
    Ok(())
}
```

Se `main` devolver `Err`, o programa imprime o erro (via `Debug`) e sai com código de status diferente de zero.

> [!warning] Não misture
> `?` em função que retorna `Option` só funciona com `Option`; em função `Result`, só com `Result`. Converta com `ok_or`/`ok()` quando necessário; veja [[Combinadores de Option e Result]].

## Exercício

Escreva `fn soma_textos(a: &str, b: &str) -> Result<i32, std::num::ParseIntError>` usando `?`.

## Veja também

- [[Option e Result]]
- [[Erros customizados]]
- [[Conversão de erros com From]]
- [[Box dyn Error]]
