---
tags: [rust, basico, funcoes]
aliases: ["retorno", "parâmetros"]
tipo: conceito
nivel: iniciante
criado: 2026-10-24
relacionados: ["[[Expressões vs instruções]]", "[[Comentários e doc comments]]", "[[Closures]]"]
---

# Funções

```rust
// Parâmetros exigem tipo; o tipo de retorno vem após ->
fn soma(a: i32, b: i32) -> i32 {
    a + b // última expressão sem ; é o valor retornado
}

fn cumprimenta(nome: &str) {
    println!("Olá, {nome}!"); // retorna ()
}

fn divide(a: i32, b: i32) -> Option<i32> {
    if b == 0 {
        return None; // retorno antecipado com return
    }
    Some(a / b)
}

fn main() {
    cumprimenta("Ana");
    println!("{}", soma(2, 3));
    println!("{:?} {:?}", divide(10, 2), divide(1, 0));
}
```

- Rust **não** tem sobrecarga de funções nem argumentos padrão/nomeados.
- A ordem de declaração das funções não importa.
- Funções podem ser aninhadas dentro de outras.

> [!warning] Ponto e vírgula muda o significado
> `a + b;` transforma a expressão em instrução e a função passa a retornar `()`, causando erro de tipo.

## Veja também

- [[Expressões vs instruções]]
- [[Comentários e doc comments]]
- [[Closures]]
